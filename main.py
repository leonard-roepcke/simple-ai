import time
import neuron
print("init ai at: " + str(time.time()))

b = neuron.inputNeuron()
a = neuron.inputNeuron()

a.setValue(1.0)
b.setValue(0.0)

n = neuron.neuron([a, b])
print(n.getValue()) 

for i in range(50):
    n.mutate()
    print(n.getValue())
