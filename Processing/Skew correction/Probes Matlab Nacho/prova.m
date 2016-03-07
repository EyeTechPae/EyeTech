imatge=imread('matriculah.png');
imGris=rgb2gray(imatge);
[m,n]=size(imGris);
U=zeros(m,n);
S=U;
h=ones(9)/9;    %box
Id=double(imGris);
If=imfilter(Id,h);  %filtro box

%filtro sobel
Hx=[-0.5, 0, 0.5];
Hy=[-0.5; 0; 0.5];

Ix=imfilter(If,Hx);
Iy=imfilter(If,Hy);

HE11=Ix.*Ix;
HE12=Ix.*Iy;
HE22=Iy.*Iy;

%filtro gausiano
Hg=(1/57)*[0 1 2 1 0
    1 3 5 3 1
    2 5 9 5 2
    1 3 5 3 1
    0 1 2 1 0];

A=imfilter(HE11,Hg);
B=imfilter(HE22,Hg);
C=imfilter(HE12,Hg);

alpha=0.04; %sensibilitat de detecció

Rp=A+B;
Rp1=Rp.*Rp;
Q=((A.*B)-(C.*C))-(alpha*Rp1);
U=Q>1000;

pixel=0;

for r=1:m
    for c=1:n
        if (U(r,c))
            
            I1=[r-pixel 1];
            I2=[r+pixel m];
            I3=[c-pixel 1];
            I4=[c+pixel n];
            
            datxi=max(I1);
            datxs=max(I2);
            datyi=max(I3);
            datys=max(I4);
            
            Bloc=Q(datxi:1:datxs,datyi:1:datys);
            
            MaxB=max(max(Bloc));
            
            if (Q(r,c)==MaxB)
                S(r,c)=1;
            end
        end
    end
end
imshow(imGris);
hold on;

for r=1:m
    for c=1:n
        if (S(r,c))
            plot(c,r,'+');
        end
    end
end



