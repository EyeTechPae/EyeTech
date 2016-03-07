imatge=imread('matricula.png');
imGris=rgb2gray(imatge);

a=ones(10,5);
h=ones(9)/9;    %box
Id=double(imGris);
If=imfilter(Id,h);  %filtro box
subplot(2,2,1)
imshow(If);

subplot(2,2,2)
If2=If>10;
imf=imfilter(If2,a);
imshow(imf-If)