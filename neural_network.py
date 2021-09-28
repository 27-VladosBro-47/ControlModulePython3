import random
import math
import numpy as np



class NeuralNetwork:
    def __init__(self, learningSpeed = 0.02, *layers):
        self.neuronsLayers = []
        self.d_neuronsLayers = []

        # conteins the sum of products neurons and weights
        # namely w00*x0 + w10*x1 + w20*x2...
        # uses in back propagation`s computate
        self.sum = []

        self.weights = []
        self.d_weights = []

        # First element of these list are not used
        self.bias = []
        self.d_bias = []

        self.learningSpeed = learningSpeed

        # Set list of layers
        assert len(layers) >= 3, "NeuralNetwork.__init__()\nMin layers are 3"
        for elementsOfLayer in layers:
            assert type(elementsOfLayer) == int , "NeuralNetwork.__init__()\nArgs must be integer-type"
            random.seed()
            self.neuronsLayers.append(np.array([random.uniform(0.05, 0.95) for i in range(elementsOfLayer)]))
            self.d_neuronsLayers.append(np.array([random.uniform(0.05, 0.95) for i in range(elementsOfLayer)]))
            self.sum.append(np.array([random.uniform(0.05, 0.95) for i in range(elementsOfLayer)]))
            random.seed()
            self.bias.append(np.array([random.uniform(0.05, 0.95) for i in range(elementsOfLayer)]))
            self.d_bias.append(np.array([random.uniform(0.05, 0.95) for i in range(elementsOfLayer)]))

        for countOfLayer in range(len(self.neuronsLayers)-1):
            self.weights.append([])
            self.d_weights.append([])
            for weights in range(self.neuronsLayers[countOfLayer+1].size):
                random.seed()
                self.weights[countOfLayer].append(np.array([random.uniform(-1.2, 1.2) for i in range(self.neuronsLayers[countOfLayer].size)]))
                self.d_weights[countOfLayer].append(np.array([random.uniform(-1.2, 1.2) for i in range(self.neuronsLayers[countOfLayer].size)]))

    def debug_showNeuronsLayers(self):
        print("======================================")
        print("NeuronsLayers")
        for i in self.neuronsLayers:
            print(f"{i}")
        print("======================================")

    def debug_show_D_NeuronsLayers(self):
        print("======================================")
        print("D-NeuronsLayers")
        for i in self.d_neuronsLayers:
            print(f"{i}")
        print("======================================")

    def debug_showWeights(self):
        print("======================================")
        print("Weights")
        for count1, elem1 in enumerate(self.weights):
            print("LAYER", count1)
            for count2, elem2 in enumerate(elem1):
                #print("WEIGHTS", count2)
                print(elem2)
        print("======================================")

    def debug_show_D_Weights(self):
        print("======================================")
        print("D-Weights")
        for count1, elem1 in enumerate(self.d_weights):
            print("LAYER", count1)
            for count2, elem2 in enumerate(elem1):
                #print("WEIGHTS", count2)
                print(elem2)
        print("======================================")

    def debug_showBias(self):
        print("======================================")
        print("Bias")
        for i in self.bias:
            print(f"{i}")
        print("======================================")

    def debug_show_D_Bias(self):
        print("======================================")
        print("D-Bias")
        for i in self.d_bias:
            print(f"{i}")
        print("======================================")

    def debug_showLastLayer(self):
        print("Last layer:")
        for count, value in enumerate(self.neuronsLayers[len(self.neuronsLayers)-1]):
            print(f"neuron[{count}] = {value}")

    def derivativeSigm(self, x):
        return (self.sigm(x) * (1 - self.sigm(x)) + 0.000001)

    def sigm(self, x):
        return (1 / (1 + math.exp(-x)))

    def calculateNeuron(self, layerIndex, neuronIndex):
        assert (layerIndex >= 1 and layerIndex < len(self.neuronsLayers)), "NeuralNetwork.calculateNeuron()\nIncorrect index of neuron`s layer"
        assert (neuronIndex >= 0 and neuronIndex < self.neuronsLayers[layerIndex].size), "NeuralNetwork.calculateNeuron()\nIncorrect index of neurons in layer"
        
        self.sum[layerIndex][neuronIndex] = (self.neuronsLayers[layerIndex-1]*self.weights[layerIndex-1][neuronIndex]).sum()
        self.neuronsLayers[layerIndex][neuronIndex] = self.sigm( self.sum[layerIndex][neuronIndex] + self.bias[layerIndex][neuronIndex])

    def fowardPropagation(self):
        for countOfLayer in range(1,len(self.neuronsLayers)):
            for countOfNeuron in range(self.neuronsLayers[countOfLayer].size):
                self.calculateNeuron(countOfLayer,countOfNeuron)
    
    # For learning
    # Set input neurons (s-elements)
    def set_S_elements_learning(self, dataList, numbOfGesture):
        assert len(dataList) == self.neuronsLayers[0].size, "NeuralNetwork.set_S_elements_learning()\n Incorrect size of dataList"
        assert (numbOfGesture >= 0 & numbOfGesture <= (self.neuronsLayers[len(self.neuronsLayers)-1]).size), "NeuralNetwork.set_S_elements_learning()\n Incorrect number of gesture"

        npDataList = np.array(dataList)
        self.neuronsLayers[0] = npDataList.copy()

        for count in range(self.d_neuronsLayers[len(self.d_neuronsLayers)-1].size):
            self.d_neuronsLayers[len(self.d_neuronsLayers)-1][count] = 0.0
            if count == numbOfGesture:
                self.d_neuronsLayers[len(self.d_neuronsLayers)-1][count] = 1.0

    # For work
    # Set input neurons (s-elements)
    def set_S_elements_work(self, dataList):
        assert len(dataList) == self.neuronsLayers[0].size, "NeuralNetwork.set_S_elements_work()\n Incorrect size of dataList"

        npDataList = np.array(dataList)
        self.neuronsLayers[0] = npDataList.copy()

    def setDifferenceAtLastLayer(self):
        self.d_neuronsLayers[len(self.d_neuronsLayers)-1] = self.d_neuronsLayers[len(self.d_neuronsLayers)-1] - self.neuronsLayers[len(self.d_neuronsLayers)-1]
        
    def levelOfEducation(self):
        level = (self.d_neuronsLayers[len(self.d_neuronsLayers)-1]**2).sum()
        return level

    def answer(self):
        for numbOfGesture, r_element in enumerate(self.neuronsLayers[len(self.neuronsLayers)-1]):
            if r_element >= 0.75: return numbOfGesture
        
        return -1

    def work(self, dataList):
        self.set_S_elements_work(dataList)
        self.fowardPropagation()
        return self.answer()

    def learning(self, dataList, numbOfGesture):
        self.set_S_elements_learning(dataList, numbOfGesture)
        self.fowardPropagation()
        self.setDifferenceAtLastLayer()
        print("Level of education =", self.levelOfEducation())
        self.backPropagation()

    def backPropagationWeights(self, layer):
        for numbOfWeightsBlock, weightsBlock in enumerate(self.weights[layer]):
            for numbOfWeight, w in enumerate(weightsBlock):
                self.d_weights[layer][numbOfWeightsBlock][numbOfWeight] = 2*(self.d_neuronsLayers[layer+1][numbOfWeightsBlock])*self.derivativeSigm(self.sum[layer+1][numbOfWeightsBlock])*self.neuronsLayers[layer][numbOfWeight]
                      
    def backPropagationNeurons(self, layer):
        for numbOfNeuron in range(self.neuronsLayers[layer].size):
            d_sum = 0.0
            for block in range(len(self.weights[layer])):
                d_sum += 2*(self.d_neuronsLayers[layer+1][block])*self.derivativeSigm(self.sum[layer+1][block])*self.weights[layer][block][numbOfNeuron]
            
            self.d_neuronsLayers[layer][numbOfNeuron] = d_sum

    def backPropagationBias(self, layer):
        for numbOfbias in range(self.bias[layer+1].size):
            self.d_bias[layer+1][numbOfbias] = 2*(self.d_neuronsLayers[layer+1][numbOfbias])*self.derivativeSigm(self.sum[layer+1][numbOfbias])

    def setDifference(self, layer):
        self.neuronsLayers[layer] += self.learningSpeed * self.d_neuronsLayers[layer]

        for count, weightsBlock in enumerate(self.weights[layer]):
            weightsBlock += self.learningSpeed * self.d_weights[layer][count]

        self.bias[layer] += self.learningSpeed * self.d_bias[layer]

    def backPropagation(self):
        for layer in range((len(self.neuronsLayers)-2),-1,-1):
            self.backPropagationWeights(layer)
            self.backPropagationNeurons(layer)
            self.backPropagationBias(layer)

            self.setDifference(layer)
  
    def saveConfigurations(self):
        pass

    def loadConfigurations(self):
        pass

    def convertList(self, notConvertedDataList):
        dataList = []
        for element in notConvertedDataList:
            dataList.append(self.sigm(element))
        return dataList

        
