function fourier(f1,f2,f3);

points = 200; %number of points you want
m = 100.0; %Points/2
x = zeros(points);

for n = 1:points    %Create the Fourier grid
    x(n) = -pi + (n/m)*pi;
end


y = cos(f1*x)+sin(f3*x)+cos(f2*x);

ck = zeros(points);
for k = 1:points    
    for t =1:points
        ck(k) = ck(k) + y(t)*exp(1j*k*pi*t/m);
    end
end


k = zeros(points);
for n =1:points
    k(n) = n;
end
subplot(2,1,1)
plot(x,y)
subplot(2,1,2)
plot(k,abs(ck-1j*ck))
xlim([0 50])

