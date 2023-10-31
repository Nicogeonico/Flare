import numpy as np

x1 = np.linspace(0, 10, 50)
x2 = np.linspace(0, 100,  50)
y = np.sqrt(np.sin(x) + np.cos(x))

a_list = [1, 2, 3, 6, 8, 10]

# print('The variable x:')
# print(x)
#
# # Comments
# print('The variable a_list:') # add a comment
# print(a_list)

def calculate_math(x):
    y = np.sqrt(np.sin(x) + np.cos(x))
    return y

print(calculate_math(x1))
y2 = calculate_math(x1)
print(y2)

y3 = y2+ 1
