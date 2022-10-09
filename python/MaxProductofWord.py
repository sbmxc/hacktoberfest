# https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def nocommon(str1,str2):
            for i in str1:
                if(i in str2):
                    return False
            return True
            # bit1=bit2=0
            # for i in str1:
            #     bit1 |= 1<< (ord(i)-ord('a'))
            # for i in str2:
            #     bit2 |= 1<< (ord(i)-ord('a'))
            # return bit1 & bit2 == 0
        maxx=0
        for x in range(len(words)):
            for y in range(x+1,len(words)):
                if(nocommon(words[x],words[y])):
                    maxx=max(maxx,len(words[x])*len(words[y]))
                    
                    
        return maxx