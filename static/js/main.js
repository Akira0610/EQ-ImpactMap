document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("query-form");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        const params = Object.fromEntries(formData.entries());

        // ✅ 防呆驗證條件
        const errors = [];
        const now = new Date();
        const startTime = params.start_time ? new Date(params.start_time) : null;
        const endTime = params.end_time ? new Date(params.end_time) : null;
        const minMag = params.min_magnitude;
        const maxMag = params.max_magnitude;

        // ✅ 最小震度不得為負數或非數字
        if (minMag && (!/^\d+(\.\d+)?$/.test(minMag) || parseFloat(minMag) < 0)) {
            errors.push("❌ 最小規模請輸入非負數的阿拉伯數字");
        }

        // ✅ 最大震度需為數字且 ≥ 最小值
        if (maxMag && (!/^\d+(\.\d+)?$/.test(maxMag))) {
            errors.push("❌ 最大規模請輸入阿拉伯數字");
        }

        if (minMag && maxMag && parseFloat(maxMag) < parseFloat(minMag)) {
            errors.push("❌ 最大規模不能小於最小規模");
        }

        // ✅ 時間格式與邏輯
        if (startTime && isNaN(startTime.getTime())) {
            errors.push("❌ 起始時間格式錯誤");
        }

        if (endTime && isNaN(endTime.getTime())) {
            errors.push("❌ 結束時間格式錯誤");
        }

        if (startTime && startTime > now) {
            errors.push("❌ 起始時間不得超過今天");
        }

        if (startTime && endTime && startTime > endTime) {
            errors.push("❌ 起始時間不可晚於結束時間");
        }

        // ✅ 顯示錯誤訊息
        if (errors.length > 0) {
            alert(errors.join("\n"));
            return;
        }

        // ✅ 若全部為空 → 抓取近期 40 筆地震
        const allEmpty = Object.values(params).every(v => !v.trim());
        if (allEmpty) {
            params.min_magnitude = "0";
        }

        // ✅ 傳送查詢條件給後端
        const res = await fetch("/map", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                features: await fetchEarthquakeData(params)
            }),
        });

        const html = await res.text();
        document.getElementById("map-container").innerHTML = html;
    });
});

// ✅ 向後端查詢地震資料（轉 GET）
async function fetchEarthquakeData(params) {
    const urlParams = new URLSearchParams(params).toString();

    try {
        const res = await fetch('/earthquakes?${urlParams}');

        // 🔴 若伺服器回傳錯誤（如 500、404）
        if (!res.ok) {
            throw new Error('後端錯誤（狀態碼 ${res.status}）');
        }

        const data = await res.json();

        // ✅ 回傳資料格式正確才解析
        return data.features || [];

    } catch (err) {
        console.error("[❌ 前端錯誤]", err);
        alert("❌ 查詢失敗：後端可能無法處理這筆請求，請檢查輸入條件或稍後再試！");
        return [];
    }
}

