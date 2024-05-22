''' generates a list of list of list. 3D matrix. 

output: 

[
    [   [10, 11, 12, 13, 14],
        [10, 11, 12, 13, 14], 
        [10, 11, 12, 13, 14], 
        [10, 11, 12, 13, 14], 
        [10, 11, 12, 13, 14]
    ], 
    [
        [10, 11, 12, 13, 14], 
        [10, 11, 12, 13, 14], 
        [10, 11, 12, 13, 14], 
        [10, 11, 12, 13, 14], 
        [10, 11, 12, 13, 14]
    ], 
    [
        [10, 11, 12, 13, 14], 
        [10, 11, 12, 13, 14], 
        [10, 11, 12, 13, 14], 
        [10, 11, 12, 13, 14], 
        [10, 11, 12, 13, 14]
    ], 
    [
        [10, 11, 12, 13, 14], [10, 11, 12, 13, 14], 
[10, 11, 12, 13, 14], [10, 11, 12, 13, 14], [10, 11, 12, 13, 14]], [[10, 11, 12, 13, 14], [10, 11, 12, 13, 14], [10, 11, 12, 13, 14], [10, 11, 12, 13, 14], [10, 11, 12, 13, 14]]]

'''
lst = [  [   [i for i in range(10,15) ] for j in range (20,25) ]  for k in range(5)  ]
print (lst )