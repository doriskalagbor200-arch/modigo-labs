def find_index(numbers, target):
    count =-1
    for i in numbers:
        count += 1
        if i == target:
            return count
    return -1
print(find_index([1, 3, 5, 7, 9], 5))