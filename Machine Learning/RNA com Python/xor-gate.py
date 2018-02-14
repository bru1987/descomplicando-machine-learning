#!/usr/bin/env python
# -*- coding: utf-8 -*-

from numpy import exp, array, random, dot


class NeuronLayer():
    def __init__(self, number_of_neurons, number_of_inputs_per_neuron):
        self.synaptic_weights = 2 * random.random((number_of_inputs_per_neuron, number_of_neurons)) - 1


class NeuralNetwork():
    def __init__(self, layer1, layer2):
        self.layer1 = layer1
        self.layer2 = layer2

    # Função sigmóide, em formato S
    # Passamos as entradas multiplicados pelos pesos por essa função
    # para normalizar os calores entre 0 e 1.
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    # A derivada da função sigmóide
    # Este é o gradiente da curva sigmóide
    # Ela indica o quão confiante estamos com relação aos pesos existentes.
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    # Nós treinamos as redes neurais por um processo de tentativa e erro.
    # Ajustando os pesos sinápticos toda vez.
    def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
        for iteration in xrange(number_of_training_iterations):
            # Passando o set de treinamento pela rede neural
            output_from_layer_1, output_from_layer_2 = self.think(training_set_inputs)

            # Calcula o erro para a segunda camada (a diferença entre a sada desejada
            # e a saída prevista).
            layer2_error = training_set_outputs - output_from_layer_2
            layer2_delta = layer2_error * self.__sigmoid_derivative(output_from_layer_2)

            # Calcula o erro para a primeira camada (olhando para os pesos da primeira camada,
            # podemos determinar o quanto a camada 1 contribuiu para o erro da camada 2).
            layer1_error = layer2_delta.dot(self.layer2.synaptic_weights.T)
            layer1_delta = layer1_error * self.__sigmoid_derivative(output_from_layer_1)

            # Calcula por quanto ajustar os pesos
            layer1_adjustment = training_set_inputs.T.dot(layer1_delta)
            layer2_adjustment = output_from_layer_1.T.dot(layer2_delta)

            # Ajuste dos pesos
            self.layer1.synaptic_weights += layer1_adjustment
            self.layer2.synaptic_weights += layer2_adjustment

    # A rede neural pensa!
    def think(self, inputs):
        output_from_layer1 = self.__sigmoid(dot(inputs, self.layer1.synaptic_weights))
        output_from_layer2 = self.__sigmoid(dot(output_from_layer1, self.layer2.synaptic_weights))
        return output_from_layer1, output_from_layer2

    # A rede neural escreve seus pesos
    def print_weights(self):
        print ("    Camada 1 (4 neurônios, cada um com 3 entradas): ")
        print ("self.layer1.synaptic_weights")
        print ("    Camada 2 (1 neurônio, cada um com 4 entradas):")
        print ("self.layer2.synaptic_weights")

if __name__ == "__main__":

    # Geração de números aleatórios
    random.seed(1)

    # Criação da camada 1 (4 neurônios, cada um com 3 entradas)
    layer1 = NeuronLayer(4, 3)

    # Criaço da camada 2 (um único neurônio com 4 entradas)
    layer2 = NeuronLayer(1, 4)

    # Combina as camadas para criar uma rede neural
    neural_network = NeuralNetwork(layer1, layer2)

    print ("Valores aleatórios de pesos sinápticos: ")
    neural_network.print_weights()

    # O set de treinamento. Temos 7 exemplos, cada um consistindo de 3 valores de entrada
    # e 1 valor de sada
    training_set_inputs = array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1], [0, 0, 0], [1,1,0] ])
    training_set_outputs = array([[1, 0, 0, 1, 1, 0, 0, 0]]).T

    # Treinando a rede neural usando um training set
    # Número de iterações: 60000.
    neural_network.train(training_set_inputs, training_set_outputs, 60000)

    print ("Novos pesos sinápticos após treinamento:  ")
    neural_network.print_weights()

    # Testando a rede neural com a nova situação
    print ("Considerando a nova situação [1, 1, 0] -> ?: ")
    hidden_state, output = neural_network.think(array([1, 1, 0]))
    print ("output")
