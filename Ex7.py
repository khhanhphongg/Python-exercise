#Ex7
if __name__ == '__main__':
    A = [1,2,3,4,5,6,7,8,9,10]*3
    value = int(input("Enter a number:"))
    if value in A:
        A.remove(value)
        print("Number has been deleted")
        print("New list:", A)
    else:
        print("Number not in the list")