#Time Limit Exceeded
class Solution:
    def containsNearbyDuplicate(self, nums: 'List[int]', k: 'int') -> 'bool':
        def helper1(n):
            for e in range(n + 1, n + k + 1):
                if nums[n] == nums[e]:
                    return True
                pass
        def helper2(n):
            for e in range(n + 1, len(nums)):
                if nums[n] == nums[e]:
                    return True
                pass
        x = len(nums) - k
        if x < 0:
            x = 0
        for e in range(x, len(nums) - 1):
            if helper2(e):
                return True
        for i in range(0, len(nums)):
            if (i + k < len(nums) and helper1(i)) or (k >= len(nums) and helper2(i)):
                return True
        return False

#RunTime: 40 ms
class Solution:
    def containsNearbyDuplicate(self, nums: 'List[int]', k: 'int') -> 'bool':
        if len(nums) == len(set(nums)):
            return False
        dis = []
        for i in range(len(nums)):
            if i != len(nums) - 1 -nums[::-1].index(nums[i]):
                dis.append([kk for kk, x in enumerate(nums) if x == nums[i] ])
        for i in range(len(dis)):
            for j in range(1,len(dis[i])):
                if dis[i][j] - dis[i][j-1] <= k:
                    return True
        return False
