classes = []
if issubclass(D, A):
    classes.append("A")
if issubclass(D, B):
    classes.append("B")
if issubclass(D, C):
    classes.append("C")
print(" ".join(classes))

