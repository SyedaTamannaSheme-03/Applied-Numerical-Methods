import numpy as np
import matplotlib.pyplot as plt

#Step 1:Array Input and Declare Y (Where, Y is already Given and Y=F(X)

X = np.array([2.00, 4.25, 5.25, 7.81, 9.20, 10.60])
Y = np.array([7.2, 7.1, 6.0, 5.0, 3.5, 5.0])

#Step 2:Storing Values in an Array and Implementing Newton’s Divided Difference Interpolation

store = np.zeros((6, 6))
s = 5
i = 0
while s >= 0:
    store[s, 0] = Y[i]
    s = s - 1
    i = i + 1
print("The Storing Array is:")
print(store)
print("\n")

#step 3:Generating B(B is the last Row Value)

def divideddiff(store, X):
    n = 0
    for i in range(1, 6):
        j = 5
        while j >= i:
            store[j, i] = float((store[j-1, i-1] - store[j, i-1])/(X[6 + n - j] - X[5 - j]))
            j = j - 1
        n = n+1

    return store
divideddiff(store, X)
print(" Implementing Newton’s Divided Difference Interpolation :")
print(store)
print("\n")

#Step 4:Slicing Last Row

coefficient = store[5, :]

print("Values of B ")
print(coefficient)
print("\n")

#step_5:Generating Polynomial

final_pol = np.polynomial.Polynomial([0.]) #Our Target Polynomial
n = coefficient.shape[0]
print("Coefficient Size:", n) #Get Number of Co-Efficients
print("\n")

for i in range(n):
    p = np.polynomial.Polynomial([1.]) #Create a Dummy Polynomial
    for j in range(i):
        # Each vector has Degree of i
        # Their terms are dependant on 'x' values
        p_temp = np.polynomial.Polynomial([-X[j], 1.]) # (x - x_j)
        p = np.polymul(p, p_temp)  #Multiply Dummy with Expression
    p = p * coefficient[i]  #Apply Co-efficient
    final_pol = np.polyadd(final_pol, p)   #Add Target polynomial

p = np.flip(final_pol[0].coef, axis=0)
print("Final Co-efficient: ")
print(p)
print("\n")

#step 6: Generating Polynomial

x_axis = np.linspace(0, 10, num=5000)
y_axis = np.polyval(p, x_axis)

plt.plot(x_axis, y_axis)
plt.show()
print("\n")
