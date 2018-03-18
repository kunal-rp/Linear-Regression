function [theta, J_history] = gd(x, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = gd(X, y, theta, alpha, num_iters) updates theta by
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples

%for each theta will keep track of the cost
J_history = zeros(num_iters, 1);



for iter = 1:num_iters,

    %get the h value for this set of theta
    err = (x * theta) - y

    for i = 1: size(theta,1),
      theta(i) = theta(i) - (alpha / m) * sum( err .* x(:,i))
    end



    % Save the cost J in every iteration
    J_history(iter) = getCost(x, y, theta);

end
