// java-fetcher/src/EarthquakeFetcher.java

import java.io.*;
import java.net.*;
import java.nio.file.*;

public class EarthquakeFetcher {
    public static void main(String[] args) {
        String urlStr = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson";
        String outputPath = "out/usgs_data.json";

        try {
            // 建立 URL 物件
            URL url = new URL(urlStr);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");

            // 檢查回應碼
            if (conn.getResponseCode() == 200) {
                InputStream inputStream = conn.getInputStream();
                String json = new String(inputStream.readAllBytes());
                inputStream.close();

                // 確保輸出資料夾存在
                Files.createDirectories(Paths.get("out"));

                // 寫入 JSON 檔案
                Files.write(Paths.get(outputPath), json.getBytes());
                System.out.println("地震資料已寫入到 " + outputPath);
            } else {
                System.err.println("無法抓取資料，HTTP 狀態碼: " + conn.getResponseCode());
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
