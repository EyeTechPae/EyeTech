void init() {
  background(background.x, background.y, background.z);
  image(logo, posLogo.x, posLogo.y);
  image(start, 579, 455);
  if (keyCode==ENTER||mousePressed==true && mouseX>579 && mouseX<750 && mouseY>455 && mouseY<500) state="initTools";
}
void initTools() {
  background(background.x, background.y, background.z);//191,242,238

  background.x=background.x+(191-background.x)*0.01;
  background.y=background.y+(242-background.y)*0.01;
  background.z=background.z+(238-background.z)*0.01;

  pushMatrix();
  image(logo, posLogo.x, posLogo.y);
  tint(255, 255-background.x*1.3-64);
  popMatrix();
  plates.displayPlatesModeALL();
  available.displayAvailable();
  displayTT();

  if (background.x>140)state="initMap";
}
void initMap() {
  tint(255);
  background(background.x, background.y, background.z);
  image(littleLogo, 20, 20);
  //image(logo, posLogo.x, posLogo.y);
  m.displayModeALL();
  m.initCars();

  plates.displayPlatesModeALL();
  available.displayAvailable();
  displayTT();
  m.positionAll.y=m.positionAll.y+(500-m.positionAll.y)*0.05;
   if (m.positionAll.y<510)state="initCameras";
}
void fullLoad() {
  background(background.x, background.y, background.z);
  image(littleLogo, 20, 20);

  if (key=='p') {
    plates.displayPlatesMode1();
  } else {
    plates.displayPlatesModeALL();
    available.displayAvailable();
    displayTT();
    m.displayModeALL();
      m.initCars();

    cameras();
  }
  
}