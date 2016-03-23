class Map {
  Car[] cars;

  PVector rotation;
  PVector position1, positionAll, originalPosition;
  int carNumber;
  int currentFreeCars;

  Map(PVector _rotation, PVector _position1, PVector _positionAll) {

    rotation=_rotation.get();
    position1=_position1.get();
    positionAll=_positionAll.get();
    originalPosition=positionAll.get();
    // initialize all cars
    PVector pos, rot;
    carNumber=20;//!!
    int currentFreeCars=0;

    cars=new Car[carNumber];
    rot=new PVector(0, 0, 0);
    pos=new PVector(-40,52,405);
    cars[0]=new Car(0, rot, pos);
    rot.set(0, 0, 0);
    pos.set(-40,52,387);
    cars[1]=new Car(0, rot, pos);
    rot.set(0, 0, 0);
    pos.set(-40,52,372);
    cars[2]=new Car(0, rot, pos);
    rot.set(0, 0, 0);
    pos.set(-40,52,360);
    cars[3]=new Car(0, rot, pos);
    rot.set(0, 0, 0);
    pos.set(-40,52,348);
    cars[4]=new Car(0, rot, pos);
    rot.set(0, 0, 0);
    pos.set(-40,52,336);
    cars[5]=new Car(0, rot, pos);
    rot.set(0, 0, 0);
    pos.set(-40,52,324);
    cars[6]=new Car(0, rot, pos);
    rot.set(0, 0, 0);
    pos.set(-40,52,312);
    cars[7]=new Car(0, rot, pos);
    rot.set(0, 0, 0);
    pos.set(-40,52,300);
    cars[8]=new Car(0, rot, pos);
    rot.set(0, 0, 0);
    pos.set(-40,52,288);
    cars[9]=new Car(0, rot, pos);
    rot.set(0, 0, 0);
    pos.set(-40,52,276);
    cars[10]=new Car(0, rot, pos);
    
    ////cars[1]=new Car(0, rot, pos);
    rot.set(0, 0, 0);
    pos.set(-40,52,257);
    cars[11]=new Car(0, rot, pos);
    rot.set(0, 0, 0);
    pos.set(-40,52,243);
    cars[12]=new Car(0, rot, pos);
    rot.set(0, 0, 0);
    pos.set(-40,52,197);
    cars[13]=new Car(0, rot, pos);
    rot.set(0, 0, 0);
    pos.set(-40,52,183);
    cars[14]=new Car(0, rot, pos);
    rot.set(0, 0, 0);
    pos.set(-40,52,324);
    cars[15]=new Car(0, rot, pos);
    rot.set(0, 0, 0);
    pos.set(-40,52,312);
    cars[16]=new Car(0, rot, pos);
    rot.set(0, 0, 0);
    pos.set(-40,52,300);
    cars[17]=new Car(0, rot, pos);
    rot.set(0, 0, 0);
    pos.set(-40,52,288);
    cars[18]=new Car(0, rot, pos);
    rot.set(0, 0, 0);
    pos.set(-40,52,276);
    cars[19]=new Car(0, rot, pos);
    
    
  }
  
  /*  void displayModeMAP() {
   //this mode shows the rotating parking and hide the cameras
   //hide cameras
   background(0);
   
   //translate(600,300,0);
   pushMatrix();   
   rotateX(rotation.x);
   rotateY(rotation.y+millis()*0.0005);
   rotateZ(rotation.z+PI);
   translate(position2.x, position2.y, position2.z);
   for (int i=0; i<cars.length; i++) {
   cars[i].display();
   }
   shape(parking);
   popMatrix();
   } */
  void displayModeALL() {
    m.update();

    pushMatrix();   
    translate(positionAll.x, positionAll.y, positionAll.z);
    rotateX(rotation.x);
    rotateY(rotation.y);
    rotateZ(rotation.z+PI);
    for (int i=0; i<cars.length; i++) {
      cars[i].display();
    }
    parking.setFill(#6497A5);
    shape(parking);
   
    popMatrix();
  }



  void update() {
    int free=0;
    String data[]=loadStrings("data.txt");
    for (int i=0; i<carNumber; i++) {
      cars[i].state=int(data[i]);
      if (cars[i].state==0)free++;
    }
    currentFreeCars=free;
    carNumber=cars.length;
  }
  void initCars() {
    for (int i=0; i<m.cars.length; i++) {
      cars[i].initCar();
    }
  }
}