# 異なるdictionaryにあるファイルを読み込み，表示するprogrammingを書いてみた

import os
file_path = os.path.join("C:", "/Users", "旬な駿", "Documents", "python-myself", "useful_memo.txt")
# 1度ファイルパスを表示してみる
print(file_path)

#file_pathが存在するか教えてもらう
which = os.path.isfile(file_path)
print(which)

with open(file_path, "r") as f:
    print(f.read())
# ファイルパスについてトラブってしまったらコチラ
# https://cocodrips.hateblo.jp/entry/2015/07/19/120028

# charangeに進みます．
# http://tinyurl.com/hll6t3q
# 何か質問するプログラムを書いて，入力された回答をファイルに書き出そう．

ans = input("Q, What is goal you should achieve?:")

import os
file_ans = os.path.join("C:", "/Users", "旬な駿", "Documents", "python-vol.2-dokugaku-programer", "Part.1", "9.file", "ansers.txt")
with open(file_ans, "w+") as f:
    f.write(ans)

# このwirh open(___, "")の部分を「"fail"」にすると，ファイル名がfileになり，「適当に名前を付けたファイルパス」にすると，ファイル名がパスの最後の形式になることが判明した．
# リストに含まれている要素をCSVファイルに書き出そう．

data = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

import csv
with open("st_charange.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(data[0])
    w.writerow(data[1])
    w.writerow(data[2])

# リストを日本語に置き換えてCSVファイルに書き出そう．

data_prime =  [["トップガン", "リスキービジネス", "マイノリティーリポート"], ["タイタニック", "レヴェナント：蘇りし者", "インセプション"], ["トレーニングデイ", "マン オブ ファイア", "ファイト"]]


with open("st_charange.csv", "a", encoding="cp932", newline="") as h:
    a = csv.writer(h, delimiter=",")
    a.writerow(data_prime[0])
    a.writerow(data_prime[1])
    a.writerow(data_prime[2])

with open("st_charange.csv", "r", encoding="cp932") as g:
    r = csv.reader(g, delimiter=",")
    for row in r:
        print(",".join(row))

# encoding="cp932"とすると，ファイルの中身が非アスキー文字で正しく表示される．
# encoding="utf-8"とすると，VScode上で非アスキー文字が正しく表示される．