class Solution:
    def countCharacters(self, s: str) -> dict[str, int]:
        counter = {}
        for c in s:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
        return counter
    def anagramKey(self, s: str) -> str:
        counter = self.countCharacters(s)
        key = ""
        for i in range(ord("a"), ord("z") + 1):
            c = chr(i)
            if c in counter:
                for _ in range(counter[c]):
                    key += c
        return key

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups_by_key = {}
        for s in strs:
            key = self.anagramKey(s)
            if key not in groups_by_key:
                groups_by_key[key] = []
            groups_by_key[key].append(s)
        return [group for group in groups_by_key.values()]
