package com.example;

import org.springframework.web.bind.annotation.*;
import java.sql.*;
import java.util.*;

@RestController
@RequestMapping("/sensors")
public class SensorController {

    private Connection getConnection() throws SQLException {
        String url = "jdbc:snowflake://<account>.snowflakecomputing.com";
        return DriverManager.getConnection(url, "USER", "PASSWORD");
    }

    @GetMapping("/latest")
    public List<Map<String,Object>> getLatest() throws SQLException {
        try (Connection conn = getConnection()) {
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM SENSOR_READINGS ORDER BY timestamp DESC LIMIT 100");
            List<Map<String,Object>> list = new ArrayList<>();
            while (rs.next()) {
                Map<String,Object> row = new HashMap<>();
                row.put("sensorId", rs.getString("sensorId"));
                row.put("timestamp", rs.getTimestamp("timestamp"));
                row.put("temperature", rs.getDouble("temperature"));
                row.put("humidity", rs.getDouble("humidity"));
                list.add(row);
            }
            return list;
        }
    }
}
