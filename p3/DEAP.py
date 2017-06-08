import random
import math
import numpy as np

import config

from deap import base
from deap import creator
from deap import tools
from deap import algorithms

# # Read your ANN structure from "config.py":
# num_inputs = config.nnet['n_inputs']
# num_hidden_nodes = config.nnet['n_h_neurons']
# num_outputs = config.nnet['n_outputs']

# my_game = p3.main()
# best = []

# creator.create("FitnessMax", base.Fitness, weights = (1.0,))
# creator.create("Individual", list, fitness = creator.FitnessMax)

# toolbox = base.Toolbox()
# # Prepare your individuals below.
# toolbox.register("attr_real", random.uniform, 0, 1)
# toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_real, 14)
# toolbox.register("population", tools.initRepeat, list, toolbox.individual, n = config.game['n_agents'])

# # Fitness Evaluation:
# def evalANN(individual):
#     return ,
#     # comma at the end is necessarys since DEAP stores fitness values as a tuple

# toolbox.register("evaluate", evalANN)

# # Define your selection, crossover and mutation operators below:
# toolbox.register("mate", tools.cxUniform)
# toolbox.register("mutate", tools.mutGaussian, indpb = 0.05)
# toolbox.register("select", tools.selBest, tournsize = 10)
# toolbox.register("map", map)


# # Define EA parameters: n_gen, pop_size, prob_xover, prob_mut:
# # You can define them in the "config.py" file too.
# # ...
# CXPB, MUTPB, NGEN = 0.5, 0.2, 50
# pop = toolbox.population()
# # Create initial population (each individual represents an agent or ANN):
# for ind in pop:
#     # ind (individual) corresponds to the list of weights
#     # ANN class is initialized with ANN parameters and the list of weights
#     ann = ANN(num_inputs, num_hidden_nodes, num_outputs, ind)
#     my_game.add_agent(ann)

# # Let's evaluate the fitness of each individual.
# # First, simulation should be run!
# my_game.game_loop(False) # Set it to "False" for headless mode;
# #recommended for training, otherwise learning process will be very slow!
    
# # Let's collect the fitness values from the simulation using
# fitnesses = list(map(toolbox.evaluate, pop))
# for ind, fit in zip(pop, fitnesses):
#     ind.fitness.values = fit

# data = []

# for g in range(1, NGEN):
#     # Start creating the children (or offspring)
#     # First, Apply selection:
#     offspring = toolbox.select(pop, len(pop))
        
#     # Apply variations (xover and mutation), Ex: algorithms.varAnd(?, ?, ?, ?)
#     # offspring = algorithms.varAnd(pop, toolbox, CXPB, MUTPB)

#     offspring = [toolbox.clone(ind) for ind in pop]

#     for child1, child2 in zip(pop[::2], pop[1::2]):
#         if random.random() < CXPB:
#             toolbox.mate(child1, child2)
#             del child1.fitness.values
#             del child2.fitness.values

#     for mutant in offspring:
#         if random.random() < MUTPB:
#             toolbox.mutate(mutant)
#             del mutant.fitness.values

#     # Repeat the process of fitness evaluation below. You need to put the recently
#     # created offspring-ANN's into the game (Line 55-69) and extract their fitness values:
#     for ind in offspring:
#         ann = ANN(num_inputs, num_hidden_nodes, num_outputs, ind)

#     fits = list(map(toolbox.evaluate, offspring))
#     for ind, fit in zip(offspring, fits):
#         ind.fitness.values = fit

#     # One way of implementing elitism is to combine parents and children to give them equal chance to compete:
#     # For example: pop[:] = pop + offspring
#     # Otherwise you can select the parents of the generation from the offspring population only: pop[:] = offspring
#     pop[:] = offspring
#     # This is the end of the "for" loop (end of generations!)