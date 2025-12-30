#Ex6
if __name__ == '__main__':
    A = [1,2,3,4,5,6,7,8,9,10]
    value = int(input("Enter a number:"))
    counter = 0
    for i in range(0, len(A)):
        if A[i] == value:
            counter = counter + 1
    print("Times of value: ", counter)