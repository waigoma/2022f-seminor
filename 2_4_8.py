import pandas as pd

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
print(college.to_string())

# (c)
# i. summery() 関数を使って数値的に要約せよ

