arr = []

def increasing_quick_sort(arr):
     if len(arr) <= 1:
          return arr
     
     pivot = arr[len(arr)//2]
     left = [i for i in arr if i < pivot]
     right = [i for i in arr if i > pivot]
     middle = [i for i in arr if i == pivot]

     return increasing_quick_sort(left) + middle + increasing_quick_sort(right)

def decreasing_quick_sort(arr):
     if len(arr) <= 1:
          return arr
     
     pivot = arr[len(arr)//2]
     left = [i for i in arr if i > pivot]
     right = [i for i in arr if i < pivot]
     middle = [i for i in arr if i == pivot]

     return decreasing_quick_sort(left) + middle + decreasing_quick_sort(right)