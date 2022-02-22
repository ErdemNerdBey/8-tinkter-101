from operator import neg


def count_positives_sum_negatives(arr):
    pos = list()
    neg = list()
    if arr == ():
        return list()

    for num in arr:
        if num > 0:
            pos.append(arr[num])

        else:
            neg.append(arr[num + 9])
            print(arr[num])
            print(neg)
    gesumt = sum(neg)
    return len(pos), gesumt



  
print(count_positives_sum_negatives(() ) )   