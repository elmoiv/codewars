def split_and_add(nums, n):
    if n > 0 and len(nums) > 1:
      A, B = nums[:len(nums) // 2], nums[len(nums) // 2:]
      if len(A) < len(B) and len(nums) != 2:
        A.insert(0, 0)
      return split_and_add([i + B[n] for n, i in enumerate(A)], n - 1)
    return nums
