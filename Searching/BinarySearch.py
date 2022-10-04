def search(nums: List[int], target: int) -> int:
      """
      Takes in a sorted list and a target value and returns the position
      of the target in the list. If the target is not in the list, `-1` is returned.
      """
      left = 0
      right = len(nums)

      # Loop until the left index is greater than the right index.
      while left < right:
          mid = (left + right) // 2
          if nums[mid] >= target:
              right = mid
          else:
              left = mid + 1

      # Handle cases where the final `mid` value is out of bounds.
      #This happens when target is greater than the last element in the array.
      try:
          mid = (left + right) // 2
          return mid if nums[mid] == target else -1
      except:
          return -1
