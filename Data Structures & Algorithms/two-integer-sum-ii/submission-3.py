class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            left = i + 1
            right = len(numbers) - 1
            ans = target - numbers[i]

            while left <= right:
                # Get the mid by shift with left
                mid = left + ((right - left) // 2)
                if numbers[mid] == ans:
                    return [i+1, mid+1]
                if numbers[mid] > ans:
                    right = mid - 1
                    continue
                if numbers[mid] < ans:
                    left = mid + 1
                    continue

        # Basically will not return this since it will 
        # always be ONE valid solution
        return []