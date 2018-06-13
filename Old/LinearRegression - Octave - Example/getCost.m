function J = getCost(x, y, theta)
%COMPUTECOST Compute cost for linear regression
%   J = getCost(x, y, theta) computes the cost of using theta as the
%   parameter for linear regression to fit the data points in X and y

% number of training examples
m = length(y);

%predicted values
caluclated_values = x * theta

% (predicted-actual)^2
s = (caluclated_values - y).^2

J = 1/(2 * m) * sum(s)
