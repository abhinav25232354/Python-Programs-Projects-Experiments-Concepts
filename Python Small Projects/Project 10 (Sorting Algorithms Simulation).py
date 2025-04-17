l = [122, 2434, 123, 121, 23987]
result = []

for value in l:
    if not result:
        result.append(value)
    else:
        inserted = False
        for i in range(len(result)):
            if value < result[i]:
                result.insert(i, value)
                inserted = True
                break
        if not inserted:
            result.append(value)

print("Sorted list:", result)