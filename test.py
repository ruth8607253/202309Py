import random
import statistics

class Player:
    def __init__(self, name, d1=0, d2=0, d3=0, d4=0):
        self.__dice1 = d1
        self.__dice2 = d2
        self.__dice3 = d3
        self.__dice4 = d4
        self.name = name

    def __play(self) -> int:
        Dice = [self.__dice1, self.__dice2, self.__dice3, self.__dice4]

        if len(set(Dice)) == 1:
            if sum(Dice) == 4:
                score = 13
            elif sum(Dice) == 8:
                score = 14
            elif sum(Dice) == 12:
                score = 15
            elif sum(Dice) == 16:
                score = 16
            elif sum(Dice) == 24:
                score = 17
            else:
                score = 18
        elif len(set(Dice)) == 4 or Dice.count(self.__dice1) == 3 or Dice.count(self.__dice2) == 3 or Dice.count(
                self.__dice3) == 3 or Dice.count(self.__dice4) == 3:
            score = 0
        else:
            score = sum(Dice) - min(statistics.multimode(Dice)) * 2

        return score

    @property
    def value(self) -> int:
        return self.__play()

    def __repr__(self) -> str:
        descript = ""
        descript += f"{self.name}\n"
        descript += f"骰子1={self.__dice1}\n"
        descript += f"骰子2={self.__dice2}\n"
        descript += f"骰子3={self.__dice3}\n"
        descript += f"骰子4={self.__dice4}\n"
        descript += f"得分={self.value}分"
        return descript

if __name__ == "__main__":
    while True:
        p1 = Player("robert", random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))
        p2 = Player("john", random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))

        print(p1.value)
        print(p1)

        print(p2.value)
        print(p2)

        if p1.value == 0 or p2.value == 0:
            print("重新开始游戏。")
            continue

        # 添加其他结束游戏的条件

        input("按 Enter 键继续游戏...")
