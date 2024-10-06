class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True
        sentence1 = sentence1.split()
        sentence2 = sentence2.split()
        l = 0 
        r1 = len(sentence1) - 1
        r2 = len(sentence2) - 1
        while l<=r1 and l<=r2 and sentence1[l] == sentence2[l] :
            l += 1
        while r1>=-1 and r2>=-1 and sentence1[r1] == sentence2[r2] :
            r1 -= 1 
            r2 -= 1 
        if l>r1 or l>r2 :
            return True 
        return False

