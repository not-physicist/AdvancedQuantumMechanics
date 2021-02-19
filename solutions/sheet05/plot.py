import numpy as np
import matplotlib.pyplot as plt

def delta(kR, phi):
    return(np.arctan(-np.sin(kR)**2/(kR/phi + np.sin(2*kR)/2)))

def sigma(kR, phi):
    return(4*np.pi/kR**2*np.sin(delta(kR, phi))**2)

phi_list = np.array([1,10,100])
legend=["$\Phi=1$","$\Phi=10$","$\Phi=100$"]
kR = np.linspace(0,10,1000)
plt.figure(num=11)
for i in [0,1,2]:
    plt.plot(kR, delta(kR,phi_list[i]),label=legend[i])
plt.xlabel("kR")
plt.ylabel("$\delta_0$")
plt.legend()
plt.savefig("c1.png", bbox_inches="tight")

plt.figure(num=2)
for i in [0,1,2]:
    plt.plot(kR, sigma(kR,phi_list[i]),label=legend[i])
plt.xlabel("kR")
plt.ylabel("$\sigma / R^2$")
plt.legend()
plt.savefig("c2.png", bbox_inches="tight")
