function [ theta_recta ] = TfHough(imGris,orientacio)
%TFHOUGH(imGris): retorna l'angle d'inclinació de la orientació triada
% orientacions: 'horizontal' 'vertical'

%% TRANSFORMADA DE HOUGH:
A=edge(imGris,'sobel',orientacio);    %encontramos los bordes
%figure()
%imshow(A);
[m,n]=size(A);
theta=-30:30;                           %Restringimos los angulos
lTheta=length(theta);                   %Guardamos el tamaño de theta
rho1=0:(m^2+n^2)^0.5/100:(m^2+n^2)^0.5;
lRho=length(rho1);
N=zeros(lRho,lTheta);                   %Matriu que conta les interseccions

for i=1:m,
    for j=1:n,
        if A(i,j)==1
            for k=1:lTheta,
                rho2=i*cos(theta(k)*pi/180)+j*sin(theta(k)*pi/180);
                Q=1;
                while Q<lRho
                    if(rho1(Q)<rho2 && rho2<rho1(Q+1))
                        N(Q,k)=N(Q,k)+1;
                    end
                    Q=Q+1;
                end
            end
        end
    end
end

%% Determinem l'angle d'inclinació
recta=N(1,1);
for i=1:lRho
    for j=1:lTheta
        if N(i,j)>recta
            recta=N(i,j);
            theta_recta=theta(j);
        end
    end
end

end

