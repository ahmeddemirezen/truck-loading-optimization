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
        for j in _data["j"]:
            # product i position constraints
            prob += x[i] + (lx[i] * _data["pRadius"][i]) + (wx[i] * _data["pRadius"][i]) <= _data["vLength"][j] * u[j] + (1 - p[i][j]) * 100000
            prob += y[i] + (ly[i] * _data["pRadius"][i]) + (wy[i] * _data["pRadius"][i]) <= _data["vWide"][j] * u[j] + (1 - p[i][j]) * 100000
            prob += z[i] + _data["pHeight"][i] <= _data["vHeight"][j] * u[j] + (1 - p[i][j]) * 100000
    
    for i in _data["i"]:
        for k in range(i):
            # overlaping constraints
            prob += x[i] + (lx[i] * _data["pRadius"][i]) + (wx[i] * _data["pRadius"][i]) <= x[k] + ((1-xp[i][k]) * 100000)
            prob += y[i] + (ly[i] * _data["pRadius"][i]) + (wy[i] * _data["pRadius"][i]) <= y[k] + ((1-yp[i][k]) * 100000)
            prob += z[i] + _data["pHeight"][i] <= z[k] + ((1-zp[i][k]) * 100000)
    for i in _data["i"]:
        for k in range(i):
            # overlaping constraints
            prob += x[k] + (lx[k] * _data["pRadius"][k]) + (wx[k] * _data["pRadius"][k]) <= x[i] + (1-xn[i][k]) * 100000 
            prob += y[k] + (ly[k] * _data["pRadius"][k]) + (wy[k] * _data["pRadius"][k]) <= y[i] + (1-yn[i][k]) * 100000 
            prob += z[k] + _data["pHeight"][k] <= z[i] + (1-zn[i][k]) * 100000

    for i in _data["i"]:
        for k in range(i):
            for j in _data["j"]:
                # relational position of package i and k only have one position.
                prob += xp[i][k] + xn[i][k] + yp[i][k] + yn[i][k] + zp[i][k] + zn[i][k] >= p[i][j] + p[k][j] - 1

    for i in _data["i"]:
        for k in range(i):
            # 3 vertices of package k should be on a package i if k is on i.
            prob += x[k] >= x[i]
            prob += x[k] <= x[i] + _data["pRadius"][i] + (1-zp[i][k]) * 100000

            prob += y[k] >= y[i]
            prob += y[k] <= y[i] + _data["pRadius"][i] + (1-zp[i][k]) * 100000

            prob += x[k] + _data["pRadius"][k] >= x[i]
            prob += x[k] + _data["pRadius"][k] <= x[i] + _data["pRadius"][i] + (1-zp[i][k]) * 100000

            prob += y[k] + _data["pRadius"][k] >= y[i] 
            prob += y[k] + _data["pRadius"][k] <= y[i] + _data["pRadius"][i] + (1-zp[i][k]) * 100000

    for i in _data["i"]:
        # every package k should be on an another package i if its not on surface.
        prob += lpSum(zn[i][k] for k in range(i)) <= q[i]
        prob += lpSum(zn[i][k] for k in range(i)) >= q[i]

        prob += z[i] <= (1 - q[i]) * 100000

    for i in _data["i"]:
        # direction constraints
        prob += lx[i] + ly[i] == 1
        prob += lx[i] + wx[i] == 1
        prob += wx[i] + wy[i] == 1
        prob += ly[i] + wy[i] == 1    

    for j in _data["j"]:
        # balance constraints
        prob += gx[j] - (_data["vLength"][j]/2) <= absL[j] 
        prob += (_data["vLength"][j]/2) - gx[j] <= absL[j]
        prob += gy[j] - (_data["vWide"][j]/2) <= absW[j]
        prob += (_data["vWide"][j]/2) - gy[j] <= absW[j]
        prob += gz[j] <= absH[j]
        prob += (gz[j] * (-1)) <= absH[j]

        prob += absL[j] == exp[j] - exn[j]
        prob += absW[j] == eyp[j] - eyn[j]
        prob += absH[j] == ezp[j] - ezn[j]
    
    for i in _data["i"]:
        for j in _data["j"]:
            # balance constraints
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

    for j in _data["j"]:
        # balance constraints
        prob += lpSum((_data["pMass"][i] * d[i][j]) for i in _data["i"]) - lpSum((_data["pMass"][i] * e[i][j]) for i in _data["i"]) - lpSum((_data["pMass"][i] * bBalance[i][j] * _data["pRadius"][i] / 2) for i in _data["i"]) - lpSum((_data["pMass"][i] * cBalance[i][j] * _data["pRadius"][i] / 2) for i in _data["i"]) == 0
    
    for i in _data["i"]:
        for j in _data["j"]:
            # balance constraints
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
    
    for j in _data["j"]:
        # balance constraints
        prob += lpSum((_data["pMass"][i] * tBalance[i][j]) for i in _data["i"]) - lpSum((_data["pMass"][i] * vBalance[i][j]) for i in _data["i"]) - lpSum((_data["pMass"][i] * rBalance[i][j] * _data["pRadius"][i] * 0.5) for i in _data["i"]) - lpSum((_data["pMass"][i] * sBalance[i][j] * _data["pRadius"][i] * 0.5) for i in _data["i"]) == 0
    
    for i in _data["i"]:
        for j in _data["j"]:
            # balance constraints
            prob += mBalance[i][j] >= gz[j] - (1 - p[i][j]) * 100000
            prob += mBalance[i][j] <= p[i][j] * 100000
            prob += mBalance[i][j] <= gz[j]

            prob += nBalance[i][j] >= z[i] - (1 - p[i][j]) * 100000
            prob += nBalance[i][j] <= p[i][j] * 100000
            prob += nBalance[i][j] <= z[i]
    
    for j in _data["j"]:
        # balance constraints
        prob += lpSum((_data["pMass"][i] * mBalance[i][j]) for i in _data["i"]) - lpSum((_data["pMass"][i] * nBalance[i][j]) for i in _data["i"]) - lpSum((_data["pMass"][i] * p[i][j] * _data["pHeight"][i] * 0.5) for i in _data["i"]) - lpSum((_data["pMass"][i] * sBalance[i][j] * _data["pHeight"][i] * 0.5) for i in _data["i"]) == 0
    
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

data["vLength"] = [4500]
data["vHeight"] = [230]
data["vWide"] = [2000]
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

data2["vLength"] = [400,250]
data2["vHeight"] = [300,250]
data2["vWide"] = [250,250]
data2["vMass"] = [40000,40000]
#endregion

CreateModel(data2)