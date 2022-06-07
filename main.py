import random
import sys  # 导入所需的模块
import pygame
from pygame.locals import *
import constant
import part_1
import part_2
import datetime_get
import datetime
import guest_picture
import part_3
import preserve_money
import get_money
import math
import get_requriement

pygame.init()  # 使用pygame之前必须初始化
#  这是整个程序中的第一句代码，它的作用是自动检测 Pygame 软件包是否正常可用，并检查电脑的硬件调用接口、基础功能是否存在问题，
#  比如音频、光驱、声卡驱动等设备。同时，它会完成 Pygame 中所有模块的初始化操作，比如 display（显示模块）、font（字体模块）、mixer（声音控制模块）、cursors（光标控制模块）等。

screen = pygame.display.set_mode((1300, 730))  # 设置主屏窗口
pygame.display.set_caption('pizza house')  # 设置窗口的标题，即游戏名称
logo = pygame.image.load('D:/pythonProject/images/logo.jpg')
pygame.display.set_icon(logo)  # 设置图标
f = pygame.font.SysFont(['隶书', 'microsoftsansserif'], 45)  # 引入字体类型
f_new = pygame.font.SysFont(['隶书', 'microsoftsansserif'], 40)
f_new_1 = pygame.font.SysFont(['隶书', 'microsoftsansserif'], 30)
page_1_text6 = f_new_1.render('仅供参考,热爱生活,好运加倍', True, (82, 139, 139), None)

x_1, y_1, x_2, y_2, x_3, y_3 = 0, 0, 0, 0, 0, 0  # 页面1坐标变量
x_2_1, y_2_1 = 0, 0  # 页面2鼠标移动
x_2_2, y_2_2 = 0, 0  # 页面2鼠标点击
x_3_1, y_3_1 = 0, 0  # 页面3鼠标移动
x_3_2, y_3_2 = 0, 0  # 页面3鼠标点击
guest_no = 0
guest = guest_picture.guest_1
num1 = 0  # 确保音频不会重复载入
num2 = 0
num3 = 0
num4 = 0
num5 = 0

