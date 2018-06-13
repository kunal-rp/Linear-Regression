

fprintf("Running\n")

data = load('ex1data1.txt')

%Set x, y, and m variables from data
m = size(data,2)
x = zeros(size(data,1),m-1)
for i = 1:m-1,
  x(:,i) = data(:,i);
end
y = data(:,m)
m = length(y)

%normalize X values ; add extra column of 1's for X0
%x = normalize(x)
x = [ones(m,1),x]


%set theta values to )'s ; get current cost
theta = zeros(size(x,2),1)


options = optimset('GradObj', 'on', 'MaxIter', 100);
[optTheta, functionVal, exitFlag] = fminunc(@costFunction(x,y,theta),theta,options);
