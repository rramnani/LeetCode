# O(N) time, N ->  no. of people in the orgChart
# O(d) time, d -> depth of the OrgChart/orgTree
def getLowestCommonManager(topManager, reportOne, reportTwo):
    # Write your code here.
	return getOrgInfo(topManager, reportOne, reportTwo).lowestCommonManager
	
def getOrgInfo(manager, reportOne, reportTwo):
	numberImpReports = 0
	for directReport in manager.directReports:
		print(manager.name, directReport.name)
		orgInfo = getOrgInfo(directReport, reportOne, reportTwo)
		if orgInfo.lowestCommonManager is not None: # if this is our lowestCommonManager, then we return
			return orgInfo
		numberImpReports += orgInfo.numberImpReports # if we, as a manager, have any of the direct reports, then we increase the count since we have it
	if manager == reportOne or manager == reportTwo: # it is possible that the manager was one of the imp reports
		numberImpReports+=1
	lowestCommonManager = manager if numberImpReports == 2 else None
	return OrgInfo(lowestCommonManager, numberImpReports) # pass this count to its parent/manager

class OrgInfo:
	def __init__(self, lowestCommonManager, numberImpReports):
		self.lowestCommonManager = lowestCommonManager
		self.numberImpReports = numberImpReports

# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
