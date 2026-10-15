class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = str(len(strs))
        if len(strs) > 0:
            encoded += ":"
            for s in strs:
                encoded += "{:d}:".format(len(s))
            for s in strs:
                encoded += s
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
        if len(s) == 0:
            raise ValueError("Empty")
        
        array_length, i = self.readInt(s, 0)

        str_lengths = []
        strs = []

        if i < len(s) and s[i] == ":":
            i += 1

            for _ in range(array_length):
                str_length, i = self.readInt(s, i)
                str_lengths.append(str_length)
                i += 1

            for length in str_lengths:
                strs.append(s[i:i + length])
                i += length

        if i != len(s):
            raise ValueError("Did not read the entire input")
        return strs