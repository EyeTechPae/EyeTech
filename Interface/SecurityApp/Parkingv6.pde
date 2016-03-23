import processing.video.*;
Movie cam1, cam2, cam3, cam4, cam5, cam6;
PImage logo, start, littleLogo;
PFont font,font2;
Plates plates;
Map m;
Available available;
PVector rotM, posM1, posM2, rotP, posP, rotA, posA, posLogo;
PShape whiteCar;
PShape parking;

String state;
//float x, y;
PVector background;
void setup() {
  background(0);
  surface.setTitle("EyeTech"); 
  surface.setIcon(littleLogo);
  //String[] params = { "/home/enric/Desktop/script.sh" };
  //launch(params);
  state="initTools";///////!!!!!1
  size(1200, 600, OPENGL);
  logo=requestImage("logo.png");
  start=requestImage("start.png");
  littleLogo=requestImage("littlelogo.png");
  font=createFont("airstrike.ttf",32);
  font2=createFont("Anke",12);
  
  rotM=new PVector(0, 0, 0);
  posM1=new PVector(800, 250, 0);
  posM2=new PVector(800, 600, 0); //init map outside display
  rotP=new PVector(0, 0, 0);
  posP=new PVector(1050, 400, 0);
  rotA=new PVector(0, 0, 0);
  posA=new PVector(100, 550, 0);
  posLogo=new PVector(500, 100, 0);
  background=new PVector(0, 0, 0);
  available=new Available(rotA, posA, 0, 4);
  m=new Map(rotM, posM1, posM2);
  plates=new Plates(rotP, posP);

  whiteCar=loadShape("cotxe.obj");
  whiteCar.scale(1.1);
  parking=loadShape("parquingReversed.obj");
  parking.scale(1.5);
    initializeCameras();

}
void draw() {
  lights();
  ambientLight(102, 102, 102);
  noStroke();
  smooth();
 // directionalLight(51, 102, 126, -1, 0, 0);  
  if (state=="init") init();
  if (state=="initTools") initTools();
  if (state=="initMap")initMap();
  if(state=="initCameras")fullLoad();
}