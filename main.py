import time
import neuronalNet
print("init ai at: " + str(time.time()))

n1 = neuronalNet.NeuronalNet()
for i in range(100):
    n1.mutate()
    print(n1.run([1, 0]))