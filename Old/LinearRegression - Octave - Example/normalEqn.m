function theta = normalEqn(x, y)

theta = inv(x' * x) * (x' * y)
