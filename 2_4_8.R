# (a) 関数を使ってデータを college という名前で取り込め
college <- read.csv("College.csv")

# (b) 次の関数を実行せよ
rownames(college)=college[,1]
# fix(college)

college=college[,-1]
# fix(college)

# (c)
# i. summery()
# summary(college)

# ii. pairs() 関数を使って散布図行列を作成せよ
# pairs() が使えなかった。
library(psych)
psych::pairs.panels(college[,1:10])
