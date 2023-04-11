class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # want to store one's we are used before and see if the current one we can sum to
        hash_map = {}

        # want to iterate over the loop and grab the number as well as index to return
        for idx,value in enumerate(nums):
            # let's get the goal
            goal = target - value

            # check to see if the goal is in the hashmap
            if goal in hash_map:
                # return the idex's
                return ([hash_map[goal],idx])
            # else store it in the hash_map
            else:
                hash_map[value] = idx
