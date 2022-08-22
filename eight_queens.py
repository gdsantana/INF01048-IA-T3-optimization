from random import random


def evaluate(individual):
    """
    Recebe um indivíduo (lista de inteiros) e retorna o número de ataques
    entre rainhas na configuração especificada pelo indivíduo.
    Por exemplo, no individuo [2,2,4,8,1,6,3,4], o número de ataques é 9.

    :param individual:list
    :return:int numero de ataques entre rainhas no individuo recebido
    """
    attacks = 0
    for i in range(8):
        for j in range(i+1,8):
            #mesma linha
            if individual[i]==individual[j]:
                attacks+=1
            #diagonal pra cima
            if individual[i]==individual[j] + (j-i):
                attacks+=1
            #diagonal pra baixo
            if individual[i]==individual[j] - (j-i):
                attacks+=1
    return attacks


def tournament(participants):
    """
    Recebe uma lista com vários indivíduos e retorna o melhor deles, com relação
    ao numero de conflitos
    :param participants:list - lista de individuos
    :return:list melhor individuo da lista recebida
    """
    conflitos = [evaluate(tentativa) for tentativa in participants]
    i = conflitos.index(min(conflitos))
    return participants[i]


def crossover(parent1, parent2, index):
    cross1 = parent1[:index] + parent2[index:]
    cross2 = parent2[:index] + parent1[index:]
    return cross1, cross2


def mutate(individual, m):
    """
    Recebe um indivíduo e a probabilidade de mutação (m).
    Caso random() < m, sorteia uma posição aleatória do indivíduo e
    coloca nela um número aleatório entre 1 e 8 (inclusive).
    :param individual:list
    :param m:int - probabilidade de mutacao
    :return:list - individuo apos mutacao (ou intacto, caso a prob. de mutacao nao seja satisfeita)
    """
    if random.random() < m:
        pos = random.randint(0,7)
        num = random.randint(1,8)
        individual[pos] = num
    return individual


def run_ga(g, n, k, m, e):
    """
    Executa o algoritmo genético e retorna o indivíduo com o menor número de ataques entre rainhas
    :param g:int - numero de gerações
    :param n:int - numero de individuos
    :param k:int - numero de participantes do torneio
    :param m:float - probabilidade de mutação (entre 0 e 1, inclusive)
    :param e:bool - se vai haver elitismo
    :return:list - melhor individuo encontrado
    """
    raise NotImplementedError  # substituir pelo seu codigo
