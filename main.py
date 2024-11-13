import numpy as np

array1 = np.array([1,2,3])
print("array1",array1)

a2 = np.linspace(0,100,21)
print("a2",a2)

a3 = np.zeros(9)
print("a3",a3)

a4 = np.ones(12)
print("a4",a4)

random1 = np.random.rand(2,3)
print("random1",random1)

random1 = np.random.rand(2,3)*23
print("random1",random1)

np.random.seed(18)
random2 = np.random.rand(2,3)
print("random2",random2)

random2 = random1.reshape(3,2)
print("random2",random2)