void cameras() {
  textSize(30);
  textFont(font);
  fill(255);
  image(cam1, 225, 50, 250, 150);
  text("CAM1", 225, 195);
  image(cam2, 475, 50, 250, 150);
  text("CAM2", 475, 195);
  image(cam3, 725, 50, 250, 150);
  text("CAM3", 725, 195);
  image(cam4, 225, 200, 250, 150);
  text("CAM4", 225, 345);
  image(cam5, 475, 200, 250, 150);
  text("CAM5", 475, 345);
  image(cam6, 725, 200, 250, 150);
  text("CAM6", 725, 345);


  if (key=='1'||key=='2'||key=='3'||key=='4'||key=='5'||key=='6')background(0);

  if (key=='1') {
    image(cam1, 0, 0, 1200, 600) ;
    text("CAM1", 0, 590);
  }
  if (key=='2') {
    image(cam2, 0, 0, 1200, 600) ;
    text("CAM2", 0, 590);
  }
  if (key=='3') {
    image(cam3, 0, 0, 1200, 600) ;
    text("CAM3", 0, 590);
  }
  if (key=='4') {
    image(cam4, 0, 0, 1200, 600) ;
    text("CAM4", 0, 590);
  }
  if (key=='5') {
    image(cam5, 0, 0, 1200, 600) ;
    text("CAM5", 0, 590);
  }
  if (key=='6') {
    image(cam6, 0, 0, 1200, 600) ;
    text("CAM6", 0, 590);
  }
}
void initializeCameras() {
  frameRate(30);
  cam1=new Movie(this, "vid1.avi");
  cam2=new Movie(this, "vid2.avi");
  cam3=new Movie(this, "vid3.avi");
  cam4=new Movie(this, "vid4.avi");
  cam5=new Movie(this, "vid5.avi");
  cam6=new Movie(this, "vid6.avi");

  cam1.play();
  cam2.play();
  cam3.play();
  cam4.play();
  cam5.play();
  cam6.play();
}
void movieEvent(Movie m) {
  m.read();
}