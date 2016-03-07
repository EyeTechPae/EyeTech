imatge=imread('matricula.png');
imGris=rgb2gray(imatge);

h=ones(9)/9;    %box
Id=double(imGris);
If=imfilter(Id,h);  %filtro box

h2=ones(5)/5;    %box
Id2=double(imGris);
If2=imfilter(Id2,h2);

subplot(2,2,1)
imshow(If-If2)

subplot(2,2,2)
If2=If>10
imshow(If2)
%filtro sobel
Hx=[-0.5, 0, 0.5];
Hy=[-0.5; 0; 0.5];
h=conv(Hx,Hy)
Hg=(1/57)*[0 1 2 1 0
    1 3 5 3 1
    2 5 9 5 2
    1 3 5 3 1
    0 1 2 1 0];
sobels=[-1 -2 -1
    0 0 0
    1 2 1]
ss=sobels';

Ix=imfilter(If2,sobels);
Iy=imfilter(If2,Hg);
subplot(2,2,3)
imshow(Ix)
subplot(2,2,4)

imshow(Iy)
