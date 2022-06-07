import pygame
import datetime_get
import linecache


background_1_1 = pygame.image.load("D:/pythonProject/images/background_1.jpg")
background_1_2_0 = pygame.image.load("D:/pythonProject/images/page_1_press.png")
background_1_4_0 = pygame.image.load("D:/pythonProject/images/question.png")
background_1_5_0 = pygame.image.load("D:/pythonProject/images/page_1_press_2.png")
background_1_6_0 = pygame.image.load("D:/pythonProject/images/close.png")
background_1_2 = pygame.transform.scale(background_1_2_0, (200, 130))
background_1_3 = pygame.transform.scale(background_1_2_0, (200, 70))
background_1_4 = pygame.transform.scale(background_1_4_0, (480, 400))
background_1_5 = pygame.transform.scale(background_1_5_0, (415, 35))
background_1_6 = pygame.transform.scale(background_1_6_0, (40, 35))
text_contact_1 = "第 " + str(datetime_get.nowadays) + " 天"
background_1_2_new = pygame.transform.scale(background_1_2_0, (170, 110))
background_1_3_new = pygame.transform.scale(background_1_2_0, (170, 50))

def everyday_question(row):  # 读取文件获得答案
    answer = linecache.getline('D:/pythonProject/everyday_question.txt', row)
    return answer
