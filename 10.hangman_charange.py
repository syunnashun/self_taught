# 第10章のチャレンジ
# http://tinyurl.com/j7rb8or
# hangman関数を，答えを与えられたリストの中からランダムに決定する仕様に改造する

import random

def hangman(word_list):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|       |       ",
             "|       o       ",
             "|      /|\      ",
             "|      / \      ",
             "|               "
             ]
    word = random.choice(word_list)
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to hangman!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Gusee the one word."
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose.\nThe answer is {}.".format(word))

word_list = ["cat", "dog", "rat"]
hangman(word_list)