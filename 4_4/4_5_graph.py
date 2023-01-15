import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# 関数に投入するデータを作成
x = y = np.arange(-10, 10, 0.1)
X, Y = np.meshgrid(x, y)

# 2変数の平均値を指定
myu = np.array([-1.25, 1.25])

# 2変数の分散共分散行列を指定
# 相関係数 0
sigma1 = np.array([[10, 0], [0, 10]])
# 相関係数 0.7
sigma2 = np.array([[10, 7], [7, 10]])


# 二次元正規分布の確率密度を返す関数
def gaussian(z, sigma):
    # 分散共分散行列の行列式
    det = np.linalg.det(sigma)
    print(det)
    # 分散共分散行列の逆行列
    inv = np.linalg.inv(sigma)
    n = z.ndim
    print(inv)
    return np.exp(-np.diag((z - myu) @ inv @ (z - myu).T) / 2.0) / (np.sqrt((2 * np.pi) ** n * det))


def plot(sigma):
    z = np.c_[X.ravel(), Y.ravel()]
    gaussian_z = gaussian(z, sigma)
    shape = X.shape
    gaussian_z = gaussian_z.reshape(shape)

    # 二次元正規分布をplot
    fig = plt.figure(figsize=(15, 15))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(X, Y, gaussian_z, rstride=1, cstride=1, cmap=cm.coolwarm)
    plt.show()


plot(sigma1)
plot(sigma2)
