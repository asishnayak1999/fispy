import matplotlib.pyplot as plt

sem = [1,2,3]

m1= [34,90,65]
m2= [54,76,43]

plt.plot(sem,m1,label="RAJ")
plt.plot(sem,m2,label="Asish")

plt.legend()

plt.xlabel('sem..')
plt.ylabel('Marks.')
plt.show()