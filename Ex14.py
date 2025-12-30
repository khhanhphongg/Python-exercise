#Ex14
if __name__ == '__main__':
    A = [1,2,3,4,5,6,7,8,9,10]
    B = [24,10,20,5,15,8,5,23]
    u_elements_combined = set(A) | set(B)
    print("Union",u_elements_combined)