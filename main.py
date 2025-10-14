import time
import neuron
print("init ai at: " + str(time.time()))

inputNeuron = neuron.inputNeuron()
outputNeuron = neuron.neuron([inputNeuron])

inputNeuron.setValue(1)
print(outputNeuron.getValue)