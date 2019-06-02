int value;
int tmp_sensor = A1;
float voltage;
float temperatureC;
void setup(){
    Serial.begin(9600);
    pinMode(tmp_sensor,INPUT);
}
void loop() {
    value = analogRead(tmp_sensor);
    voltage = value * 5.0 / 1024.0;
    temperatureC  = (voltage - 0.5) / 0.01;
    Serial.println(temperatureC);
    delay(500);
}
