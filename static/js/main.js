function setInnerHTML(elm, html) {
    elm.innerHTML = html;

    Array.from(elm.querySelectorAll("script"))
        .forEach(oldScriptEl => {
            const newScriptEl = document.createElement("script");

            Array.from(oldScriptEl.attributes).forEach(attr => {
                newScriptEl.setAttribute(attr.name, attr.value)
            });

            const scriptText = document.createTextNode(oldScriptEl.innerHTML);
            newScriptEl.appendChild(scriptText);

            oldScriptEl.parentNode.replaceChild(newScriptEl, oldScriptEl);
        });
}

/*
{
Array<{
    coordinate: [number, number, number];
    magnitude: number;
    place: string;
    time: number;
}>
}

*/


document.addEventListener("DOMContentLoaded", async () => {
    const form = document.getElementById("query-form");
    let deckGl;
    const { DeckGL, ScatterplotLayer } = deck;

    function createScatterLayer(data) {
        return new ScatterplotLayer({
            id: 'circles',
            data: data,
            radiusMinPixels: 0.5,
            getPosition: d => d.coordinates,
            getColor: [255, 0, 0],
            getRadius: d => d.magnitude * 8000,
            pickable: true
        })
    }

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
        const data = await fetchEarthquakeInfo(params);

        // console.log("[✅ 後端回傳]", data);
        updateLayer(data);
    });

    function updateLayer(data) {
        if (deckGl === undefined) return;

        deckGl.setProps({ layers: [createScatterLayer(data),] })
    }

    const initialData = await fetchEarthquakeInfo()

    deckGl = new DeckGL({
        container: "map-container",
        mapStyle: 'https://basemaps.cartocdn.com/gl/dark-matter-gl-style/style.json',
        initialViewState: {
            longitude: 123.45,
            latitude: 23,
            zoom: 5
        },
        getTooltip: function({object}) {
            return object && `
                ${object.time}
                ${object.coordinates}
                ${object.place}
                ${object.magnitude}
            `;
        } ,
        controller: true,
        layers: [
            createScatterLayer(initialData)
        ]
    });
});

/**
 * @param {object} param 篩選地震資料的條件
 */
async function fetchEarthquakeInfo(params = {}) {
    return fetch(
        "/earthquake-info",
        {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(params),
        })
        .then(res => res.json())
        .catch(error => console.error("[❌ 前端錯誤]", error));
}

