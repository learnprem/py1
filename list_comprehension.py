

list1 = []
list1 = [i  for i in range(10)  if i % 2 == 0 ]
print (list1)

list1 = []
# same as above, but error. may be because of the else is 
# treated as for ... else ? 
# list1 = [i  for i in range(10)  if i % 2 == 0  else i]
print(list1)


list1 = []
list1 = ["Even "  if i % 2 == 0 else "Odd" for i in range(10)  ]
print (list1)

