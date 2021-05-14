a = [64,25,12,15,11]
print('Before sorting: ',a)

def selection_sort(a):
    for i in range(len(a)):
        min_idx = i
        for j in range(i+1,len(a)):
            if a[j] <  a[min_idx]:
                min_idx = j
        a[i],a[min_idx]=a[min_idx],a[i]
    print("Output for selection sort is below")
    for i in a:
        print(i, end=' ')

def bubble_sort(a):
    array_length = len(a)
    for i in range(array_length):
        for j in range(0, array_length-i-1):
            if a[j] > a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    print("\n output for bubble sort is below")
    for i in a:
        print (i, end= ' ')

def insertion_sort(a):
    for i in range(1,len(a)):
        key =a[i]
        j = i-1
        while j>=0 and key <a[j]:
            a[j+1] =a[j]
            j = j-1
        a[j+1] = key
    print("\n output for Insertion sort is below")
    for i in a:
        print (i, end= ' ')


def merge_sort(a):
    if len(a)>1:
        mid = len(a)//2
        L = a[:mid]
        R = a[mid:]
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        while i<len(L) and j < len(R):
            if L[i]>R[j]:
                a[k] = L[i]
                i+=1
            else:
                a[k] = R[j]
                j+=1
            k+=1
        while i <len(L):
            a[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            a[k] = R[j]
            j+=1
            k+=1

a = [64,25,12,15,11]
selection_sort(a)
a = [64,25,12,15,11]
bubble_sort(a)
a = [64,25,12,15,11]
insertion_sort(a)
a = [12, 11, 13, 5, 6, 7]
print("Given array is ",a, end="\n")
merge_sort(a)
print('\n Output after Merge sort')
for i in a:
    print(i, end =' ')

