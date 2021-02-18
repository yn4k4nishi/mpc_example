# MPC demo

![](result.png)

## 依存関係
python3
- matplotlib
- numpy
- cvxpy

## モデル
$x$をロボットの座標$[x,y]^T$,$u$をロボットの速度$[v_x,v_y]^T$、tは制御とすると、
$$
x' = Ax + Bu \\
A = \left[ \begin{array}{cc}
    1 & 0 \\
    0 & 1 \\
\end{array} \right],
B = \left[ \begin{array}{c}
    t \\
    t \\
\end{array} \right] \\
$$
