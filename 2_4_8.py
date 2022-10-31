import pandas as pd

# (a) 関数を使ってデータを college という名前で取り込め
college = pd.read_csv("College.csv")

# (b) 次の関数を実行せよ
# > rownames(college)=college[,1]
# > fix(college)

print(college.to_string())


