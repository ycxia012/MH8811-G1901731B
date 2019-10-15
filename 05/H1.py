import json
#function for open the file
def op_f(filename):
    fh=open(filename)
    data=json.load(fh)
    fh.close()
    return data
    

#function for serialize
def serialize(l):
    s=json.dumps(l)
    return s

 #input files       
filename=input('H1-1.json,H1-2.json,H1-3.json,H1-4.json or H1-5.json?')

#Load the json file
d1=op_f(filename)
print(d1)
print(type(d1))
print('Success!')
    
#Convert the data into string
s=serialize(d1)
print(type(s)) 

#Write the sting to the file
filename1=input('what will be the name of the new file?')
with open(filename1,'w') as f_w:
    json.dump(s,f_w)
    f_w.close()
    print('Success!')

#Read the string
with open(filename1) as f_r:
       d2=json.load(f_r)
       f_r.close()
print(d2)
print(type(d2))
print('Success!')

#To deserialization function
d2=json.loads(d2)
print(d2)
print(type(d2))

#function for comparison
def my_compare(d1,d2):
    if type(d1) == type(d2):
        if type(d1) == type([]):
            print(diff_lst(d1,d2))
        if type(d1) == type({}):
            print(diff_dict(d1,d2))
    else:
        return False

#function for compare the list
def diff_lst(d1,d2):
    if len(d1) == 0:
        return True
    v=d1[0]
    for v1 in d2:
        if type(v) != type(v1):
            return False

        if type(v) == list:
            if not diff_lst(v,v1):
                return False

        if type(v) == dict:
            if not diff_dict(v,v1):
                return False

    return True

#function for comapre the dict
def diff_dict(d1,d2):
        for k,v in d1.items():
            if k not in d2.keys():
                return False
            v1 =d2[k]

        if type(v) != type(v1):
            return False

        elif type(v) == dict:    
            if not diff_dict(v,v1):
                return False

        elif type(v) == list:
            if not diff_lst(v,v1):
                return False

        return True

my_compare(d1,d2)