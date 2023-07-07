from collections import Counter


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_size = k
        counter = Counter(answerKey[:k])
        
        start = 0
        
        for i in range(k, len(answerKey)):
            counter[answerKey[i]] += 1
            
            while min(counter['T'], counter['F']) > k:
                counter[answerKey[start]] -= 1
                start += 1
            
            max_size = max(max_size, i - start + 1)
        
        return max_size