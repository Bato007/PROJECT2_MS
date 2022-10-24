from crops import *
SEASONS = ['SPRING', 'SUMMER', 'FALL']

class Season(object):
    def __init__(self):
        self.SEASON = SEASONS[0]
        self.available_crops = []

        self.current_day = 0
        self.current_year = 0

    def getCurrentDate(self):
        return {
            'day': self.current_day,
            'year': self.current_year
        }

    def currentSeason(self):
        if self.current_day == 86:
            self.SEASON = SEASONS[0]
            self.current_day = 0
            current_year += 1
            self.generateSeasonCrops()
        elif self.current_day == 57:
            self.SEASON = SEASONS[2]
            self.generateSeasonCrops()
        elif self.current_day == 29:
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
