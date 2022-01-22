from pulp import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import drawCube as dc

# MIP mathematical model that solves the grasp problem
# declare some variables
# i indices for the cargo
# k sub indices for the cargo
# j indices for the trucks
# r(i) data for the radius of the cargo
# c(j) data for the capacity of the truck
# h(i) data for the height of the cargo
# W(j) data for the width of the truck
# L(j) data for the length of the truck
# H(j) data for the height of the truck
# m(i) data for the mass of the cargo
# p(i,j) variable for the cargo i is loaded on truck j
# u(j) variable for the truck j is used
# x(i), y(i), z(i) variables for the coordinates of the cargo i
# xp(i,k) 1 if item i is placed to the left of item k in the same bin, 0 otherwise. 
# yp(i,k) 1 if item i is placed above item k in the same bin, 0 otherwise.
# zp(i,k) 1 if item i is placed in front of item k in the same bin, 0 otherwise.
# xn(i,k) 1 if item i is placed to the right of item k in the same bin, 0 otherwise.
# yn(i,k) 1 if item i is placed below item k in the same bin, 0 otherwise.
# zn(i,k) 1 if item i is placed behind item k in the same bin, 0 otherwise.
# objective is to minimize the number of used trucks
# data = {}
# data["i"] = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
# data["k"] = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
# data["j"] = [0,1]
# data["l"] = [0,1,2,3]
# data["pRadius"] = [100,100,100,70,70,100,70,70,100,70,70,100,70,70,100,70,70,100,70,70]
# data["pHeight"] = [80,80,80,60,60,80,60,60,80,60,60,80,60,60,80,60,60,80,60,60]
# data["vLength"] = [1000,1000]
# data["vHeight"] = [250,250]
# data["vWide"] = [400,400]
# data["vMass"] = [40000,40000]
# data["vType"] = ["Container", "Truck"]
# data["m"] = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]



data = {}
data["i"] = [0,1,2,3,4,5,6]
data["k"] = [0,1,2,3,4,5,6]
data["j"] = [0,1]
data["l"] = [0,1,2,3]
data["pRadius"] = [100,100,100,100,100,100,100]
data["pHeight"] = [100,100,100,100,100,100,100]
data["vLength"] = [400,250]
data["vHeight"] = [300,250]
data["vWide"] = [250,250]
data["vMass"] = [40000,40000]
data["m"] = [100,100,100,100,100,100,100]

# variables
p = LpVariable.dicts("p", (data["i"], data["j"]), 0, 1, LpBinary)
u = LpVariable.dicts("u", data["j"], 0, 1, LpBinary)
x = LpVariable.dicts("x", data["i"], 0, None, LpContinuous)
y = LpVariable.dicts("y", data["i"], 0, None, LpContinuous)
z = LpVariable.dicts("z", data["i"], 0, None, LpContinuous)
# 1 if the length of item i is parallel to X-axis, 0 otherwise. 
lx = LpVariable.dicts("lx", data["i"], 0, 1, LpBinary)
# 1 if the length of item i is parallel to Y-axis, 0 otherwise.
ly = LpVariable.dicts("ly", data["i"], 0, 1, LpBinary)
# 1 if the width of item i is parallel to X-axis, 0 otherwise.
wx = LpVariable.dicts("wx", data["i"], 0, 1, LpBinary)
# 1 if the width of item i is parallel to Y-axis, 0 otherwise.
wy = LpVariable.dicts("wy", data["i"], 0, 1, LpBinary)

gx = LpVariable.dicts("gx", data["j"], 0, None, LpContinuous)
gy = LpVariable.dicts("gy", data["j"], 0, None, LpContinuous)
gz = LpVariable.dicts("gz", data["j"], 0, None, LpContinuous)

absL = LpVariable.dicts("absL", data["j"], 0, None, LpContinuous)
absW = LpVariable.dicts("absW", data["j"], 0, None, LpContinuous)
absH = LpVariable.dicts("absH", data["j"], 0, None, LpContinuous)

exp = LpVariable.dicts("exp", data["j"], 0, None, LpContinuous)
exn = LpVariable.dicts("exn", data["j"], 0, None, LpContinuous)
eyp = LpVariable.dicts("eyp", data["j"], 0, None, LpContinuous)
eyn = LpVariable.dicts("eyn", data["j"], 0, None, LpContinuous)
ezp = LpVariable.dicts("ezp", data["j"], 0, None, LpContinuous)
ezn = LpVariable.dicts("ezn", data["j"], 0, None, LpContinuous)

