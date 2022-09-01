from os import popen
import random
from select import select
import matplotlib.pyplot as graph_plot

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

def selection(pop, k):
    popRand = []
    for x in range(k):
        popRand.append(pop[random.randint(0,len(pop)-1)])
    chosen1 = tournament(popRand)
    popRand.remove(chosen1)
    chosen2 = tournament(popRand)

    return chosen1, chosen2

def get_values(pop):
    all = map(evaluate, pop)
    all = list(all)
    highest = max(all)
    lowest = min(all)
    average = sum(all)/len(all)

    return highest, lowest, average

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
    pop = []
    graph = []
    
    for x in range(n):
        indiv = []
        for y in range(8):
            indiv.append(random.randint(1,8))
        pop.append(indiv)

    graph.append(get_values(pop))

    for x in range(g):
        popNext = []
        if e:
            popNext.append(tournament(pop))
        while len(popNext) < n:
            p1, p2 = selection(pop,k)
            o1, o2 = crossover(p1,p2,random.randint(1,8))
            o1 = mutate(o1,m)
            o2 = mutate(o2,m)
            popNext.append(o1)
            popNext.append(o2)
        pop = popNext
        graph.append(get_values(pop))

    highest_values = list(map(lambda x: x[0], graph))
    lowest_values = list(map(lambda x: x[1], graph))
    average_values = list(map(lambda x: x[2], graph))

    y = []
    for x in range(0, g+1):
        y.append(x)
    
    png, what = graph_plot.subplots()
    what.set_xlabel("Generations")
    what.set_ylabel("Fitness")
    what.set_xlim(0, g)
    what.set_ylim(0, 40)
    what.plot(y, highest_values, label="Min Fitness")
    what.plot(y, lowest_values, label="Max Fitness")
    what.plot(y, average_values, label="Avgerage Fit")
    what.legend()
    what.grid()
    png.savefig("plot.png")


    return tournament(pop)
