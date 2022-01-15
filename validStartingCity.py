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
