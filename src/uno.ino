// Arduino Uno: Soil Moisture + LDR (CDS) Sensor Reading
// Prints values in standard units separated by commas

#define SOIL_PIN A0
#define LDR_PIN  A1

void setup() {
  Serial.begin(9600);
}

void loop() {
  // Read raw analog values
  int soilRaw = analogRead(SOIL_PIN);
  int ldrRaw = analogRead(LDR_PIN);

  // Convert to standard units
  // Soil moisture (percentage)
  float soilPercent = map(soilRaw, 1023, 0, 0, 100);  
  // LDR (approximate lux conversion)
  float ldrLux = (float)(250000 / (ldrRaw + 1)); // simple approximate

  // Print values in CSV format
  Serial.print(soilPercent, 1);
  Serial.print(",");
  Serial.println(ldrLux, 1);

  delay(1000);
}
