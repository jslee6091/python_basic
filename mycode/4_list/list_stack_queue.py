# stack
seutak = [2, 3, 4, 5]
seutak.append(23)
seutak.append(123)
seutak.pop()
seutak.extend([33,22])
print(seutak)

# queue
kue = [4, 7, 8, 2]
kue.append(333)
kue.append(222)
kue.append(65)
kue.pop(0)
print(kue)

# tuple
tue = [3, 4, 5]
tue2 = (3, 4, 5)
print(type(tue), type(tue2))
tue3 = (1)
tue4 = (1,)
print(type(tue3), type(tue4))

# set
ss = set([1, 2, 3])
print(ss)
ss.add(4)
print(ss)
ss.remove(3)
print(ss)
ss.update([6, 7, 8, 9])
print(ss)
ss.clear()
print(ss)
