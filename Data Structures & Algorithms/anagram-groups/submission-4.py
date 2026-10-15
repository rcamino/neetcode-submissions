class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups_by_key = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in groups_by_key:
                groups_by_key[key] = []
            groups_by_key[key].append(s)
        return [group for group in groups_by_key.values()]
