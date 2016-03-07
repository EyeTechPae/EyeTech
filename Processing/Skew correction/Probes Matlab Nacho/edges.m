imatge=imread('mat2.jpg');
imGris=rgb2gray(imatge);
%imshow(imGris)
[m,n]=size(imGris)
 for i=1:m/2
     for j=1:n
         horsup(i,j)=imGris(i,j);
     end
 end
imshow(horsup)

%A=imGris(0:round(m/2),:;0:4,:)
angle1=TfHough(C,'horizontal')

%D=imrotate(C,-angle1);
%figure()
%imshow(D)

%% 
