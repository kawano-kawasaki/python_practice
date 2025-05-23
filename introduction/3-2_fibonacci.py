# フィボナッチ級数
# 2項の和により次項が定まる

# 多重入力
a, b = 0, 1
while a < 10:
    # endで出力末尾を改行から文字列に変更
    print(a, end=',')
    a, b = b, a+b

# isとaの間には自動でスペースが挿入される
print('The final number is', a)