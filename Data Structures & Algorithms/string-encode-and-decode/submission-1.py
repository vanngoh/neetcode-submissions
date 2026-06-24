class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = {}
        for i in range(len(strs)):
            encoding[i] = strs[i]
        return f"{encoding}"

    def decode(self, s: str) -> List[str]:
        decoding = ast.literal_eval(s)
        return list(decoding.values())