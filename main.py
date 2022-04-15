import random

"""
Я створив клас Me(Power, Warrior) дочірній від класів Power і Warrior.
Клас Power задає поля power для класів Me та Enemy.
При створенні екземпляру класу Me створюється поле ворога self.my_enemy = Enemy().
Відбувається стільки битв, скільки в циклі викликається метод fight(self, num).
Якщо у когось з суперників поле power стає меншим або рівним 0,
то цикл переривається достроково з відповідним повідомленням.
Поле power у суперників в кожній битві збільшується на свої рандомні значення з
arm_list та defence_list, та зеншується на подібні значення суперника.
"""

warrior_list = ['Козак', 'Самурай', 'Лицар', 'Центуріон', 'Вікінґ']
enemy_list = ['Відьмак', 'Зомбі', 'Перевертень', 'Ґоблін', 'Орк']
arm_list = [['Шабля', 10], ['Меч', 20], ['Молот Тора', 30], ['Спис', 40], ['Лук', 50]]
defence_list = [['Без захисту', 0], ['Кольчуга', 10], ['Обладунки', 20]]

class Power:
    def __init__(self):
        super().__init__()
        self.power = random.randint(7,12) * 10

class Warrior:
    def __init__(self):
        super().__init__()
        self.warrior = warrior_list[random.randint(0,4)]

class Enemy(Power):
    def __init__(self):
        super().__init__()
        self.enemy = enemy_list[random.randint(0,4)]

class Me(Power, Warrior):
    def __init__(self, name):
        super().__init__()
        self.my_name = self.warrior + ' ' + name
        self.my_enemy = Enemy()
        print('Суперники:')
        print(self.my_name, 'з початковою міццю:', str(self.power))
        print(self.my_enemy.enemy, 'з початковою міццю:', str(self.my_enemy.power))
        print()
        print('*' * 30)
        print()

    def fight(self, num):
        print('Битва %s відбулася:' % num)
        rand1 = arm_list[random.randint(0,4)]
        rand2 = defence_list[random.randint(0, 2)]
        pow1 = rand1[1] + rand2[1]
        self.power += pow1
        self.my_enemy.power -= pow1
        print(self.my_name + ':')
        print('\t' + 'Зброя: ' + rand1[0])
        print('\t' + 'Захист: ' + rand2[0])
        rand1 = arm_list[random.randint(0, 4)]
        rand2 = defence_list[random.randint(0, 2)]
        pow2 = rand1[1] + rand2[1]
        self.power -= pow2
        self.my_enemy.power += pow2
        print('\t' + 'Міць: ' + str(self.power))
        print(self.my_enemy.enemy + ':')
        print('\t' + 'Зброя: ' + rand1[0])
        print('\t' + 'Захист: ' + rand2[0])
        print('\t' + 'Міць: ' + str(self.my_enemy.power))
        if pow1 > pow2: print('Переміг: ' + self.my_name)
        elif pow1 < pow2: print('Переміг: ' + self.my_enemy.enemy)
        else: print('Нічия')
        print()
        print('-' * 30)
        print()
        if self.power > 0 and self.my_enemy.power > 0: return False
        elif self.power <= 0:
            print('Війна закінчилась - переміг %s, а %s - вбитий' % (self.my_enemy.enemy, self.my_name))
            return True
        else:
            print('Війна закінчилась - переміг %s, а %s - вбитий' % (self.my_name, self.my_enemy.enemy))
            return True


me = Me('Роман')
flag = True
for i in range(1, 9):
    if me.fight(i):
        flag = False
        break
if flag: print('Досить битись - пора на пиво!!!')