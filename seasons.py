from crops import *
import copy

SEASONS = ['SPRING', 'SUMMER', 'FALL']

PROFITS_PER_SEASON = {
    "SPRING": {},
    "SUMMER": {},
    "FALL": {},
}

class Season(object):
    def __init__(self, DAYS_TO_SIMULATE):
        self.SEASON = SEASONS[0]
        self.available_crops = []

        self.DAYS_TO_SIMULATE = DAYS_TO_SIMULATE
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
        try:
            sorted_profits = sorted(PROFITS_PER_SEASON[self.SEASON], key=lambda x:PROFITS_PER_SEASON[self.SEASON][x]['finalProfits'])
        except:
            sorted_profits = []

        if (self.SEASON == SEASONS[0]):
            self.available_crops = getSpringCrops()
        elif (self.SEASON == SEASONS[1]):
            self.available_crops = getSummerCrops()
        elif (self.SEASON == SEASONS[2]):
            self.available_crops = getFallCrops()

        try:
            selectedCrops = []
            if (len(sorted_profits) >= 5):
                bestProfits = sorted_profits[0:5]
                for crop in self.available_crops:
                    if (crop().name in bestProfits):
                        selectedCrops.append(crop)

                self.available_crops = selectedCrops
        except:
            pass
    
        self.available_cost_growth = [(item().cost, item().growth_time) for item in self.available_crops]

    def daysLeft(self) -> int:
        return self.DAYS_TO_SIMULATE - self.current_day
    
    def setInitialSeed(self, cropName, info):
        PROFITS_PER_SEASON[self.SEASON][cropName] = info

    def updateSeed(self, cropName):
        PROFITS_PER_SEASON[self.SEASON][cropName]['seedsBought'] += 1

    def updateProfits(self, cropName, total):
        try:
            PROFITS_PER_SEASON[self.SEASON][cropName]
        except:
            PROFITS_PER_SEASON[self.SEASON][cropName] = copy.deepcopy(PROFITS_PER_SEASON[SEASONS[SEASONS.index(self.SEASON) - 1]][cropName])
            PROFITS_PER_SEASON[self.SEASON][cropName]['seedsBought'] = 0

        try:
            PROFITS_PER_SEASON[self.SEASON][cropName]['totalFromHarvest'] += total
        except:
            PROFITS_PER_SEASON[self.SEASON][cropName]['totalFromHarvest'] = total

        totalSpent = PROFITS_PER_SEASON[self.SEASON][cropName]['cost'] * PROFITS_PER_SEASON[self.SEASON][cropName]['seedsBought']
        totalReceived = PROFITS_PER_SEASON[self.SEASON][cropName]['totalFromHarvest']
        PROFITS_PER_SEASON[self.SEASON][cropName]['finalProfits'] = totalReceived - totalSpent

    def getProfits(self):
        return PROFITS_PER_SEASON
