# Q1 Squares of a Sorted Array
# example :
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].



from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pos =[]
        neg = []
        size =len(nums)
        for num in nums:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)
        # case 1 all positive
        if len(neg) == 0:
            return [x*x for x in pos]
        # case 2 all negative value in array
        elif len(pos) == 0:
            res = [x*x for x in neg]
            res.reverse()
            return res
    # case 3 contaisn both negative and positive
        neg = [x*x for x in neg][::-1]
        pos = [x*x for x in pos]
        n,m = len(neg) , len(pos)
        res = []
        i = j = 0
        while i < n and j < m:
            if neg[i] <= pos[j]:
                res.append(neg[i])
                i += 1
            else:
                res.append(pos[j])
                j += 1
        # while loop khatam h
        while i < n:
            res.append(neg[i])
            i += 1
        while j < m:
            res.append(pos[j])
            j += 1
        return res
        
nums = [-4,-1,0,3,10]
sol = Solution()
answer = sol.sortedSquares(nums)
print(answer)

            
      
        
        




            
            
      
        
        




            

            
      
        
        




            