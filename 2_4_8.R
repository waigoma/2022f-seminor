# (a) 関数を使ってデータを college という名前で取り込め
college = read.csv("College.csv")

# (b) 次の関数を実行せよ
# fix(college)
rownames(college)=college[,1]
# fix(college)

college=college[,-1]
# fix(college)

# (c)
# i. summery()
# summary(college)

# ii. pairs() 関数を使って散布図行列を作成せよ
# pairs(college[,1:10])

# iii. plot() 関数で Outstate と Private の箱ひげ図を並べて作成せよ
plot(college$Private, college$Outstate)


