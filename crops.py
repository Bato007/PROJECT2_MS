from random import choices

class Crop(object):
  def __init__(self, name, growth_time, cost, profits, seasons=0):
    self.name = name
    self.growth_time = growth_time # Excludes day of planted
    self.cost = cost
    self.profits = profits
    self.seasons = seasons

    self.quality_prob = [0.50, 0.25, 0.15, 0.10]
    self.is_ready = False
    self.lived_time = 0

  # Make the plant grow
  def grow(self):
    if (self.lived_time >= self.growth_time):
      self.is_ready = True
    else:
      self.lived_time += 1

  # Get profit by selling the plant
  def harvest(self):
    return choices(self.profits, weights=self.quality_prob)[0]

x = Crop(
  'Blue Jazz',
  7,
  30,
  [50, 62, 75, 100],
)
print(x.harvest())

class ReGrowthCrop(Crop):
  def __init__(self, name, growth_time, cost, profits, regrowth_time, seasons=0):
    super().__init__(name, growth_time, cost, profits, seasons)
    self.regrowth_time = regrowth_time

# === SPRING CROPS ===
class BlueJazz(Crop):
  def __init__(self):
    super().__init__(
      'Blue Jazz',
      7,
      30,
      [50, 62, 75, 100],
    )

class Cauliflower(Crop):
  def __init__(self):
    super().__init__(
      'Cauliflower',
      12,
      80,
      [175, 218, 262, 350]
    )

class CoffeeBean(ReGrowthCrop):
  def __init__(self):
    super().__init__(
      'Coffee Bean',
      10,
      2500,
      [15, 18, 22, 30],
      2,
      1
    )

class Garlic(Crop):
  def __init__(self):
    super().__init__(
      'Garlic',
      4,
      40,
      [60, 75, 90, 120]
    )

class GreenBean(ReGrowthCrop):
  def __init__(self):
    super().__init__(
      'Green Bean',
      10,
      60,
      [40, 50, 60, 80],
      3
    )

class Kale(Crop):
  def __init__(self):
    super().__init__(
      'Kale',
      6,
      70,
      [110, 137, 165, 220]
    )

class Parsnip(Crop):
  def __init__(self):
    super().__init__(
      'Parsnip',
      4,
      20,
      [35, 43, 52, 70]
    )

class Potato(Crop):
  def __init__(self):
    super().__init__(
      'Potato',
      6,
      50,
      [80, 100, 120, 160]
    )

class Rhubarb(Crop):
  def __init__(self):
    super().__init__(
      'Rhubarb',
      13,
      100,
      [220, 275, 330, 440]
    )

class Strawberry(ReGrowthCrop):
  def __init__(self):
    super().__init__(
      'Strawberry',
      8,
      100,
      [120, 150, 180, 240],
      4
    )

class Tulip(Crop):
  def __init__(self):
    super().__init__(
      'Tulip',
      6,
      20,
      [30, 37, 45, 60]
    )

class UnmilledRice(Crop):
  def __init__(self):
    super().__init__(
      'Unmilled Rice',
      8,
      40,
      [30, 37, 45, 60]
    )

# === SUMMER CROPS ===
class Blueberry(ReGrowthCrop):
  def __init__(self):
    super().__init__(
      'Blueberry',
      13,
      80,
      [50, 62, 75, 100],
      4
    )

class Corn(ReGrowthCrop):
  def __init__(self):
    super().__init__(
      'Corn',
      14,
      150,
      [50, 62, 75, 100],
      4,
      1
    )

class Hops(ReGrowthCrop):
  def __init__(self):
    super().__init__(
      'Hops',
      11,
      60,
      [25, 31, 37, 50],
      1
    )

class HotPepper(ReGrowthCrop):
  def __init__(self):
    super().__init__(
      'Hot Pepper',
      5,
      40,
      [40, 50, 60, 80],
      3
    )

class Melon(Crop):
  def __init__(self):
    super().__init__(
      'Melon',
      12,
      80,
      [250, 312, 375, 500]
    )

class Poppy(Crop):
  def __init__(self):
    super().__init__(
      'Poppy',
      7,
      100,
      [140, 175, 210, 280]
    )

class Radish(Crop):
  def __init__(self):
    super().__init__(
      'Radish',
      6,
      40,
      [90, 112, 135, 180]
    )

class RedCabbage(Crop):
  def __init__(self):
    super().__init__(
      'Red Cabbage',
      9,
      100,
      [260, 325, 390, 520],
    )

class Starfruit(Crop):
  def __init__(self):
    super().__init__(
      'Starfruit',
      13,
      400,
      [750, 937, 1125, 1500],
    )

class SummerSpangle(Crop):
  def __init__(self):
    super().__init__(
      'Summer Spangle',
      8,
      50,
      [90, 112, 135, 180],
    )

class Tomato(ReGrowthCrop):
  def __init__(self):
    super().__init__(
      'Tomato',
      11,
      50,
      [60, 75, 90, 120],
      4
    )

class Wheat(Crop):
  def __init__(self):
    super().__init__(
      'Wheat',
      4,
      10,
      [25, 31, 37, 50],
      1
    )

# === FALL CROPS ===
class Amaranth(Crop):
  def __init__(self):
    super().__init__(
      'Amaranth',
      7,
      70,
      [150, 187, 225, 300],
    )

class Artichoke(Crop):
  def __init__(self):
    super().__init__(
      'Artichoke',
      8,
      30,
      [160, 200, 240, 320],
    )

class Beet(Crop):
  def __init__(self):
    super().__init__(
      'Beet',
      6,
      20,
      [100, 125, 150, 200],
    )

class BokChoy(Crop):
  def __init__(self):
    super().__init__(
      'Bok Choy',
      4,
      50,
      [80, 100, 120, 160],
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
      5
    )

class FairyRose(Crop):
  def __init__(self):
    super().__init__(
      'Fairy Rose',
      12,
      200,
      [290, 362, 435, 580]
    )

class Grape(ReGrowthCrop):
  def __init__(self):
    super().__init__(
      'Grape',
      10,
      60,
      [80, 100, 120, 160],
      3
    )

class Pumpkin(Crop):
  def __init__(self):
    super().__init__(
      'Pumpkin',
      13,
      100,
      [320, 400, 480, 640]
    )

class Yam(Crop):
  def __init__(self):
    super().__init__(
      'Yam',
      10,
      60,
      [160, 200, 240, 320]
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
