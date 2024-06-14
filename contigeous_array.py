'''program to find the max of sum of 4 numbers (example list=[-2,0,2,4] find max of sum 2 numbers
the answer would be 4 -->2+4=6,-2+2=0,etc)'''
'''def max_sum(array,number):
    narray=len(array)
    if number>narray:
        return 'subarray of size greater than the array isnot possible'
    current_sum=sum(array[:number])
    max_sum=float('-inf')
    for i in range(1,narray-number+1):
        current_sum=current_sum-array[i-1]+array[i+number-1]
        max_sum=max(max_sum,current_sum)
    return max_sum


array1=[4,3,2,7,1,9]
number=3
print(max_sum(array1,number))'''


'''basket ball a=[4,3,2,7,1,9] where we need to add the element with its index
thst is (4x0,3x1....) r=[0,3,4,21,4,45] and we need to apply the above operation
max max=[7,28,29,70] max=70--->subarray=[7,1,9]'''

def max_sum(array,number):
    narray=len(array)
    max_sum=float('-inf')
    for i in range(narray-number+1):
        current_sum=0
        for j in range(number):
            current_sum+=(i+j)*array[i+j]
            max_sum=max(max_sum,current_sum)
    return max_sum


array1=[4,3,2,7,1,9]
number=3
print(max_sum(array1,number))
