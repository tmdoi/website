import processing.serial.*;

Serial myPort;
int xPos = 1; 
int lastXPos = 1;
int lastHeight = 0;

void setup() {
  size(800, 600);  // ウィンドウのサイズを設定
  printArray(Serial.list());
  String portName = Serial.list()[6];
  myPort = new Serial(this, portName, 115200);

  background(0);  // グラフの背景色を設定
}

void draw() {
  while (myPort.available() > 0) {
    String inData = myPort.readStringUntil('\n');
    if (inData != null) {
      inData = trim(inData); 
      float inByte = float(inData);
      inByte = map(inByte, -1024, 1024, 0, height);

      stroke(127, 34, 255);  // グラフの色を設定
      line(lastXPos, lastHeight, xPos, height - inByte);  // データに基づいて線を描く

      lastXPos = xPos;
      lastHeight = int(height - inByte);

      if (xPos >= width) {
        xPos = 0;
        lastXPos = 0;
        background(0);  // 画面をクリア
      } else {
        xPos++;
      }
    }
  }
}
