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
    private static final String URL_STR = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson";
    private static final String OUTPUT_PATH = "./out/usgs_data.json";

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

        // 添加關閉鉤子
        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
            System.out.println("正在關閉排程器...");
            scheduler.shutdown();
            try {
                if (!scheduler.awaitTermination(60, TimeUnit.SECONDS)) {
                    scheduler.shutdownNow();
                }
            } catch (InterruptedException e) {
                scheduler.shutdownNow();
                Thread.currentThread().interrupt();
            }
        }));

        fetchTask.run();
        scheduler.scheduleAtFixedRate(fetchTask, 30, 5, TimeUnit.MINUTES);
    }

    private static void fetchEarthquakeData() throws IOException {
        HttpURLConnection conn = null;
        try {
            URL url = new URL(URL_STR);
            conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("GET");

            if (conn.getResponseCode() == HttpURLConnection.HTTP_OK) {
                String json;
                try (InputStream inputStream = conn.getInputStream()) {
                    json = new String(inputStream.readAllBytes());
                }

                // 確保目錄存在
                Files.createDirectories(Paths.get("out"));
                Files.writeString(Paths.get(OUTPUT_PATH), json);
            } else {
                throw new IOException("HTTP response code: " + conn.getResponseCode());
            }
        } finally {
            if (conn != null) {
                conn.disconnect();
            }
        }
    }

    public static String getUrlStr() {
        return URL_STR;
    }
}
