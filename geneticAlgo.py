import random

def generate_gene():
    return [random.randint(0, 7) for _ in range(8)]
    
def fitness(gene) :
    score = 0
    for i in range(8) :
        row = gene[i]
        for j in range(8) :
           if row == gene[j] and i == j :
               continue
           if abs(row - gene[j]) == abs(i - j) :
               continue
           if row - gene[j] == 0 :
               continue
           if i - j == 0 :
               continue
           score += 1 
           
    return score/2 
    
def probability(gene, fitness) :
    return fitness(gene)/28
    
def reproduce(x, y) :
    cut_index = random.randint(0, 8)
    return x[0:cut_index] + y[cut_index:8]
    
def mutate(x) :
    c = random.randint(0, 7)
    m = random.randint(1, 8)
    x[c] = m
    return x
    
def genetic_queen(population) :
    new_generation = []
    generator = 1
    child = population[0]
    #probabilities = [probability(n, fitness) for n in population]
    for i in range(len(population)) :
        x = population[random.randint(0, len(population)-1)]
        y = population[random.randint(0, len(population)-1)]
        if fitness(x) < fitness(child) :
            x = child
        if fitness(x) < fitness(y) :
            x = y
        while x != y :
            y = population[random.randint(0, len(population)-1)]
        child = reproduce(x, y)
        #if random.random() < 0.03 :
        child = mutate(child)
        #new_generation.append(child)
        f = fitness(child)
        print("Generator : ",end=' ')
        print(generator)
        print(child, end='')
        print(" : ", end='')
        print(f)
        generator+=1
        if fitness(child) == 28 :
            print("solution found")
            break
    #return new_generation    

population = []
for _ in range(100) :
    population.append(generate_gene())
genetic_queen(population)