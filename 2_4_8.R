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
# plot(college$Private, college$Outstate)

# iv. Top10perc 変数から新たな質的変数 Elite を作成せよ
# 高校での成績が上位 10% だった者の割合が 50% 以上か否かによって、大学を 2 つのグループに分ける
Elite=rep("No", nrow(college))
Elite[college$Top10perc>=50]="Yes"
Elite=as.factor(Elite)
college=data.frame(college, Elite)
# summary 関数でエリートの大学がいくつあるか示せ
summary(college$Elite)
#  No Yes
# 699  78

# plot() 関数で Outstate と Elite の箱ひげ図を並べて作成せよ
plot(college$Elite, college$Outstate)

# v. hist() 関数でいくつかの量的変数のヒストグラムを作成せよ。
# ビンの数を変えてみること。par(mfrow=c(2,2)) が便利である。
# これを使うとウィンドウが 4 分割され、4 つの図を同時に描くことができる。
# また、関数に渡す引数を調整することにより、ウィンドウを分割する方法を変更することができる。
par(mfrow=c(2,2))
hist(college$Apps)
hist(college$perc.alumni, col=2)
hist(college$S.F.Ratio, col=3, breaks=10)
hist(college$Expend, breaks=100)

# vi. データをさらに詳しく調べ、どのような知見を得たか説明せよ。
par(mfrow=c(1,1))
plot(college$Outstate, college$Grad.Rate)
# High tuition correlates to high graduation rate.
plot(college$Accept / college$Apps, college$S.F.Ratio)
# Colleges with low acceptance rate tend to have low S:F ratio.
plot(college$Top10perc, college$Grad.Rate)
# Colleges with the most students from top 10% perc don't necessarily have
# the highest graduation rate. Also, rate > 100 is erroneous!