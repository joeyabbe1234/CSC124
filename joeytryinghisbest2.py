import random
import time
import matplotlib.pyplot as plt

start_time = time.time()
arr2 = []
start = 0
stop = 100000
limit = int(input("enter the number of intergers: "))

def mergeSort(arr):
    print("Splitting ",arr)
    if len(arr)>1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                arr[k]=lefthalf[i]
                i=i+1
            else:
                arr[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            arr[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            arr[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",arr)

arr = [random.randint(start, stop) for iter in range(limit)]
mergeSort(arr)
print(time.time() - start_time, "seconds")
arr2.append(time.time() - start_time)
print(arr2)

start = 0
stop = 100000
limit = int(input("enter the number of intergers: "))
arr = [random.randint(start, stop) for iter in range(limit)]
mergeSort(arr)
print(time.time() - start_time, "seconds")
arr2.append(time.time() - start_time)
print(arr2)

start = 0
stop = 100000
limit = int(input("enter the number of intergers: "))
arr = [random.randint(start, stop) for iter in range(limit)]
mergeSort(arr)
print(time.time() - start_time, "seconds")
arr2.append(time.time() - start_time)
print(arr2)

start = 0
stop = 100000
limit = int(input("enter the number of intergers: "))
arr = [random.randint(start, stop) for iter in range(limit)]
mergeSort(arr)
print(time.time() - start_time, "seconds")
arr2.append(time.time() - start_time)
print(arr2)

x = [10,100,1000,10000]
y = arr2
plt.xlabel('Number of integers')
plt.ylabel('execution time')
plt.plot(x, y)
plt.title("Merge Sort")
plt.show()