def generateDataList(count):
    dataList = []

    if count == 0:
        random.seed()
        dataList.append(random.uniform(0.07, 0.12))
        random.seed()
        dataList.append(random.uniform(0.07, 0.12))
        random.seed()
        dataList.append(random.uniform(0.27, 0.32))
        random.seed()
        dataList.append(random.uniform(0.27, 0.32))
        random.seed()
        dataList.append(random.uniform(0.07, 0.12))
        random.seed()
        dataList.append(random.uniform(0.87, 0.92))
        random.seed()
        dataList.append(random.uniform(0.27, 0.32))
        random.seed()
        dataList.append(random.uniform(0.47, 0.52))
        random.seed()
        dataList.append(random.uniform(0.67, 0.72))
        random.seed()
        dataList.append(random.uniform(0.17, 0.22))
    elif count == 1:
        random.seed()
        dataList.append(random.uniform(0.87, 0.92))
        random.seed()
        dataList.append(random.uniform(0.87, 0.92))
        random.seed()
        dataList.append(random.uniform(0.07, 0.12))
        random.seed()
        dataList.append(random.uniform(0.47, 0.52))
        random.seed()
        dataList.append(random.uniform(0.47, 0.52))
        random.seed()
        dataList.append(random.uniform(0.67, 0.72))
        random.seed()
        dataList.append(random.uniform(0.57, 0.62))
        random.seed()
        dataList.append(random.uniform(0.27, 0.32))
        random.seed()
        dataList.append(random.uniform(0.07, 0.12))
        random.seed()
        dataList.append(random.uniform(0.17, 0.22))
    elif count == 2:
        random.seed()
        dataList.append(random.uniform(0.87, 0.92))
        random.seed()
        dataList.append(random.uniform(0.77, 0.82))
        random.seed()
        dataList.append(random.uniform(0.67, 0.72))
        random.seed()
        dataList.append(random.uniform(0.57, 0.62))
        random.seed()
        dataList.append(random.uniform(0.47, 0.52))
        random.seed()
        dataList.append(random.uniform(0.37, 0.42))
        random.seed()
        dataList.append(random.uniform(0.27, 0.32))
        random.seed()
        dataList.append(random.uniform(0.17, 0.22))
        random.seed()
        dataList.append(random.uniform(0.07, 0.12))
        random.seed()
        dataList.append(random.uniform(0.07, 0.12))
    elif count == 3:
        random.seed()
        dataList.append(random.uniform(0.07, 0.12))
        random.seed()
        dataList.append(random.uniform(0.07, 0.12))
        random.seed()
        dataList.append(random.uniform(0.17, 0.22))
        random.seed()
        dataList.append(random.uniform(0.27, 0.32))
        random.seed()
        dataList.append(random.uniform(0.37, 0.42))
        random.seed()
        dataList.append(random.uniform(0.47, 0.52))
        random.seed()
        dataList.append(random.uniform(0.57, 0.62))
        random.seed()
        dataList.append(random.uniform(0.67, 0.72))
        random.seed()
        dataList.append(random.uniform(0.77, 0.82))
        random.seed()
        dataList.append(random.uniform(0.87, 0.92))
    elif count == 4:
        random.seed()
        dataList.append(random.uniform(0.47, 0.52))
        random.seed()
        dataList.append(random.uniform(0.57, 0.62))
        random.seed()
        dataList.append(random.uniform(0.67, 0.72))
        random.seed()
        dataList.append(random.uniform(0.07, 0.12))
        random.seed()
        dataList.append(random.uniform(0.27, 0.32))
        random.seed()
        dataList.append(random.uniform(0.17, 0.22))
        random.seed()
        dataList.append(random.uniform(0.07, 0.12))
        random.seed()
        dataList.append(random.uniform(0.07, 0.12))
        random.seed()
        dataList.append(random.uniform(0.67, 0.72))
        random.seed()
        dataList.append(random.uniform(0.37, 0.42))
    
    return dataList

