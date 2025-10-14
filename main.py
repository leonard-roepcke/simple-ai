import time
import neuronalNet
print("init ai at: " + str(time.time()))

n1 = neuronalNet.NeuronalNet(2,1,2,4)
print(n1.run([0, 1]))