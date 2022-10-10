# creating a random neuron

inputs = [1.2, 5.1, 2.1]  # random outputs of a previous layer
weights = [3.1, 2.1, 8.7]  # random weights equal to the number of the inputs
bias = 3  # every unique neuron has a bias

output = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + bias
print(output)
