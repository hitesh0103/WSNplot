import numpy as np
import matplotlib as plt
import ENERGY


dk1=[]
dk2=[]
dk3=[]
dE1=[]
dE2=[]
dE3=[]
dA=[] 
k1 = 0
k2 = 0 
k3 = 0
alpha1=0.9
alpha2=0.9
alpha3=0.9

number_of_sensors = int(input("Enter the number of sensors:- "))
energy_of_ClusterHead = float(input("Enter the energy of cluster head:- "))
threshold_energy = float(input("Enter the threshold energy:- "))
number_of_sensors_subleach = number_of_sensors
number_of_sensors_svmleach = number_of_sensors 
energy_of_ClusterHead_svmleach = energy_of_ClusterHead
energy_of_ClusterHead_subleach = energy_of_ClusterHead

##lamb_param  and beta_param is the gain in the energy  of  that we get by optimally choosing these paramters we have chosen
## these parameters by using deep learning techniques as to how much difference in the enrgy would come using different models.
lamb_param = float(input("Enter the lamb_param:- "))
beta_param = float(input("Enter beta_param:- "))

for r in range(1, 1999):
    energy_of_ClusterHead = energy_of_ClusterHead * alpha1
    for i in range(number_of_sensors):
        
        a0 = energy_of_ClusterHead*r
        a1 = number_of_sensors - a0
        if a1 != 0:
            a2 = energy_of_ClusterHead/a1
            Energy1 = a2
            dE1.append(Energy1)
            if dE1[i] > threshold_energy:
                k1 = number_of_sensors
            else:
                number_of_sensors = number_of_sensors - 1
    dk1.append(k1)

#print(dk1)


for r in range(1, 1999):
    energy_of_ClusterHead_subleach = energy_of_ClusterHead_subleach * alpha3
    for i in range(number_of_sensors_subleach):
        
        a0 = energy_of_ClusterHead_subleach*r
        a1 = number_of_sensors_subleach - a0
        if a1 != 0:
            a2 = energy_of_ClusterHead_subleach/a1
            a3=a2+beta_param
            Energy = a2
            dE3.append(Energy)
            if dE3[i] > threshold_energy:
                k3 = number_of_sensors_subleach
            else:
                number_of_sensors_subleach = number_of_sensors_subleach - 1
    dk3.append(k3)

#print(dk3)

ENERGY.EGY()


for r in range(1, 1999):
    energy_of_ClusterHead_svmleach = energy_of_ClusterHead_svmleach * alpha2
    for i in range(number_of_sensors_svmleach):
        
        a0 = energy_of_ClusterHead_svmleach*r
        a1 = number_of_sensors_svmleach - a0
        if a1 != 0:
            a2 = energy_of_ClusterHead_svmleach/a1
            a3 = a2 + lamb_param
            Energy = a3
            dE2.append(Energy)
            if dE2[i] > threshold_energy:
                k2 = number_of_sensors_svmleach
            else:
                number_of_sensors_svmleach = number_of_sensors_svmleach - 1
    dk2.append(k2)

#print(dk1)
