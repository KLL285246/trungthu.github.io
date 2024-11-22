import turtle
from PIL import Image
import time
import pygame
from pygame.locals import *
import math

# init pygame
pygame.init()
screen = pygame.display.set_mode((700, 800))
pygame.display.set_caption("VỢ YÊU CỦA ANH")

# color
BLACK = (0, 0, 0)
PINK = (255, 102, 255)
PINK_T = (238, 204, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

#font
font = pygame.font.Font("5.ttf", 120)
font1 = pygame.font.Font("2.ttf", 25)
#text
text_ready = font.render("READY", True, PINK)
text_go = font.render("GO", True, PINK)
#text_chuc = ["TRUNG", "THU", "15-08", "ANH", "YEU", "VO", "NHAT", "TREN", "DOI"]
text_tt = ["  TREN DOI", " NHAT NHAT", "VO DE THUONG", " CHONG YEU", " VUI VE NHAT", "HANH PHUC","VO XINH DEP", "CHONG CHUC", " 15 -08- 2024", " TRUNG THU"]
text_end = font1.render("I LOVE YOU", True, WHITE)

#images
bgtime = pygame.image.load("loan.jpg").convert()
bgtt = pygame.image.load("bgtt.jpg").convert()

#sound
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
sound_pygame = pygame.mixer.Sound("musictt.mp3")
sound_end = pygame.mixer.Sound("TrungThu.mp3")

# variable
running1 = True
running2 = True

#dem nguoc
clock = pygame.time.Clock()
counter = 7
text = font.render(str(counter), True, PINK)
time_deplay = 1000
time_event = pygame.USEREVENT + 1
pygame.time.set_timer(time_event, time_deplay)

# screen delay
while running1:
    clock.tick(60)
    #background 
    screen.blit(bgtime, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == time_event:
            counter -= 1
            text = font.render(str(counter), True, PINK)

    #draw text
    if counter <= 3 and counter >= 0:
        text_rect = text.get_rect(center = screen.get_rect().center)
        screen.blit(text, text_rect)

    #end
    if counter == -3:
        running1 = False
    elif counter == -2:
        screen.blit(text_go, (270, 300))
    elif counter == -1:
        screen.blit(text_ready, (150, 300))

    pygame.display.flip()

sound_pygame.play()
# dem nguoc 20
count = 20

# Hàm vẽ trái tim sử dụng phương trình parametric
def draw_heart(surface, center_x, center_y, size):
    points = []
    
    # Lặp qua các giá trị của t từ 0 đến 2 * pi để tạo hình trái tim
    for t in range(0, 360):
        # Chuyển đổi từ độ sang radian
        t_rad = math.radians(t)

        # Công thức parametric của hình trái tim
        x = 16 * math.sin(t_rad) ** 3
        y = 13 * math.cos(t_rad) - 5 * math.cos(2 * t_rad) - 2 * math.cos(3 * t_rad) - math.cos(4 * t_rad)

        # Nhân với kích thước và dịch chuyển tâm đến vị trí mong muốn
        x *= size
        y *= size

        # Chuyển đổi tọa độ để phù hợp với cửa sổ Pygame
        x += center_x
        y = center_y - y

        # Thêm điểm vào danh sách
        points.append((x, y))
    
    # Vẽ trái tim bằng cách nối các điểm
    pygame.draw.polygon(surface, RED, points)

# Hàm vẽ hình trái tim nhỏ
def draw_small_heart(surface, color, center, size):
    for angle in range(0, 360, 1):
        t = math.radians(angle)
        x = 16 * math.sin(t)**3
        y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
        x *= size / 32  # Chỉnh kích thước trái tim nhỏ
        y *= size / 32
        pygame.draw.circle(surface, color, (int(center[0] + x), int(center[1] - y)), 2)

small_hearts_posv = [(250, 250), (450, 250), (450, 550), (250, 550)]
small_hearts_post = [(150, 150), (550, 150), (150, 650), (550, 650)]
small_hearts_posg = [(350, 100), (600, 400), (350, 700), (100, 400)]
small_hearts_posn = [(100, 100), (600, 100), (600, 700), (100, 700)]

def draw_heart_pos(surface, color, small_heart_pos, size):
        for pos in small_heart_pos:
            draw_small_heart(surface, color, pos, size)
# screen trung thu
while running2:
    clock.tick(60)
    #background
    screen.blit(bgtt, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running2 = False
        if event.type == time_event:
            count -= 1
            if count <= -1 and count >= -10:
                text_temp = font1.render(text_tt[count], True, WHITE) 
               
    if count == -30: 
        running2 = False
    if count <= 15:
        draw_heart(screen, 350, 400, 5)
    if count <= -1 and count >= -10:
        screen.blit(text_temp, (290, 390))
    if count <= -11 :
        screen.blit(text_end, (303, 390))

    # Vẽ các hình trái tim nhỏ xung quanh làm viền
    if count > 5:
        if count <= 13:
            draw_heart_pos(screen, PINK, small_hearts_posg, 50)
        if count <= 11:
            draw_heart_pos(screen, PINK, small_hearts_posv, 50)
        if count <= 9:
            draw_heart_pos(screen, PINK, small_hearts_post, 50)
        if count <= 7:
            draw_heart_pos(screen, PINK, small_hearts_posn, 50)
    else:
        if count % 2:
            draw_heart_pos(screen, RED, small_hearts_posn, 50)
            draw_heart_pos(screen, RED, small_hearts_post, 50)
            draw_heart_pos(screen, RED, small_hearts_posv, 50)
            draw_heart_pos(screen, RED, small_hearts_posg, 50)
        else : 
            draw_heart_pos(screen, PINK, small_hearts_posn, 50)
            draw_heart_pos(screen, PINK, small_hearts_post, 50)
            draw_heart_pos(screen, PINK, small_hearts_posv, 50)
            draw_heart_pos(screen, PINK, small_hearts_posg, 50)

    # Cập nhật màn hình
    pygame.display.flip()

    pygame.display.update()

pygame.quit()

# screen draw turtle
window = turtle.Screen()
window.bgcolor("#ecc7f0")
window.title("VỢ YÊU CỦA ANH")

# Tạo nhạc
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)
pygame.init()
sound_turtle = pygame.mixer.Sound("ghequa.wav")
pygame.mixer.Sound.play(sound_turtle)


# Khởi tạo Turtle
t = turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()

t._color('PINK_T')  # Đặt màu nền hồng

# Thay đổi màu nét trái tim 0
t.speed(2)
t.pencolor('pink')
t.goto(-310, -250)
t.pencolor('RED')
t.goto(-310, 50)

# Thay đổi màu nét trái tim 1 
t1.speed(2)
t1.pencolor('pink')
t1.goto(310, -250)
t1.pencolor('RED')
t1.goto(310, 50)

def drawHeart(turtle_object): 
    turtle_object.begin_fill()
    turtle_object.fillcolor('RED')
    turtle_object.left(45)
    turtle_object.forward(100)
    turtle_object.circle(50, 180)
    turtle_object.right(90)
    turtle_object.circle(50, 180)
    turtle_object.forward(100)
    turtle_object.end_fill()
     

for i in range(4):
    drawHeart(t)
    drawHeart(t1)
    t.right(45)
    t1.right(45)

# Thay đổi màu nét trái tim 2
t2.speed(2)
t2.pencolor('pink')
t2.goto(0, -100)
t2.pencolor('RED')
t2.goto(0, 230)

for i in range(4):
    drawHeart(t2)
    t2.right(45)


t.penup()
t.goto(-310, 60)  
t.pendown()
t.color("pink")
t.write("EM YÊU", align="center", font=("2.ttf", 12, "bold"))

t1.penup()
t1.goto(310, 60)  
t1.pendown()
t1.color("pink")
t1.write("CUC CƯNG BÉ BỎNG", align="center", font=("2.ttf", 12, "bold"))

t2.penup()
t2.goto(0, 240)  
t2.pendown()
t2.color("pink")
t2.write("VỢ YÊU", align="center", font=("2.ttf", 12, "bold"))

time.sleep(1)

t.penup()
t.goto(-310, 40)  
t.pendown()
t.color("pink")
t.write("PHAN THỊ KIM LOAN", align="center", font=("2.ttf", 12, "bold"))

t1.penup()
t1.goto(310, 40)  
t1.pendown()
t1.color("pink")
t1.write("PHAN THỊ KIM LOAN", align="center", font=("2.ttf", 12, "bold"))

t2.penup()
t2.goto(0, 220)  
t2.pendown()
t2.color("pink")
t2.write("PHAN THỊ KIM LOAN", align="center", font=("2.ttf", 12, "bold"))

time.sleep(1)

t2.penup()
t2.goto(0, -135)  
t2.pendown()
t2.color('RED')
t2.write("HÔM NAY LÀ TRUNG THU 15 -08 - 2024 NÈ VỢ YÊU", align="center", font=("5.ttf", 12, "bold"))

time.sleep(1)

t2.penup()
t2.goto(0, -155)  
t2.pendown()
t2.color('RED')
t2.write("ANH CÙNG VỢ ĐÓN TRUNG THU NHA VỢ YÊU", align="center", font=("5.ttf", 12, "bold"))

time.sleep(1)

t2.penup()
t2.goto(0, -175)  
t2.pendown()
t2.color('RED')
t2.write("CHỒNG CHÚC VỢ YÊU LUÔN CÓ SỨC KHỎE TỐT, TRÍ TUỆ CAO", align="center", font=("5.ttf", 12, "bold"))

time.sleep(1)

t2.penup()
t2.goto(0, -195)  
t2.pendown()
t2.color('RED')
t2.write("LUÔN VUI TƯƠI, YÊU ĐỜI, HẠNH PHÚC VÀ MÃI TƯƠI CƯỜI", align="center", font=("5.ttf", 12, "bold"))

time.sleep(1)

t2.penup()
t2.goto(0, -215)  
t2.pendown()
t2.color('RED')
t2.write("HỌC TẬP TỐT VÀ CỐ GẮNG CHO TƯƠNG LAI CỦA CHÚNG TA", align="center", font=("5.ttf", 12, "bold"))

time.sleep(1)

t2.penup()
t2.goto(0, -235)  
t2.pendown()
t2.color('RED')
t2.write("ANH YÊU VÀ THƯƠNG VỢ NHIỀU LẮM LUÔN ĐÓ", align="center", font=("5.ttf", 12, "bold"))

time.sleep(1)

t2.penup()
t2.goto(0, -255)  
t2.pendown()
t2.color('RED')
t2.write("VỢ CŨNG NHỚ YÊU VÀ THƯƠNG ANH NỮA NHA", align="center", font=("5.ttf", 12, "bold"))

time.sleep(1)

t2.penup()
t2.goto(0, -275)  
t2.pendown()
t2.color('RED')
t2.write("CHỒNG SẼ MÃI BÊN VỢ, YÊU THƯƠNG, QUAN TÂM, CHĂM SÓC VÀ BẢO VỆ VỢ YÊU", align="center", font=("5.ttf", 12, "bold"))

time.sleep(1)

t2.penup()
t2.goto(0, -295)  
t2.pendown()
t2.color('RED')
t2.write("CẢM ƠN VỢ YÊU ĐÃ ĐẾN BÊN ANH VÀ CHO ANH MỘT CUỘC ĐỜI TRỌN VẸN", align="center", font=("5.ttf", 12, "bold"))

time.sleep(1)

t2.penup()
t2.goto(0, -315)  
t2.pendown()
t2.color('RED')
t2.write("CHỒNG SẼ MÃI YÊU VỢ, MÃI MÃI, KHÔNG BAO GIỜ RỜI XA", align="center", font=("5.ttf", 12, "bold"))

time.sleep(1)


t2.pencolor("pink")
t2.goto(0, -392)
t2.pencolor("blue")
t2.goto(470, -392)
t2.goto(470, 400)
t2.goto(-470, 400)
t2.goto(-470, -392)
t2.goto(0, -392)

time.sleep(2)

pygame.mixer.Sound.play(sound_end)
# Đóng cửa sổ Turtle
turtle.done()
