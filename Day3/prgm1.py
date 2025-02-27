
def partition_batches(arr,size):
    lst = []
    for i in range(0,len(arr),size):
        lst.append(arr[i:size+i])
    return lst
arr = list(range(430))

print(partition_batches(arr,50))