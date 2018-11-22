import numpy as np
import math

class Resultado:
    def __init__(self, cadA, cadB, pasos, tiempo, hipA, hipB):
        self.cadA = cadA
        self.cadB = cadB
        self.pasos = pasos
        self.tiempo = tiempo
        self.largoA = len(cadA)
        self.largoB = len(cadB)
        self.hipA = math.ceil(hipA)
        self.hipB = math.ceil(hipB)

    def __str__(self):
        return "{0},{1},{2},{3},{4},{5},{6},{7}".format(self.cadA, self.largoA, self.cadB, self.largoB, self.pasos, self.tiempo, self.hipA, self.hipB)

    @staticmethod
    def Pasos(arrayResultados):
        return np.array([x.pasos for x in arrayResultados])

    @staticmethod
    def Tiempos(arrayResultados):
        return np.array([x.tiempo for x in arrayResultados])

    @staticmethod
    def HipotesisA(arrayResultados):
        return np.array([x.hipA for x in arrayResultados])

    @staticmethod
    def HipotesisB(arrayResultados):
        return np.array([x.hipB for x in arrayResultados])

    @staticmethod
    def Errores(x, y):
        arr = []
        for i in range(len(x)):
            arr.append(y[i]-x[i])
        return np.array(arr)