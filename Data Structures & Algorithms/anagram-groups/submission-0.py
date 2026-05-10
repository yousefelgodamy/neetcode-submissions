class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def createDict(a: str) -> dict:
            count = defaultdict(int) # letter to count
            for i in a:
                count[i] += 1
            return count

        count_map = [] # list of foundational count dicts to indices
        result = [] # list of lists

        for word in strs:
            word_count = createDict(word)
            is_matched = False
            for i in range(len(count_map)):
                prev_count = count_map[i]
                if prev_count == word_count:
                    result[i].append(word)
                    is_matched = True
                    break

            if not is_matched:
                count_map.append(word_count)
                result.append([word])
        return result

