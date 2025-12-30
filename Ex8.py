#Ex8
if __name__ == '__main__':
    A = [1,2,3,4,5,6,7,8,9,10]*3
    value = int(input("Enter a number: "))
    while value in A:
        A.remove(value)

    print("New list:", A)