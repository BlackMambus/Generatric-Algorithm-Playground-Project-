import random
import matplotlib.pyplot as plt

# 🎯 Target string to evolve
TARGET = "1010101010101010"
POP_SIZE = 100
MUTATION_RATE = 0.01
GENERATIONS = 100

# 🧬 Individual representation
def random_individual(length):
    return ''.join(random.choice('01') for _ in range(length))

def fitness(individual):
    return sum(1 for i, j in zip(individual, TARGET) if i == j)

def mutate(individual):
    return ''.join(
        bit if random.random() > MUTATION_RATE else random.choice('01')
        for bit in individual
    )

def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:]

def select(population):
    sorted_pop = sorted(population, key=fitness, reverse=True)
    return sorted_pop[:2]  # Elitism: top 2

# 🧪 Main GA loop
def run_ga():
    population = [random_individual(len(TARGET)) for _ in range(POP_SIZE)]
    best_fitness = []

    for generation in range(GENERATIONS):
        new_population = []
        parents = select(population)
        best = max(population, key=fitness)
        best_fitness.append(fitness(best))

        while len(new_population) < POP_SIZE:
            child = mutate(crossover(*parents))
            new_population.append(child)

        population = new_population
        print(f"Gen {generation}: Best = {best} Fitness = {fitness(best)}")

        if fitness(best) == len(TARGET):
            print("🎉 Target reached!")
            break

    return best_fitness

# 📊 Plotting fitness over generations
def plot_fitness(fitness_history):
    plt.plot(fitness_history)
    plt.title("Fitness Over Generations")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    history = run_ga()
    plot_fitness(history)



