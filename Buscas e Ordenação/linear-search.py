def find_age(vector, age):
    position = 0

    while position <= len(vector) -1:
        if vector[position] == age:
            return position
        
        position += 1
        
    return -1
        
ages = [10, 55, 73, 49, 22, 77, 54, 25, 80]

result = find_age(ages, 1)

if result == -1: 
    print("The number was'nt found")
else:
    print(f"The wished number was found in the {result} index.")

