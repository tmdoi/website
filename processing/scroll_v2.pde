import processing.serial.*;

Serial myPort;
float prevY = 0;

void setup() {
  size(800, 600);
  printArray(Serial.list());
  String portName = Serial.list()[6];
  myPort = new Serial(this, portName, 115200);
  background(0);
}

void draw() {
  while (myPort.available() > 0) {
    String inBuffer = myPort.readStringUntil('\n');

    if (inBuffer != null) {
      inBuffer = trim(inBuffer);
      float inByte = float(inBuffer);
      inByte = map(inByte, -1024, 1024, 0, height);

      // Shift the screen content to the left
      PImage img = get();
      set(-1, 0, img);

      stroke(127, 34, 255);
      line(width - 2, prevY, width - 1, height - inByte);
      
      // Clear the last pixel column
      stroke(0);
      line(width - 1, 0, width - 1, height);

      prevY = height - inByte;
    }
  }
}
