from random import choices
from math import ceil

FERTILIZER_TYPES = [
  {
    'name': 'fertilizer_basic',
    'cost': 100,
    'quality_prob': [0.88, 0.08, 0.04, 0]
  },
  {
    'name': 'fertilizer_quality',
    'cost': 150,
    'quality_prob': [0.78, 0.14, 0.08, 0]
  },
  {
    'name': 'speed_basic',
    'cost': 100,
    'growth_reduction': 0.10
  },
  {
    'name': 'speed',
    'cost': 150,
    'growth_reduction': 0.25
  },
] 
QUALITY_PROBABILITIES = [0.95, 0.05, 0, 0]

class Crop(object):
  def __init__(self, name, growth_time, cost, profits, seasons=[]):
    self.name = name
    self.growth_time = growth_time # Excludes day of planted
    self.cost = cost
    self.profits = profits
    self.seasons = seasons
    self.quality_prob = QUALITY_PROBABILITIES[:]

    self.is_ready = False
    self.lived_time = 0

  def __str__(self) -> str:
    return self.name

  # Apply the fertilizer to the crop
  def useFertilizer(self, index):
    fertilizer = FERTILIZER_TYPES[index]
    if ('speed' in fertilizer['name']):
      self.growth_time -= ceil(self.growth_time * fertilizer['growth_reduction'])
    else:
      self.quality_prob = fertilizer['quality_prob']

  # Make the plant grow
  def grow(self):
    if (self.lived_time >= self.growth_time):
      self.is_ready = True
    else:
      self.lived_time += 1

  # Get profit by selling the plant
  def harvest(self):
    return choices(self.profits, weights=self.quality_prob)[0]

class ReGrowthCrop(Crop):
  def __init__(self, name, growth_time, cost, profits, regrowth_time, seasons=[]):
    super().__init__(name, growth_time, cost, profits, seasons)
    self.regrowth_time = regrowth_time

  # Make the plant grow
  def grow(self):
    if (self.lived_time == self.growth_time):
      self.is_ready = True
    elif (self.lived_time > self.growth_time):
      real_time = self.lived_time - self.growth_time
      if (real_time % self.regrowth_time == 0):
        self.is_ready = True
    self.lived_time += 1

  # Get profit by selling the plant
  def harvest(self):
    self.is_ready = False
    crop = choices(self.profits, weights=self.quality_prob)[0]
    self.quality_prob = QUALITY_PROBABILITIES
    return crop

# === SPRING CROPS ===
class BlueJazz(Crop):
  def __init__(self):
    super().__init__(
      'Blue Jazz',
      7,
      30,
      [50, 62, 75, 100],
      seasons=['SPRING']
    )

class Cauliflower(Crop):
  def __init__(self):
    super().__init__(
      'Cauliflower',
      12,
      80,
      [175, 218, 262, 350],
      seasons=['SPRING']
    )

class CoffeeBean(ReGrowthCrop):
  def __init__(self):
    super().__init__(
      'Coffee Bean',
      10,
      100,
      [15, 18, 22, 30],
      2,
      seasons=['SPRING', 'SUMMER']
    )

class Garlic(Crop):
  def __init__(self):
    super().__init__(
      'Garlic',
      4,
      40,
      [60, 75, 90, 120],
      seasons=['SPRING']
    )

class GreenBean(ReGrowthCrop):
  def __init__(self):
    super().__init__(
      'Green Bean',
      10,
      60,
      [40, 50, 60, 80],
      3,
      seasons=['SPRING']
    )

class Kale(Crop):
  def __init__(self):
    super().__init__(
      'Kale',
      6,
      70,
      [110, 137, 165, 220],
      seasons=['SPRING']
    )

class Parsnip(Crop):
  def __init__(self):
    super().__init__(
      'Parsnip',
      4,
      20,
      [35, 43, 52, 70],
      seasons=['SPRING']
    )

class Potato(Crop):
  def __init__(self):
    super().__init__(
      'Potato',
      6,
      50,
      [80, 100, 120, 160],
      seasons=['SPRING']
    )

class Rhubarb(Crop):
  def __init__(self):
    super().__init__(
      'Rhubarb',
      13,
      100,
      [220, 275, 330, 440],
      seasons=['SPRING']
    )

class Strawberry(ReGrowthCrop):
  def __init__(self):
    super().__init__(
      'Strawberry',
      8,
      100,
      [120, 150, 180, 240],
      4,
      seasons=['SPRING']
    )

class Tulip(Crop):
  def __init__(self):
    super().__init__(
      'Tulip',
      6,
      20,
      [30, 37, 45, 60],
      seasons=['SPRING']
    )

class UnmilledRice(Crop):
  def __init__(self):
    super().__init__(
      'Unmilled Rice',
      8,
      40,
      [30, 37, 45, 60],
      seasons=['SPRING']
    )

