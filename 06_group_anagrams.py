class Solution:
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            
        groups = []
        
        sorted_to_words = {}
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in sorted_to_words:
                sorted_to_words[sorted_word] = [word]
            else:
                sorted_to_words[sorted_word].append(word)

        for v in sorted_to_words.values():
            groups.append(v)
                    
        return groups
    
    def groupAnagrams_brute(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        if len(strs) == 2 and strs[0] == strs[1]:
            return [strs]     
        
        groups = []
        
        for word1 in strs:
            group = []
            for word2 in strs:
                if Solution.isAnagram(word1, word2):
                    group.append(word2)
            if group not in groups:        
                groups.append(group)        
        return groups
    
    def isAnagram(word1, word2):
        if sorted(word1) == sorted(word2):
            return True
        elif word1 == "" and word2 == "":
            return True
