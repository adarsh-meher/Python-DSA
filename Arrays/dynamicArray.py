'''
Create dynamic array. Includes the following functionalities : 
    1. Create an empty array with user-specified size. Defaults to 1 if none provided.
    2. Return length of array.
    3. Return object at specified index of the array.
    4. Append object at the end of an array.
    5. Resize array if the current size is full

'''


import sys
import ast
import ctypes
import typing
print(typing.__spec__)
print(typing.__package__)

class DynamicArray:
    '''Class to implement dynamic array.

    '''
    def __init__(self,size: int = 1):
        self._n = 0
        self._capacity = size
        self._A = self._make_array(self._capacity)
    
    def __len__(self):
        return self._n
    
    def __getitem__(self,pos):
        if 0<=pos<self._n:
            return self._A[pos]
        return IndexError("Invalid Index")
    
    def display_array(self):
        if self._n==0:
            print('No data yet in the array.')
        return [ self._A[i] for i in range(self._n)]


    def append(self,obj):
        print("Append data to array.")
        print(f"Current array size : {self._n}")
        print(f"Current array capacity : {self._capacity}")
        if self._n==self._capacity:
            self._resize(self._capacity*2)
        self._A[self._n]=obj
        self._n = self._n+1

    def _resize(self,inc_size):
        print("Resizing array : ")
        B = self._make_array(inc_size)
        for i in range(self._n):
            B[i] = self._A[i]
        self._A = B
        self._capacity = inc_size
    
    def _make_array(self,c):
        print(f"Creating an array of size  :{c}")
        return (c*ctypes.py_object)()





if __name__ == '__main__':
    
    print("Execute dynamic array.")
    print('To exit the demo, input `exit`')

    arrsize = input('Provide initial array size (defaults to 1) : ')
    dynArr = DynamicArray(size=int(arrsize))
    print(dynArr)

    numList = input("Input list of numbers to add to array : ")
    if numList.rstrip().lower()=='exit':exit
    
    numList = ast.literal_eval(numList)

    for i in numList:
        dynArr.append(i)

    print("Array after append : ")
    print(dynArr.display_array())




    



         
        









