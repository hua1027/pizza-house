import pygame
import linecache
import constant

background_3_1_0 = pygame.image.load("D:/pythonProject/images/wood.png")  # 托盘
background_3_1 = pygame.transform.scale(background_3_1_0, (1100, 1100))
background_3_2_0 = pygame.image.load("D:/pythonProject/images/box.png")  # 食材盒
background_3_2 = pygame.transform.scale(background_3_2_0, (430, 430))
background_3_5 = pygame.transform.scale(background_3_2_0, (800, 700))  # 面盒
background_3_3_0 = pygame.image.load("D:/pythonProject/images/background_3.jpeg")  # 棋盘格背景
background_3_3 = pygame.transform.scale(background_3_3_0, (1300, 730))
background_3_4_0 = pygame.image.load("D:/pythonProject/images/oven.png")  # 烤箱
background_3_4 = pygame.transform.scale(background_3_4_0, (700, 600))
background_3_6_0 = pygame.image.load("D:/pythonProject/images/decorate.png")  # 装饰
background_3_6 = pygame.transform.scale(background_3_6_0, (400, 600))
background_3_7_0 = pygame.image.load("D:/pythonProject/images/dough.png")  # 面团
background_3_7 = pygame.transform.scale(background_3_7_0, (300, 210))
background_3_8_0 = pygame.image.load("D:/pythonProject/images/dialog_box.png")  # 对话框
background_3_8 = pygame.transform.scale(background_3_8_0, (380, 250))

food_1_0 = pygame.image.load("D:/pythonProject/images/food_1.png")  # 洋葱
food_2_0 = pygame.image.load("D:/pythonProject/images/food_2.png")  # 西蓝花
food_3_0 = pygame.image.load("D:/pythonProject/images/food_3.png")  # 蘑菇
food_4_0 = pygame.image.load("D:/pythonProject/images/food_4.png")  # 西红柿
food_5_0 = pygame.image.load("D:/pythonProject/images/food_5.png")  # 虾仁
food_6_0 = pygame.image.load("D:/pythonProject/images/food_6.png")  # 火腿
food_7_0 = pygame.image.load("D:/pythonProject/images/food_7.png")  # 培根
food_1 = pygame.transform.scale(food_1_0, (100, 100))
food_2 = pygame.transform.scale(food_2_0, (140, 140))
food_3 = pygame.transform.scale(food_3_0, (140, 140))
food_4 = pygame.transform.scale(food_4_0, (190, 180))
food_5 = pygame.transform.scale(food_5_0, (70, 70))
food_6 = pygame.transform.scale(food_6_0, (80, 80))
food_7 = pygame.transform.scale(food_7_0, (290, 290))
face_1 = pygame.Surface((113, 85), flags=pygame.HWSURFACE)  # 番茄酱
face_1.fill((255, 69, 0))
face_2 = pygame.Surface((113, 85), flags=pygame.HWSURFACE)  # 沙拉酱
face_2.fill((255, 222, 173))

dough_0 = pygame.image.load("D:/pythonProject/images/pancake.png")
dough = pygame.transform.scale(dough_0, (650, 650))


def text():
    if constant.v1 != -1:
        constant.text1 = linecache.getline('D:/pythonProject/veg_more.txt', constant.v1)
        # print(text1)
    if constant.v2 != -1:
        constant.text2 = linecache.getline('D:/pythonProject/veg_less.txt', constant.v2)
    if constant.m1 != -1:
        constant.text3 = linecache.getline('D:/pythonProject/meat_more.txt', constant.m1)
    if constant.m2 != -1:
        constant.text4 = linecache.getline('D:/pythonProject/meat_less.txt', constant.m2)

card_0 = pygame.image.load("D:/pythonProject/images/card.jpg")
card = pygame.transform.scale(card_0, (1050, 950))