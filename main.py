from math import e as mathe, exp, floor, log
from random import random, randint, sample
import copy
from seasons import *
import numpy as np
import matplotlib.pyplot as plt

DAYS_TO_SIMULATE = 28 * 3
INITIAL_WALLET = 500

def getBest(array):
  return sorted(array, key=lambda x: x.wallet)[-1]

def currentDistribution(day):
  return 3 * exp(-0.1 * day) + 0.3

class Candidate(object):
  def __init__(self, wallet = INITIAL_WALLET, init_crops = [], available_crops = [], favorite_crops=[]) -> None:
    self.mutate_crops = 2
    self.wallet = wallet
    self.full_crop = []
    self.season = Season(DAYS_TO_SIMULATE, favorite_crops=favorite_crops)

    self.season.currentSeason()
    if ((init_crops is None) or (len(init_crops) == 0)):
      self.buyCrops(self.season.daysLeft(), available_crops)
    else:
      self.buySameCrops(init_crops)

    self.init_crops = copy.deepcopy(self.full_crop)

  def buyCrops(self, daysLeft, available_crops = [], iterationCount=25):
    store_crops = self.season.available_crops
    
    ## Buying if there is money, and no more than 15 seeds
    for i in range(iterationCount):
      # Generate a crop
      buyFlag = random()
      randomCrop = store_crops[randint(0, len(store_crops) - 1)]()


      if ((self.wallet - randomCrop.cost) > 0 and buyFlag > 0.5):  
        try:
          # If it's a regrowth crop, only buy it if it will generate an income during CURRENT season
          n = floor(randomCrop.profits[0] / randomCrop.cost)
          
          if (randomCrop.cost <= self.wallet and ((randomCrop.growth_time) + ((n + 1) * randomCrop.regrowth_time)) < daysLeft and random() <= currentDistribution(self.season.current_day % 28)):
            try:
              self.season.updateSeed(
                randomCrop.name
              )
            except:
              self.season.setInitialSeed(
                randomCrop.name,
                {
                  "seedsBought": 1,
                  "cost": randomCrop.cost,
                  "finalProfits": 0,
                }
              )

            self.wallet -= randomCrop.cost
            self.full_crop.append(randomCrop)
          else:
            return
        except:
          if (randomCrop.cost <= self.wallet and randomCrop.growth_time < daysLeft):
            try:
              self.season.updateSeed(
                randomCrop.name
              )
            except:
              self.season.setInitialSeed(
                randomCrop.name,
                {
                  "seedsBought": 1,
                  "cost": randomCrop.cost,
                  "finalProfits": 0,
                }
              )

            self.wallet -= randomCrop.cost
            self.full_crop.append(randomCrop)
          else:
            return
        
        # If the lowest costing seed doesn't have time to grow (and hasn't been bought above)
        filtered = list(filter(lambda tup: tup[0] == min(self.season.available_cost_growth)[0], self.season.available_cost_growth))
        lowest = min(filtered, key=lambda tup: tup[1])
        if lowest[0] > self.wallet and lowest[1] > daysLeft:
          return

  def buySameCrops(self, init_crops):
    for crop in init_crops:
      
      try:
        self.season.updateSeed(
          crop.name
        )
      except:
        self.season.setInitialSeed(
          crop.name,
          {
            "seedsBought": 1,
            "cost": crop.cost,
          }
        )

      self.full_crop.append(crop)
      self.wallet -= crop.cost

  def fitness(self):
    return self.wallet

  def mutate(self):
    for _ in range(self.mutate_crops):
      crop = self.full_crop.pop(randint(0, len(self.full_crop) - 1))
      self.wallet += crop.cost

    self.buyCrops(self.season.daysLeft(), iterationCount=2)
    self.candidates = copy.deepcopy(self.full_crop)

  def simulate(self, simulate_days):
    # Every day
    for _ in range(simulate_days):
      for crop in self.full_crop:
        # Remove crop if it's out of season
        if (self.season.SEASON not in crop.seasons):
          self.full_crop.remove(crop)
          break

        # Grow crop, and sell it if possible
        crop.grow()

        try:
          if (crop.lived_time - crop.growth_time % crop.regrowth_time == 0):
            moneyFromHarvest = crop.harvest()
            self.season.updateProfits(crop.name, moneyFromHarvest)
            self.wallet += moneyFromHarvest
        except:
          if (crop.lived_time >= crop.growth_time):
            moneyFromHarvest = crop.harvest()
            self.season.updateProfits(crop.name, moneyFromHarvest)
            self.wallet += moneyFromHarvest

            # Remove crop if it won't regrow
            self.full_crop.remove(crop)

      # Buy crops every day
      self.buyCrops(self.season.daysLeft())
      self.season.currentSeason()

