import pygame

background_2_1_0 = pygame.image.load("D:/pythonProject/images/background_2.png")
background_2_1 = pygame.transform.scale(background_2_1_0, (1400, 980))
face_1 = pygame.Surface((160, 40), flags=pygame.HWSURFACE)
face_1.fill((139, 26, 26))
face_2 = pygame.Surface((115, 40), flags=pygame.HWSURFACE)
face_2.fill((139, 26, 26))
face_3 = pygame.Surface((183, 40), flags=pygame.HWSURFACE)
face_3.fill((139, 26, 26))
face_4 = pygame.Surface((225, 40), flags=pygame.HWSURFACE)
face_4.fill((139, 26, 26))
face_5 = pygame.Surface((210, 50), flags=pygame.HWSURFACE)
face_5.fill((255, 160, 122))
background_2_2_0 = pygame.image.load("D:/pythonProject/images/clock.png")  # 时钟
background_2_2 = pygame.transform.scale(background_2_2_0, (35, 35))
background_2_3_0 = pygame.image.load("D:/pythonProject/images/money.png")  # 金币
background_2_3 = pygame.transform.scale(background_2_3_0, (35, 35))
background_2_4_0 = pygame.image.load("D:/pythonProject/images/arrow_right.png")  # →原图
background_2_4_1 = pygame.transform.scale(background_2_4_0, (45, 45))  # →正常
background_2_4_2 = pygame.transform.scale(background_2_4_0, (70, 70))  # →放大
background_2_5_0 = pygame.image.load("D:/pythonProject/images/heart.png")  # 桃心原图
background_2_5 = pygame.transform.scale(background_2_5_0, (55, 55))  # 桃心