while True:
    # 循环获取事件，监听事件状态
    # global x_1, y_1, x_2, y_2, x_3, y_3
    # global x_2_1, y_2_1
    for event in pygame.event.get():
        # 判断用户是否点了"X"关闭按钮,并执行if代码段 # pygame.QUIT 指点击右上角窗口的"X"号
        if event.type == pygame.QUIT:
            pygame.quit()  # 卸载所有模块
            sys.exit()  # 终止程序，确保退出程序

        if constant.game_state == 0:
            preserve_money.preserve_money()
            pygame.quit()  # 卸载所有模块
            sys.exit()  # 终止程序，确保退出程序

        if constant.game_page == 1:
            x_1 = 0
            y_1 = 0
            x_2 = 0
            y_2 = 0
            x_3 = 0
            y_3 = 0
            if event.type == pygame.MOUSEMOTION:
                x_1, y_1 = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_2, y_2 = event.pos
                if constant.page1_question == 1:
                    x_3, y_3 = event.pos
        elif constant.game_page == 2:
            x_2_1 = 0
            y_2_1 = 0
            x_2_2 = 0
            y_2_2 = 0
            if event.type == pygame.MOUSEMOTION:
                x_2_1, y_2_1 = event.pos
                # print(x_2_1, y_2_1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_2_2, y_2_2 = event.pos
                # print(x_2_2, y_2_2)

        elif constant.game_page == 3:
            x_3_1 = 0
            y_3_1 = 0
            x_3_2 = 0
            y_3_2 = 0
            # 鼠标移动
            if event.type == pygame.MOUSEMOTION:
                x_3_1, y_3_1 = event.pos
                # print(x_2_1, y_2_1)
            if event.type == pygame.MOUSEBUTTONDOWN:
                num4 = 0
                x_3_2, y_3_2 = event.pos
                # print(x_3_2, y_3_2)

    if constant.game_page == 1:
        if num1 == 0:
            pygame.mixer.music.load("music/page_1.mp3")
            pygame.mixer.music.play(-1)  # -1：循环播放
            num1 = num1 + 1

        screen.blit(part_1.background_1_1, (0, 0))  # 页面1大背景
        page_1_text1 = f.render(part_1.text_contact_1, True, (85, 107, 47), None)  # 正常字体
        page_1_text2 = f.render('开始营业', True, (85, 107, 47), None)
        page_1_text3 = f.render('每日一问', True, (85, 107, 47), None)
        page_1_text1_new = f_new.render(part_1.text_contact_1, True, (185, 183, 107), None)  # 按钮动态字体
        page_1_text2_new = f_new.render('开始营业', True, (189, 183, 107), None)
        page_1_text3_new = f_new.render('每日一问', True, (189, 183, 107), None)
        if 1065 <= x_1 <= 1235:
            if constant.page1_question == 0:  # 没有点击“每日一问”功能
                if 150 >= y_1 >= 40:  # 按钮1动态
                    screen.blit(part_1.background_1_2_new, (1065, 40))
                    screen.blit(page_1_text1_new, (1065, 50))
                    screen.blit(page_1_text2_new, (1070, 90))
                    screen.blit(part_1.background_1_3, (1050, 170))
                    screen.blit(page_1_text3, (1060, 180))
                elif 240 >= y_1 >= 170:  # 按钮2动态
                    screen.blit(part_1.background_1_3_new, (1065, 180))
                    screen.blit(page_1_text3_new, (1070, 185))
                    screen.blit(part_1.background_1_2, (1050, 30))
                    screen.blit(page_1_text1, (1060, 40))
                    screen.blit(page_1_text2, (1060, 90))
                else:
                    screen.blit(part_1.background_1_2, (1050, 30))
                    screen.blit(part_1.background_1_3, (1050, 170))
                    screen.blit(page_1_text1, (1060, 40))
                    screen.blit(page_1_text2, (1060, 90))
                    screen.blit(page_1_text3, (1060, 180))
            else:
                screen.blit(part_1.background_1_2, (1050, 30))
                screen.blit(part_1.background_1_3, (1050, 170))
                screen.blit(page_1_text1, (1060, 40))
                screen.blit(page_1_text2, (1060, 90))
                screen.blit(page_1_text3, (1060, 180))
        else:
            screen.blit(part_1.background_1_2, (1050, 30))
            screen.blit(part_1.background_1_3, (1050, 170))
            screen.blit(page_1_text1, (1060, 40))
            screen.blit(page_1_text2, (1060, 90))
            screen.blit(page_1_text3, (1060, 180))
        if 1065 <= x_2 <= 1335:
            if 40 <= y_2 <= 150:  # 跳转页面2
                if num4 == 0:
                    sound = pygame.mixer.Sound('music/ou1.mp3')
                    sound.play()
                    num4 = 1
                x_2 = 0
                y_2 = 0
                constant.game_page = 2
                num4 = 0
                num5 = 0

            elif 180 <= y_2 <= 230:  # 触发“每日一问”功能
                constant.page1_question = 1
                constant.page1_get_question = 1
                if num4 == 0:
                    sound = pygame.mixer.Sound('music/ou1.mp3')
                    sound.play()
                    num4 = 1
        else:
            pass
        if constant.page1_question == 1:
            constant.page1_press_2 = constant.page1_press_2 + 1  # 确保答案在刷新一段时间后再出现
            global x
            screen.blit(part_1.background_1_4, (470, 6))
            screen.blit(part_1.background_1_6, (820, 50))
            page_1_text4_1 = f.render('闭眼等待3秒', True, (85, 107, 47), None)
            page_1_text4_2 = f.render('获得答案:)', True, (85, 107, 47), None)
            screen.blit(page_1_text4_1, (530, 90))
            screen.blit(page_1_text4_2, (530, 150))
            if constant.page1_get_question == 1:  # 获取随机答案
                x = random.randint(1, 146)
                constant.page1_get_question = 0
            answer = part_1.everyday_question(x)
            page_1_text5 = f.render(answer, True, (205, 179, 139), None)
            if constant.page1_press_2 >= 400:  # 显示答案
                screen.blit(page_1_text5, (517, 270))
                screen.blit(part_1.background_1_5, (480, 220))
                screen.blit(page_1_text6, (490, 220))
                if num5 == 0:
                    sound = pygame.mixer.Sound('music/out_2.mp3')
                    num4 = 0
                    sound.play()
                    num5 = 1
            if 823 <= x_3 <= 860 and 55 <= y_3 <= 75:  # 退出“每日一问”功能
                if num4 == 0:
                    sound = pygame.mixer.Sound('music/ou1.mp3')
                    sound.play()
                    num4 = 1
                x_1 = 0
                y_1 = 0
                x_2 = 0
                y_2 = 0
                x_3 = 0
                y_3 = 0
                num4 = 0
                num5 = 0
                constant.page1_question = 0
                constant.page1_press_2 = 0
    if constant.game_page == 2:
        if num2 == 0:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("music/page_2.mp3")
            pygame.mixer.music.play(-1)  # -1：循环播放
            num2 = num2 + 1

        screen.blit(part_2.background_2_1, (-10, -82))  # 页面2大背景
        screen.blit(part_2.face_1, (15, 0))  # 几个小窗口背景
        screen.blit(part_2.face_2, (213, 0))
        screen.blit(part_2.background_2_5, (208, -7))  # 顾客心情图标

        screen.blit(part_2.face_4, (1058, 0))
        # 时间
        screen.blit(part_2.background_2_2, (20, 1))  # 小时钟标志
        f_2 = pygame.font.SysFont(['隶书', 'microsoftsansserif'], 21)  # 时间字体格式
        text_contact_1 = "第 " + str(datetime_get.nowadays) + " 天"
        text_1 = f_2.render(text_contact_1, True, (255, 193, 193), None)
        screen.blit(text_1, (70, 0))
        ISOTIMEFORMAT = '%H ：%M'  # 时间格式
        theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
        text_2 = f_2.render(theTime, True, (255, 193, 193), None)
        screen.blit(text_2, (70, 19))
        # 资金
        screen.blit(part_2.background_2_3, (1065, 0))
        if constant.if_get_money == 0:
            get_money.get_money()
            constant.float_money = float(constant.now_money)
            constant.if_get_money = 1

        f_3 = pygame.font.SysFont(['隶书', 'microsoftsansserif'], 22)  # 资金字体格式
        get_money.format_money(constant.float_money)
        text_3 = f_3.render(constant.format_money, True, (255, 193, 193), None)
        screen.blit(text_3, (1100, 7))

        # 结束营业
        if 830 <= x_2_1 <= 1020 and 0 <= y_2_1 <= 40:
            screen.blit(part_2.face_5, (825, 0))
            f_4 = pygame.font.SysFont(['隶书', 'microsoftsansserif'], 38)  # 结束营业字体格式
            text_4 = f_4.render('结 束 营 业', True, (139, 62, 47), None)
            screen.blit(text_4, (830, 6))
        else:
            screen.blit(part_2.face_3, (832, 0))
            f_5 = pygame.font.SysFont(['隶书', 'microsoftsansserif'], 30)  # 结束营业字体格式
            text_4 = f_5.render('结 束 营 业', True, (255, 193, 193), None)
            screen.blit(text_4, (845, 6))

        if 1230 <= x_2_1 <= 1270:
            if 345 >= y_2_1 >= 310:
                pygame.draw.circle(screen, (211, 211, 211), (1255, 325), 30, width=0)
                screen.blit(part_2.background_2_4_2, (1220, 290))
            else:
                screen.blit(part_2.background_2_4_1, (1230, 305))
        else:
            screen.blit(part_2.background_2_4_1, (1230, 305))

        if 835 <= x_2_2 <= 1020 and 0 <= y_2_2 <= 35:
            constant.game_state = 0
            preserve_money.preserve_money()
        if 1235 <= x_2_2 <= 1270 and 310 <= y_2_2 <= 340:
            if num4 == 0:
                sound = pygame.mixer.Sound('music/ou1.mp3')
                sound.play()
                num4 = 1
            x_2_2 = 0
            y_2_2 = 0
            constant.game_page = 3
            num3 = 0
            num4 = 0
            num5 = 0
            # pygame.mixer.music.stop()

        constant.guest_appear_time = constant.guest_appear_time + 1
        if constant.guest_appear_time >= 80:
            if constant.if_guest == 0:
                if constant.get_guest_no == 0:
                    guest_no = random.randint(1, 7)
                    num5 = 0
                    num4 = 0
                    constant.get_guest_no = 1
                    get_requriement.requirement()
                constant.if_guest = 1
            if constant.if_guest == 1:
                part_3.text()
                if guest_no == 1:
                    guest = guest_picture.guest_1
                elif guest_no == 2:
                    guest = guest_picture.guest_2
                elif guest_no == 3:
                    guest = guest_picture.guest_3
                elif guest_no == 4:
                    guest = guest_picture.guest_4
                elif guest_no == 5:
                    guest = guest_picture.guest_5
                elif guest_no == 6:
                    guest = guest_picture.guest_6
                elif guest_no == 7:
                    guest = guest_picture.guest_7

                if num5 == 0:
                    sound = pygame.mixer.Sound('music/out_2.mp3')
                    num4 = 0
                    sound.play()
                    num5 = 1
                screen.blit(guest, (310, 120))  # 绘制人物
                # print(constant.text1)
                screen.blit(part_3.background_3_8, (560, 40))  # 绘制气泡框
                if constant.cook == 0:
                    f = pygame.font.SysFont(['隶书', 'microsoftsansserif'], 30)
                    text_r_1 = f.render(constant.text1, True, (0, 205, 102), None)
                    text_r_2 = f.render(constant.text2, True, (0, 205, 102), None)
                    text_r_3 = f.render(constant.text3, True, (0, 205, 102), None)
                    text_r_4 = f.render(constant.text4, True, (0, 205, 102), None)
                    screen.blit(text_r_1, (590, 90))
                    screen.blit(text_r_2, (590, 120))
                    screen.blit(text_r_3, (590, 150))
                    screen.blit(text_r_4, (590, 180))
                # 不符合的要求及金额明细
                if constant.cook == 1:
                    f = pygame.font.SysFont(['隶书', 'microsoftsansserif'], 30)
                    text1 = f.render(constant.no_requirement1, True, (0, 205, 102), None)
                    text2 = f.render(constant.no_requirement2, True, (0, 205, 102), None)
                    text3 = f.render(constant.no_requirement3, True, (0, 205, 102), None)
                    text4 = f.render(constant.no_requirement4, True, (0, 205, 102), None)
                    screen.blit(text1, (590, 90))
                    screen.blit(text2, (590, 120))
                    screen.blit(text3, (590, 150))
                    screen.blit(text4, (590, 180))
                    screen.blit(part_3.card, (520, -220))
                    text_m1_0 = '单价:' + str(30)
                    constant.cost = round(constant.cost, 2)
                    text_m2_0 = '耗材:' + str(constant.cost)
                    constant.loss_p = round(constant.loss_p, 2)
                    text_m3_0 = '等待扣费:' + str(constant.loss_p * 0.5)
                    constant.loss = round(constant.loss, 2)
                    text_m4_0 = '完成度扣费:' + str(constant.loss)
                    x = 30 - constant.cost - constant.loss_p * 0.5 - constant.loss
                    x = round(x, 2)
                    text_m5_0 = '收入:' + str(x)
                    text_m1 = f.render(text_m1_0, True, (255, 248, 220), None)
                    text_m2 = f.render(text_m2_0, True, (255, 248, 220), None)
                    text_m3 = f.render(text_m3_0, True, (255, 248, 220), None)
                    text_m4 = f.render(text_m4_0, True, (255, 248, 220), None)
                    text_m5 = f.render(text_m5_0, True, (255, 248, 220), None)
                    if num5 == 0:
                        sound = pygame.mixer.Sound('music/out_2.mp3')
                        sound.play()
                        num5 = 1
                    screen.blit(text_m1, (933, 205))
                    screen.blit(text_m2, (933, 235))
                    screen.blit(text_m3, (933, 265))
                    screen.blit(text_m4, (933, 295))
                    screen.blit(text_m5, (933, 350))
                    screen.blit(part_1.background_1_3_new, (933, 400))
                    text_m6 = f.render('好  的', True, (85, 107, 147), None)
                    screen.blit(text_m6, (970, 410))

        # 判断不符合要求的损失
        if constant.cook == 1 and constant.if_check == 0:
            if constant.v1 // 7 == 0:
                if constant.food_1_num <= 3:
                    constant.if_null = 1
                    constant.loss = constant.loss + 1
                    constant.no_requirement1 = constant.no_requirement1 + '洋葱怎么这么少？'
            elif constant.v1 // 7 == 1:
                if constant.food_2_num <= 3:
                    constant.if_null = 1
                    constant.loss = constant.loss + 1
                    constant.no_requirement1 = constant.no_requirement1 + '西蓝花怎么这么少？'
            elif constant.v1 // 7 == 2:
                if constant.food_3_num <= 3:
                    constant.if_null = 1
                    constant.loss = constant.loss + 1
                    constant.no_requirement1 = constant.no_requirement1 + '蘑菇怎么这么少？'
            elif constant.v1 // 7 == 3:
                if constant.food_4_num <= 3:
                    constant.if_null = 1
                    constant.loss = constant.loss + 1
                    constant.no_requirement1 = constant.no_requirement1 + '西红柿怎么这么少？'
            elif constant.v1 // 7 == 4:
                constant.if_null = 1
                if constant.food_1_num + constant.food_2_num + constant.food_3_num + constant.food_4_num <= 5:
                    constant.loss = constant.loss + 1
                    constant.no_requirement1 = constant.no_requirement1 + '蔬菜怎么这么少？'

            if constant.v2 // 7 == 0:
                if constant.food_1_num > 0:
                    constant.if_null = 1
                    constant.loss = constant.loss + 1
                    constant.no_requirement2 = constant.no_requirement2 + '洋葱怎么这么多？'
            elif constant.v2 // 7 == 1:
                if constant.food_2_num > 0:
                    constant.if_null = 1
                    constant.loss = constant.loss + 1
                    constant.no_requirement2 = constant.no_requirement2 + '西蓝花怎么这么多？'
            elif constant.v2 // 7 == 2:
                if constant.food_3_num > 0:
                    constant.if_null = 1
                    constant.loss = constant.loss + 1
                    constant.no_requirement2 = constant.no_requirement2 + '蘑菇怎么这么多？'
            elif constant.v2 // 7 == 3:
                if constant.food_4_num > 0:
                    constant.if_null = 1
                    constant.loss = constant.loss + 1
                    constant.no_requirement2 = constant.no_requirement2 + '西红柿怎么这么多？'
            elif constant.v2 // 7 == 4:
                constant.if_null = 1
                if constant.food_1_num + constant.food_2_num + constant.food_3_num + constant.food_4_num > 0:
                    constant.loss = constant.loss + 1
                    constant.no_requirement2 = constant.no_requirement2 + '为什么有蔬菜？'

            if constant.m1 // 3 == 0:
                if constant.food_5_num <= 3:
                    constant.if_null = 1
                    constant.loss = constant.loss + 1
                    constant.no_requirement3 = constant.no_requirement3 + '虾仁怎么这么少？'
            elif constant.m1 // 3 == 1:
                if constant.food_6_num <= 3:
                    constant.if_null = 1
                    constant.loss = constant.loss + 1
                    constant.no_requirement3 = constant.no_requirement3 + '火腿怎么这么少？'
            elif constant.m1 // 3 == 2:
                if constant.food_7_num <= 3:
                    constant.if_null = 1
                    constant.loss = constant.loss + 1
                    constant.no_requirement3 = constant.no_requirement3 + '培根怎么这么少？'
            elif constant.m1 // 3 == 3:
                if constant.food_5_num + constant.food_6_num + constant.food_7_num <= 5:
                    constant.if_null = 1
                    constant.loss = constant.loss + 1
                    constant.no_requirement3 = constant.no_requirement3 + '肉怎么这么少？'

            if constant.m2 // 3 == 0:
                if constant.food_5_num > 0:
                    constant.if_null = 1
                    constant.loss = constant.loss + 1
                    constant.no_requirement4 = constant.no_requirement4 + '为什么有虾仁？'
            elif constant.m2 // 3 == 1:
                if constant.food_6_num > 0:
                    constant.if_null = 1
                    constant.loss = constant.loss + 1
                    constant.no_requirement4 = constant.no_requirement4 + '为什么有火腿？'
            elif constant.m2 // 3 == 2:
                if constant.food_7_num > 0:
                    constant.if_null = 1
                    constant.loss = constant.loss + 1
                    constant.no_requirement4 = constant.no_requirement4 + '为什么有培根？'
            elif constant.m2 // 3 == 3:
                if constant.food_5_num + constant.food_6_num + constant.food_7_num > 0:
                    constant.if_null = 1
                    constant.loss = constant.loss + 1
                    constant.no_requirement4 = constant.no_requirement4 + '为什么有肉？'
            constant.if_check = 1
            if constant.if_null == 0:
                constant.no_requirement1 = constant.no_requirement1 + '棒极了！真美味！'
                constant.if_null = 1

        if constant.if_guest == 1 and constant.cook == 1:
            if 940 <= x_2_2 <= 1093 and 407 <= y_2_2 <= 440:
                constant.if_guest = 0
                constant.cook = 0
                if num4 == 0:
                    sound = pygame.mixer.Sound('music/ou1.mp3')
                    sound.play()
                    num4 = 1

                constant.float_money = constant.float_money + (
                            30 - constant.cost - constant.loss_p * 0.5 - constant.loss)

                constant.guest_appear_time = 0
                constant.get_guest_no = 0
                constant.cost = 0
                constant.loss = 0
                constant.food_1_num, constant.food_3_num, constant.food_3_num, constant.food_4_num, constant.food_5_num, constant.food_6_num, constant.food_7_num = 0, 0, 0, 0, 0, 0, 0
                constant.v1 = -1
                constant.v2 = -1
                constant.m1 = -1
                constant.m2 = -1
                constant.text1, constant.text2, constant.text3, constant.text4 = '', '', '', ''
                constant.no_requirement1 = ''
                constant.no_requirement2 = ''
                constant.no_requirement3 = ''
                constant.no_requirement4 = ''
                constant.if_check = 0
                constant.loss_p = 0
                constant.if_null = 0

    if constant.game_page == 3:
        if num3 == 0:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("music/page_3.mp3")
            pygame.mixer.music.play(-1)  # -1：循环播放
            num3 = num3 + 1
        constant.guest_patience = constant.guest_patience + 1
        screen.blit(part_3.background_3_3, (0, 0))
        pygame.draw.rect(screen, (250, 235, 215), (0, 90, 1300, 730), 0)
        # 托盘
        screen.blit(part_3.background_3_1, (70, -50))
        # 食材盒
        screen.blit(part_3.background_3_2, (-110, -50))
        screen.blit(part_3.background_3_2, (70, -50))
        screen.blit(part_3.background_3_2, (250, -50))
        screen.blit(part_3.background_3_2, (430, -50))
        screen.blit(part_3.background_3_2, (610, -50))
        screen.blit(part_3.background_3_2, (790, -50))
        screen.blit(part_3.background_3_2, (970, -50))
        screen.blit(part_3.background_3_2, (790, 120))
        screen.blit(part_3.background_3_2, (970, 120))
        screen.blit(part_3.background_3_5, (-230, 10))
        # 食材
        screen.blit(part_3.background_3_7, (25, 280))  # 面团
        # 烤箱
        screen.blit(part_3.background_3_4, (750, 280))
        # 装饰
        screen.blit(part_3.background_3_6, (10, 520))
        # 第一个时间框
        screen.blit(part_2.face_1, (15, 0))
        screen.blit(part_2.background_2_2, (20, 1))  # 小时钟标志
        f_2 = pygame.font.SysFont(['隶书', 'microsoftsansserif'], 21)  # 时间字体格式
        text_contact_1 = "第 " + str(datetime_get.nowadays) + " 天"
        text_1 = f_2.render(text_contact_1, True, (255, 193, 193), None)
        screen.blit(text_1, (70, 0))
        ISOTIMEFORMAT = '%H ：%M'  # 时间格式
        theTime = datetime.datetime.now().strftime(ISOTIMEFORMAT)
        text_2 = f_2.render(theTime, True, (255, 193, 193), None)
        screen.blit(text_2, (70, 19))
        # 第二个顾客耐心度框
        screen.blit(part_2.face_2, (213, 0))
        screen.blit(part_2.background_2_5, (208, -7))
        f_6 = pygame.font.SysFont(['隶书', 'microsoftsansserif'], 32)  # 耐心度字体格式
        text_p_0 = str(100 - constant.guest_patience // 85) + '%'
        text_p = f_6.render(text_p_0, True, (255, 193, 193), None)
        screen.blit(text_p, (260, 2))
        # 第三个完成制作框
        if 830 <= x_3_1 <= 1020 and 0 <= y_3_1 <= 40:
            screen.blit(part_2.face_5, (825, 0))
            f_6 = pygame.font.SysFont(['隶书', 'microsoftsansserif'], 38)  # 结束营业字体格式
            text_4 = f_6.render('完 成 制 作', True, (139, 62, 47), None)
            screen.blit(text_4, (830, 6))
        else:
            screen.blit(part_2.face_3, (832, 0))
            f_5 = pygame.font.SysFont(['隶书', 'microsoftsansserif'], 30)  # 结束营业字体格式
            text_4 = f_5.render('完 成 制 作', True, (255, 193, 193), None)
            screen.blit(text_4, (845, 6))
        # 第四个金额框
        screen.blit(part_2.face_4, (1058, 0))
        screen.blit(part_2.background_2_3, (1065, 0))
        get_money.format_money(constant.float_money)
        f_4 = pygame.font.SysFont(['隶书', 'microsoftsansserif'], 22)
        text_3 = f_4.render(constant.format_money, True, (255, 193, 193), None)
        screen.blit(text_3, (1100, 7))
        # 绘制食材盒食材
        screen.blit(part_3.food_1, (70, 100))
        screen.blit(part_3.food_1, (45, 150))
        screen.blit(part_3.food_1, (65, 150))
        screen.blit(part_3.food_1, (35, 105))
        screen.blit(part_3.food_2, (200, 100))
        screen.blit(part_3.food_2, (245, 140))
        screen.blit(part_3.food_2, (195, 135))
        screen.blit(part_3.food_2, (210, 105))
        screen.blit(part_3.food_2, (245, 95))
        screen.blit(part_3.food_2, (185, 95))
        screen.blit(part_3.food_3, (350, 100))
        screen.blit(part_3.food_3, (370, 100))
        screen.blit(part_3.food_3, (340, 140))
        screen.blit(part_3.food_3, (380, 145))
        screen.blit(part_3.food_3, (400, 105))
        screen.blit(part_3.food_4, (540, 85))
        screen.blit(part_3.food_4, (520, 100))
        screen.blit(part_3.food_4, (570, 90))
        screen.blit(part_3.food_4, (580, 125))
        screen.blit(part_3.food_4, (530, 75))
        screen.blit(part_3.food_4, (515, 120))
        screen.blit(part_3.food_5, (765, 120))
        screen.blit(part_3.food_5, (815, 130))
        screen.blit(part_3.food_5, (820, 155))
        screen.blit(part_3.food_5, (780, 160))
        screen.blit(part_3.food_6, (980, 170))
        screen.blit(part_3.food_6, (970, 150))
        screen.blit(part_3.food_6, (950, 120))
        screen.blit(part_3.food_6, (990, 125))
        screen.blit(part_3.food_6, (945, 180))
        screen.blit(part_3.food_6, (930, 145))
        screen.blit(part_3.food_7, (1130, 5))
        screen.blit(part_3.food_7, (1140, -15))
        screen.blit(part_3.food_7, (1160, -25))
        screen.blit(part_3.food_7, (1130, -45))
        screen.blit(part_3.face_1, (1130, 310))
        screen.blit(part_3.face_2, (950, 310))

        # 放面饼
        if 75 <= x_3_2 <= 280 and 325 <= y_3_2 <= 455 and constant.if_dough == 0:
            constant.if_dough = 1
            constant.cost = constant.cost + 3
            x_3_2 = 0
            y_3_2 = 0
        if constant.if_dough == 1:
            screen.blit(part_3.dough, (290, 170))

        # 放芝士
        if 950 <= x_3_2 <= 1060 and 315 <= y_3_2 <= 400 and constant.if_dough == 1:
            constant.if_sauce_2 = 1
            x_3_2 = 0
            y_3_2 = 0
            constant.cost = constant.cost + 0.6
        if constant.if_sauce_2 == 1 and constant.if_dough == 1:
            pygame.draw.circle(screen, (245, 222, 179), (625, 500), 185, width=0)
        # 番茄酱
        if 1130 <= x_3_2 <= 1240 and 315 <= y_3_2 <= 400 and constant.if_dough == 1:
            constant.if_sauce_1 = 1
            x_3_2 = 0
            y_3_2 = 0
            constant.cost = constant.cost + 0.6
        if constant.if_sauce_1 == 1 and constant.if_dough == 1:
            pygame.draw.circle(screen, (255, 69, 0), (625, 500), 185, width=0)

        # 确认当前所选食材种类
        if constant.if_dough == 1:
            if 130 <= y_3_2 <= 230:
                if 49 <= x_3_2 <= 160:
                    constant.food_kind = 1
                    x_3_2, y_3_2 = 0, 0
                elif 230 <= x_3_2 <= 345:
                    constant.food_kind = 2
                    x_3_2, y_3_2 = 0, 0
                elif 405 <= x_3_2 <= 525:
                    constant.food_kind = 3
                    x_3_2, y_3_2 = 0, 0
                elif 585 <= x_3_2 <= 705:
                    constant.food_kind = 4
                    x_3_2, y_3_2 = 0, 0
                elif 765 <= x_3_2 <= 885:
                    constant.food_kind = 5
                    x_3_2, y_3_2 = 0, 0
                elif 945 <= x_3_2 <= 1065:
                    constant.food_kind = 6
                    x_3_2, y_3_2 = 0, 0
                elif 1125 <= x_3_2 <= 1245:
                    constant.food_kind = 7
                    x_3_2, y_3_2 = 0, 0

        # 获取摆放食材位置
        if constant.food_kind != 0 and math.sqrt((x_3_2 - 625) ** 2 + (y_3_2 - 502) ** 2) <= 225:
            if constant.food_kind == 1:
                constant.a1.append(x_3_2)
                constant.a2.append(y_3_2)
                if num4 == 0:
                    sound = pygame.mixer.Sound('music/ou1.mp3')
                    sound.play()
                    num4 = 1
                x_3_2, y_3_2 = 0, 0
            elif constant.food_kind == 2:
                constant.b1.append(x_3_2)
                constant.b2.append(y_3_2)
                if num4 == 0:
                    sound = pygame.mixer.Sound('music/ou1.mp3')
                    sound.play()
                    num4 = 1
                x_3_2, y_3_2 = 0, 0
            elif constant.food_kind == 3:
                constant.c1.append(x_3_2)
                constant.c2.append(y_3_2)
                if num4 == 0:
                    sound = pygame.mixer.Sound('music/ou1.mp3')
                    sound.play()
                    num4 = 1
                x_3_2, y_3_2 = 0, 0
            elif constant.food_kind == 4:
                constant.d1.append(x_3_2)
                constant.d2.append(y_3_2)
                if num4 == 0:
                    sound = pygame.mixer.Sound('music/ou1.mp3')
                    sound.play()
                    num4 = 1
                x_3_2, y_3_2 = 0, 0
            elif constant.food_kind == 5:
                constant.e1.append(x_3_2)
                constant.e2.append(y_3_2)
                if num4 == 0:
                    sound = pygame.mixer.Sound('music/ou1.mp3')
                    sound.play()
                    num4 = 1
                x_3_2, y_3_2 = 0, 0
            elif constant.food_kind == 6:
                constant.f1.append(x_3_2)
                constant.f2.append(y_3_2)
                if num4 == 0:
                    sound = pygame.mixer.Sound('music/ou1.mp3')
                    sound.play()
                    num4 = 1
                x_3_2, y_3_2 = 0, 0
            elif constant.food_kind == 7:
                constant.g1.append(x_3_2)
                constant.g2.append(y_3_2)
                if num4 == 0:
                    sound = pygame.mixer.Sound('music/ou1.mp3')
                    sound.play()
                    num4 = 1
                x_3_2, y_3_2 = 0, 0
        # 绘制食材
        for i in range(len(constant.a1)):
            screen.blit(part_3.food_1, (constant.a1[i] - 30, constant.a2[i] - 45))
        for i in range(len(constant.b1)):
            screen.blit(part_3.food_2, (constant.b1[i] - 65, constant.b2[i] - 80))
        for i in range(len(constant.c1)):
            screen.blit(part_3.food_3, (constant.c1[i] - 95, constant.c2[i] - 45))
        for i in range(len(constant.d1)):
            screen.blit(part_3.food_4, (constant.d1[i] - 100, constant.d2[i] - 80))
        for i in range(len(constant.e1)):
            screen.blit(part_3.food_5, (constant.e1[i] - 30, constant.e2[i] - 45))
        for i in range(len(constant.f1)):
            screen.blit(part_3.food_6, (constant.f1[i] - 30, constant.f2[i] - 35))
        for i in range(len(constant.g1)):
            screen.blit(part_3.food_7, (constant.g1[i] - 35, constant.g2[i] - 199))
        if constant.food_kind != 0:
            if constant.food_kind == 1:
                screen.blit(part_3.food_1, (x_3_1 - 30, y_3_1 - 45))
            elif constant.food_kind == 2:
                screen.blit(part_3.food_2, (x_3_1 - 65, y_3_1 - 80))
            elif constant.food_kind == 3:
                screen.blit(part_3.food_3, (x_3_1 - 95, y_3_1 - 45))
            elif constant.food_kind == 4:
                screen.blit(part_3.food_4, (x_3_1 - 100, y_3_1 - 80))
            elif constant.food_kind == 5:
                screen.blit(part_3.food_5, (x_3_1 - 30, y_3_1 - 45))
            elif constant.food_kind == 6:
                screen.blit(part_3.food_6, (x_3_1 - 30, y_3_1 - 35))
            elif constant.food_kind == 7:
                screen.blit(part_3.food_7, (x_3_1 - 35, y_3_1 - 199))

        # 触发完成制作事件
        if 835 <= x_3_2 <= 1020 and 0 <= y_3_2 <= 35:
            x_3_2 = 0
            y_3_2 = 0
            num2 = 0
            num4 = 0
            num5 = 0
            constant.cook = 1
            constant.if_dough = 0
            constant.if_sauce_1 = 0
            constant.if_sauce_2 = 0
            constant.game_page = 2
            constant.food_1_num, constant.food_3_num, constant.food_3_num, constant.food_4_num, constant.food_5_num, constant.food_6_num, constant.food_7_num = len(
                constant.a1), len(constant.b1), len(constant.c1), len(constant.d1), len(constant.e1), len(
                constant.f1), len(constant.g1)
            constant.cost = constant.cost + len(constant.a1) * 0.5 + len(constant.b1) * 0.5 + len(
                constant.c1) * 0.4 + len(constant.d1) * 0.3 + len(constant.e1) * 1 + len(constant.f1) * 0.8 + len(
                constant.g1) * 1
            constant.food_kind = 0
            constant.a1, constant.a2, constant.b1, constant.b2, constant.c1, constant.c2, constant.d1, constant.d2, constant.e1, constant.e2, constant.f1, constant.f2, constant.g1, constant.g2 = [], [], [], [], [], [], [], [], [], [], [], [], [], []
            constant.loss_p = constant.guest_patience // 85
            constant.guest_patience = 0

    pygame.display.flip()  # 更新屏幕内容
