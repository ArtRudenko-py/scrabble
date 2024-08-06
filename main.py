from scrabble import desk
from scrabble import packet
from scrabble import player

print("Количество очков за букву:")
print()
a = desk()
r = packet()
print("Введите имя: ")
player1 = player(input())
print("Введите имя: ")
player2 = player(input())
player1.random()

player2.random()

while True:

    print("Ходит первый игрок: ")

    for i in range(7):
        player1.random2()
        print("Введите букву, которую хотите установить.")
        print("Либо введите 0 если хотите завершить ход. ")
        g = input()
        if g == "0":
            break

        print("Введите строку: ")
        s = int(input())
        print("Введите столбец: ")
        p = int(input())
        player1.step(a, s, p, g)

        a.description()

    player1.restore(r)
    result = r.end_game()

    if result == 1:
        break

    print("Ходит второй игрок: ")

    for i in range(7):
        player2.random2()
        print("Введите букву, которую хотите установить.")
        print("Либо введите 0 если хотите завершить ход. ")
        g = input()
        if g == "0":
            break

        print("Введите строку: ")
        s = int(input())
        print("Введите столбец: ")
        p = int(input())
        player2.step(a, s, p, g)

        a.description()
    player2.restore(r)
    result = r.end_game()

    if result == 1:
        break

print(player1.point_output())
print(player2.point_output())