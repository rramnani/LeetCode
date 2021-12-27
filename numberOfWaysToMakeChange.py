# O(Nd) time, d-> no. of denominations, O(N) space, N=> target amount
def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.
	ways = [0 for amount in range(n+1)]
	ways[0] = 1
	for denom in denoms:
		for amount in range(1, n+1):
			#print("n = ", val,"i =", i)
			if denom <= amount:
				ways[amount] += ways[amount - denom]
    return ways[-1]
