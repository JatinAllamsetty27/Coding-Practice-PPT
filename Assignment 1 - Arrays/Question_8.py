def findErrorNums(nums):
    num_set = set()
    duplicate = -1
    totalSum = 0

    for num in nums:
        if num in num_set:
            duplicate = num
        num_set.add(num)
        totalSum += num

    n = len(nums)
    expectedSum = n * (n + 1) // 2
    missing = expectedSum - totalSum + duplicate

    return [duplicate, missing]
