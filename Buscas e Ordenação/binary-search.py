def find_age(vector, age):
    vector.sort()

    print(vector)

    start = 0
    end = len(vector) - 1

    while start <= end:
        middle = (start + end) // 2

        if vector[middle] == age:
            return middle
        elif age < vector[middle]:
            end = middle - 1
            print("Is minus than the middle value")
        elif age > vector[middle]:
            start = middle + 1
            print("Is more than the middle value")

    return -1

ages = [55, 72, 15, 18, 60, 88, 41, 33, 20, 16]

result = find_age(ages, 57)

if result == -1:
    print("The entered age is'nt in the vector.")
else:
    print(f"The entered number were found in the index {result}.")

