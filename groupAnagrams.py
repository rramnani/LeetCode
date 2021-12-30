# O(w*N*logN) time, O(w*N) space, w -> no. of words, N -> length of longest word/string
# Using dictionary/hash table: simpler/optimal
def groupAnagrams(words):
	anagrams = {}
    for word in words:
		sortedWord = "".join(sorted(word))
		print(sortedWord, word, anagrams)
		if sortedWord in anagrams:
			anagrams[sortedWord].append(word) # store the list of the words that correspond to the given anagram
		else:
			anagrams[sortedWord] = [word]
	return list(anagrams.values())
