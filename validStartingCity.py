# Brute force
# O(N^2) time, O(1) space
def validStartingCity(distances, fuel, mpg):
	numberOfCities = len(distances)
	for startingCityIdx in range(numberOfCities):
		milesRemaining = 0
		for currentCityIdx in range(startingCityIdx, startingCityIdx + numberOfCities):
			if milesRemaining < 0: # we have -ve amount of gas
				continue
			currentCityIdx = currentCityIdx % numberOfCities
			milesRemaining += fuel[currentCityIdx] * mpg - distances[currentCityIdx]
		if milesRemaining >= 0:
			return startingCityIdx

    return -1


# O(N) time, O(1) space

class Solution:
    def validStartingCity(self, distances, fuel, mpg):

        numberOfCities = len(distances)
        milesRemaining = 0
        indexOfStartingCityCandidate = 0
        milesRemainingAtStartingCityCandidate = 0

        for cityIdx in range(1, numberOfCities):
            distanceFromPreviousCity = distances[cityIdx - 1]
            fuelFromPreviousCity = fuel[cityIdx - 1]

            milesRemaining += fuelFromPreviousCity * mpg - distanceFromPreviousCity

            if milesRemaining < milesRemainingAtStartingCityCandidate:
                indexOfStartingCityCandidate = cityIdx
                milesRemainingAtStartingCityCandidate = milesRemaining
                

        return indexOfStartingCityCandidate
