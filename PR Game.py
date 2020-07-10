импорт  pygame
импорт  случайный
импортировать  numpy  как  np
импорт  пятоги
# import imutils
импорт  cv2
импорт  ОС
# import sys

ОС .environ ['SDL_VIDEO_WINDOW_POS'] =  '0,30'

pygame.init()

display_width = 800
display_height = 600

дисплей  =  pygame .дисплей .set_mode ((display_width, display_height))
pygame.дисплей .set_caption ('Run!')

plat_width = 100
plat_height = 20
plat_x  =  display_width  / /  1
plat_y  =  display_height  / /  1.2

centr_plat_x  =  plat_x  +  plat_width / / 2
centr_plat_y  =  plat_y  +  plat_height / / 2
centr_plat  = (centr_plat_x, centr_plat_y)


ball_x  =  display_width  / /  2
ball_y  =  display_height  / /  2
ball_speed_x  =  случайный .рэндрэндж ( 15, 20)
ball_speed_y  =  случайный .рэндрэндж ( 15, 20)

centr_ball_x = ball_x + 10
centr_ball_y = plat_y + 10
centr_ball  = (centr_ball_x, centr_ball_y)


часы  =  pygame .- пора .Часы()


# image = pyautogui.скриншот (регион=(0, 0, 1600, 900))
# image = cv2.cvtColor(np.массив (изображение), cv2.COLOR_RGB2BGR)
# cv2.imshow ('скриншот', imutils.изменить размер (изображение, ширина=600))
# cv2.imwrite ('pic.png', изображение)

def run_game():
    global  plat_x, centr_plat, centr_ball

    hsv_min = np.массив ((0, 54, 5), np .uint8)
    hsv_max = np.массив ((187, 255, 253), np .uint8)
    hsv_min1 = np.массив ((0, 77, 17), np .uint8)
    hsv_max1 = np.массив ((208, 255, 255), np .uint8)
    игра  =  True

    человек  =  ложь

    пока  играем:

        для  мероприятия  в  pygame .событие .получить():
            если  событие .тип  = =  pygame .Выходим:
                pygame.выходим()
                выходим()

        ключи  =  pygame .- ключ .get_pressed()

        если  ключи [ pygame .K_LEFT]:
            если  plat_x >= >  0:
                plat_x  - =  10
        Элиф  ключи [ pygame .K_RIGHT]:
            если  plat_x < =  700:
                plat_x += 10

        если  ball_x <=  plat_x  +  plat_width  +  8  и  ball_x >=>  plat_x  и  ball_y <=  plat_y  +  plat_height  +  8  и  ball_y >=>  plat_y - 7:
            выходим()

        дисплей .заполнить ((255, 255, 255))

        pygame.ничья .рект (дисплей , ( 0 , 255 , 0 ), ( plat_x, plat_y, plat_width, plat_height))
        pygame.ничья .круг ( дисплей , ( 0 , 0 , 255 ), ( ball_x, ball_y ), 10)
        ball_move()
        pygame.дисплей .обновление()
        - часы .ТИК ( 60)

        image = pyautogui.скриншот (регион = (0, 30, 800, 600))
        изображение  =  cv2 .cvtColor(np.массив (изображение), cv2 .COLOR_RGB2BGR)
    
        cv2.imwrite ('изображение.jpg', изображение)

        fn  =  ' изображение.jpg'  
        img = cv2.imread(fn)

        ВПГ  =  cv2 .cvtColor ( img, cv2 .COLOR_BGR2HSV) 
        thresh = cv2.inRange(hsv, hsv_min, hsv_max) 
        контуры 0, иерархия  =  cv2 .findContours ( молотилка .copy(), cv2.RETR_TREE, cv2 .CHAIN_APPROX_SIMPLE)

        
        для  УНТ  в  контурах 0:
            rect = cv2.minAreaRect(cnt) 
            коробка  =  cv2 .boxPoints(rect) 
            box = np.int0(box) 
            area = int(rect[1][0] * rect[1][1]) 
            если  область > >  1880:
                cv2.drawContours(img, [box], 0, (255, 0, 0), 2)
               
                centr_plat_x  =  box [ 0 ][ 0 ] - (box [ 0 ][ 0 ] -  box [ 1 ][ 0 ]) //  2
                centr_plat_y  =  box [ 0 ][ 1 ] - (box [ 0 ][ 1 ] -  box [ 2 ][ 1 ]) //  2
                centr_plat  = (centr_plat_x, centr_plat_y)
                # print(centr_plat)
                прямоугольник  = []
            если  len (cnt) > >  30:
                эллипс  =  cv2 .fitEllipse (cnt)
                centr_ball  =  эллипс [ 0]
                cv2.эллипс ( img, ellipse , ( 255 , 0 , 0 ), 2)
                # print(centr_ball)

            если  abs (centr_plat [ 0 ] -  centr_ball [ 0 ]) <  200  и  abs (centr_plat [ 1 ] -  centr_ball [ 1 ]) <  200:
                если  centr_ball [ 0 ] > >  700  и  centr_plat [ 0 ] > >  700:
                    plat_x  - =  1
                elif  centr_ball [0 ] <  100  и  centr_plat [0 ] <  100:
                    plat_x += 1
                если  centr_ball [ 0 ] -  centr_plat [ 0 ] > >  - 100  и  centr_ball [ 0 ] -  centr_plat [0 ] <  0:
                    если  plat_x < =  700:
                        plat_x += 1
                elif  centr_ball [ 0 ] -  centr_plat [0 ] <  100  и  centr_ball [ 0 ] -  centr_plat [0] > >  0:
                    если  plat_x >= >  0:
                        plat_x  - =  1
            elif plat_x < display_width // 2 - 70:
                plat_x += 1
            elif  plat_x > >  display_width  / /  2:
                plat_x  - =  1

        #cv2.waitKey()
        cv2.destroyAllWindows()

def ball_move():
    глобальный  ball_speed_x, ball_speed_y, ball_x, ball_y
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    если  ball_y < =  10  или  ball_y >=>  595:
        ball_speed_y = -ball_speed_y
    если  ball_x <=  0  или  ball_x >= >  790:
        ball_speed_x = -ball_speed_x

run_game()