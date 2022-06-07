#  用来存放所有常量
game_page = 1
game_state = 1
page1_question = 0
page1_get_question = 0
page1_press_2 = 0
now_money = 0
format_money = ''
if_get_money = 0
float_money = 0.0  # 浮点数形式金额

if_guest = 0  # 是否有客人的标志，1有0无
guest_appear_time = 0  # 用来计时控制客人每隔一段时间出现
get_guest_no = 0  # 用来判断是否已经随机获取了客人序号
guest_patience = 0  # 顾客耐心程度

cost = 0  # 披萨成本: 面团3r，酱料0.6r，洋葱0.5r，西蓝花0.5r，蘑菇0.4r，西红柿0.3r，虾仁1r，火腿0.8r，培根1r
food_kind = 0  # 记录当前所用原材料编号
if_dough = 0  # 判断目前是否已有面饼
if_sauce_1 = 0  # 判断是否已经放置番茄酱料 (255, 69, 0)
if_sauce_2 = 0  # 判断是否已经放置芝士酱料

loss = 0  # 用来扣除没有满足要求的金额

food_1_num = 0
food_2_num = 0
food_3_num = 0
food_4_num = 0
food_5_num = 0
food_6_num = 0
food_7_num = 0

a1 = []
a2 = []
b1 = []
b2 = []
c1 = []
c2 = []
d1 = []
d2 = []
e1 = []
e2 = []
f1 = []
f2 = []
g1 = []
g2 = []

v1 = -1  # 多菜
v2 = -1  # 少菜
m1 = -1  # 多肉
m2 = -1  # 少肉
text1, text2, text3, text4 = '', '', '', ''
cook = 0  # 做披萨的状态,1表示制作完成

no_requirement1 = ''
no_requirement2 = ''
no_requirement3 = ''
no_requirement4 = ''


if_check = 0  # 用来保证只对做出的披萨进行一次判断
if_null = 0
loss_p = 0