class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26
        matches = 0

        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1

        for i in range(len(s2) - len(s1)):
            if matches == 26:
                return True

            left_char_index = ord(s2[i]) - ord('a')
            right_char_index = ord(s2[i + len(s1)]) - ord('a')

            s2Count[left_char_index] -= 1
            if s2Count[left_char_index] == s1Count[left_char_index]:
                matches += 1
            elif s2Count[left_char_index] + 1 == s1Count[left_char_index]:
                matches -= 1

            s2Count[right_char_index] += 1
            if s2Count[right_char_index] == s1Count[right_char_index]:
                matches += 1
            elif s2Count[right_char_index] - 1 == s1Count[right_char_index]:
                matches -= 1

        return matches == 26
