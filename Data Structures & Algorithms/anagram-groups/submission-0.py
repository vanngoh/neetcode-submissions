class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]
        
        if len(strs) == 1:
            return [strs]

        outputs = []
        hashmap = {}
        for idx, txt in enumerate(strs):
            sorted_txt = "".join(sorted(txt))
            if hashmap.get(sorted_txt, None) is None:
                hashmap[sorted_txt] = len(outputs)
                outputs.append([txt])
                continue
            else:
                outputs[hashmap[sorted_txt]].append(txt)

        return outputs

            