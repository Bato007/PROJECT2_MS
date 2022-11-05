from crops import *
SEASONS = ['SPRING', 'SUMMER', 'FALL']

class Season(object):
    def __init__(self):
        self.SEASON = SEASONS[0]
        self.available_crops = []

        self.current_day = 0
        self.current_year = 0
        self.available_costs = []
        self.available_growths = []

    def getCurrentDate(self):
        return {
            'day': self.current_day,
            'year': self.current_year
        }

    def currentSeason(self):
        if self.current_day == 84:
            self.SEASON = SEASONS[0]
            self.current_day = 0
            self.current_year += 1
            self.generateSeasonCrops()
        elif self.current_day == 56:
            self.SEASON = SEASONS[2]
            self.generateSeasonCrops()
        elif self.current_day == 28:
            self.SEASON = SEASONS[1]
            self.generateSeasonCrops()
        elif self.current_day == 0:
            self.SEASON = SEASONS[0]
            self.generateSeasonCrops()
        
        self.current_day += 1
        return self.available_crops

    def generateSeasonCrops(self):
        if (self.SEASON == SEASONS[0]):
            self.available_crops = getSpringCrops()
        elif (self.SEASON == SEASONS[1]):
            self.available_crops = getSummerCrops()
        elif (self.SEASON == SEASONS[2]):
            self.available_crops = getFallCrops()
        self.available_cost_growth = [(item().cost, item().growth_time) for item in self.available_crops]

    def daysLeft(self) -> int:
        return ((SEASONS.index(self.SEASON) + 1) * 28) - self.current_day
