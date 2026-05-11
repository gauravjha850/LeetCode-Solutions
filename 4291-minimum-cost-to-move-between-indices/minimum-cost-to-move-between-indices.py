class Solution(object):
    def minCost(self, nums, queries):
        n = len(nums)
        # v1[i] is the cost to reach index i from index 0 (moving right)
        v1 = [0] * n
        # v2[i] is the cost to reach index i from index n-1 (moving left)
        v2 = [0] * n
        
        # Precompute costs for moving Right
        for i in range(n - 1):
            # Closest to i is i+1 if distance to i+1 is smaller than distance to i-1
            if i == 0 or (nums[i] - nums[i - 1]) > (nums[i + 1] - nums[i]):
                v1[i + 1] = v1[i] + 1
            else:
                v1[i + 1] = v1[i] + (nums[i + 1] - nums[i])
        
        # Precompute costs for moving Left
        for i in range(n - 1, 0, -1):
            # Closest to i is i-1 if distance to i-1 is smaller or equal to i+1
            if i == n - 1 or (nums[i] - nums[i - 1]) <= (nums[i + 1] - nums[i]):
                v2[i - 1] = v2[i] + 1
            else:
                v2[i - 1] = v2[i] + (nums[i] - nums[i - 1])
                
        res = []
        for l, r in queries:
            if l < r:
                # Moving right: difference in prefix sums
                res.append(v1[r] - v1[l])
            else:
                # Moving left: difference in suffix sums
                res.append(v2[r] - v2[l])
        return res

        