class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # convert magazine str characters to list
        maglist = [x for x in magazine]
        
        for char in ransomNote:
            if char in maglist:
                maglist.pop(maglist.index(char))
            else:
                return False
            
        return True
        