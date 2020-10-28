# Topic: HashTable
# 202. Happy Number - Easy

class Solution:
    def isHappy(self, n: int) -> bool:
        hashSet=set()
        while n not in hashSet:
            if n != 1:
                hashSet.add(n)
                n = sum(int(i)**2 for i in str(n))
            else:
                return True
        return False
