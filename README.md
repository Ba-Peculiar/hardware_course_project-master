<h1>Environment Monitoring System with DHT11 and Mobile App Integration</h1>

  <h2>Project Description</h2>
  <p>
    This project is an environment monitoring system that uses a <strong>DHT11 sensor</strong> to measure temperature 
    and humidity in real-time. The sensor data is processed and displayed on a mobile app, allowing users to monitor 
    their environment conveniently. This project is ideal for smart home systems, environmental research, or personal use.
  </p>

  <h2>Features</h2>
  <ul>
    <li><strong>Temperature Measurement:</strong> Reads and displays the current temperature in Celsius.</li>
    <li><strong>Humidity Measurement:</strong> Monitors and displays the current humidity percentage.</li>
    <li><strong>Mobile App Integration:</strong> Displays real-time data on a user-friendly app interface.</li>
    <li><strong>Wireless Communication:</strong> Connects the hardware to the app seamlessly using an ESP32 (or similar microcontroller).</li>
    <li><strong>Compact and Cost-Effective:</strong> Utilizes the DHT11 sensor for accurate and affordable measurements.</li>
  </ul>

  <h2>Hardware Components</h2>
  <ul>
    <li><strong>DHT11 Sensor:</strong> To measure temperature and humidity.</li>
    <li><strong>ESP32 (or any microcontroller):</strong> To process sensor data and communicate with the mobile app.</li>
    <li><strong>Jumper Wires:</strong> For connections between components.</li>
    <li><strong>Breadboard:</strong> For prototyping and assembling the circuit.</li>
    <li><strong>Power Source:</strong> USB cable, battery, or any suitable power supply.</li>
  </ul>

  <h2>Software Requirements</h2>
  <ul>
    <li><strong>Arduino IDE:</strong> To program the ESP32/microcontroller.</li>
    <li><strong>Mobile App (Custom-built):</strong> Displays real-time sensor readings. (Developed using Flutter or any preferred framework.)</li>
    <li><strong>Libraries:</strong>
      <ul>
        <li><code>DHT</code> library for DHT11 sensor.</li>
        <li><code>WiFi</code> and <code>HTTPClient</code> libraries for communication with the app.</li>
      </ul>
    </li>
  </ul>
