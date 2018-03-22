function [jVal, gradient] = costFunction(x,y,theta)

  % number of training examples
  m = length(y);

  %predicted values
  caluclated_values = (x * theta)

  % (predicted-actual)^2
  s = (caluclated_values - y).^2

  jVal = 1/(2 * m) * sum(s)

  %get the h value for this set of theta
  err = (x * theta) - y

  for i = 1: size(theta,1),
    gradient(i) = sum( err .* x(:,i))
  end