# === SUMMER CROPS ===
class Blueberry(ReGrowthCrop):
  def __init__(self):
    super().__init__(
      'Blueberry',
      13,
      80,
      [50, 62, 75, 100],
      4,
      seasons=['SUMMER']
    )

class Corn(ReGrowthCrop):
  def __init__(self):
    super().__init__(
      'Corn',
      14,
      150,
      [50, 62, 75, 100],
      4,
      seasons=['SUMMER', 'FALL']
    )

class Hops(ReGrowthCrop):
  def __init__(self):
    super().__init__(
      'Hops',
      11,
      60,
      [25, 31, 37, 50],
      1,
      seasons=['SUMMER']
    )

class HotPepper(ReGrowthCrop):
  def __init__(self):
    super().__init__(
      'Hot Pepper',
      5,
      40,
      [40, 50, 60, 80],
      3,
      seasons=['SUMMER']
    )

class Melon(Crop):
  def __init__(self):
    super().__init__(
      'Melon',
      12,
      80,
      [250, 312, 375, 500],
      seasons=['SUMMER']
    )

class Poppy(Crop):
  def __init__(self):
    super().__init__(
      'Poppy',
      7,
      100,
      [140, 175, 210, 280],
      seasons=['SUMMER']
    )

class Radish(Crop):
  def __init__(self):
    super().__init__(
      'Radish',
      6,
      40,
      [90, 112, 135, 180],
      seasons=['SUMMER']
    )

class RedCabbage(Crop):
  def __init__(self):
    super().__init__(
      'Red Cabbage',
      9,
      100,
      [260, 325, 390, 520],
      seasons=['SUMMER']
    )

class Starfruit(Crop):
  def __init__(self):
    super().__init__(
      'Starfruit',
      13,
      400,
      [750, 937, 1125, 1500],
      seasons=['SUMMER']
    )

class SummerSpangle(Crop):
  def __init__(self):
    super().__init__(
      'Summer Spangle',
      8,
      50,
      [90, 112, 135, 180],
      seasons=['SUMMER']
    )

class Tomato(ReGrowthCrop):
  def __init__(self):
    super().__init__(
      'Tomato',
      11,
      50,
      [60, 75, 90, 120],
      4,
      seasons=['SUMMER']
    )

class Wheat(Crop):
  def __init__(self):
    super().__init__(
      'Wheat',
      4,
      10,
      [25, 31, 37, 50],
      seasons=['SUMMER', 'FALL']
    )

# === FALL CROPS ===
class Amaranth(Crop):
  def __init__(self):
    super().__init__(
      'Amaranth',
      7,
      70,
      [150, 187, 225, 300],
      seasons=['FALL']
    )

class Artichoke(Crop):
  def __init__(self):
    super().__init__(
      'Artichoke',
      8,
      30,
      [160, 200, 240, 320],
      seasons=['FALL']
    )

class Beet(Crop):
  def __init__(self):
    super().__init__(
      'Beet',
      6,
      20,
      [100, 125, 150, 200],
      seasons=['FALL']
    )

class BokChoy(Crop):
  def __init__(self):
    super().__init__(
      'Bok Choy',
      4,
      50,
      [80, 100, 120, 160],
      seasons=['FALL']
    )

class Cranberries(ReGrowthCrop):
  def __init__(self):
    super().__init__(
      'Cranberries',
      7,
      240,
      [75, 93, 112, 150],
      5
    )

class Eggplant(ReGrowthCrop):
  def __init__(self):
    super().__init__(
      'Eggplant',
      5,
      20,
      [60, 75, 90, 120],
      5,
      seasons=['FALL']
    )

class FairyRose(Crop):
  def __init__(self):
    super().__init__(
      'Fairy Rose',
      12,
      200,
      [290, 362, 435, 580],
      seasons=['FALL']
    )

class Grape(ReGrowthCrop):
  def __init__(self):
    super().__init__(
      'Grape',
      10,
      60,
      [80, 100, 120, 160],
      3,
      seasons=['FALL']
    )

class Pumpkin(Crop):
  def __init__(self):
    super().__init__(
      'Pumpkin',
      13,
      100,
      [320, 400, 480, 640],
      seasons=['FALL']
    )

class Yam(Crop):
  def __init__(self):
    super().__init__(
      'Yam',
      10,
      60,
      [160, 200, 240, 320],
      seasons=['FALL']
    )

def getSpringCrops():
  return [
    BlueJazz, Cauliflower, CoffeeBean, Garlic,
    GreenBean, Kale, Parsnip, Potato, Rhubarb,
    Strawberry, Tulip, UnmilledRice,
  ]

def getSummerCrops():
  return [
    Blueberry, Corn, Hops, HotPepper, Melon,
    Poppy, Radish, RedCabbage, Starfruit,
    SummerSpangle, Tomato, Wheat
  ]

def getFallCrops():
  return [
    Amaranth, Artichoke, Beet, BokChoy, Cranberries,
    Eggplant, FairyRose, Grape, Pumpkin, Yam
  ]
