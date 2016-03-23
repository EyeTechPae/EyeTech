class Available{
  PVector pos,rot;
  int free,total;
  Available(PVector _rot, PVector _pos,int _free, int _total){
    rot=_rot;
    pos=_pos;
  free=_free;
  total=_total;
  }
  void displayAvailable(){
free=m.currentFreeCars;
total=m.carNumber;
  pushMatrix();
     translate(pos.x, pos.y, pos.z);

  rotateX(rot.x);
    rotateY(rot.y+millis()*0.0007);
    rotateZ(rot.z);
  
pushMatrix();
    fill(0,250,10);
    translate(0,(free)*200/total/(-2),0);
    box(50,(free)*200/total,50);
    popMatrix();
    
     fill(200,100,50,50);
    translate(0,-200/2,0);
    box(55,200,55);
   
    popMatrix();
  }
}