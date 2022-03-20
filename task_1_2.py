numbers = range(1, 1000, 2)
# numbers = list(range(1, 1000, 2))
print(numbers)
for i in numbers:
    cube = i ** 3
    dig_sum = 0
    while cube != 0:
        dig_sum += cube % 10
        cube //= 10
        print(cube)



# print(s)
#

# cube_list = []
#     cube_list.extend(cube)
# print(type(cube_list))
# for i in cube:
#     i = i.split()
#     print(sum(list(i)))





