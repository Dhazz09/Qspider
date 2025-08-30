#list methods
def analyze_list_methods():
    sample = [1, 2, 3]
    print("Initial list:", sample)
    
    # Special (dunder) methods demonstration
    print("\n--- Special Methods ---")
    print("__add__ (concatenation):", sample.__add__([4, 5]))
    print("__contains__ (check membership):", sample.__contains__(2))
    print("__eq__ (equality):", sample.__eq__([1, 2, 3]))
    print("__getitem__ (indexing):", sample.__getitem__(1))
    print("__len__ (length):", sample.__len__())
    print("__iter__ (iteration):", [x for x in sample.__iter__()])
    print("__mul__ (repeat):", sample.__mul__(2))
    print("__rmul__ (repeat, reversed):", sample.__rmul__(2))
    print("__str__ (string):", sample.__str__())
    print("__repr__ (repr):", sample.__repr__())
    print("__reversed__ (reverse iterator):", [x for x in sample.__reversed__()])

    # Normal list methods
    print("\n--- Normal Methods ---")
    sample.append(4)
    print("append(4):", sample)

    sample2 = sample.copy()
    print("copy():", sample2)

    print("count(2):", sample.count(2))

    sample.extend([5, 6])
    print("extend([5,6]):", sample)

    print("index(3):", sample.index(3))

    sample.insert(1, 99)
    print("insert(1, 99):", sample)

    popped = sample.pop()
    print("pop():", popped, "list=", sample)

    sample.remove(99)
    print("remove(99):", sample)

    sample.reverse()
    print("reverse():", sample)

    sample.sort()
    print("sort():", sample)

    sample.clear()
    print("clear():", sample)

if __name__ == "__main__":

    analyze_list_methods()