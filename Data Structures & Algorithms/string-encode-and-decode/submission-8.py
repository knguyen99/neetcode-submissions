class Solution:

    def encode(self, strs: List[str]) -> str:
        return str(len(strs))+ "`" + "`".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "0`":
            return []
        if s == "1`":
            return [""]
        return s.split("`")[1:]