min_num = None
lst = [9, 41, 12, 3, 74, 15]
for the_num in lst:
    if min_num is None:
        min_num = the_num
    else:
        if the_num < min_num:
            min_num = the_num
print(lst)
print(min_num)
