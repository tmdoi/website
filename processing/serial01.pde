import processing.serial.*;

Serial myPort;  // シリアルポート

void setup() {
  printArray(Serial.list());  // 使用可能なシリアルポートを表示

  // ポート名は環境により異なるので、上記のリストから適切なものを選びます。
  String portName = Serial.list()[0];
  myPort = new Serial(this, portName, 115200);  // ボーレートは Micro:bit の設定に合わせます
}

void draw() {
  while (myPort.available() > 0) {
    String inData = myPort.readStringUntil('\n');
    if (inData != null) {
      inData = trim(inData);  // 改行文字の削除
      println("Received: " + inData);
    }
  }
}