d = LpVariable.dicts("d", (data["i"], data["j"]), 0, None, LpContinuous)
e = LpVariable.dicts("e", (data["i"], data["j"]), 0, None, LpContinuous)

bBalance = LpVariable.dicts("b", (data["i"], data["j"]), 0, 1, LpBinary)
cBalance = LpVariable.dicts("c", (data["i"], data["j"]), 0, 1, LpBinary)
tBalance = LpVariable.dicts("t", (data["i"], data["j"]), 0, None, LpContinuous)
vBalance = LpVariable.dicts("v", (data["i"], data["j"]), 0, None, LpContinuous)
rBalance = LpVariable.dicts("r", (data["i"], data["j"]), 0, None, LpContinuous)
sBalance = LpVariable.dicts("s", (data["i"], data["j"]), 0, None, LpContinuous)
mBalance = LpVariable.dicts("m", (data["i"], data["j"]), 0, None, LpContinuous)
nBalance = LpVariable.dicts("n", (data["i"], data["j"]), 0, None, LpContinuous)


xp = LpVariable.dicts("xp", (data["i"], data["k"]), 0, 1, LpBinary)
yp = LpVariable.dicts("yp", (data["i"], data["k"]), 0, 1, LpBinary)
zp = LpVariable.dicts("zp", (data["i"], data["k"]), 0, 1, LpBinary)
xn = LpVariable.dicts("xn", (data["i"], data["k"]), 0, 1, LpBinary)
yn = LpVariable.dicts("yn", (data["i"], data["k"]), 0, 1, LpBinary)
zn = LpVariable.dicts("zn", (data["i"], data["k"]), 0, 1, LpBinary)

o = LpVariable.dicts("o", (data["i"], data["k"]), 0, 1, LpBinary)
beta = LpVariable.dicts("beta", (data["i"], data["k"],data["l"]), 0, 1, LpBinary)
ground = LpVariable.dicts("ground", data["i"], 0, 1, LpBinary)
absv = LpVariable.dicts("absv", (data["i"],data["k"]), 0, None, LpContinuous)
mik = LpVariable.dicts("mik", (data["i"],data["k"]), 0, 1, LpBinary)
suitH = LpVariable.dicts("suitH", (data["i"],data["k"]), 0, 1, LpBinary)
s = LpVariable.dicts("s", (data["i"],data["k"]), 0, 1, LpBinary)
n1 = LpVariable.dicts("n1", (data["i"],data["k"]), 0, 1, LpBinary)
n2 = LpVariable.dicts("n2", (data["i"],data["k"]), 0, 1, LpBinary)
n3 = LpVariable.dicts("n3", (data["i"],data["k"]), 0, 1, LpBinary)
n4 = LpVariable.dicts("n4", (data["i"],data["k"]), 0, 1, LpBinary)

q = LpVariable.dicts("q",data["i"], 0, 1, LpBinary)


# objective
prob = LpProblem("grasp", LpMinimize)
prob += lpSum([((u[j] * data["vHeight"][j] * data["vLength"][j] * data["vWide"][j]) - (p[i][j] * data["pRadius"][i] * data["pRadius"][i] * data["pHeight"][i])) for j in data ["j"] for i in data["i"]])
# prob += lpSum([(exp[j] + exn[j] + eyp[j] + eyn[j] + ezp[j] + ezn[j]) for j in data["j"]])


# constraints
for i in data["i"]:
    for j in data["j"]:
        prob += p[i][j] <= u[j]
for i in data["i"]:
    prob += lpSum([p[i][j] for j in data["j"]]) == 1
for i in data["i"]:
    for j in data["j"]:
        prob += x[i] + (lx[i] * data["pRadius"][i]) + (wx[i] * data["pRadius"][i]) <= data["vLength"][j] * u[j] + (1 - p[i][j]) * 100000
        prob += y[i] + (ly[i] * data["pRadius"][i]) + (wy[i] * data["pRadius"][i]) <= data["vWide"][j] * u[j] + (1 - p[i][j]) * 100000
        prob += z[i] + data["pHeight"][i] <= data["vHeight"][j] * u[j] + (1 - p[i][j]) * 100000
