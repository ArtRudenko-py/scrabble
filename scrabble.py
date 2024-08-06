import random

a = {"А": 1, "Б": 3, "В": 1, "Г": 3, "Д": 2, "Е": 1, "Ё": 3, "Ж": 5, "З": 5, "И": 1, "Й": 4, "К": 2, "Л": 2, "М": 2,
     "Н": 1, "О": 1, "П": 2, "Р": 1, "С": 1, "Т": 1, "У": 2, "Ф": 10, "Х": 5, "Ц": 5, "Ч": 5, "Ш": 8, "Щ": 10, "Ъ": 10,
     "Ы": 4, "Ь": 3, "Э": 8, "Ю": 8, "Я": 3}


class desk:
    def __init__(self):
        self.__board = []
        for i in range(15):
            self.__board.append([])
            for j in range(15):
                self.__board[i].append([])

    def set_alpha(self, x, y, q, ):
        self.__board[x - 1][y - 1] = q

    def description(self):
        for i in range(15):
            print(self.__board[i])


class packet:
    def __init__(self):
        self.__packet = {"А": 8, "Б": 2, "В": 4, "Г": 2, "Д": 4, "Е": 8, "Ё": 1, "Ж": 1, "З": 2, "И": 5, "Й": 1, "К": 4,
                         "Л": 4, "М": 3, "Н": 5, "О": 10, "П": 4, "Р": 5, "С": 5, "Т": 5, "У": 4, "Ф": 1, "Х": 1,
                         "Ц": 1, "Ч": 1, "Ш": 1, "Щ": 1, "Ъ": 1, "Ы": 2, "Ь": 2, "Э": 1, "Ю": 1, "Я": 2}

    def alpha_from_packet(self, alph):
        self.__packet[alph] -= 1

    def packet(self, r):
        return self.__packet[r]

    def packet_display(self):
        print(self.__packet)

    def end_game(self):
        d = 0

        for v in self.__packet:
            if self.__packet[v] != 0:
                d = 1
        if d == 0:
            return 1
        else:
            return 0


class player:
    def __init__(self, name):
        self.__name = name
        self.__alph = []
        self.__point = 0

    def random(self):
        while len(self.__alph) < 7:
            d = ("ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ")
            s = random.randint(0, len(d) - 1)

            c = d[s]
            self.__alph.append(c)

    def random2(self):

        print(self.__alph)

    def step(self, s, f, g, b):

        self.__alph.remove(b)

        s.set_alpha(f, g, b)
        a = {"А": 1, "Б": 3, "В": 1, "Г": 3, "Д": 2, "Е": 1, "Ё": 3, "Ж": 5, "З": 5, "И": 1, "Й": 4, "К": 2, "Л": 2,
             "М": 2,
             "Н": 1, "О": 1, "П": 2, "Р": 1, "С": 1, "Т": 1, "У": 2, "Ф": 10, "Х": 5, "Ц": 5, "Ч": 5, "Ш": 8, "Щ": 10,
             "Ъ": 10,
             "Ы": 4, "Ь": 3, "Э": 8, "Ю": 8, "Я": 3}
        if b in a.keys():
            self.__point += a[b]

    def restore(self, f):
        while len(self.__alph) != 7:

            d = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ"
            w = random.randint(0, len(d) - 1)
            e = d[w]

            if f.packet(e) > 0:
                self.__alph.append(e)
                f.alpha_from_packet(e)

    def point_output(self):
        return self.__point


