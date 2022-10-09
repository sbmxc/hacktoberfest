from collections import OrderedDict

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = OrderedDict()
        for i in s:
            try:
                if(a[i]):
                    a[i]=a[i]+1
                
            except:
                a[i]=1
           
        for k,v in a.items():
            if v==1:
                return s.index(k)
        return -1
            

        