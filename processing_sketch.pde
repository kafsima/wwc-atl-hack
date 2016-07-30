import processing.serial.*;
import java.util.*;
import java.text.*;


int end = 10;
String serial;
String prevValue = "";
Serial port;
PrintWriter output;

void setup() {
  //println(port.list());
  
  output = createWriter("sensor_data.txt");
  
  String portName = Serial.list()[3];
  port = new Serial(this, portName, 115200);
  port.clear();
  
  serial = port.readStringUntil(end);
  serial = null;
}

void draw() {
  while (port.available() > 0) {
    serial = port.readStringUntil(end);
  }
  if (serial != null && prevValue != serial) {
    String now = new SimpleDateFormat("yyyy.MM.dd.HH.mm.ss").format(new Date());
    output.println(now + '|' + serial);
    prevValue = serial;
  }
}

void keyPressed() {
  output.flush();
  output.close();
  exit();
}
