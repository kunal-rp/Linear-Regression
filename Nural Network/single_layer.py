from numpy import exp, array, random, dot

class NeuralNetwork():
	def __init__(self):
		#seed the random number , so it generates the same number every time
		#the program runs
		#random.seed(1)

		#We model a single neuron, with 3 inputs and 1 output
		#we assign random weights to the 3 X 1 matrix , with range of -1 to 1
		#the mean of the weights will be zero
		self.synaptic_weights = 2 * random.random((3,1)) - 1


	#the sigmoid function , which describes a s shaped curve
	# we pass the weighted sum from the inputs
	# will normalize between 0 and 1
	def __sigmoid(self, x):
		return 1 / (1 + exp(-x))



	#gradient of the sigmoid curve
	def __sigmoid_derivative(self, x):
		return x * (1 - x)



	def train(self, training_inputs, training_outputs, number_iterations):
		for iterations in xrange(number_iterations):
			#pass the training data throgh the neural network
			output = self.predict(training_inputs)


			#calculate the error
			error = training_outputs - output


			#multiply the error by the input and again by the gradient of the
			#sigmoid curve
			adjustment = dot(training_inputs.T, error * self.__sigmoid_derivative(output))

			#adjust the weights
			self.synaptic_weights += adjustment

	#pass inputs through our neural network
	def predict(self, inputs):

		return self.__sigmoid(dot(inputs, self.synaptic_weights))

if __name__ == '__main__':

	#initialize single neuron neural network
	neural_network = NeuralNetwork()

	print 'Random starting synaptic weights'
	print neural_network.synaptic_weights

	#training set
	training_inputs = array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
	training_outputs = array([0,1,1,0]).T

	#train the neural network using the training set
	#do 10000 times and make small adujtments every time
	neural_network.train(training_inputs,training_outputs,10000)

	print 'New synaptic weights'
	print neural_network.synaptic_weights

	#Test the neural network
	print '[1,0,0] ->'
	print neural_network.predict(array([1,0,0]))
