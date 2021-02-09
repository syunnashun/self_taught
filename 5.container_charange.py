# 第5章のチャレンジ
# http://tinyurl.com/z54w9cb
# 好きな歌手を答えると，そのプレイリストを辞書型で教えてくれるプログラムを書いてみた

my_favorite = ["緑黄色社会", "山下智久", "FUNKY MONKEY BABYS", "乃木坂46"]
my_place = [(35.212, 136.4821), (38.1541, 140.5152)]
Who_I_am = {'sports':'softeni', 'height':'162.5', 'weight':'47.75', 'favoite':'myself'}

answer = input("Type sports, height, weight or favorite.:")
if answer in Who_I_am:
    result = Who_I_am[answer]
    print(result)

play_list = []
def lists(x):
    if x == "緑黄色社会":
        play_list.append('夏を生きる')
        play_list.append('Mela!')
        play_list.append('Shout Baby')
    elif x == "山下智久":
        play_list.append('SUMEER NUDE.13')
        play_list.append('CHANGE')
        play_list.append('Night Cold')
        play_list.append('カラフル')
    elif x == "FUNKY MONKEY BABYS" :
        play_list.append('告白')
        play_list.append('あとひとつ')
    elif x == "乃木坂46":
        play_list.append('裸足でSummer')
        play_list.append('インフルエンサー')
        play_list.append('ガールズルール')
    else:
        print("There is no songs which I love.")

my_songs = dict()
final_answer = input("Type your favorite singer.:")
if final_answer in my_favorite:
    lists(final_answer)
    my_songs[final_answer] = play_list
    print(my_songs)
else:
    print("The singer isn't my favorite!")