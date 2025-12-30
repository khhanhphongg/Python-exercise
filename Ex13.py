#Ex13
if __name__ == '__main__':
    A = [1,2,3,4,5,6,7,8,9,10]
    B = [2,4,1,0,1,5,0,8,0,5]
    common_elements = set(A) & set(B)
    print("Intersection numbers:",common_elements)