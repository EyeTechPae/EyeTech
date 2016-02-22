function [ BW, invBW ] = binarization( filename, thr)
% binarization:
% Inputs:
%  * filename: name of the file to be binarized.
%  * threshold: threshold of the binarization. Must be between 0.0 and 1.0.
% Outputs:
%  * BW:  binarized image.
%  * invBW: inverted binarized image. 
% 
%  The image 'filename' is binarized according to the threshold 'thr' 
%  defined by the user.

[Img,Map,Alpha] = imread(filename);
Img = double(Img);

if ~isempty(Map)    % Convert indexed image to RGB
    Img = Img + 1;
    Img = reshape(cat(3,Map(Img,1),Map(Img,2),Map(Img,3)),size(Img,1),size(Img,2),3);
else
    Img = Img/255;  % Rescale to [0,1]
end
InvImg= abs(1-Img);
BW=im2bw(Img, thr);
invBW=im2bw(InvImg, thr);
figure
imshow(BW)
figure
imshow(invBW)
figure
imshow(Img)
end
