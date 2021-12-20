# O(1) time, O(1) space
# Stack: LIFO -> Last In First Out
# Feel free to add new properties and methods to the class.
class MinMaxStack:
	def __init__(self):
		self.minMaxStack=[]
		self.stack=[]
    def peek(self):
        # Write your code here.
		return self.stack[len(self.stack)-1]

    def pop(self):
        # Write your code here.
		self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        # Write your code here.
		newMinMax = {"min":number, "max":number}
		if len(self.minMaxStack): # check if min/max already exist and update if needed
			lastMinMax=self.minMaxStack[len(self.minMaxStack)-1]
			newMinMax["min"]=min(lastMinMax["min"], number)
			newMinMax["max"]=max(lastMinMax["max"], number)
		self.minMaxStack.append(newMinMax)
		self.stack.append(number)
        pass

    def getMin(self):
        # Write your code here.
		return self.minMaxStack[len(self.minMaxStack)-1]["min"]

    def getMax(self):
        # Write your code here.
        return self.minMaxStack[len(self.minMaxStack)-1]["max"]
