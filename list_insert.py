'''
inserts an element into an existing  list. from position 0 to end of the list. 

'''
array1 = []
def insert(list1, value, index):
    if index < 0 or  index > len(list1) :
        print(f"Out of index. Length is {len(list1)}")
        return list1 
        # raise IndexError("give index in boundary")
    else: 
        list_f = list1[0:index]
        list_f.append(value )
        list_b = list1[index:]
        list_new = list_f + list_b 
        return list_new 



while True :

    values = int(input ("Enter the value "))
    index = int(input("Enter the location "))

    array1 = insert(array1, values, index)
    print(f" The List is : {array1}")

    choice = input ("Quit ?? [y | y] ")
    print (choice)
    if choice == 'y' or choice == 'Y'  :
        print("Quiting")
        break 
    