for i in data["i"]:
    for k in range(i):
        prob += x[i] + (lx[i] * data["pRadius"][i]) + (wx[i] * data["pRadius"][i]) <= x[k] + ((1-xp[i][k]) * 100000)
        prob += y[i] + (ly[i] * data["pRadius"][i]) + (wy[i] * data["pRadius"][i]) <= y[k] + ((1-yp[i][k]) * 100000)
        prob += z[i] + data["pHeight"][i] <= z[k] + ((1-zp[i][k]) * 100000)
for i in data["i"]:
    for k in range(i):
        prob += x[k] + (lx[k] * data["pRadius"][k]) + (wx[k] * data["pRadius"][k]) <= x[i] + (1-xn[i][k]) * 100000 
        prob += y[k] + (ly[k] * data["pRadius"][k]) + (wy[k] * data["pRadius"][k]) <= y[i] + (1-yn[i][k]) * 100000 
        prob += z[k] + data["pHeight"][k] <= z[i] + (1-zn[i][k]) * 100000 
for i in data["i"]:
    for k in range(i):
        for j in data["j"]:
            prob += xp[i][k] + xn[i][k] + yp[i][k] + yn[i][k] + zp[i][k] + zn[i][k] >= p[i][j] + p[k][j] - 1

for i in data["i"]:
    for k in range(i):
        prob += x[k] >= x[i]
        prob += x[k] <= x[i] + data["pRadius"][i] + (1-zp[i][k]) * 100000

        prob += y[k] >= y[i]
        prob += y[k] <= y[i] + data["pRadius"][i] + (1-zp[i][k]) * 100000

        prob += x[k] + data["pRadius"][k] >= x[i]
        prob += x[k] + data["pRadius"][k] <= x[i] + data["pRadius"][i] + (1-zp[i][k]) * 100000

        prob += y[k] + data["pRadius"][k] >= y[i] 
        prob += y[k] + data["pRadius"][k] <= y[i] + data["pRadius"][i] + (1-zp[i][k]) * 100000

for i in data["i"]:
    prob += lpSum(zn[i][k] for k in range(i)) <= q[i]
    prob += lpSum(zn[i][k] for k in range(i)) >= q[i]

    prob += z[i] <= (1 - q[i]) * 100000

# is vehicle container or truck (if else)

# for k in range(i):
#     prob += lpSum(zp[i][k] for i in data["i"]) <= lpSum((1 - zn[k][i]) for i in data["i"])
#     prob += lpSum(zp[i][k] for i in data["i"]) >= lpSum((1 - zn[k][i]) for i in data["i"])






for i in data["i"]:
    prob += lx[i] + ly[i] == 1
    prob += lx[i] + wx[i] == 1
    prob += wx[i] + wy[i] == 1
    prob += ly[i] + wy[i] == 1

for j in data["j"]:
    prob += gx[j] - (data["vLength"][j]/2) <= absL[j] 
    prob += (data["vLength"][j]/2) - gx[j] <= absL[j]
    prob += gy[j] - (data["vWide"][j]/2) <= absW[j]
    prob += (data["vWide"][j]/2) - gy[j] <= absW[j]
    prob += gz[j] <= absH[j]
    prob += (gz[j] * (-1)) <= absH[j]

    prob += absL[j] == exp[j] - exn[j]
    prob += absW[j] == eyp[j] - eyn[j]
    prob += absH[j] == ezp[j] - ezn[j]

for i in data["i"]:
    for j in data["j"]:
        prob += d[i][j] >= gx[j] - (1 - p[i][j]) * 100000
        prob += d[i][j] <= p[i][j] * 100000
        prob += d[i][j] <= gx[j]

        prob += e[i][j] >= x[i] - (1 - p[i][j]) * 100000
        prob += e[i][j] <= p[i][j] * 100000
        prob += e[i][j] <= x[i]

        prob += bBalance[i][j] <= lx[i]
        prob += bBalance[i][j] <= p[i][j]
        prob += bBalance[i][j] >= lx[i] + p[i][j] - 1

        prob += cBalance[i][j] <= wx[i]
        prob += cBalance[i][j] <= p[i][j]
        prob += cBalance[i][j] >= wx[i] + p[i][j] - 1
