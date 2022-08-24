import numpy as np
import pandas as pd

def compute_mse(theta_0, theta_1, data):
    
    
    
    summation = 0 
   
    n = len(data)
    
    for i in range (0,n): 
        h = theta_0 + (theta_1*data[i, 0])
        squared_diff = (h - data[i, 1])**2
        summation = summation + squared_diff
    MSE = summation/n
    #print(MSE) 
    return MSE
    
    


def step_gradient(theta_0, theta_1, data, alpha):
    thetas = []
    summationf0 = 0
    summationf1 = 0
    
    n = len(data)
    for i in range (0,n): 
        h = theta_0 + (theta_1*data[i, 0])
        summationf0 += (h - data[i, 1])
        summationf1 += (h - data[i, 1])*(data[i, 0])
    
    
    

    d0 = 2*summationf0/n
    theta_0 = theta_0 - (alpha*d0)
    thetas.append(theta_0)
    
    d1 = 2*summationf1/n
    theta_1 = theta_1 - (alpha*d1)
    thetas.append(theta_1)
    
    

    return thetas


def fit(data, theta_0, theta_1, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de theta_0 e theta_1.
    Ao final, retorna duas listas, uma com os theta_0 e outra com os theta_1
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os theta_0 e outra com os theta_1 obtidos ao longo da execução
    """
    list_of_thetas0 = []
    list_of_thetas1 = []
    list_of_all_thetas = []

    theta0,theta1 = step_gradient(theta_0,theta_1,data,alpha)
    list_of_thetas0.append(theta0)
    list_of_thetas1.append(theta1)
    
    
    
    for i in range (0,num_iterations): 
        theta0,theta1 = step_gradient(theta0,theta1,data,alpha)
        list_of_thetas0.append(theta0)
        list_of_thetas1.append(theta1)
    
    list_of_all_thetas.append(list_of_thetas0)
    list_of_all_thetas.append(list_of_thetas1)
    
    #print(list_of_all_thetas)
    return list_of_all_thetas



