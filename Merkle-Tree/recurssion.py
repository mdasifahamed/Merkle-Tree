"""
Reccursion
"""

# def sum(n):

#     if n==1:
#         return 1
#     result=n+sum(n-1)
#     print(result)


# sum(5)
# def recursive_sum(arr):
#     # Base case: If the array is empty, the sum is 0.
#     if not arr:
#         return 0
#     # Recursive case: Calculate the sum of elements using recursion.
#     else:
#         # The sum is the first element plus the sum of the rest of the elements.
#         return arr[0] + recursive_sum(arr[1:])
    


# print(recursive_sum([1,2,3,4,5]))



# Recuursive Even Sum 

def evensum(arr):
    arr1 = arr
    if not arr1:
        return 0
    if arr[0]%2 !=0:
        arr1=arr1[1:]
        return arr1[0] + evensum(arr1[1:])
    else:
        return arr1[0] + evensum(arr1[1:])




print(evensum([2,4,6,8,10,12,12]))
