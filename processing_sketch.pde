import processing.serial.*;
import java.util.*;
import java.text.*;


Serial mySerial;
String val;
PrintWriter output;

void setup() {
  size(800, 600);
  
  println(Serial.list());
  
  String portName = Serial.list()[3];
  mySerial = new Serial(this, portName, 115200);
  
  output = createWriter("sensor_data.txt");
}

void draw () {
  if (mySerial.available() > 0) {
    val = mySerial.readStringUntil('\n');
  }
  if (val != null) {
    String now = new SimpleDateFormat("yyyy.MM.dd.HH.mm.ss").format(new Date());
    output.println(now + '|' + val);
  }
  //println(val);
}
