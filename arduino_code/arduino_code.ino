String serialData;

void setup()
{
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop()
{
  if (Serial.available()) {
    serialData = Serial.readStringUntil('\n');
    if (serialData == "0") {
      Serial.println("Turn On");
      digitalWrite(13, HIGH);
    }
    else if (serialData == "1") {
      Serial.println("Turn Off");
      digitalWrite(13, LOW);
    }
  }
}
