lst = [9, 41, 12, 3, 74, 15]


def my_min(lst):
    smallest_so_far = None
    for the_num in lst:
        if smallest_so_far is None:
            smallest_so_far = the_num
        else:
            if the_num < smallest_so_far:
                smallest_so_far = the_num
    return smallest_so_far


print(lst)
print(my_min(lst))


def my_max(lst):
    largest_so_far = None
    for the_num in lst:
        if largest_so_far is None:
            largest_so_far = the_num
        else:
            if the_num > largest_so_far:
                largest_so_far = the_num
    return largest_so_far


print(lst)
print(my_max(lst))


def my_average(lst):
    sum = 0
    for the_num in lst:
        sum = sum + the_num  
    average = sum / len(lst)
    return average


print(lst)
print(my_average(lst))


def my_median(lst):
    med = sorted(lst)
    r = int(len(med) / 2)

    if len(med) % 2 == 1:
        return med[r]
    else:
        return (med[r] + med[r - 1])/2


print(lst)
print(my_median(lst))


def my_range(lst):
    a = my_max(lst)
    b = my_min(lst)
    range = a - b
    return range

print(lst)
print(my_range(lst))