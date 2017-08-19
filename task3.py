# coding=utf8

class Altman(object):
    def __init__(self):
        self.rank = 1
        self.blood = self.rank * 30
        self.attackPower = self.rank * 10

    def upgrade(self):
        self.rank = self.rank+1
        self.blood = self.rank * 30

    def attack(self, monster):
        monster.blood = monster.blood - self.attackPower * 2 / 3.0



class Monster(object):
    def __init__(self, blood, attackPower):
        self.blood = blood
        self.attackPower = attackPower

    def counterattack(self, altman):
        altman.blood = altman.blood - self.attackPower * 1 / 2.0


def game(altman, monster):
    count = 0
    for m in monster:
        count = count + 1
        print "***奥特曼开始攻击第{0}只怪兽***".format(count)
        while 1:
            print "奥特曼的血量为{0}，等级为{1}级".format(altman.blood, altman.rank) + ",第{0}只怪兽的血量为{1}。".format(count, m.blood)
            if altman.blood > 0:
                altman.attack(m)
            else:
                print "*奥特曼死亡，挑战失败！"
                exit(1)
            if m.blood > 0:
                m.counterattack(altman)
            else:
                print "*第{0}只怪兽被奥特曼消灭了！".format(count)
                break

        altman.upgrade()
        print "*奥特曼等级提升为{0}级!".format(altman.rank)

    print "*奥特曼挑战成功！"


if __name__ == "__main__":
    altman = Altman()
    monster = [Monster(12, 5), Monster(12, 10), Monster(22, 15), Monster(28, 20), Monster(33, 50)]
    print "------------------------游戏开始----------------------------"
    game(altman, monster)



