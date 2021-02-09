# 第6章のチャレンジ
# http://tinyurl.com/hapm4dx

example = "カミュ"
print(example[0], example[1], example[2])

入力1 = input("あなたは何を書きますか？:")
入力2 = input("あなたの思い人の名は？")
print("私は昨日{}を書いて，{}に送った！".format(入力1, 入力2))

"aldous Huxley was born in 1894.".capitalize()

'どこで？　だれが？　いつ？'.split(' ')

words = ["The", "fox", "jumped", "over", "the", "fence", "."]
sentence = " ".join(words)
sentence = sentence[0:-2] + "."
print(sentence)

sky = "A screaming comes across the sky."
sky = sky.replace("s", "$")
print(sky)

"Hemingway".index("m")

"'君の膵臓が食べたい'なんてね。"
plus = "three" + "three" + "three"
mult = "three" * 3
print(plus)
print(mult)
if plus == mult:
    print("Good job!")

sample_sentence = "四月の晴れた寒い日で，時計がどれも十三時を打っていた。"
slce = sample_sentence[0:11]
print(slce)