for j in data["j"]:
    prob += lpSum((data["m"][i] * d[i][j]) for i in data["i"]) - lpSum((data["m"][i] * e[i][j]) for i in data["i"]) - lpSum((data["m"][i] * bBalance[i][j] * data["pRadius"][i] / 2) for i in data["i"]) - lpSum((data["m"][i] * cBalance[i][j] * data["pRadius"][i] / 2) for i in data["i"]) == 0

for i in data["i"]:
    for j in data["j"]:
        prob += tBalance[i][j] >= gy[j] - (1 - p[i][j]) * 100000
        prob += tBalance[i][j] <= p[i][j] * 100000
        prob += tBalance[i][j] <= gy[j]

        prob += vBalance[i][j] >= y[i] - (1 - p[i][j]) * 100000
        prob += vBalance[i][j] <= p[i][j] * 100000
        prob += vBalance[i][j] <= y[i]

        prob += rBalance[i][j] <= ly[i]
        prob += rBalance[i][j] <= p[i][j]
        prob += rBalance[i][j] >= ly[i] + p[i][j] - 1

        prob += sBalance[i][j] <= wy[i]
        prob += sBalance[i][j] <= p[i][j]
        prob += sBalance[i][j] >= wy[i] + p[i][j] - 1
for j in data["j"]:
    prob += lpSum((data["m"][i] * tBalance[i][j]) for i in data["i"]) - lpSum((data["m"][i] * vBalance[i][j]) for i in data["i"]) - lpSum((data["m"][i] * rBalance[i][j] * data["pRadius"][i] * 0.5) for i in data["i"]) - lpSum((data["m"][i] * sBalance[i][j] * data["pRadius"][i] * 0.5) for i in data["i"]) == 0

for i in data["i"]:
    for j in data["j"]:
        prob += mBalance[i][j] >= gz[j] - (1 - p[i][j]) * 100000
        prob += mBalance[i][j] <= p[i][j] * 100000
        prob += mBalance[i][j] <= gz[j]

        prob += nBalance[i][j] >= z[i] - (1 - p[i][j]) * 100000
        prob += nBalance[i][j] <= p[i][j] * 100000
        prob += nBalance[i][j] <= z[i]

for j in data["j"]:
    prob += lpSum((data["m"][i] * mBalance[i][j]) for i in data["i"]) - lpSum((data["m"][i] * nBalance[i][j]) for i in data["i"]) - lpSum((data["m"][i] * p[i][j] * data["pHeight"][i] * 0.5) for i in data["i"]) - lpSum((data["m"][i] * sBalance[i][j] * data["pHeight"][i] * 0.5) for i in data["i"]) == 0


# weight capacity constraint
for j in data["j"]:
    prob += lpSum([data["m"][i] * p[i][j] for i in data["i"]]) <= data["vMass"][j]
# solve the model
prob.solve()
# print the solution
print("Status:", LpStatus[prob.status])
for v in prob.variables():
    if(v.name[0:1] == "x"):
        print(v.name, "=", v.varValue)

# Draw 3D cube using Axes3D module for solution
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(1)
fig1 = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')
ay = fig1.add_subplot(111, projection='3d')
for i in data["i"]:
    if(p[i][0].varValue == 1):
        point = [int(x[i].varValue), int(y[i].varValue), int(z[i].varValue)]        
        size = [data["pRadius"][i], data["pRadius"][i], data["pHeight"][i]]        
        dc.drawCube(point, size, ax,"r")
        vPoint = [0,0,0]
        vSize = [data["vLength"][0],data["vWide"][0], data["vHeight"][0]]
        dc.drawCube(vPoint, vSize, ax,"g")
    elif(p[i][1].varValue == 1):
        point = [int(x[i].varValue), int(y[i].varValue), int(z[i].varValue)]
        size = [data["pRadius"][i], data["pRadius"][i], data["pHeight"][i]]
        dc.drawCube(point, size, ay,"g")
        vPoint = [0,0,0]
        vSize = [data["vLength"][1],data["vWide"][1], data["vHeight"][1]]
        dc.drawCube(vPoint, vSize, ay,"b")
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ay.set_xlabel('X Label')
ay.set_ylabel('Y Label')
ay.set_zlabel('Z Label')
# show ax and ay in th
plt.show()