class Car{
  int state;
  PVector rotation;
  PVector position;
  PVector randomRotation,randomPosition,originalRotation, originalPosition;
  
  
  Car(int _state, PVector _rotation, PVector _position){
   state=_state;
   rotation=_rotation.get();
   position=_position.get();
   
    originalRotation=_rotation.get();
    originalPosition=_position.get();
    randomRotation=randomRotation.random3D();
    randomRotation.mult(2);
    randomPosition=randomPosition.random3D();
    randomPosition.mult(3000);
    position=randomPosition.get();
    rotation=randomRotation.get();
    
   
  }
  void display(){
    pushMatrix();
   rotateX(rotation.x);
   rotateY(rotation.y+PI/2);
   rotateZ(rotation.z);
   translate(position.x,position.y,position.z);
   shape(whiteCar);
   if(state==0)whiteCar.setFill(#02BF3C);
   if(state==1)whiteCar.setFill(#C62020);

   popMatrix();
  }
  void initCar(){
    position.x=position.x+(originalPosition.x-position.x)*0.1;
    position.y=position.y+(originalPosition.y-position.y)*0.1;
    position.z=position.z+(originalPosition.z-position.z)*0.1;

    rotation.x=rotation.x+(originalRotation.x-rotation.x)*0.1;
    rotation.y=rotation.y+(originalRotation.y-rotation.y)*0.1;
    rotation.z=rotation.z+(originalRotation.z-rotation.z)*0.1;
    
  }
  
 
}
    
  