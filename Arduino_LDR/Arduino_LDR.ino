void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  // print out the value you read:
  Serial.print("LDR1 value = ");
  Serial.println(sensorValue);
  delay(5000);        // delay in between reads for stability

    // read the input on analog pin 0:
  int sensorValue1 = analogRead(A1);
  // print out the value you read:
  Serial.print("LDR2 value = ");
  Serial.println(sensorValue1);
  delay(5000);        // delay in between reads for stability

    // read the input on analog pin 0:
  int sensorValue2 = analogRead(A2);
  // print out the value you read:
  Serial.print("LDR3 value = ");
  Serial.println(sensorValue2);
  delay(5000);        // delay in between reads for stability

    // read the input on analog pin 0:
  int sensorValue3 = analogRead(A3);
  // print out the value you read:
  Serial.print("LDR4 value = ");
  Serial.println(sensorValue3);
  delay(5000);        // delay in between reads for stability

    // read the input on analog pin 0:
  int sensorValue4 = analogRead(A4);
  // print out the value you read:
  Serial.print("LDR5 value = ");
  Serial.println(sensorValue4);
  delay(5000);        // delay in between reads for stability
    // read the input on analog pin 0:
  int sensorValue5 = analogRead(A5);
  // print out the value you read:
  Serial.print("LDR6 value = ");
  Serial.println(sensorValue5);
  delay(500);        // delay in between reads for stability
  
}
