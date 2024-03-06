def calculate_average(nums):
    """calculate_average"""
    total = sum(nums)
    count = len(nums)
    average = total / count
    return average


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)