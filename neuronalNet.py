import neuron

class NeuronalNet:
    def __init__(self, inputSize:int, outputSize, hidenLayer, hidenSize):
        # self.b = neuron.inputNeuron()
        # self.a = neuron.inputNeuron()
        # self.n = neuron.neuron([self.a, self.b])

        self.inputs = [neuron.inputNeuron() for _ in range(inputSize)]
        self.hidenlayer = []
        for layer in range(hidenLayer):
            self.hidenlayer.append([])
            for _ in range(hidenLayer):
                if layer == 0:
                    self.hidenlayer[-1].append(neuron.neuron(self.inputs))
                else:
                    self.hidenlayer[-1].append(neuron.neuron(self.hidenlayer[-2]))
        self.outputs = [neuron.neuron(self.hidenlayer[-1])] * outputSize

        
    def run(self, input):

        [inputNeuron.setValue(i) for i, inputNeuron in zip(input, self.inputs)]

        return [output.getValue() for output in self.outputs]

    def mutate(self):
        for layer in self.hidenlayer:
            for neuron in layer:
                neuron.mutate()
        
        for neuron in self.outputs:
            neuron.mutate()