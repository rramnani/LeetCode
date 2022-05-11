# O(M * N * logN) time, where M = max. length of a single log, N = no. of logs in the list
# O(M * N) space
class Solution(object):
    def reorderLogFiles(self, logs):

        letter_log, digit_log = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digit_log.append(log)
            else:
                letter_log.append(log.split())

        letter_log.sort(key = lambda x: x[0])
        print(letter_log)
        letter_log.sort(key = lambda x: x[1:])

        print(letter_log)

        for i in range(len(letter_log)):
            letter_log[i] = " ".join(letter_log[i])

        return letter_log + digit_log

def main():
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    solution = Solution()
    res = solution.reorderLogFiles(logs)
    print(res)

if __name__ == "__main__": 
    main()
