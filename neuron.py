from abc import ABC, abstractmethod

class baseNeuron(ABC):
    @abstractmethod
    def getValue(self) -> float:
        pass

class neuron(baseNeuron):
    def __init__(self):
        self.trigger: float = 0.5
        self.inputNeurons: list[baseNeuron] = []
        self.inputWeights: list[float] = []
    
    def getValue(self):
        ans = 0
        i = 0
        for i, n in enumerate(inputNeurons):
            ans += n.getValue() * self.inputWeights[i]
            i += 1
        return ans / i >= self.trigger
    
class inputNeuron(baseNeuron):
    def __init__(self):
        self.value = 0.0
    
    def getValue(self):
        return self.value
    
    def setValue(self,value: float):
        self.value = value