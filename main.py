from math import log
from random import random, randint
from seasons import *

season = Season()
crop = []
available_crops = []
initialMoney = 500
# Next day that will rain
def getArrivalTime(p, _lambda):
  return - log(1 - p) / _lambda

# Config variables
_rain_lambda = 1
next_rain_day = getArrivalTime(random(), _rain_lambda)

season.currentSeason()
available_crops = season.available_crops

available_costs = [item().cost for item in available_crops]

while initialMoney:
  randomCrop = available_crops[randint(0, len(available_crops) - 1)]
  if (randomCrop().cost <= initialMoney):
    initialMoney -= randomCrop().cost
    crop.append(randomCrop)
  
  if initialMoney < min(available_costs):
    break

print(crop)