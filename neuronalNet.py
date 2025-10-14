import neuron
import math

def softmax(values):
    exp_values = [math.exp(v) for v in values]
    total = sum(exp_values)
    return [v / total for v in exp_values]


class NeuronalNet:
    def __init__(self, inputSize:int, outputSize, hidenLayer, hidenSize, mutation_rate=0.6):
        # self.b = neuron.inputNeuron()
        # self.a = neuron.inputNeuron()
        # self.n = neuron.neuron([self.a, self.b])
        self.score = -float('inf')
        self.mutation_rate = mutation_rate

        self.inputs = [neuron.inputNeuron() for _ in range(inputSize)]
        self.hidenlayer = []
        for layer in range(hidenLayer):
            self.hidenlayer.append([])
            for _ in range(hidenLayer):
                if layer == 0:
                    self.hidenlayer[-1].append(neuron.neuron(self.inputs))
                else:
                    self.hidenlayer[-1].append(neuron.neuron(self.hidenlayer[-2]))
        self.outputs = [neuron.neuron(self.hidenlayer[-1]) for _ in range(outputSize)]


        
    def run(self, input):

        for i, inputNeuron in zip(input, self.inputs):
            inputNeuron.setValue(i)

        return softmax([output.getFloatValue() for output in self.outputs])

    def mutate(self):
        for layer in self.hidenlayer:
            for neuron in layer:
                neuron.mutate(self.mutation_rate)
        
        for neuron in self.outputs:
            neuron.mutate(self.mutation_rate)