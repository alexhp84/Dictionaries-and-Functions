def get_statistics(numbers):
    """
    creates a list based on numbers
    it calculates the total, and average, as well as printing the highest and lowest numbers
    :param numbers:
    :return:
    """
    result = {}
    result["sum"] = sum(numbers)
    result["avg"] = sum(numbers) / len(numbers)
    result["min"] = min(numbers)
    result["max"] = max(numbers)
    result["len"] = len(numbers)

    return result

numbers = [4, 8, 2, 10, 6]
result = get_statistics(numbers)
print(f"The total is",result["sum"])
print(f"The average is",result["avg"])
print(f"The lowest number is",result["min"])
print(f"The highest number is",result["max"])
print(f"There are",result["len"],"numbers in the list")
