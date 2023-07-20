import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm

# pandas の表示オプション
pd.set_option('display.max_columns', 100)  # 表示する列数の設定
pd.set_option('display.max_rows', 100)  # 表示する行数の設定

# (a) データセットに含まれる各変数の散布図を作成する
Auto = pd.read_csv("Auto.csv", na_values="?")  # na_valuesで'?'を欠損値として扱う
Auto = Auto.dropna()  # 欠損値を含む行を削除

# pairs(Auto) 相関図の作成
# sns.pairplot(Auto)
# plt.show()

# (b) cor() 関数を使い、相関行列を計算する。変数 name は相関行列に含めないこと。
correlation_matrix = Auto.drop(columns='name').corr()
print(correlation_matrix)

# (c) lm() 関数を使い、mpg を応答変数、name 以外のすべてを予測変数とする線形重回帰を当てはめる。
# このとき、summary() 関数を使い、当てはまったモデルの結果を表示する。
# 線形回帰モデルの作成
formula = "mpg ~ cylinders + displacement + horsepower + weight + acceleration + year + origin"
lm_fit1 = smf.ols(formula=formula, data=Auto).fit()
# モデルの summary を表示
print(lm_fit1.summary())

# i. 予測変数と応答変数に関係はあるか
# statsmodels の anova_lm() 関数を使い、このモデルの分散分析表を表示する。
# 分散分析を実行
anova_table = anova_lm(lm_fit1)
print(anova_table)

# ii. 予測変数のうちどれが応答変数と統計的に優位な関係にあると思われるか
#
# iii. 変数 year の係数はどのようなことを示唆しているか
#
