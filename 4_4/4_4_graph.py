from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

# データ
range_start = -5
range_end = 5
myu1 = -1.25
myu2 = 1.25
sigma = 1
sigma_4 = 4


# 確率密度関数
def pdf():
    # 横軸の値
    x = np.linspace(range_start, range_end, 1000)

    # 確率密度関数
    y1 = norm.pdf(x, myu1, sigma)
    y2 = norm.pdf(x, myu2, sigma_4)

    # 確率密度関数のグラフ
    plt.plot(x, y1, label="class1", color="green")
    plt.plot(x, y2, label="class2", color="purple")

    # ベイズ決定境界線
    plt.vlines(bayes_decision_line(myu1, myu2), min(y1), max(y1), color="black", linestyle="dashed")

    # グラフの表示
    plt.legend()
    plt.show()


# ヒストグラム
def hist():
    # 正規分布に従うランダムデータを 20 個生成
    hist1 = norm.rvs(loc=myu1, scale=sigma, size=20)
    hist2 = norm.rvs(loc=myu2, scale=sigma_4, size=20)

    # データのヒストグラム
    plt.hist(hist1, bins=16, color="green", range=(-4, 4))
    plt.hist(hist2, bins=16, color="purple", range=(-4, 4), hatch="//", fill=None, edgecolor="purple")

    # ベイズ決定境界線
    plt.vlines(bayes_decision_line(myu1, myu2), 0, 6, color="black", linestyle="dashed")

    # グラフの表示
    plt.legend()
    plt.show()


# ベイズ決定境界
def bayes_decision_line(m1, m2):
    return (m1 + m2) / 2


pdf()
# hist()
