%   normalize(X) returns a normalized version of X
% X_norm  : the normalized values of X
% me    : the mean value of X
% st     : the standard deviation of X

function [X_norm] = normalize(X)


X_norm = X;
numofcolumns = size(X_norm,2);

me = zeros(1, numofcolumns);
st = zeros(1, numofcolumns);
for i = 1 : numofcolumns,
  me(:,i) = mean(X_norm(:,i))
  X_norm(:,i) = X_norm(:,i) - me(:,i);

  st(:,i) = std(X_norm(:,i));
  X_norm(:,i) = X_norm(:,i) / st(:,i);
end
