#Ex4
if __name__ == '__main__':
    A = [1,2,3,4,5,6,7,8,9,10]
    value = int(input("Enter a number:"))
    if value in A:
        firstIndex = A.index(value)
        print("First Index:", firstIndex)
    else:
        print("Not found")