import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

public class EarthquakeFetcher {
    private static final String urlStr = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson";
    private static final String outputPath = "./out/usgs_data.json";

    public static void main(String[] args) {
        ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(1);

        Runnable fetchTask = () -> {
            try {
                fetchEarthquakeData();
                System.out.println("資料更新完成：" + java.time.LocalDateTime.now());
            } catch (IOException e) {
                System.err.println("資料抓取失敗: " + e.getMessage());
            }
        };

        // 先跑一次
        fetchTask.run();
        // 每5分鐘跑一次
        scheduler.scheduleAtFixedRate(fetchTask, 30, 5, TimeUnit.MINUTES);
    }

    private static void fetchEarthquakeData() throws IOException {
        URL url = new URL(urlStr);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");

        if (conn.getResponseCode() == 200) {
            String json;
            try (InputStream inputStream = conn.getInputStream()) {
                json = new String(inputStream.readAllBytes());
            }

            // 確保目錄存在
            Files.createDirectories(Paths.get("out"));
            Files.writeString(Paths.get(outputPath), json);
        } else {
            throw new IOException("HTTP response code: " + conn.getResponseCode());
        }
    }

    public static String getUrlStr() {
        return urlStr;
    }
}
