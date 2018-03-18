clear ; close all; clc

fprintf("Running\n")

data = load('ex1data2.txt')



%Set x, y, and m variables from data

m = size(data,2)
x = zeros(size(data,1),m-1)
for i = 1:m-1,
  x(:,i) = data(:,i);
end
y = data(:,m)

%m = number of examples
m = length(y)

x = normalize(x)
x = [ones(m,1),x]



theta = zeros(size(x,2),1)

% Some gradient descent settings
iterations = 2000;
alpha = 0.01;

J = getCost(x, y, theta);
fprintf('With theta = [0 ; 0]\nCost computed = %f\n', J);

[theta, cost_history] = gradDes(x,y,theta,alpha,iterations)

% print theta to screen
fprintf('Theta found by gradient descent:\n');
fprintf('%f\n', theta);

plot([1 : length(cost_history)],cost_history)
