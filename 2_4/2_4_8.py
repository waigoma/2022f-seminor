# csv 読み込み用
import pandas as pd
# データの可視化用
import seaborn as sns
import matplotlib.pyplot as plt
# ベンチ用
import time

# 表示上限を設定
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# (a) 関数を使ってデータを college という名前で取り込め
college = pd.read_csv("College.csv")

# (b) 次の関数を実行せよ
# > rownames(college)=college[,1]
# > fix(college)
college.index = college.iloc[:, 0]
print(college.to_string())

# > college=college[,-1]
# > fix(college)
college = college.drop(columns=college.columns[[0]])
print(college.to_string())

# (c)
# i. summery() 関数を使って数値的に要約せよ
print(college.describe())

# ii. pairs() 関数を使って散布図行列を作成せよ
sns.pairplot(college.iloc[:, 1:10]).savefig('college_pairs.png')

# iii. plot() 関数で Outstate と Private の箱ひげ図を並べて作成せよ
college.loc[:, ["Outstate", "Private"]].boxplot(by="Private").get_figure().savefig('college_boxplot.png')

# iv. Top10perc 変数から新たな質的変数 Elite を作成せよ
# 高校での成績が上位 10% だった者の割合が 50% 以上か否かによって、大学を 2 つのグループに分ける
# Elite=rep("No", nrow(college))
# Elite[college$Top10perc>=50]="Yes"
# Elite=as.factor(Elite)
# college=data.frame(college, Elite)

# for 文 ver
# elite = []
# for top10perc in college.loc[:, "Top10perc"]:
#     if top10perc >= 50:
#         elite.append("Yes")
#     else:
#         elite.append("No")
# college["Elite"] = elite

# # 1000 回 実行時間測定 & 平均出力
# time_sum = 0
# for i in range(1000):  # for 分
#     start = time.time()
#     elite = []
#     for top10perc in college.loc[:, "Top10perc"]:
#         if top10perc >= 50:
#             elite.append("Yes")
#         else:
#             elite.append("No")
#     college["Elite"] = elite
#     time_sum += time.time() - start
#     college = college.drop(columns="Elite")
# print("0, ", time_sum / 1000)
#
# time_sum = 0
# for i in range(1000):  # 多分速い
#     start = time.time()
#     elite = ["No"] * len(college)
#     college["Elite"] = elite
#     college.loc[college["Top10perc"] >= 50, "Elite"] = "Yes"
#     time_sum += time.time() - start
#     college = college.drop(columns="Elite")
# print("1, ", time_sum / 1000)
#
# time_sum = 0
# for i in range(1000):  # 行数少ない
#     start = time.time()
#     college.loc[college["Top10perc"] >= 50, "Elite"] = "Yes"
#     college.loc[college["Top10perc"] < 50, "Elite"] = "No"
#     time_sum += time.time() - start
#     college = college.drop(columns="Elite")
# print("2, ", time_sum / 1000)

# for 使わない ver
elite = ["No"] * len(college)
college["Elite"] = elite
college.loc[college["Top10perc"] >= 50, "Elite"] = "Yes"
# college.loc[college["Top10perc"] < 50, "Elite"] = "No"

# summary 関数でエリートの大学がいくつあるか示せ
print(college.loc[:, "Elite"].value_counts())

# plot() 関数で Outstate と Elite の箱ひげ図を並べて作成せよ
college.loc[:, ["Outstate", "Elite"]].boxplot(by="Elite").get_figure().savefig('elite_boxplot2.png')

# v. hist() 関数でいくつかの量的変数のヒストグラムを作成せよ。
# ビンの数を変えてみること。par(mfrow=c(2,2)) が便利である。
# これを使うとウィンドウが 4 分割され、4 つの図を同時に描くことができる。
# また、関数に渡す引数を調整することにより、ウィンドウを分割する方法を変更することができる。
fig = plt.figure(figsize=(10, 10))

ax1 = fig.add_subplot(2, 2, 1)
ax1.hist(college.loc[:, "Apps"], bins=30)
ax1.set_title("Apps")

ax2 = fig.add_subplot(2, 2, 2)
ax2.hist(college.loc[:, "Outstate"], bins=20)
ax2.set_title("Outstate")

ax3 = fig.add_subplot(2, 2, 3)
ax3.hist(college.loc[:, "Top25perc"], bins=10)
ax3.set_title("Top25perc")

ax4 = fig.add_subplot(2, 2, 4)
ax4.hist(college.loc[:, "Expend"], bins=5)
ax4.set_title("Expend")

fig.savefig('college_hist.png')

# vi. データをさらに詳しく調べ、どのような知見を得たか説明せよ。
