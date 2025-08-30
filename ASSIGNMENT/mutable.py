#program to check whether the datatypes are mutable or not
def is_mute(data):
    try:
        a=id(data)
        if isinstance(data,list):
            data.append(None)
        elif isinstance(data,dict):
            data["test"]=True
        elif isinstance(data,set):
            data.add("test")
        elif isinstance(data,bytearray):
            data[0]=255
        else:
            data+=data
        a=id(data)
    except Exception:
        return False
d=[10,"hello",(1,2,3,4),[11,12,13,14,15],{"a":1,"b":2},{1,2,3,4},bytearray(b"abc")]
for i in d:
    if(is_mute(i)):
        print(f"{i} is MUTABLE and it belongs to {type(i)} ")    
    else:
        print(f"{i} is NON-MUTABLE and it belongs to {type(i)}")
