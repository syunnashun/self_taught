# 第7章のチャレンジ
# http://tinyurl.com/z2m2115

beautiful_girls = ['浜辺美波', '吉岡里帆', '永野芽郁', '多部未華子']
for show in beautiful_girls:
    print(show)

x = 25
for x in range(25, 51):
    print(x)
    x += 1

# 無限ループする数字当てプログラムを書いてみた（3回間違えると，BYEBYEしちゃうよ）
# さらに，例外処理として，数字以外が入力されたときに警告を出すようプログラムにしてみた

answer = [1, 44, 777, 10000, 20000410]
miss = 0
while True:
    try:
        number = input("Type the secret number.:")
        number = int(number)
        if number in answer:
            print('Pinporn! {} is important.'.format(number))
            break
        else:
            print('Bubbu~! {} is not the password.'.format(number))
            miss += 1
            if miss == 3:
                print('ByeBye~.')
                break
    except ValueError:
        print("Are you kidding? Type 'number'!")
        miss += 1

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
multiple_list = []

for i in list1:
    for j in list2:
        multiple_list.append(i * j)
print(multiple_list)