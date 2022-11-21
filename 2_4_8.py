# csv 読み込み用
import pandas as pd
# データの可視化用
import seaborn as sns

# 表示上限を設定
pd.set_option('display.max_columns', 100)

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
college.loc[:, ["Outstate", "Private"]].boxplot(by="Private").get_figure().savefig('college_boxplot.png')
