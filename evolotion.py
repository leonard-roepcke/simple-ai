import neuronalNet
import copy

class Evolution:
    def __init__(self, values, hidenlayer=2, hidenSize=4, spread=0.4, defosion=0.99):
        self.values = values
        self.input_size = len(values[0][0])
        self.output_size = len(values[0][1])
        self.hidenlayer = hidenlayer
        self.hidenSize = hidenSize
        self.bestNet = neuronalNet.NeuronalNet(self.input_size, self.output_size, hidenlayer, hidenSize, spread)
        self.spread = spread
        self.defosion = defosion
        
    def run(self, rounds=1000, population=100):
        self.real_spread = self.spread
        for rund in range(rounds):
            print(f"Round {rund+1}/{rounds}, Best Score: {self.bestNet.score}")

            nets = [self.bestNet]  
            for _ in range(population-1):
                new_net = copy.deepcopy(self.bestNet)  
                new_net.mutate()                       
                nets.append(new_net)
            
            for net in nets:
                score = 0
                for value in self.values:
                    output = net.run(value[0])
                    expected = value[1]
                    print(f"Input: {value[0]}, Output: {[round(o, 4) for o in output]}, Expected: {expected}")
                    score -= sum([(o - e) ** 2 for o, e in zip(output, expected)])  
                
                net.score = score
                if score > self.bestNet.score:
                    self.bestNet = net
                    self.bestNet.score = score
            
            self.real_spread *= self.defosion
