from pulp import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import drawCube as dc
import random

def CreateModel(_data):
    # Variables
    # p: 1 if the package is in the vehicle j, 0 otherwise
    p = LpVariable.dicts("p", (_data["i"], _data["j"]), 0, 1, LpBinary)
    # u: 1 if the vehicle j used, 0 otherwise
    u = LpVariable.dicts("u", _data["j"], 0, 1, LpBinary)

    # x: the x position of the package i.
    x = LpVariable.dicts("x", _data["i"], 0, None, LpContinuous)
    # y: the y position of the package i.
    y = LpVariable.dicts("y", _data["i"], 0, None, LpContinuous)
    # z: the z position of the package i.
    z = LpVariable.dicts("z", _data["i"], 0, None, LpContinuous)

    #
    x_ = LpVariable.dicts("x_", _data["i"], 0, None, LpContinuous)
    y_ = LpVariable.dicts("y_", _data["i"], 0, None, LpContinuous)
    z_ = LpVariable.dicts("z_", _data["i"], 0, None, LpContinuous)

    absX = LpVariable.dicts("absX", (_data["i"], _data["k"]), 0, None, LpContinuous)
    absY = LpVariable.dicts("absY", (_data["i"], _data["k"]), 0, None, LpContinuous)
    absZ = LpVariable.dicts("absZ", (_data["i"], _data["k"]), 0, None, LpContinuous)
    absZtoGround = LpVariable.dicts("absZtoGround", _data["i"], 0, None, LpContinuous)
    absZtoZ_ = LpVariable.dicts("absZtoZ_", _data["i"], 0, None, LpContinuous)
    z_Top = LpVariable.dicts("z_Top", _data["i"], 0, 1, LpBinary)

    # 1 if the length of item i is parallel to X-axis, 0 otherwise. 
    lx = LpVariable.dicts("lx", _data["i"], 0, 1, LpBinary)
    # 1 if the length of item i is parallel to Y-axis, 0 otherwise.
    ly = LpVariable.dicts("ly", _data["i"], 0, 1, LpBinary)
    # 1 if the width of item i is parallel to X-axis, 0 otherwise.
    wx = LpVariable.dicts("wx", _data["i"], 0, 1, LpBinary)
    # 1 if the width of item i is parallel to Y-axis, 0 otherwise.
    wy = LpVariable.dicts("wy", _data["i"], 0, 1, LpBinary)

    # gx: continuous variables denoting barycenter of bin j on the x-, y- and z- axes respectively 
    gx = LpVariable.dicts("gx", _data["j"], 0, None, LpContinuous)
    gy = LpVariable.dicts("gy", _data["j"], 0, None, LpContinuous)
    gz = LpVariable.dicts("gz", _data["j"], 0, None, LpContinuous)

    # absL, absW, absH: absolute length, width and height of bin j
    absL = LpVariable.dicts("absL", _data["j"], 0, None, LpContinuous)
    absW = LpVariable.dicts("absW", _data["j"], 0, None, LpContinuous)
    absH = LpVariable.dicts("absH", _data["j"], 0, None, LpContinuous)

    # exp, exn, eyp, eyn, ezp, ezn: the package k position on the x+, x-, y+, y-, z+ and z- axes respectively
    exp = LpVariable.dicts("exp", _data["j"], 0, None, LpContinuous)
    exn = LpVariable.dicts("exn", _data["j"], 0, None, LpContinuous)
    eyp = LpVariable.dicts("eyp", _data["j"], 0, None, LpContinuous)
    eyn = LpVariable.dicts("eyn", _data["j"], 0, None, LpContinuous)
    ezp = LpVariable.dicts("ezp", _data["j"], 0, None, LpContinuous)
    ezn = LpVariable.dicts("ezn", _data["j"], 0, None, LpContinuous)

    # d[i][j] = p[i][j] * gx[j] 
    d = LpVariable.dicts("d", (_data["i"], _data["j"]), 0, None, LpContinuous)
    # e[i][j] = p[i][j] * x[i]
    e = LpVariable.dicts("e", (_data["i"], _data["j"]), 0, None, LpContinuous)

    # bBalance[i][j] = p[i][j] * lx[i]
    bBalance = LpVariable.dicts("b", (_data["i"], _data["j"]), 0, 1, LpBinary)
    # cBalance[i][j] = p[i][j] * wx[i]
    cBalance = LpVariable.dicts("c", (_data["i"], _data["j"]), 0, 1, LpBinary)
    # tBalance[i][j] = p[i][j] * gy[j]
    tBalance = LpVariable.dicts("t", (_data["i"], _data["j"]), 0, None, LpContinuous)
    # vBalance[i][j] = p[i][j] * y[i]
    vBalance = LpVariable.dicts("v", (_data["i"], _data["j"]), 0, None, LpContinuous)
    # rBalance[i][j] = p[i][j] * ly[i]
    rBalance = LpVariable.dicts("r", (_data["i"], _data["j"]), 0, None, LpContinuous)
    # sBalance[i][j] = p[i][j] * wy[i]
    sBalance = LpVariable.dicts("s", (_data["i"], _data["j"]), 0, None, LpContinuous)
    # mBalance[i][j] = p[i][j] * gz[j]
    mBalance = LpVariable.dicts("m", (_data["i"], _data["j"]), 0, None, LpContinuous)
    # nBalance[i][j] = p[i][j] * z[i]
    nBalance = LpVariable.dicts("n", (_data["i"], _data["j"]), 0, None, LpContinuous)

    # position binary variables for the info of the package i to k
    xp = LpVariable.dicts("xp", (_data["i"], _data["k"]), 0, 1, LpBinary)
    yp = LpVariable.dicts("yp", (_data["i"], _data["k"]), 0, 1, LpBinary)
    zp = LpVariable.dicts("zp", (_data["i"], _data["k"]), 0, 1, LpBinary)
    xn = LpVariable.dicts("xn", (_data["i"], _data["k"]), 0, 1, LpBinary)
    yn = LpVariable.dicts("yn", (_data["i"], _data["k"]), 0, 1, LpBinary)
    zn = LpVariable.dicts("zn", (_data["i"], _data["k"]), 0, 1, LpBinary)

    # 1 if there is any package bottom of the i.
    q = LpVariable.dicts("q",_data["i"], 0, 1, LpBinary)

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

    # Model Creation
    prob = LpProblem("grasp", LpMinimize)

    # Objective Function
    prob += lpSum([((u[j] * _data["vHeight"][j] * _data["vLength"][j] * _data["vWide"][j]) - (p[i][j] * _data["pRadius"][i] * _data["pRadius"][i] * _data["pHeight"][i])) for j in _data["j"] for i in _data["i"]])

    # Constraints

    for i in _data["i"]:
        for j in _data["j"]:
            # put the package i in the bin j when vehicle u j is used.
            prob += p[i][j] <= u[j]
    
    for i in _data["i"]:
        # every package i must be put in vehicle j.
        prob += lpSum([p[i][j] for j in _data["j"]]) == 1
    
    for i in _data["i"]:
        prob += x_[i] - x[i] == lx[i] * _data["pRadius"][i] + ly[i] * _data["pRadius"][i]
        prob += y_[i] - y[i] == wx[i] * _data["pRadius"][i] + wy[i] * _data["pRadius"][i]
        prob += z_[i] - z[i] == _data["pHeight"][i]

    for i in _data["i"]:
        for j in _data["j"]:
            # product i position constraints
            prob += x_[i] <= _data["vLength"][j] * u[j] + (1 - p[i][j]) * 100000
            prob += y_[i] <= _data["vWide"][j] * u[j] + (1 - p[i][j]) * 100000
            prob += z_[i] <= _data["vHeight"][j] * u[j] + (1 - p[i][j]) * 100000
    
    for i in _data["i"]:
        for k in range(i):
            # overlaping constraints
            prob += x_[i] - x[k] <= ((1-xp[i][k]) * 100000)
            prob += y_[i] - y[k] <= ((1-yp[i][k]) * 100000)
            prob += z_[i] - z[k] <= ((1-zp[i][k]) * 100000)
    for i in _data["i"]:
        for k in range(i):
            # overlaping constraints
            prob += x_[k] - x[i] <= ((1-xn[i][k]) * 100000)
            prob += y_[k] - y[i] <= ((1-yn[i][k]) * 100000)
            prob += z_[k] - z[i] <= ((1-zn[i][k]) * 100000)
    for i in _data["i"]:
        for k in range(i):
            prob += absX[i][k] >= x[i] - x[k]
            prob += absY[i][k] >= y[i] - y[k]
            prob += absZ[i][k] >= z[i] - z[k]

            prob += absX[i][k] >= x[k] - x_[i]
            prob += absY[i][k] >= y[k] - y_[i]
            prob += absZ[i][k] >= z[k] - z_[i]

            prob += absX[i][k] - x_[i] <= (1-xp[i][k]) * 100000
            prob += absY[i][k] - y_[i] <= (1-yp[i][k]) * 100000
            prob += absZ[i][k] - z_[i] <= (1-zp[i][k]) * 100000

            prob += absX[k][i] - x_[k] <= (1-xn[i][k]) * 100000
            prob += absY[k][i] - y_[k] <= (1-yn[i][k]) * 100000
            prob += absZ[k][i] - z_[k] <= (1-zn[i][k]) * 100000
    for i in _data["i"]:
        prob += z_[i] - z[i] >= 0 
        prob += z[i] - z_[i] <= 0
    for i in _data["i"]:
        for j in _data["j"]:
            prob += p[i][j] * _data["vHeight"][j] - z_[i] >= 100
    for i in _data["i"]:
        for k in range(i):
            for j in _data["j"]:
                # relational position of package i and k only have one position.
                prob += xp[i][k] + xn[i][k] + yp[i][k] + yn[i][k] + zp[i][k] + zn[i][k] >= p[i][j] + p[k][j] - 1

    for i in _data["i"]:
        for k in range(i):
            # 3 vertices of package k should be on a package i if k is on i.
            prob += x[k] >= x[i]
            prob += x[k] <= x_[i] + (1-zp[i][k]) * 100000

            prob += y[k] >= y[i]
            prob += y[k] <= y_[i] + (1-zp[i][k]) * 100000

            prob += x_[k] >= x[i]
            prob += x_[k] <= x_[i] + (1-zp[i][k]) * 100000

            prob += y_[k] >= y[i] 
            prob += y_[k] <= y_[i] + (1-zp[i][k]) * 100000

    
    # every package i should be placed on package k if i is on k.
    
    
    for i in _data["i"]:
        for k in range(i):
            prob += z[k] <= zp[i][k] * 100000 

        
    for i in _data["i"]:
        # direction constraints
        prob += lx[i] + ly[i] == 1
        prob += lx[i] + wx[i] == 1
        prob += wx[i] + wy[i] == 1
        prob += ly[i] + wy[i] == 1    
    
    for j in _data["j"]:
        # weight capacity constraints
        prob += lpSum([_data["pMass"][i] * p[i][j] for i in _data["i"]]) <= _data["vMass"][j]
    
    prob.solve()

    print("Status:", LpStatus[prob.status])
    for v in prob.variables():
        if(v.name[0:1] == "x"):
            print(v.name, "=", v.varValue)

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    figures = []
    plots = []
    for j in _data["j"]:
        if(u[j].varValue == 1):
            figures.append(plt.figure(j))
            plots.append(figures[-1].add_subplot(111, projection='3d'))
            for i in _data["i"]:
                point = [int(x[i].varValue), int(y[i].varValue), int(z[i].varValue)]        
                size = [_data["pRadius"][i], _data["pRadius"][i], _data["pHeight"][i]]  
                dc.drawCube(point,size,plots[-1],colors[i % len(colors)])
                plots[-1].text(point[0], point[1], point[2], str(i), fontsize=15)
                vPoint = [0,0,0]
                vSize = [_data["vLength"][0],_data["vWide"][0], _data["vHeight"][0]]
                dc.drawCube(vPoint, vSize, plots[-1],colors[j % len(colors)])
                plots[-1].set_xlabel("x axis")
                plots[-1].set_ylabel("y axis")
                plots[-1].set_zlabel("z axis")
                plt.title("Vehicle" + str(j))
    plt.show()




def SaveModel(_prob):
    _prob.writeMPS("test.mps")

#region Data1
data = {}
data["i"] = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
data["k"] = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
data["j"] = [0]
data["l"] = [0,1,2,3]

data["pRadius"] = [100,100,100,70,70,100,70,70,100,70,70,100,70,70,100,70,70,100,70,70]
data["pHeight"] = [80,80,80,60,60,80,60,60,80,60,60,80,60,60,80,60,60,80,60,60]
data["pMass"] = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]

data["vLength"] = [1500]
data["vHeight"] = [230]
data["vWide"] = [1000]
data["vMass"] = [40000]
#endregion
#region Data2
data2 = {}
data2["i"] = [0,1,2,3,4,5,6]
data2["k"] = [0,1,2,3,4,5,6]
data2["j"] = [0,1]
data2["l"] = [0,1,2,3]

data2["pRadius"] = [100,100,100,100,100,100,100]
data2["pHeight"] = [100,100,100,100,100,100,100]
data2["pMass"] = [100,100,100,100,100,100,100]
# x
data2["vLength"] = [400,250]
# z
data2["vHeight"] = [300,250]
# y
data2["vWide"] = [250,250]
data2["vMass"] = [40000,40000]
#endregion