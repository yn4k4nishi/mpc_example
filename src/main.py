#! /usr/bin/python3
# -*- coding: utf-8 -*-

import cvxpy as cp
import matplotlib.pyplot as plt
import numpy as np

# パラメータ
n = 2 # 状態 と 入力 の次元
T = 5 # horizon : 何周期、予測するか
dt = 0.01 # 制御周期[s]

u_min = -np.inf # 入力の最小値
u_max =  np.inf # 入力の最大値

print("horizon : " + str(T))
print("制御周期 : " + str(dt) + "[s]")
print()

# モデルのパラメータ
A = np.eye(n) # 2x2の単位行列
B = dt * np.eye(n)
print("A = \n",A)
print("B = \n",B)
print()

# 評価関数の重み
Q = np.eye(n)
R = 0.00001 * np.eye(n) 
print("Q = \n",Q)
print("R = \n",R)
print()

# 初期値
x_0 = np.array([0,0])

# 変数
x = cp.Variable((n, T))  # 状態
u = cp.Variable((n, T))  # 入力

# 経路情報
x_ref = np.matrix([
    [0  ,0.5,1.8,2.7,4.0],
    [0  ,2.2,3.0,1.5,2.0]
])

cost = 0
constraints = [x[:,0] == x_0]
for t in range(T-1):
    # 評価関数
    cost += cp.quad_form(x[:,t+1] - np.squeeze(np.asarray(x_ref[:,t+1])), Q)    
    cost += cp.quad_form(u[:,t+1] - u[:,t], R)

    # 制約
    constraints += [ x[:,t+1] == A @ x[:,t] + B @ u[:,t] ]
    constraints += [ u_min <= u[:,t], u[:,t] <= u_max ]

prob = cp.Problem(cp.Minimize(cost), constraints)
prob.solve(verbose=True)


# plot
plt.figure(figsize=(16.0,8.0))
plt.subplot(1,2,1)
plt.plot(np.squeeze(np.asarray(x_ref[0])),np.squeeze(np.asarray(x_ref[1]))        , 'o-', label='ideal')
plt.plot(np.squeeze(np.asarray(x[0,:].value)),np.squeeze(np.asarray(x[1,:].value)), 'o-', label='predict')
plt.axis('equal')
plt.legend()
plt.title("robot 2D state")

plt.subplot(1,2,2)
time = np.linspace(0,T*dt, T)
plt.plot(time, u[0,:].value, 'o-', label='$v_x$ [m/s]')
plt.plot(time, u[1,:].value, 'o-', label='$v_y$ [m/s]')
plt.legend()
plt.xlabel("time [s]")
plt.title("input")

plt.show()
