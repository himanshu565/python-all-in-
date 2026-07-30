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

            
# Q2 Complete the find_max function. It takes as input a list of integers, nums, and returns a number.

# max_so_far is initialized as negative infinity.
# Compare each number in nums to max_so_far. If any number is larger than max_so_far, replace max_so_far with that value.
# After iterating over every number, return max_so_far. If nums is empty, return negative infinity.

def find_max(nums):
    if nums == []:
        return float("-inf")

    max_so_far = float("-inf")
    for num in nums:
        if num > max_so_far:
            max_so_far = num
    return max_so_far
        


run_cases = [([1, 2, 3, 4, 5], 5), ([1, 2, 300, 4, 5], 300)]

submit_cases = run_cases + [
    ([1, 20, 3, 4, 5], 20),
    ([-1, 2, 3, 4, 5], 5),
    ([1, 2, 3, 21, 18], 21),
    ([], float("-inf")),
    ([-1, -2, -3, -4, -5], -1),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Inputs: {input1}")
    result = find_max(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

        
        




            
            
      
        
        




            

            
      
        
        




            