# Q1  3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.
def threeSum(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):

        # Skip duplicate first elements
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

            elif total < 0:
                left += 1

            else:
                right -= 1

    return result

# // this one is giving runtime error
    def threeSum(self, nums: List[int]) -> List[List[int]]:

	res = set()
	#1. Split nums into three lists: negative numbers, positive numbers, and zeros
	n, p, z = [], [], []
	for num in nums:
		if num > 0:
			p.append(num)
		elif num < 0: 
			n.append(num)
		else:
			z.append(num)

	#2. Create a separate set for negatives and positives for O(1) look-up times
	N, P = set(n), set(p)

	#3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
	#   i.e. (-3, 0, 3) = 0
	if z:
		for num in P:
			if -1*num in N:
				res.add((-1*num, 0, num))

	#3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
	if len(z) >= 3:
		res.add((0,0,0))

	#4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
	#   exists in the positive number set
	for i in range(len(n)):
		for j in range(i+1,len(n)):
			target = -1*(n[i]+n[j])
			if target in P:
				res.add(tuple(sorted([n[i],n[j],target])))

	#5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
	#   exists in the negative number set
	for i in range(len(p)):
		for j in range(i+1,len(p)):
			target = -1*(p[i]+p[j])
			if target in N:
				res.add(tuple(sorted([p[i],p[j],target])))

	return res
#  best one yet
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        neg = defaultdict(int)
        pos = defaultdict(int)
        zeros = 0
        
        for x in nums:
            if x < 0:
                neg[x] += 1
            elif x > 0:
                pos[x] += 1
            else:
                zeros += 1
        
        r = []
        
        if zeros:
            for n in neg:
                if -n in pos:
                    r.append((0, n, -n))
        
            if zeros > 2:
                r.append((0,0,0))

        for set_a, set_b in ((neg, pos), (pos, neg)):
            set_a_items = list(set_a.items())
            for i, (x, q) in enumerate(set_a_items):
                for x2, q2 in set_a_items[i:]:
                    if x != x2 or (x == x2 and q > 1):
                        if -x-x2 in set_b:
                            r.append((x, x2, -x-x2))

        return r