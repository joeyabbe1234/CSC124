import random
import matplotlib.pyplot as plt
import time

start_time = time.time()
arr2 = []
start = 0
stop = 100000
limit = int(input("enter the number of intergers: "))

def insertionSort(arr):
	
	for i in range(1,len(arr)):
		current = arr[i]
		while i>0 and arr[i-1]>current:
			arr[i] = arr[i-1]
			i = i-1
			arr[i] = current

	
	return arr


arr = [random.randint(start, stop) for iter in range(limit)]
insertionSort(arr)
print(arr)
print(time.time() - start_time, "seconds")
arr2.append(time.time() - start_time)
print(arr2)

start = 0
stop = 1000000
limit = int(input("enter the number of intergers: "))
arr = [random.randint(start, stop) for iter in range(limit)]
insertionSort(arr)
print(arr)
print(time.time() - start_time, "seconds")
arr2.append(time.time() - start_time)
print(arr2)

start = 0
stop = 1000000
limit = int(input("enter the number of intergers: "))
arr = [random.randint(start, stop) for iter in range(limit)]
insertionSort(arr)
print(arr)
print(time.time() - start_time, "seconds")
arr2.append(time.time() - start_time)
print(arr2)

start = 0
stop = 1000000
limit = int(input("enter the number of intergers: "))
arr = [random.randint(start, stop) for iter in range(limit)]
insertionSort(arr)
print(arr)
print(time.time() - start_time, "seconds")
arr2.append(time.time() - start_time)
print(arr2)


x = [10,100,1000,10000]
y = arr2
plt.xlabel('Number of integers')
plt.ylabel('execution time')
plt.plot(x, y)
plt.title("Insertion Sort")
plt.show()
