class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        Solution 1:
        Loop through all words
            Loop through each letter, and compare to the prefix string
            modify the prefix string as you go
        return

        Solution 2:
        While loop until prefixes no longer match
        return
        '''
        prefix_string = ""
        i = 0
        while True:
            try:
                letter = strs[0][i]
                for word in strs:
                    if word[i] != letter:
                        return prefix_string
                prefix_string += letter
            except:
                return prefix_string
            i += 1