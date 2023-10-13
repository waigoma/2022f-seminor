import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm
import statsmodels.api as sm

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
# print(correlation_matrix)

# (c) lm() 関数を使い、mpg を応答変数、name 以外のすべてを予測変数とする線形重回帰を当てはめる。
# このとき、summary() 関数を使い、当てはまったモデルの結果を表示する。

# 予測変数と応答変数を設定
X = Auto.drop(['mpg', 'name'], axis=1)
y = Auto['mpg']

# 定数項（切片）をモデルに追加
X = sm.add_constant(X)

# 線形回帰モデルを作成
model = sm.OLS(y, X).fit()

# i. 予測変数と応答変数に関係はあるか
print(model.summary())

# ii. 予測変数のうちどれが応答変数と統計的に優位な関係にあると思われるか
#
# iii. 変数 year の係数はどのようなことを示唆しているか
#
