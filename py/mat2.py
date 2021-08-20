import matplotlib.pyplot as plt

states = ['Delhi','AP','MP']

pop = [1.2,4.9,3.8]
plt.plot(states,pop)
plt.title('pop in crores')
plt.xlabel('States')
plt.ylabel('Population')
plt.show()