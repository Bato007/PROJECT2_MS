from math import floor, log
from random import random, randint
from seasons import *

season = Season()
full_crop = []
wallet = 500
# Next day that will rain
def getArrivalTime(p, _lambda):
  return - log(1 - p) / _lambda

# Config variables
_rain_lambda = 1
next_rain_day = getArrivalTime(random(), _rain_lambda)

# Season initial crop
season.currentSeason()
available_costs = [item().cost for item in season.available_crops]
available_growths = [item().growth_time for item in season.available_crops]

## Function to buy crops
def buyCrops(wallet, daysLeft):
  global season, full_crop
  seedCount = 0
  ## Buying if there is money, and no more than 25 seeds
  while wallet and seedCount < 25:
    # Generate a crop
    randomCrop = season.available_crops[randint(0, len(season.available_crops) - 1)]
    try:
      # If it's a regrowth crop, only buy it if it will generate an income during CURRENT season
      n = floor(randomCrop().profits[0] / randomCrop().cost)
      if (randomCrop().cost <= wallet and ((randomCrop().growth_time) + (n * randomCrop().regrowth_time)) <= daysLeft):
        wallet -= randomCrop().cost
        seedCount += 1
        full_crop.append(randomCrop())
    except:
      # If it's a normal crop, only buy if it has a chance to grow before the CURRENT season ends
      if (randomCrop().cost <= wallet and (randomCrop().growth_time) <= daysLeft):
        wallet -= randomCrop().cost
        seedCount += 1
        full_crop.append(randomCrop())
    
    # If there is no money, and no time to grow any seed, don't buy anything that day
    if wallet < min(available_costs) or min(available_growths) > daysLeft:
      return wallet
  return wallet

# Start the first purchase with 28 days left in the season    
wallet = buyCrops(wallet, 28)

DAYS_TO_SIMULATE = 70

print('INITIAL MONEY', wallet)
print('INITIAL SEASON', season.SEASON)

# Every day
for i in range(DAYS_TO_SIMULATE):
  for crop in full_crop:
    # Remove crop if it's out of season
    if  (season.SEASON not in crop.seasons):
      full_crop.remove(crop)
      break

    # Grow crop, and sell it if possible
    crop.grow()
    if (crop.is_ready):
      wallet += crop.harvest()

      # Remove crop if it won't regrow
      try:
        crop.regrowth_time
      except:
        full_crop.remove(crop)

  # Buy crops every day
  wallet = buyCrops(wallet, season.daysLeft())
  season.currentSeason()

# Once the simulation days end, let the rest of the crops grow
while len(full_crop) > 0:
  for crop in full_crop:
    if  (season.SEASON not in crop.seasons):
      full_crop.remove(crop)
      break

    crop.grow()
    if (crop.is_ready):
      wallet += crop.harvest()
      full_crop.remove(crop)

print('FINAL MONEY', wallet)
print('FINAL SEASON', season.SEASON)