class Population(object):
  def __init__(self) -> None:
    self.candidates = []

  def generate(self, amount):
    self.candidates = [Candidate() for _ in range(amount)]

  def generate_new_candidate(self):
    new_candidates = []
    for candidate in self.candidates:
      new_candidates.append(Candidate(init_crops=candidate.init_crops, favorite_crops=candidate.season.PROFITS_PER_SEASON))
    self.candidates = copy.deepcopy(new_candidates)

  def sort(self):
    self.candidates = sorted(self.candidates, key=lambda x: x.wallet)

  def getUniqueCrops(self, crops_names, crops, candidate):
    for crop in candidate.init_crops:
      if (crop.name not in crops_names):
        
        # Find the crop class
        for season_crop in candidate.season.available_crops:
          if (isinstance(crop, season_crop)):
            crops.append(season_crop)
            crops_names.append(crop.name)
            break

  def cross(self, candidate_a: Candidate, candidate_b: Candidate):
    # Gets unique crops
    crops_names = []
    crops = []
    
    self.getUniqueCrops(crops_names, crops, candidate_a)
    self.getUniqueCrops(crops_names, crops, candidate_b)

    self.candidates.append(Candidate(available_crops=crops))

class Simulation(object):
  def simulate(self, pop_num=4, iterations=10, simulate_days=DAYS_TO_SIMULATE, select=0.5, mutate=0.1):
    population = Population()
    population.generate(pop_num)
    self.best_candidates = []

    for i in range(iterations):
      print('# Iteration', i)

      # Fills needed population
      while (len(population.candidates) < pop_num):
        candidates = sample(population.candidates, 2)
        population.cross(candidates[0], candidates[1])

      # Tries to mutate children
      for candidate in population.candidates:
        if (random() < mutate): candidate.mutate()

      # Simulation for every candidate
      for j, candidate in enumerate(population.candidates):
        candidate.simulate(simulate_days)
        print('# Candidate:', j, '- finish with:', candidate.wallet)

      # Sort for better candidates
      population.sort()
      print('Best in gen', i, 'has wallet:', population.candidates[-1].wallet, '\n')
      self.best_candidates.append(population.candidates[-1])

      # === FUNCION DE SELECCION ===
      population.candidates = population.candidates[int(pop_num*select):]
      population.generate_new_candidate()

simulation = Simulation()
simulation.simulate()

x = []
y = []
for i, candidate in enumerate(simulation.best_candidates):
  x.append(i + 1)
  y.append(candidate.wallet)

fig = plt.figure(figsize = (10, 5))
# creating the bar plot
plt.bar(x, y, color ='maroon', width = 0.4)
plt.xlabel("Ages")
plt.ylabel("Wallet")
plt.title("Best candidates over the ages")
plt.show()

best_candidate = getBest(simulation.best_candidates)
print('=> The best candidate bought the following crops')
print('#'*40)

for season in best_candidate.season.PROFITS_PER_SEASON:
  current_dict = best_candidate.season.PROFITS_PER_SEASON[season]
  sorted_profits = sorted(current_dict, key=lambda x:current_dict[x]['finalProfits'])[0:5]
  print('\nTOP 5 MOST PROFITABLE SEEDS IN ', season, sorted_profits)
  sorted_bought = sorted(current_dict, key=lambda x:current_dict[x]['seedsBought'])[0:5]
  print('TOP 5 MOST BOUGHT SEEDS IN ', season, sorted_bought)
  print('\n')


print('#'*40)
print('=> At the end got', best_candidate.wallet)