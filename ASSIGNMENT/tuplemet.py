# Object to analyze (tuple)
obj = (1, 2, 3, 2)

methods = [
    '__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__',
    '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
    '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__',
    '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__',
    '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
    '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
    'count', 'index'
]

print(f"Analyzing object: {obj}\nType: {type(obj)}\n")

for method in methods:
    try:
        attr = getattr(obj, method)
        if callable(attr):
            # Safe demo calls
            if method == "__add__":
                result = attr((9, 9))
            elif method == "__contains__":
                result = attr(2)
            elif method == "__getitem__":
                result = attr(1)
            elif method == "__mul__":
                result = attr(2)
            elif method == "__rmul__":
                result = attr(2)
            elif method == "count":
                result = attr(2)
            elif method == "index":
                result = attr(2)
            elif method == "__format__":
                result = attr("")
            elif method == "__eq__":
                result = attr((1, 2, 3, 2))
            elif method == "__ne__":
                result = attr((1, 2, 3))
            elif method == "__ge__":
                result = attr((1, 2, 3))
            elif method == "__gt__":
                result = attr((1,))
            elif method == "__le__":
                result = attr((1, 2, 3))
            elif method == "__lt__":
                result = attr((1, 2, 3, 2, 4))
            else:
                result = attr()
            print(f"{method:20s} -> {result}")
        else:
            print(f"{method:20s} -> {attr}")
    except Exception as e:
        print(f"{method:20s} -> ERROR: {e}")