class Solution:
    separator = chr(256)
    empty = chr(257)

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return self.empty
        return self.separator.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == self.empty:
            return []
        return s.split(self.separator)
