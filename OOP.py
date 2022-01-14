group_B9121_10_03_01otzi = []
class B9121_10_03_01otzi():
    anarchist_catch = 0

    def __init__(self, name_surname, gender, matan_pluses, rang, food_quality, social_credit=5, hp=0):
        self.name_surname = name_surname
        self.gender = gender
        self.matan_pluses = matan_pluses
        self.rang = rang
        self.food_quality = food_quality
        self.social_credit = matan_pluses * 10
        self.hp = food_quality * 100

    def ans_matan(self):
        self.matan_pluses += 1
        self.social_credit += 5
        print('good job, %s' %self.name_surname)

    def matan_kontrol(self):
        self.hp -= 30
        print('God, pls, help')

    def change_gender(self):
        if self.gender == 'M':
            self.gender = 'F'
            print('welcome to Famale club, %s'%self.name_surname)
        else:
            self.gender = "M"
            print('welcome to Male club, %s'%self.name_surname)

    def catch_an_7_2_anarchist(self):
        if self.anarchist_catch == 0:
            self.social_credit += 150000
            print('Mission completed')
            B9121_10_03_01otzi.anarchist_catch = 1
        else:
            self.social_credit -= 100
            print('LIER!!')


kid_2 = B9121_10_03_01otzi('Vlada_B', 'F', 9, 'godness', 0.3)
group_B9121_10_03_01otzi.append(kid_2)
kid_9 = B9121_10_03_01otzi('Artem_M', 'M', 7, 'regular_kid', 1.1)
group_B9121_10_03_01otzi.append(kid_9)

print(kid_2.hp)
kid_2.matan_kontrol()
kid_2.matan_kontrol()
print(kid_2.hp)
print('\n')

print(kid_9.social_credit)
kid_9.catch_an_7_2_anarchist()
print(kid_9.social_credit)
print('\n')

print(kid_2.social_credit)
kid_2.catch_an_7_2_anarchist()
print(kid_2.social_credit)
print('\n')

print(kid_9.gender)
kid_9.change_gender()
print(kid_9.gender)
print('\n')

print(kid_9.matan_pluses)
kid_9.ans_matan()
print(kid_9.matan_pluses)