# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
# EXPLANATION:
# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
# The correct answer would be 17.
# Hint: Don't forget to check for bad values like None.
# EXAMPLES:
# counting_sheep([]), --> 0
# counting_sheep([True, True, None, True, None, False]) --> 3
# counting_sheep([False, False, False, None, None, None]) --> 0

def count_sheep(arr):
    print (sum(sheep for sheep in arr if sheep == True))

def count_sheep2(arr):
    Sheep_sum = 0
    for sheep in arr:
        if sheep == True:
            Sheep_sum += 1
    print(Sheep_sum)


count_sheep([True,  True,  True,  False, None, True, 'Cow'])

count_sheep2([True,  True,  True,  False, None, True, 'Cow'])


