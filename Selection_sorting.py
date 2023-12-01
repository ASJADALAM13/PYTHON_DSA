#1.
#ALgo
"""
1.FIND THE MINIMUM VALUE IN THE ARRAY
2.SWAP IT WITH THE VALUE IN THE CURRENT POSITION 
3.REPEAT THE PROCESS FOR ALL THE ELEMENTS
"""
def selection_sort(arr):
    l=len(arr)
    for i in range(0,l):
        mini=i
        for j in range(i+1,l):
            if arr[j]<arr[mini]:
                mini=j
        arr[i],arr[mini]=arr[mini],arr[i]
    print(arr)
#selection_sort([9,7,1,9,20])

 
#2.
def optimized_bubble_sort(arr):
    l=len(arr)
    for i in range(l-1,0,-1):
        flag=True
        for j in range(i):
            if arr[j]>arr[j+1]:   # If Swap is made falg=False
                arr[j],arr[j+1]=arr[j+1],arr[j]  
                flag=False 
        if flag:
            print("This array is sorted")   #If swap does not made than this means that this array is already sorted
        break
    print(arr)
#optimized_bubble_sort([1,5,2,3])


#3.
#In Insertion Sort, the array is divided into a sorted and an unsorted region.
def insertion_sort(arr):
    l=len(arr)

    for i in range(1,l):
        key=arr[i] 
        j=i

        while(j>=1 and arr[j-1]>key):
            arr[j]=arr[j-1]
            j=j-1
        arr[j]=key
        

    print(arr)

""" #0,1,2,3,4
lst=[9,8,5,4,3]
insertion_sort(lst)"""



















































































