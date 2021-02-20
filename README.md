# MPC example

![](result.png)

## 依存関係
python3
- matplotlib
- numpy
- cvxpy
    - version 1.1.10

#### 依存関係のインストール
`pip3 install -r requirements.txt`

## 実行
### ローカル

- `python3 src/main.py` 

経路をランダムにする場合は`-r`
プロットを"result.png"で保存する場合は`-s`をつける

ex ) `python3 src/main.py -r -s`

### Github Action
[issue#1](https://github.com/yn4k4nishi/mpc_example/issues/1)で"/run"とコメントすると数分後に結果の画像がコメントされる
