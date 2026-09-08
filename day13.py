# Q1 We need to show our users which people they follow have the lowest follower counts. That way they'll know when the people they follow aren't popular enough to be worth following anymore.

# Implement the "find minimum" algorithm on the right by completing the find_minimum() function. It accepts a list of integers nums and returns the smallest number in the l
def find_minimum(nums: list[int]) -> float | None:
    minimum = float("inf")
    if len(nums) == 0:
        return None
    for num in nums:
        if num < minimum:
            minimum = num
    return minimum


# Q2 Complete the get_quest_status function. It accepts a progress dictionary (structure defined above) and should return the value of the "status" field for the "bridge_run" quest. You do not need to use any loops for this task.


from typing import Any

def get_quest_status(progress):
    return progress["quests"]["bridge_run"]["status"]