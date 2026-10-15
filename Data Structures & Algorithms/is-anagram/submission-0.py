class Solution:
    def countCharacters(self, s: str) -> dict:
        counter = {}
        for c in s:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
        return counter

    def counterMatches(self, counter: dict, other_counter: dict) -> bool:
        for key in counter:
            if key not in other_counter or counter[key] != other_counter[key]:
                return False
        return True

    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = self.countCharacters(s)
        t_counter = self.countCharacters(t)
        return self.counterMatches(s_counter, t_counter) and self.counterMatches(t_counter, s_counter)
