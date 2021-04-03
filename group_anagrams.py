#your solution sucks lmao, 5 and 9 percentile

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup_hashes = {}
        for i in strs:
            lookup_hashes[i] = self.get_hash_word(i)
        # print(lookup_hashes)
            
        seen = []
        result = []
        
        for j in strs:
            if lookup_hashes[j] not in seen:
                seen.append(lookup_hashes[j])
                result.append([j])
            else:
                for res in result:
                    if lookup_hashes[j] == lookup_hashes[res[0]]:
                        res.append(j)
        
        return(result)
    
    def get_hash_word(self, word):
        result = {}
        for i in word:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
        return(result)
    
    def add_hash(self, ith):
        hash_result = self.get_hash_word(ith)
        return {ith: hash_result}
       

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup_hashes = list(map(self.add_hash, strs))
        result = []
        for i in strs:
            if result == []:
                result.append([])
        return("hello")
    
    
    def get_hash_word(self, word):
        result = {}
        for i in word:
            if i not in result:
                result[i] = 1
            else:
                result[i] += 1
        return(result)
    
    def add_hash(self, ith):
        hash_result = self.get_hash_word(ith)
        return {ith: hash_result}