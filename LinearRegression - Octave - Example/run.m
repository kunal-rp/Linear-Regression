clear ; close all; clc

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
x = normalize(x)
x = [ones(m,1),x]


%set theta values to )'s ; get current cost
theta = zeros(size(x,2),1)
J = getCost(x, y, theta);
fprintf('With theta = [0 ; 0]\nCost computed = %f\n', J);

% Perform gradient descent
iterations = 100;
alpha = 0.3;
[theta, cost_history] = gradDes(x,y,theta,alpha,iterations)

% print results
fprintf('Theta found by gradient descent:\n');
fprintf('%f\n', theta);

%plot the cost history
plot([1 : length(cost_history)],cost_history)

fprintf('Theta found by normal equation:\n');
theta = normalEqn(x,y)
