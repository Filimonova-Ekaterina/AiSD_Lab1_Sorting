import random
from random import randint
import matplotlib.pyplot as plt
import time
import math
import numpy as np
def selection_sort(arr):
   for i in range(0, len(arr) - 1):
       temp = i
       for j in range(i + 1, len(arr)):
           if arr[j] < arr[temp]:
               temp = j
       arr[i], arr[temp] = arr[temp], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while (j >= 0 and temp < arr[j]):
            arr[j + 1] = arr[j]
            j = j - 1
            arr[j + 1] = temp

def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def merge_sort(arr):
    if len(arr)==1:
        return arr
    mid = (len(arr)-1) // 2
    lst1 = merge_sort(arr[:mid+1])
    lst2 = merge_sort(arr[mid+1:])
    result = merge(lst1, lst2)
    return result
    
def merge(lst1, lst2):
    lst = []
    i = 0
    j = 0
    while(i<=len(lst1)-1 and j<=len(lst2)-1):
         if lst1[i]<=lst2[j]:
             lst.append(lst1[i])
             i+=1
         else:
               lst.append(lst2[j])
               j+=1
    if i>len(lst1)-1:
         while(j<=len(lst2)-1):
               lst.append(lst2[j])
               j+=1
    else:
         while(i<=len(lst1)-1):
               lst.append(lst1[i])
               i+=1
    return lst   


def shell_sort(arr, sequence):

    gaps = []
    if sequence == 'shell':
        gap = len(arr) // 2
        while gap > 0:
            gaps.append(gap)
            gap //= 2
    elif sequence == 'pratt':
        i, j = 0, 0
        while True:
            gap = (2 ** i) * (3 ** j)
            if gap > len(arr):
                break
            gaps.append(gap)
            if i < j:
                i += 1
            else:
                j += 1
        gaps.reverse()
    elif sequence == 'hibbard':
        k = 1
        while (2 ** k) - 1 < len(arr):
            gaps.append((2 ** k) - 1)
            k += 1

    for gap in gaps:
        for i in range(gap, len(arr)):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
        left = []
        mid=[]
        right=[]
        for i in arr:
            if i<pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            else:
                mid.append(i)
        return quick_sort(left) + mid + quick_sort(right)

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[i] < arr[left]:
        largest = left 
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
                
def heap_sort(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


random.seed(1)
n=1000
sequence = 'shell'
ins_sort_time=[]
select_sort_time=[]
merge_sort_time=[]
quick_sort_time=[]
shell_sort_time_1=[]
shell_sort_time_2=[]
shell_sort_time_3=[]
bubble_sort_time=[]
heap_sort_time =[]
size_arr=[]

#Сортировки и их время выполнения на примере одинаково заполненных масивов
for i in range(10):
    arr = [randint(1,n) for i in range(n)]
    arr1=arr2=arr3=arr4=arr5=arr6=arr7=arr8=arr.copy()
    t_start=time.time()
    selection_sort(arr)
    select_sort_time.append(time.time()-t_start)
    t_start=time.time()
    insertion_sort(arr1)
    ins_sort_time.append(time.time()-t_start)
    t_start=time.time()
    merge_sort(arr2)
    merge_sort_time.append(time.time()-t_start)
    t_start=time.time()
    quick_sort(arr4)
    quick_sort_time.append(time.time()-t_start)
    t_start=time.time()
    shell_sort(arr5,sequence)
    shell_sort_time_1.append(time.time()-t_start)
    sequence = 'hibbard'
    t_start=time.time()
    shell_sort(arr7,sequence)
    shell_sort_time_2.append(time.time()-t_start)
    sequence = 'pratt'
    t_start=time.time()
    shell_sort(arr8,sequence)
    shell_sort_time_3.append(time.time()-t_start)
    t_start=time.time()
    bubble_sort(arr3)
    bubble_sort_time.append(time.time()-t_start)
    t_start=time.time()
    heap_sort(arr6)
    heap_sort_time.append(time.time()-t_start)
    size_arr.append(n)
    n+=100


print ("время выполнения сортировки: ")
#print("выбором ", sum(ins_sort_time)/len(ins_sort_time))
#print ("вставками ", sum(ins_sort_time)/len(ins_sort_time))
#print("пузырьком ", sum(bubble_sort_time)/len(bubble_sort_time))
print("слиянием ", sum(merge_sort_time)/len(merge_sort_time))
print("быстрой ", sum(quick_sort_time)/len(quick_sort_time))
print("шелла, последовательность шелла ", sum(shell_sort_time_1)/len(shell_sort_time_1))
print("шелла, последовательность хиббарда ", sum(shell_sort_time_2)/len(shell_sort_time_2))
print("шелла, последовательность пратта ", sum(shell_sort_time_3)/len(shell_sort_time_3))
print("пирамидальная", sum(heap_sort_time)/len(heap_sort_time))
print(size_arr)

#Использовалось для построения регрессионных кривых
#sizes = np.array(size_arr)
#times = np.array(time0)
#coeffs = np.polyfit(sizes, times, 2)
#poly = np.poly1d(coeffs)
#plt.scatter(sizes, times, color='blue')
#plt.plot(sizes, poly(sizes), color='red', label='Selection sort')

#Использовалось для графиков сортировок с квадратичной сложностью 
#plt.plot(size_arr,ins_sort_time, label='Insertion sort',marker='o',markersize = 4,color="b")
#plt.plot(size_arr,select_sort_time, label='Selection sort',marker='o',markersize = 4,color="g")
#plt.plot(size_arr,bubble_sort_time, label='Bubble sort',marker='o',markersize = 4,color="k")

#Графики сортировок с не квадратичной сложностью
plt.plot(size_arr,merge_sort_time, label='Merge sort',marker='o',markersize = 4,color="g")
plt.plot(size_arr,quick_sort_time, label='Quick sort',marker='o',markersize = 4,color="y")
plt.plot(size_arr,shell_sort_time_1, label='Shell sequence',marker='o',markersize = 4,color="m")
plt.plot(size_arr,shell_sort_time_2, label='Hibbard sequence',marker='o',markersize = 4,color="b")
plt.plot(size_arr,shell_sort_time_3, label='Pratt sequence',marker='o',markersize = 4,color="k")
plt.plot(size_arr,heap_sort_time, label='Heap sort',marker='o',markersize = 4,color="0.8")
plt.xlabel('Size of array')
plt.ylabel('Time to sort')
plt.legend()
plt.savefig("1.png")
plt.show()
