lst = [1,2,3,1,2,30]

def sep(numbers):
    unique = set()
    duplicated = []

    for i in numbers:
        if i not in unique:
            unique.add(i)
        else:
            duplicated.append(i)
    return unique, duplicated

print(sep(lst))