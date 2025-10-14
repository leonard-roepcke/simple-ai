import time
import neuronalNet
print("init ai at: " + str(time.time()))

n1 = neuronalNet.NeuronalNet(2, 2, 2, 4)
for _ in range(10):
    n1.mutate()
    print(n1.run([0, 1]))