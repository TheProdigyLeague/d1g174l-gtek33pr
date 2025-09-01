use std::collections::HashMap;
use std::io::{self, Write};
use std::thread;
use std::time::Duration;

#[derive(Debug, Clone, PartialEq, Eq, Hash)]
struct SensorId(String);

#[derive(Debug, Clone)]
enum SensorStatus {
    Nominal,
    Alert(String), // String contains alert details
}

#[derive(Debug, Clone)]
struct Sensor {
    id: SensorId,
    location: String,
    status: SensorStatus,
    last_checked: std::time::Instant,
}

impl Sensor {
    fn new(id: &str, location: &str) -> Self {
        Sensor {
            id: SensorId(id.to_string()),
            location: location.to_string(),
            status: SensorStatus::Nominal,
            last_checked: std::time::Instant::now(),
        }
    }

    fn check_status(&mut self) {
        // Simulate sensor check - randomly trigger an alert
        self.last_checked = std::time::Instant::now();
        if rand::random::<f64>() < 0.1 { // 10% chance of alert
            self.status = SensorStatus::Alert(format!("Motion detected at {}", self.location));
        } else {
            // Occasionally reset to nominal even if it was an alert before
            if rand::random::<f64>() < 0.5 {
                self.status = SensorStatus::Nominal;
            }
        }
    }
}

#[derive(Debug)]
struct SecuritySystem {
    sensors: HashMap<SensorId, Sensor>,
    alerts: Vec<String>,
}

impl SecuritySystem {
    fn new() -> Self {
        SecuritySystem {
            sensors: HashMap::new(),
            alerts: Vec::new(),
        }
    }

    fn add_sensor(&mut self, id: &str, location: &str) {
        let sensor = Sensor::new(id, location);
        self.sensors.insert(sensor.id.clone(), sensor);
        println!("[INFO] Added sensor: {} at {}", id, location);
    }

    fn monitor_sensors(&mut self) {
        for sensor in self.sensors.values_mut() {
            sensor.check_status();
            match &sensor.status {
                SensorStatus::Alert(details) => {
                    let alert_message = format!("[ALERT] Sensor {}: {}", sensor.id.0, details);
                    if !self.alerts.contains(&alert_message) { // Avoid duplicate alerts from same check cycle
                        println!("{}", alert_message);
                        self.alerts.push(alert_message);
                    }
                }
                SensorStatus::Nominal => {
                    // Optionally log nominal status or do nothing
                }
            }
        }
    }

    fn display_status(&self) {
        println!("\n--- Security System Status ---");
        if self.sensors.is_empty() {
            println!("No sensors configured.");
        }
        for sensor in self.sensors.values() {
            println!("Sensor: {}, Location: {}, Status: {:?}, Last Checked: {:?}",
                     sensor.id.0, sensor.location, sensor.status, sensor.last_checked.elapsed());
        }
        if !self.alerts.is_empty() {
            println!("\n--- Active Alerts ---");
            for alert in &self.alerts {
                println!("{}", alert);
            }
        }
        println!("-----------------------------\n");
    }
}

fn main() {
    let mut security_system = SecuritySystem::new();

    security_system.add_sensor("CAM001", "Main Entrance");
    security_system.add_sensor("MOT002", "Warehouse Section A");
    security_system.add_sensor("DOOR003", "Server Room");

    println!("\nStarting security monitoring loop (Ctrl+C to exit)...");
    loop {
        security_system.monitor_sensors();
        security_system.display_status();
        io::stdout().flush().unwrap(); // Ensure output is displayed immediately
        thread::sleep(Duration::from_secs(5)); // Check sensors every 5 seconds
    }
}
