from math import log
from random import random

# Next day that will rain
def getArrivalTime(p, _lambda):
  return - log(1 - p) / _lambda

# Config variables
_rain_lambda = 1
next_rain_day = getArrivalTime(random(), _rain_lambda)
DAYS = 31

for _ in range(DAYS):
  p = random()
  arrivalTime = getArrivalTime(p, _rain_lambda)
  print(next_rain_day)
  next_rain_day += arrivalTime
