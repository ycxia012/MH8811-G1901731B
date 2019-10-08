def my_max(data): #function for my_max
    largest_so_far = None
    for the_num in data:
        if largest_so_far is None:
            largest_so_far = the_num
        else:
            if the_num > largest_so_far:
                largest_so_far = the_num
    return largest_so_far

def my_min(data): #function for my_min
    smallest_so_far = None
    for the_num in data:
        if smallest_so_far is None:
            smallest_so_far = the_num
        else:
            if the_num < smallest_so_far:
                smallest_so_far = the_num
    return smallest_so_far

def my_average(data): #function for my_average
    sum = 0
    for the_num in data:
        sum = sum + the_num  
    average = sum / len(data)
    return average

def my_median(lst): #function for my_median
    med = sorted(lst)
    r = int(len(med) / 2)

    if len(med) % 2 == 1:
        return med[r]
    else:
        return (med[r] + med[r - 1])/2

def my_range(data): #function for my_range
    a = max(data)
    b = min(data)
    range = a - b
    return range


def getFilelines(fname):
    fhandle = open(fname)
    lines = []
    for line in fhandle:
        line = line.rstrip()
        if line:
            line = float(line)
            lines.append(line)
    fhandle.close()
    return lines

data = getFilelines('data.csv')
#print(data: max, min, average, median, range)
print(my_max(data))
print(my_min(data))
print(my_average(data))
print(my_median(data))
print(my_range(data))