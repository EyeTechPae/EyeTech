//this class loads all the plates from plates.txt and display the last 5 plates
//in MODE ALL, in MODE PLATES display the full list with the times.
class Plates {
  PVector posP, rotP;
  String plates[];
  Plates(PVector _rot, PVector _pos) {
    posP=_pos;
    rotP=_rot;
    plates=loadStrings("plates.txt");
  }

  void displayPlatesModeALL() {
    String plates[]=loadStrings("plates.txt");
    pushMatrix();
    rotateX(this.rotP.x);
    rotateY(this.rotP.y);
    rotateZ(this.rotP.z);

    translate(this.posP.x, this.posP.y, this.posP.z); 
    textFont(font2);
    fill(#A1A29A);
    rect(0, 0, 100, 150, 8);
    fill(#61625A);
    rect(0, 0, 100, 30, 8);
    fill(255);
    text(" LAST 5 PLATES", 0, 20);
    fill(0);
    for (int i=0; i<5; i++) {
      text(plates[i], 10,45+i*25);
    }
    popMatrix();
  }
  void displayPlatesMode1(){
    background(191,242,238);
   String plates[]=loadStrings("plates.txt");
   textFont(font2);
   fill(0);
   for(int i=0;i<50;i++){
     text(plates[i]+nf(hour(),2) +"-"+ nf(minute(),2) +"-"+ nf(second(),2),20,20+25*i);
   }
   println(plates.length);
  }
  void update(){
    
  }
}