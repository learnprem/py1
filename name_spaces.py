a = 1
def my_fun():
    a = 10
    print (f"function a = {a} "   )
    for aa in range(4):
        a = 17
        # print (f"for aa = {aa} "   )
        print (f"for a = {a} "   )

    print (f"function a = {a} "   )
    return None


print(f"global a = {a}")
my_fun()

