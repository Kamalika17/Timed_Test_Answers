import matplotlib.pyplot as plt
import numpy as np
import random

# mean and standard deviation for 3 features
A_mean = []
B_mean = []
A_std = []
B_std = []

for i in range(0,2):
	A_mean.append(random.randint(20,100))
	B_mean.append(random.randint(20,100))
	A_std.append(random.randint(1,3)*random.random())
	B_std.append(random.randint(1,3)*random.random())

num = 50
A_1 = []
A_2 = []
A_3 = []
B_1 = []
B_2 = []
B_3 = []

A_1 = np.random.normal(A_mean[0], A_std[0], num)
A_2 = np.random.normal(A_mean[1], A_std[1], num)
A_3 = np.random.binomial(num, 0.25, num)

B_1 = np.random.normal(B_mean[0], B_std[0], num)
B_2 = np.random.normal(B_mean[1], B_std[1], num)
B_3 = np.random.binomial(num, 0.2,  num)


#plt.scatter(A_1, B_1, label='Feature_1')
#plt.scatter(A_2, B_2, label='Feature_2')
#plt.scatter(A_3, B_3, label='Feature_3')
#plt.xlabel('Group A')
#plt.ylabel('Group B')
#plt.title('Scatter plot for Feature 1')
#plt.title('Scatter plot for Feature 2')
#plt.title('Scatter plot for Feature 3')
#plt.show()

