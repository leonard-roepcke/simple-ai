from abc import ABC, abstractmethod

class baseNeuron(ABC):
    @abstractmethod
    def getValue(self) -> float:
        pass


class neuron(baseNeuron):
    def __init__(self, connectedNeurons: list['baseNeuron']):
        self.trigger: float = 0.5
        self.inputNeurons: list[baseNeuron] = connectedNeurons
        self.inputWeights: list[float] = [1.0] * len(connectedNeurons)
    
    def getValue(self):
        if not self.inputNeurons:  # Vermeidung Division durch 0
            return 0.0
        
        total = 0.0
        for i, n in enumerate(self.inputNeurons):
            total += n.getValue() * self.inputWeights[i]

        return 1.0 if total >= self.trigger else 0.0  # explizit 0/1 zurückgeben


class inputNeuron(baseNeuron):
    def __init__(self):
        self.value = 0.0
    
    def getValue(self):
        return self.value
    
    def setValue(self, value: float):
        self.value = value
