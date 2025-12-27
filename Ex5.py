#Ex5
if __name__ == '__main__':
    A = [1,2,3,4,5,6,7,8,9,10]
    value = int(input("Enter a number:"))
    lastIndex = -1
    for i in range(0, len(A)):
        if A[i] == value:
            lastIndex = i
    if lastIndex != -1:
        print("Last Index", lastIndex)
    else:
        print("Not found")