data = NeuralNetwork(0.05, 10, 100, 100, 5)


for numbOfLearningData in range(1000):
    print(f"numbOfLearningData = {numbOfLearningData}")
    count = numbOfLearningData % 5

    if(count == 5): count = 3

    print("count =", count)
    dataList = generateDataList(count)
    #print(dataList)
    data.learning(dataList, count)
    data.debug_showLastLayer()
#data.debug_showLastLayer()


dataList = generateDataList(0)
print("ans:",data.work(dataList))
dataList = generateDataList(1)
print("ans:",data.work(dataList))
dataList = generateDataList(2)
print("ans:",data.work(dataList))
dataList = generateDataList(3)
print("ans:",data.work(dataList))
dataList = generateDataList(4)
print("ans:",data.work(dataList))

'''count = 1
dataList = generateDataList(count)
#print(dataList)
data.learning(dataList, count)
data.debug_showNeuronsLayers()

data.debug_showLastLayer()'''



'''data.debug_showNeuronsLayers()
print(" ")
data.debug_showWeights()
print(" ")
data.debug_showBias()
data.calculateNeuron(1,0)
data.fowardPropagation()'''

'''data1 = NeuralNetwork(0.02, 2, 3, 3, 2)

l1 = [0.2, 0.3]
data1.learning(l1, 0)'''
