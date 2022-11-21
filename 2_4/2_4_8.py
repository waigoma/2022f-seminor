# csv 読み込み用
import pandas as pd
# データの可視化用
import seaborn as sns

# 表示上限を設定
pd.set_option('display.max_columns', 1000)

# (a) 関数を使ってデータを college という名前で取り込め
college = pd.read_csv("College.csv")

# (b) 次の関数を実行せよ
# > rownames(college)=college[,1]
# > fix(college)
college.index = college.iloc[:, 0]
# print(college.to_string())

# > college=college[,-1]
# > fix(college)
college = college.drop(columns=college.columns[[0]])
# print(college.to_string())

# (c)
# i. summery() 関数を使って数値的に要約せよ
# print(college.describe())

# ii. pairs() 関数を使って散布図行列を作成せよ
# sns.pairplot(college.iloc[:, 1:10]).savefig('college_pairs.png')

# iii. plot() 関数で Outstate と Private の箱ひげ図を並べて作成せよ
# sns.boxplot(data=college.loc[:, ["Outstate", "Private"]]).get_figure().savefig('college_boxplot.png')
# college.loc[:, ["Outstate", "Private"]].boxplot(by="Private").get_figure().savefig('college_boxplot.png')

# iv. Top10perc 変数から新たな質的変数 Elite を作成せよ
# 高校での成績が上位 10% だった者の割合が 50% 以上か否かによって、大学を 2 つのグループに分ける
# Elite=rep("No", nrow(college))
# Elite[college$Top10perc>=50]="Yes"
# Elite=as.factor(Elite)
# college=data.frame(college, Elite)
elite = []
for top10perc in college.loc[:, "Top10perc"]:
    if top10perc >= 50:
        elite.append("Yes")
    else:
        elite.append("No")

college["Elite"] = elite

# summary 関数でエリートの大学がいくつあるか示せ
print(college.loc[:, "Elite"].value_counts())

# plot() 関数で Outstate と Elite の箱ひげ図を並べて作成せよ
college.loc[:, ["Outstate", "Elite"]].boxplot(by="Elite").get_figure().savefig('elite_boxplot2.png')

# v. hist() 関数でいくつかの量的変数のヒストグラムを作成せよ。
# ビンの数を変えてみること。par(mfrow=c(2,2)) が便利である。
# これを使うとウィンドウが 4 分割され、4 つの図を同時に描くことができる。
# また、関数に渡す引数を調整することにより、ウィンドウを分割する方法を変更することができる。


# vi. データをさらに詳しく調べ、どのような知見を得たか説明せよ。