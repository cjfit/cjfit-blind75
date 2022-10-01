class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert to lowercase
        s = s.lower()
        # regex to remove all non-alphanumeric
        s = re.sub(r'\W+', '', s)
        
        # regex to remove all underscores literally
        s = re.sub(r'_', '', s)
        
        
        # python reverse string with string comprehension
        reverse_s = s[::-1]

        print(reverse_s)
        
        return s == reverse_s