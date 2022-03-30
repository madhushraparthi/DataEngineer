# Python script to merge dict using update() method

def Merge(dict_1, dict_2):
    return(dict_2.update(dict_1))
     
# main code
dict_1 = {'a': 10, 'b': 8}
dict_2 = {'d': 6, 'c': 4}
 
# This return None
print(Merge(dict_1, dict_2))
 
# changes made in dict_2
print(dict_2)