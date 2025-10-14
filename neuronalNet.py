import neuron

class NeuronalNet:
    def __init__(self):
        self.b = neuron.inputNeuron()
        self.a = neuron.inputNeuron()
        self.n = neuron.neuron([self.a, self.b])

        
    def run(self, input = [0, 0]):
        self.a.setValue(input[0])
        self.b.setValue(input[1])
        return self.n.getValue()

    def mutate(self):
        self.n.mutate()
