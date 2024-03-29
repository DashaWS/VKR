#-*- coding:utf-8 -*-
import arcade
import os
import tkinter as tk

# Включение и отключение вывода отладочных сообщений
DEBUG = True

# Основной класс окна, в котором все рисуется
class TApp(arcade.Window):
    """ Основной класс приложения """
    def __init__(self, fs=False):
        """ Конструктор """

        # Заголовок окна
        self.title = "EmoDetect"
        self.subtitle = "Диагностика эмоционального развития"

        # Получаем реальные размеры экрана
        root = tk.Tk()
        self.SCREEN_WIDTH = root.winfo_screenwidth()
        #print(root.winfo_screenwidth())
        self.SCREEN_HEIGHT = root.winfo_screenheight()
        #print(root.winfo_screenheight())
        del root

        # Параметры масштабирования
        self.SPRITE_SCALING = 0.1
        self.VIEWPORT_MARGIN = 40

        # Открываем окно
        super().__init__(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.title, fullscreen=fs)

        # Устанавливаем рабочий каталог, где по умолчанию будут находится файлы
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Получаем размеры окна и устанавливаем окно просмотра равным этому окну приложения
        width, height = self.get_size()
        print(width, height)
        self.set_viewport(0, width, 0, height)

    def setup(self):
        """ Установка основных параметров. """
        self.setPaths()
        self.setUserVars()
        self.setFonts()
        self.setColors()
        self.setMenu()
        self.mouseX = 0
        self.mouseY = 0
        self.isMouseDown = False
        self.loadAvatars()
        self.setAbout()

    def setPaths(self):
        """ Задаем пути к ресурсам """
        self.imgPath = "images/"
        self.logoPath = self.imgPath + "logo/"
        self.avatarPath = self.imgPath+"avatars/"
        self.cardPath = self.imgPath+"cards/"
        self.detectivePath = self.imgPath+"cards/detective/"
        self.detectivePath1=self.detectivePath+"1/"
        self.detectivePath2=self.detectivePath+"2/"
        self.detectivePath3=self.detectivePath+"card/"
        self.detectivePath4=self.detectivePath+"3/"
        self.detectivePath5=self.detectivePath+"4/"
        self.soundPath = "sounds/"
        self.fontPath = "fonts/"
        self.savePath = "save"

    def setUserVars(self):
        """ Переменные описывающие состояние пользователя """
        # Номер аватара, который выбрал пользователь
        self.userAvatar = 0
        # Количество правильных ответов
        self.userGoodAnswers = 0
        print(self.userGoodAnswers, self.userAvatar)
        # Количество не правильных ответов
        self.userBadAnswers = 0
        #Номер выбранного набора карточек
        self.userChoiceCards = 0

    def setAbout(self):
        self.aboutDescription1 = "Программа предназначена для"
        self.aboutDescription2 = "диагностики психологических особенностей детей"
        self.aboutClient1 = "Гобу Мурманской области центр психолого-педагогической,"
        self.aboutClient2 = "медицинской и социальной помощи"
        self.aboutClient3 = "о заказчике 3"
        self.aboutDeveloper1 = "Дарья Сумина (студентка 4 курса, группа МКН)"
        self.aboutDeveloper2 = "Олег Иванович Ляш (руководитель)"
        #self.aboutLogo1 = arcade.Sprite(self.logoPath + "magu-masu_logo 06_white.png", 1)
        self.aboutLogo2 = arcade.Sprite(self.detectivePath4 + "1.jpg",0.6)
        self.aboutLogo1 = arcade.Sprite(self.logoPath + "cmmpk_MO.png", 0.4)

    def setFonts(self):
        # шрифты отсюда https://fonts.google.com/?selection.family=Russo+One&subset=cyrillic&sort=popularity
        self.font_title=self.fontPath+"RussoOne-Regular.ttf"
        self.font = self.fontPath+"Roboto-Black.ttf"

    def setColors(self):
        """ Задаем основные цвета """
        # Цвет фона
        self.bgcolor = arcade.color.BROWN
        # Цвет текста заголовка
        self.titlecolor = arcade.color.WHITE
        # Цвет текста подзаголовка
        self.subtitlecolor = arcade.color.LIGHT_GRAY
        # Цвет текста пункта меню
        self.menucolor = arcade.color.LIGHT_GRAY
        # Цвет текста выбранного пункта меню
        self.menucolorselected = arcade.color.YELLOW
        # Задаем фоновый цвет
        arcade.set_background_color(self.bgcolor)

    def setMenu(self):
        print('2')
        # Переменная состояния приложения
        # Если = 0, то выводится начальный экран
        self.state = 0
        self.state1=99
        # Словарь для хранения пунктов меню
        self.Menu = {}
        # Первый из отображаемых элементов меню
        self.MenuFirst = 1
        # Последний из отображаемых пунктов меню
        self.MenuLast = 5
        # Собственно сами пункты меню
        self.Menu[0] = "Стартовое меню"
        self.Menu[1] = "Выбор набора карточек"
        self.Menu[2] = "Выбор аватара"
        self.Menu[3] = "Начать"
        self.Menu[4] = "О программе"
        self.Menu[5] = "Выход"
        self.Menu[6] = "Игра Детектив"
        self.Menu[7] = "Игра Подбери маску"
        self.Menu[8] = "Игра Пятнашки"
        self.Menu[9] = "Дальше"
        self.Menu[10] = "Игра Детектив"
        self.Menu[11] = "Игра Детектив"
       
        self.Menu[99] = "Пауза"

    def loadAvatars(self):
        """ Загрузка ававтаров """
        files = os.listdir(self.avatarPath)

        self.imgAvatars = arcade.SpriteList()

        for i in files:
            self.imgAvatar = arcade.Sprite(self.avatarPath+i, 1)
            self.imgAvatar.width = 100
            self.imgAvatar.height = 100
            self.imgAvatar.center_x = 0
            self.imgAvatar.center_y = 0
            self.imgAvatars.append(self.imgAvatar)

    def on_draw(self):
        """ Рендерем экран """
        arcade.start_render()
        if self.state == 0:
            # Рисуем менюшку стартовую менюшку
            self.drawState0()
        elif self.state == 1:
            # Рисуем выбор набора карточек
            self.drawState1()
        elif self.state == 2:
            # Рисуем выбор аватара
            self.drawState2()
        elif self.state == 3:
            # Рисуем меню игр
            self.drawState3()
        elif self.state == 4:
            # Рисуем о программе
            self.drawState4()
        elif self.state == 6:
            # Рисуем игру Детектив
            self.drawState6()
        elif self.state == 7:
            # Рисуем игру Подбери маску
            self.drawState7()
        elif self.state == 8:
            # Рисуем игру Пятнашки
            self.drawState8()
        elif self.state == 9:
            # Рисуем сл игру
            self.drawState9()
        elif self.state == 10:
            # Рисуем сл игру
            self.drawState10()
        elif self.state == 11:
            # Рисуем сл игру
            self.drawState7()
        elif self.state == 5:
            # Выход
            try:
                quit()
            except:
                pass

        #if DEBUG:
            #arcade.draw_line(0,self.mouseY,self.SCREEN_WIDTH,self.mouseY,arcade.color.RED)
            #arcade.draw_line(self.mouseX, 0, self.mouseX, self.SCREEN_HEIGHT, arcade.color.RED)
            #print(self.MenuItemSelected, self.width)
            

    def drawState0(self):
        # Рисуем название программы (заголовок)
        text = self.title
        color = self.titlecolor
        text_size = 22
        x = self.SCREEN_WIDTH // 2.3
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 6
        #print(y)
        arcade.draw_text(text, x, y, color, text_size, anchor_y = "center", font_name = self.font_title)
        # Рисуем Описание программы (подзаголовок)
        text = self.subtitle
        color = self.subtitlecolor
        text_size = 30
        x = self.SCREEN_WIDTH // 3.6
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 4
        #print(x,y)
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)
        #
        self.drawMenu()
        self.imgAvatars.sprite_list[self.userAvatar].center_x = self.imgAvatars.sprite_list[self.userAvatar].width
        self.imgAvatars.sprite_list[self.userAvatar].center_y = self.SCREEN_HEIGHT - self.imgAvatars.sprite_list[self.userAvatar].height
        self.imgAvatars.sprite_list[self.userAvatar].draw()

    def drawState1(self):
        # Выбор набора карточек
        text = "Выбор набора карточек"
        color = self.titlecolor
        text_size = 44
        x = self.SCREEN_WIDTH // 3
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 6
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)

        self.imgAvatars.sprite_list[self.userAvatar].center_x = self.imgAvatars.sprite_list[self.userAvatar].width
        self.imgAvatars.sprite_list[self.userAvatar].center_y = self.SCREEN_HEIGHT - self.imgAvatars.sprite_list[self.userAvatar].height
        self.imgAvatars.sprite_list[self.userAvatar].draw()

        """ Загрузка картинок """
        files1 = os.listdir(self.detectivePath3)

        self.imgCards1 = arcade.SpriteList()
        

        for i in files1:
            self.imgCard1 = arcade.Sprite(self.detectivePath3+i, 1)
            self.imgCard1.width = 100
            self.imgCard1.height = 200
            self.imgCard1.center_x = 0
            self.imgCard1.center_y = 0
            self.imgCards1.append(self.imgCard1)

        # Вывод конкретного спрайта
        w=self.imgCards1.sprite_list[1].width
        h=self.imgCards1.sprite_list[1].height
        counter = 2
        s = 20
        x = self.SCREEN_WIDTH // 2 - (counter * w) //2.3
        y = self.SCREEN_HEIGHT // 2
        for i in range(0,len(self.imgCards1.sprite_list)):
            self.imgCards1.sprite_list[i].center_x = x
            x += w + s
            self.imgCards1.sprite_list[i].center_y = y
            counter -=1
            if counter <=0:
                counter = 5
                x = self.SCREEN_WIDTH // 2 - (counter * w) // 2.9
                y += h + s

            self.imgCards1.sprite_list[i].draw()
            # Определяем попадание курсора на набор карточек
            bottom =self.mouseY > self.imgCards1.sprite_list[i].center_y - self.imgCards1.sprite_list[i].height // 2
            top = self.mouseY < self.imgCards1.sprite_list[i].center_y + self.imgCards1.sprite_list[i].height // 2

            left = self.mouseX > self.imgCards1.sprite_list[i].center_x - self.imgCards1.sprite_list[i].width // 2
            right = self.mouseX < self.imgCards1.sprite_list[i].center_x + self.imgCards1.sprite_list[i].width // 2

            if (bottom and top) and (left and right):
                arcade.draw_rectangle_outline(self.imgCards1.sprite_list[i].center_x,self.imgCards1.sprite_list[i].center_y,self.imgCards1.sprite_list[i].width,self.imgCards1.sprite_list[i].height,color=arcade.color.RED)
                if self.isMouseDown:
                    self.userChoiceCards=i
                    #otvet=i
                    """if i==0:
                        print('dthyj')
                        self.userGoodAnswers+=1
                        print(self.userGoodAnswers)
                    else:
                        print('----')
                        self.userBadAnswers+=1
                        print(self.userBadAnswers)"""
                    #self.userAvatar = i
        #print(self.userChoiceCards)
        

    def drawState2(self):
        # Выбор аватара
        text = "Выбор аватара"
        color = self.titlecolor
        text_size = 44
        x = self.SCREEN_WIDTH // 3
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 6
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)

        #self.imgAvatars.draw()
        # Вывод конкретного спрайта
        w=self.imgAvatars.sprite_list[1].width
        h=self.imgAvatars.sprite_list[1].height
        counter = 4
        s = 20
        x = self.SCREEN_WIDTH // 2 - (counter * w) //2
        y = self.SCREEN_HEIGHT // 2
        for i in range(0,len(self.imgAvatars.sprite_list)-1):
            self.imgAvatars.sprite_list[i].center_x = x
            x += w + s
            self.imgAvatars.sprite_list[i].center_y = y
            counter -=1
            if counter <=0:
                counter = 4
                x = self.SCREEN_WIDTH // 2 - (counter * w) // 2
                y += h + s

            self.imgAvatars.sprite_list[i].draw()
            # Определяем попадание курсора на аватар
            bottom =self.mouseY > self.imgAvatars.sprite_list[i].center_y - self.imgAvatars.sprite_list[i].height // 2
            top = self.mouseY < self.imgAvatars.sprite_list[i].center_y + self.imgAvatars.sprite_list[i].height // 2

            left = self.mouseX > self.imgAvatars.sprite_list[i].center_x - self.imgAvatars.sprite_list[i].width // 2
            right = self.mouseX < self.imgAvatars.sprite_list[i].center_x + self.imgAvatars.sprite_list[i].width // 2

            if (bottom and top) and (left and right):
                arcade.draw_rectangle_outline(self.imgAvatars.sprite_list[i].center_x,self.imgAvatars.sprite_list[i].center_y,self.imgAvatars.sprite_list[i].width,self.imgAvatars.sprite_list[i].height,color=arcade.color.RED)
                if self.isMouseDown:
                    self.userAvatar = i

        # self.imgAvatars.sprite_list[self.userAvatar].center_x = 500
        # self.imgAvatars.sprite_list[self.userAvatar].center_y = 500
        # self.imgAvatars.sprite_list[self.userAvatar].draw()

    def drawState3(self):
        # Начать
        text = "Выбор игры"
        color = self.titlecolor
        text_size = 44
        x = self.SCREEN_WIDTH // 2.7
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 6
        arcade.draw_text(text, x, y, color, text_size, anchor_y = "center",font_name = self.font_title)
        self.setMenu1()
        self.drawMenu1()

        self.imgAvatars.sprite_list[self.userAvatar].center_x = self.imgAvatars.sprite_list[self.userAvatar].width
        self.imgAvatars.sprite_list[self.userAvatar].center_y = self.SCREEN_HEIGHT - self.imgAvatars.sprite_list[self.userAvatar].height
        self.imgAvatars.sprite_list[self.userAvatar].draw()

    def setMenu1(self):
        # Переменная состояния приложения
        # Если = 0, то выводится начальный экран
        #self.state = 3
        # Словарь для хранения пунктов меню
        #self.Menu1 = {}
        # Первый из отображаемых элементов меню
        self.MenuFirst1 = 6
        # Последний из отображаемых пунктов меню
        self.MenuLastii = 3
        # Собственно сами пункты меню
        #self.Menu[6] = "Игра Детектив"
        #self.Menu[7] = "Игра Подбери маску"
        #self.Menu[8] = "Игра Пятнашки"

    def drawMenu1(self):
        """ Рисуем менюшку игры """
        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15
        self.MenuItemSelected_1 = -1

        for i in range(0,self.MenuLastii):
            text = self.Menu[self.MenuFirst1+i]
            text_size = 35
            x = self.SCREEN_WIDTH // 2.7
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 3 - 20 - i*40
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.MenuItemSelected = self.MenuFirst1+i
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, anchor_y = "center",font_name = self.font_title)

    def drawState4(self):
        # О программе
        x = self.SCREEN_WIDTH // 2.5
        lineHeight = 50
        # ------------------------
        text = "О программе"
        color = self.titlecolor
        text_size = 44
        y = self.SCREEN_HEIGHT  - 2*lineHeight
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)

        text =  self.aboutDescription1
        color = self.subtitlecolor
        text_size = 20
        x = self.SCREEN_WIDTH // 2.6
        y = self.SCREEN_HEIGHT  - 3*lineHeight
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font)

        text =  self.aboutDescription2
        color = self.subtitlecolor
        text_size = 20
        x = self.SCREEN_WIDTH // 3.4
        y = self.SCREEN_HEIGHT  - 4*lineHeight
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font)

        # ------------------------
        text = "Заказчик:"
        color = self.titlecolor
        text_size = 20
        x = self.SCREEN_WIDTH // 2.2
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 3
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font)

        text = self.aboutClient1
        color = self.subtitlecolor
        text_size = 20
        x = self.SCREEN_WIDTH // 3.9
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 3 - 40
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font)

        text = self.aboutClient2
        color = self.subtitlecolor
        text_size = 20
        x = self.SCREEN_WIDTH // 2.9
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 3 - 80
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font)

        #------------------------
        text = "Разработчики: "
        color = self.titlecolor
        text_size = 20
        x = self.SCREEN_WIDTH // 2.3
        y = self.SCREEN_HEIGHT - self.SCREEN_HEIGHT // 2
        arcade.draw_text(text, x, y, color, text_size, anchor_y="center", font_name=self.font)

        text = self.aboutDeveloper1
        color = self.subtitlecolor
        text_size = 20
        x = self.SCREEN_WIDTH // 3.1
        y = self.SCREEN_HEIGHT - self.SCREEN_HEIGHT // 2 - 40
        arcade.draw_text(text, x, y, color, text_size,  anchor_y="center", font_name=self.font)

        text = self.aboutDeveloper2
        color = self.subtitlecolor
        text_size = 20
        x = self.SCREEN_WIDTH // 2.8
        y = self.SCREEN_HEIGHT - self.SCREEN_HEIGHT // 2 - 80
        arcade.draw_text(text, x, y, color, text_size, anchor_y="center", font_name=self.font)

        '''self.aboutLogo1.center_x = (self.SCREEN_WIDTH // 2) // 2
        self.aboutLogo1.center_y = 10 + self.aboutLogo2.height
        self.aboutLogo1.draw()

        self.aboutLogo2.center_x = (self.SCREEN_WIDTH // 2) + (self.SCREEN_WIDTH // 2) // 2
        self.aboutLogo2.center_y = 10 + self.aboutLogo2.height
        self.aboutLogo2.draw()'''

        self.aboutLogo1.center_x = self.SCREEN_WIDTH // 2
        self.aboutLogo1.center_y = 10 + self.aboutLogo1.height
        self.aboutLogo1.draw()

    def drawState5(self):
        # Выход из программы
        text = "Выход"
        color = arcade.color.WHITE
        text_size = 44
        x = self.SCREEN_WIDTH // 3
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 6
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)

    def drawState6(self):
        otvet=-1
        # Игра Детектив 1
        text = "Игра Детектив"
        color = arcade.color.WHITE
        text_size = 38
        x = self.SCREEN_WIDTH // 2.7
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 12
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)

        self.imgAvatars.sprite_list[self.userAvatar].center_x = self.imgAvatars.sprite_list[self.userAvatar].width
        self.imgAvatars.sprite_list[self.userAvatar].center_y = self.SCREEN_HEIGHT - self.imgAvatars.sprite_list[self.userAvatar].height
        self.imgAvatars.sprite_list[self.userAvatar].draw()

        #print(self.userChoiceCards)

        if self.userChoiceCards==0:
            text = "Найти девочку, которая получила подарок"
            files1 = os.listdir(self.detectivePath1)
        elif self.userChoiceCards == 1:
            text = "Найти мальчика, который получил подарок"
            files1 = os.listdir(self.detectivePath2)
        else:
            text = "Найти девочку, которая получила подарок"
            files1 = os.listdir(self.detectivePath1)
        color = arcade.color.WHITE
        text_size = 33
        x = self.SCREEN_WIDTH // 4.2
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 6
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)

        #------------------------------

        """ Загрузка картинок """
        #files1 = os.listdir(self.detectivePath2)

        self.imgDetectives1 = arcade.SpriteList()

        for i in files1:
            if self.userChoiceCards==0:
                self.imgDetective1 = arcade.Sprite(self.detectivePath1+i, 1)
            elif self.userChoiceCards == 1:
                self.imgDetective1 = arcade.Sprite(self.detectivePath2+i, 1)
            else:
                self.imgDetective1 = arcade.Sprite(self.detectivePath1+i, 1)
            self.imgDetective1.width = 100
            self.imgDetective1.height = 200
            self.imgDetective1.center_x = 0
            self.imgDetective1.center_y = 0
            self.imgDetectives1.append(self.imgDetective1)

        #-------------

        # Дальше
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15
        self.MenuItemSelected_2 = -1

        for i in range(0,self.MenuLasti):
            text = self.Menu[self.MenuFirst2+i]
            text_size = 35
            x = self.SCREEN_WIDTH // 1.3
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.MenuItemSelected = self.MenuFirst2+i
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)

        #------------------------------

        # Вывод конкретного спрайта
        w=self.imgDetectives1.sprite_list[1].width
        h=self.imgDetectives1.sprite_list[1].height
        counter = 4
        s = 20
        x = self.SCREEN_WIDTH // 2 - (counter * w) //2.3
        y = self.SCREEN_HEIGHT // 3
        for i in range(0,len(self.imgDetectives1.sprite_list)):
            self.imgDetectives1.sprite_list[i].center_x = x
            x += w + s
            self.imgDetectives1.sprite_list[i].center_y = y
            counter -=1
            if counter <=0:
                counter = 5
                x = self.SCREEN_WIDTH // 2 - (counter * w) // 2.9
                y += h + s

            self.imgDetectives1.sprite_list[i].draw()
            # Определяем попадание курсора на аватар
            bottom =self.mouseY > self.imgDetectives1.sprite_list[i].center_y - self.imgDetectives1.sprite_list[i].height // 2
            top = self.mouseY < self.imgDetectives1.sprite_list[i].center_y + self.imgDetectives1.sprite_list[i].height // 2

            left = self.mouseX > self.imgDetectives1.sprite_list[i].center_x - self.imgDetectives1.sprite_list[i].width // 2
            right = self.mouseX < self.imgDetectives1.sprite_list[i].center_x + self.imgDetectives1.sprite_list[i].width // 2

            if (bottom and top) and (left and right):
                arcade.draw_rectangle_outline(self.imgDetectives1.sprite_list[i].center_x,self.imgDetectives1.sprite_list[i].center_y,self.imgDetectives1.sprite_list[i].width,self.imgDetectives1.sprite_list[i].height,color=arcade.color.RED)
                if self.isMouseDown:
                    otvet=i
                    """if i==0:
                        print('dthyj')
                        self.userGoodAnswers+=1
                        print(self.userGoodAnswers)
                    else:
                        print('----')
                        self.userBadAnswers+=1
                        print(self.userBadAnswers)"""
                    #self.userAvatar = i
                    print(otvet)
                if i==0:
                    self.userGoodAnswers+=1
                else:
                    self.userBadAnswers+=1

    def drawState9(self):
        #print("ghjghj", self.userBadAnswers)
        otvet=-1
        # Игра Детектив 2
        text = "Игра Детектив"
        color = arcade.color.WHITE
        text_size = 38
        x = self.SCREEN_WIDTH // 2.7
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 12
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)

        self.imgAvatars.sprite_list[self.userAvatar].center_x = self.imgAvatars.sprite_list[self.userAvatar].width
        self.imgAvatars.sprite_list[self.userAvatar].center_y = self.SCREEN_HEIGHT - self.imgAvatars.sprite_list[self.userAvatar].height
        self.imgAvatars.sprite_list[self.userAvatar].draw()

        #print(self.userChoiceCards)

        if self.userChoiceCards==0:
            text = "Найти девочку, у которой потерялся щенок"
            files1 = os.listdir(self.detectivePath1)
        elif self.userChoiceCards == 1:
            text = "Найти мальчика, у  которого потерялся щенок"
            files1 = os.listdir(self.detectivePath2)
        else:
            text = "Найти девочку, у которой потерялся щенок"
            files1 = os.listdir(self.detectivePath1)
        color = arcade.color.WHITE
        text_size = 33
        x = self.SCREEN_WIDTH // 4.2
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 6
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)

        #------------------------------

        """ Загрузка картинок """
        #files1 = os.listdir(self.detectivePath2)

        self.imgDetectives2 = arcade.SpriteList()

        for i in files1:
            if self.userChoiceCards==0:
                self.imgDetective2 = arcade.Sprite(self.detectivePath1+i, 1)
            elif self.userChoiceCards == 1:
                self.imgDetective2 = arcade.Sprite(self.detectivePath2+i, 1)
            else:
                self.imgDetective2 = arcade.Sprite(self.detectivePath1+i, 1)
            self.imgDetective2.width = 100
            self.imgDetective2.height = 200
            self.imgDetective2.center_x = 0
            self.imgDetective2.center_y = 0
            self.imgDetectives2.append(self.imgDetective1)

        #-------------

        # Дальше
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15
        self.MenuItemSelected_2 = -1

        for i in range(0,self.MenuLasti):
            text = self.Menu[self.MenuFirst2+i]
            text_size = 35
            x = self.SCREEN_WIDTH // 1.3
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.MenuItemSelected = self.MenuFirst2+i+1
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)

        #------------------------------

        # Вывод конкретного спрайта
        w=self.imgDetectives1.sprite_list[1].width
        h=self.imgDetectives1.sprite_list[1].height
        counter = 4
        s = 20
        x = self.SCREEN_WIDTH // 2 - (counter * w) //2.3
        y = self.SCREEN_HEIGHT // 3
        for i in range(0,len(self.imgDetectives1.sprite_list)):
            self.imgDetectives1.sprite_list[i].center_x = x
            x += w + s
            self.imgDetectives1.sprite_list[i].center_y = y
            counter -=1
            if counter <=0:
                counter = 5
                x = self.SCREEN_WIDTH // 2 - (counter * w) // 2.9
                y += h + s

            self.imgDetectives1.sprite_list[i].draw()
            # Определяем попадание курсора на аватар
            bottom =self.mouseY > self.imgDetectives1.sprite_list[i].center_y - self.imgDetectives1.sprite_list[i].height // 2
            top = self.mouseY < self.imgDetectives1.sprite_list[i].center_y + self.imgDetectives1.sprite_list[i].height // 2

            left = self.mouseX > self.imgDetectives1.sprite_list[i].center_x - self.imgDetectives1.sprite_list[i].width // 2
            right = self.mouseX < self.imgDetectives1.sprite_list[i].center_x + self.imgDetectives1.sprite_list[i].width // 2

            if (bottom and top) and (left and right):
                arcade.draw_rectangle_outline(self.imgDetectives1.sprite_list[i].center_x,self.imgDetectives1.sprite_list[i].center_y,self.imgDetectives1.sprite_list[i].width,self.imgDetectives1.sprite_list[i].height,color=arcade.color.RED)
                if self.isMouseDown:
                    otvet=i
                    """if i==0:
                        print('dthyj')
                        self.userGoodAnswers+=1
                        print(self.userGoodAnswers)
                    else:
                        print('----')
                        self.userBadAnswers+=1
                        print(self.userBadAnswers)"""
                    #self.userAvatar = i
                    print(otvet)

    def drawState10(self):
        print("ghjghj", self.userBadAnswers)
        otvet=-1
        # Игра Детектив 3
        text = "Игра Детектив"
        color = arcade.color.WHITE
        text_size = 38
        x = self.SCREEN_WIDTH // 2.7
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 12
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)

        self.imgAvatars.sprite_list[self.userAvatar].center_x = self.imgAvatars.sprite_list[self.userAvatar].width
        self.imgAvatars.sprite_list[self.userAvatar].center_y = self.SCREEN_HEIGHT - self.imgAvatars.sprite_list[self.userAvatar].height
        self.imgAvatars.sprite_list[self.userAvatar].draw()

        #print(self.userChoiceCards)

        if self.userChoiceCards==0:
            text = "Найти девочку, которая уже пообедала"
            files1 = os.listdir(self.detectivePath1)
        elif self.userChoiceCards == 1:
            text = "Найти мальчика, который уже пообедал"
            files1 = os.listdir(self.detectivePath2)
        else:
            text = "Найти девочку, которая уже пообедала"
            files1 = os.listdir(self.detectivePath1)
        color = arcade.color.WHITE
        text_size = 33
        x = self.SCREEN_WIDTH // 4.2
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 6
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)

        #------------------------------

        """ Загрузка картинок """
        #files1 = os.listdir(self.detectivePath2)

        self.imgDetectives2 = arcade.SpriteList()

        for i in files1:
            if self.userChoiceCards==0:
                self.imgDetective1 = arcade.Sprite(self.detectivePath1+i, 1)
            elif self.userChoiceCards == 1:
                self.imgDetective1 = arcade.Sprite(self.detectivePath2+i, 1)
            else:
                self.imgDetective2 = arcade.Sprite(self.detectivePath1+i, 1)
            self.imgDetective2.width = 100
            self.imgDetective2.height = 200
            self.imgDetective2.center_x = 0
            self.imgDetective2.center_y = 0
            self.imgDetectives2.append(self.imgDetective2)

        #-------------

        # Дальше
        self.MenuFirst2 = 9
        self.MenuLasti = 1

        mx = self.mouseX
        my = self.mouseY
        width = 400
        height=15
        self.MenuItemSelected_2 = -1

        for i in range(0,self.MenuLasti):
            text = self.Menu[self.MenuFirst2+i]
            text_size = 35
            x = self.SCREEN_WIDTH // 1.3
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 1.2
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.MenuItemSelected = self.MenuFirst2+2
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, font_name = self.font_title)

        #------------------------------

        # Вывод конкретного спрайта
        w=self.imgDetectives1.sprite_list[1].width
        h=self.imgDetectives1.sprite_list[1].height
        counter = 4
        s = 20
        x = self.SCREEN_WIDTH // 2 - (counter * w) //2.3
        y = self.SCREEN_HEIGHT // 3
        for i in range(0,len(self.imgDetectives1.sprite_list)):
            self.imgDetectives1.sprite_list[i].center_x = x
            x += w + s
            self.imgDetectives1.sprite_list[i].center_y = y
            counter -=1
            if counter <=0:
                counter = 5
                x = self.SCREEN_WIDTH // 2 - (counter * w) // 2.9
                y += h + s

            self.imgDetectives1.sprite_list[i].draw()
            # Определяем попадание курсора на аватар
            bottom =self.mouseY > self.imgDetectives1.sprite_list[i].center_y - self.imgDetectives1.sprite_list[i].height // 2
            top = self.mouseY < self.imgDetectives1.sprite_list[i].center_y + self.imgDetectives1.sprite_list[i].height // 2

            left = self.mouseX > self.imgDetectives1.sprite_list[i].center_x - self.imgDetectives1.sprite_list[i].width // 2
            right = self.mouseX < self.imgDetectives1.sprite_list[i].center_x + self.imgDetectives1.sprite_list[i].width // 2

            if (bottom and top) and (left and right):
                arcade.draw_rectangle_outline(self.imgDetectives1.sprite_list[i].center_x,self.imgDetectives1.sprite_list[i].center_y,self.imgDetectives1.sprite_list[i].width,self.imgDetectives1.sprite_list[i].height,color=arcade.color.RED)
                if self.isMouseDown:
                    otvet=i
                    """if i==0:
                        print('dthyj')
                        self.userGoodAnswers+=1
                        print(self.userGoodAnswers)
                    else:
                        print('----')
                        self.userBadAnswers+=1
                        print(self.userBadAnswers)"""
                    #self.userAvatar = i
                    print(otvet)


    def drawState7(self):
        # Игра Подбери маску
        text = "Игра Подбери маску"
        color = arcade.color.WHITE
        text_size = 38
        x = self.SCREEN_WIDTH // 2.7
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 12
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)

        self.imgAvatars.sprite_list[self.userAvatar].center_x = self.imgAvatars.sprite_list[self.userAvatar].width
        self.imgAvatars.sprite_list[self.userAvatar].center_y = self.SCREEN_HEIGHT - self.imgAvatars.sprite_list[self.userAvatar].height
        self.imgAvatars.sprite_list[self.userAvatar].draw()

        
        text = "Какое настроение у мальчика с картинки?"
        files1 = os.listdir(self.detectivePath4)
        color = arcade.color.WHITE
        text_size = 33
        x = self.SCREEN_WIDTH // 4.2
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 6
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)

        self.aboutLogo2.center_x = self.SCREEN_WIDTH // 2
        self.aboutLogo2.center_y = y - self.aboutLogo2.height // 1.5
        self.aboutLogo2.draw()


        files = os.listdir(self.detectivePath5)

        self.imgMaskes = arcade.SpriteList()

        for i in files:
            self.imgMask = arcade.Sprite(self.detectivePath5+i, 1)
            self.imgMask.width = 100
            self.imgMask.height = 100
            self.imgMask.center_x = 0
            self.imgMask.center_y = 0
            self.imgMaskes.append(self.imgMask)

        #self.imgAvatars.draw()
        # Вывод конкретного спрайта
        w=self.imgMaskes.sprite_list[1].width
        h=self.imgMaskes.sprite_list[1].height
        counter = 2
        s = 20
        x = self.SCREEN_WIDTH // 2 - (counter * w) //2
        y = self.SCREEN_HEIGHT // 6
        for i in range(0,len(self.imgMaskes.sprite_list)):
            self.imgMaskes.sprite_list[i].center_x = x
            x += w + s
            self.imgMaskes.sprite_list[i].center_y = y
            counter -=1
            if counter <=0:
                counter = 1
                x = self.SCREEN_WIDTH // 2 - (counter * w) // 2
                #y += h + s

            self.imgMaskes.sprite_list[i].draw()
            # Определяем попадание курсора на аватар
            bottom =self.mouseY > self.imgMaskes.sprite_list[i].center_y - self.imgMaskes.sprite_list[i].height // 2
            top = self.mouseY < self.imgMaskes.sprite_list[i].center_y + self.imgMaskes.sprite_list[i].height // 2

            left = self.mouseX > self.imgMaskes.sprite_list[i].center_x - self.imgMaskes.sprite_list[i].width // 2
            right = self.mouseX < self.imgMaskes.sprite_list[i].center_x + self.imgMaskes.sprite_list[i].width // 2

            if (bottom and top) and (left and right):
                arcade.draw_rectangle_outline(self.imgMaskes.sprite_list[i].center_x,self.imgMaskes.sprite_list[i].center_y,self.imgMaskes.sprite_list[i].width,self.imgMaskes.sprite_list[i].height,color=arcade.color.RED)
                if self.isMouseDown:
                    #self.userAvatar = i
                    print('всё ок')

    def drawState8(self):
        # Игра Пятнашки
        text = "Игра Пятнашки"
        color = arcade.color.WHITE
        text_size = 44
        x = self.SCREEN_WIDTH // 3
        y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 5
        arcade.draw_text(text,x, y,color, text_size, anchor_y = "center",font_name = self.font_title)

    def drawMenu(self):
        """ Рисуем менюшку """
        mx = self.mouseX
        my = self.mouseY
        width = 300
        height=15
        self.MenuItemSelected = -1

        for i in range(0,self.MenuLast):
            text = self.Menu[self.MenuFirst+i]
            text_size = 35
            x = self.SCREEN_WIDTH // 2.7
            y = self.SCREEN_HEIGHT  - self.SCREEN_HEIGHT // 3 - 20 - i*40
            if my>y-height and my<y+height and mx>x-width//2 and mx<x+width//2:
                color = self.menucolorselected
                self.MenuItemSelected = self.MenuFirst+i
            else:
                color = self.menucolor
            arcade.draw_text(text, x, y,color, text_size, anchor_y = "center",font_name = self.font_title)

    def on_key_press(self, key, modifiers):
        """ Обработка нажатий на кнопки """
        if key == arcade.key.F:
            # Переключение между полноэкранным режимом и обычным
            self.set_fullscreen(not self.fullscreen)
            width, height = self.get_size()
            self.set_viewport(0, width, 0, height)

        if key == arcade.key.S:
            # Еще один способ переключеие между полноэкранным режимом и обычным. Разница будет заметна, если разрешение экрана будет меньше чем текущее
            self.set_fullscreen(not self.fullscreen)
            self.set_viewport(0, self.SCREEN_WIDTH, 0, self.SCREEN_HEIGHT)

        # Обрабатываем клавишу ESCAPE
        if key == arcade.key.ESCAPE:
            if self.state == 0 or self.state==5:
                self.close()
                quit()
            elif self.state > 0 and self.state < 5:
                self.state=0
            elif self.state > 5 and self.state < 15:
                self.state=3
            #elif self.state == 9:
            #    self.state=6

    def on_mouse_motion(self, x, y, dx, dy):
        """ Перемещение мышки """
        # Запоминаем текущие координаты мыши и ее смещение
        self.mouseX = x
        self.mouseY = y
        self.mouseDX = dx
        self.mouseDY = dy



    def on_mouse_press(self, x, y, button, modifiers):
        """ Когда кнопка мыши нажата """
        print(f"You clicked button number: {button}")
        if button == arcade.MOUSE_BUTTON_LEFT:
            self.bgGUIColor  = arcade.color.GREEN
            self.isMouseDown = True

    def on_mouse_release(self, x, y, button, modifiers):
        """ Когда кнопка мыши отпущена """
        if button == arcade.MOUSE_BUTTON_LEFT:
            if self.MenuItemSelected == 5:
                self.close()
                quit()

            if self.MenuItemSelected>0 and self.MenuItemSelected <=15:
                print("Перключаемся в состояние %s"%(self.MenuItemSelected))
                self.state = self.MenuItemSelected

            self.isMouseDown = False

    def update(self, delta_time):
        """ Перемещение объектов и др. логика """
        pass

def main():
    """ Main method """
    app = TApp(False)
    app.setup()
    arcade.run()

if __name__ == "__main__":
    main()
