from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        try:
            max_length = max(len(s), len(t))
            
            t_dict = defaultdict(int)
            s_dict = defaultdict(int)

            for i in range(max_length):
                print(i)
                s_dict[s[i]] += 1
                t_dict[t[i]] += 1

            return True if s_dict == t_dict else False
        except Exception as e:
            return False