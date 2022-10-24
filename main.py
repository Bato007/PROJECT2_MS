from math import log
from random import random, randint
from seasons import *

season = Season()
full_crop = []
initialMoney = 500
# Next day that will rain
def getArrivalTime(p, _lambda):
  return - log(1 - p) / _lambda

# Config variables
_rain_lambda = 1
next_rain_day = getArrivalTime(random(), _rain_lambda)

# Season initial crop
season.currentSeason()
available_costs = [item().cost for item in season.available_crops]

while initialMoney:
  randomCrop = season.available_crops[randint(0, len(season.available_crops) - 1)]
  if (randomCrop().cost <= initialMoney):
    initialMoney -= randomCrop().cost
    full_crop.append(randomCrop())
  
  if initialMoney < min(available_costs):
    break

DAYS_TO_SIMULATE = 30

print('INITIAL MONEY', initialMoney)
print('INITIAL SEASON', season.SEASON)

for i in range(DAYS_TO_SIMULATE):
  season.currentSeason()

  for crop in full_crop:
    if  (season.SEASON not in crop.seasons):
      full_crop.remove(crop)
      break

    crop.grow()
    if (crop.is_ready):
      initialMoney += crop.harvest()

      try:
        crop.regrowth_time
      except:
        full_crop.remove(crop)

print('FINAL MONEY', initialMoney)
print('FINAL SEASON', season.SEASON)