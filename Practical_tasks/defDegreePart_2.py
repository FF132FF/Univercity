import defDegree

def list(*args, **kwargs):
    s = 0
    l = []
    for i in args:
        l.append(f"Point{i} = {defDegree.deg_to_gms(i)}")
        s +=1
    for i, v in kwargs.items():
        l.append(f"{i} = {defDegree.deg_to_gms(v)}")
    return(l)

print(list(2.19, 3.14, 5.16, pole=123.11, test=222.77))