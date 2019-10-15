import json

def op_f(filename):
    fh=open(filename)
    data=json.load(fh)
    fh.close()
    return data
    


def serialize(l):
    s=json.dumps(l)
    return s

        
filename=input('H1-1.json,H1-2.json,H1-3.json,H1-4.json or H1-5.json?')

d1=op_f(filename)
print(d1)
print(type(d1))
print('Success!')
    

s=serialize(d1)
print(type(s)) 


filename1=input('what will be the name of the new file?')
with open(filename1,'w') as f_w:
    json.dump(s,f_w)
    f_w.close()
    print('Success!')


with open(filename1) as f_r:
       d2=json.load(f_r)
       f_r.close()
print(d2)
print(type(d2))
print('Success!')

d2=json.loads(d2)
print(d2)
print(type(d2))

