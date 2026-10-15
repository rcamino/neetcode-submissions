class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += "{:d}:{}".format(len(s), s)
        return encoded

    def readInt(self, s: str, start: str) -> tuple[int, int]:
        i = start
        str_n = ""
        while i < len(s) and s[i] != ":":
            if not s[i].isdigit():
                raise ValueError("Invalid length {}".format(s[i]))
            str_n += s[i]
            i += 1
        n = int(str_n)
        return (n, i)

    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []

        while i < len(s):
            n, i = self.readInt(s, i)
            if i < len(s) and s[i] == ":":
                i += 1
                strs.append(s[i:i+n])
                i += n

        if i != len(s):
            raise ValueError("Did not read the entire input")

        return strs