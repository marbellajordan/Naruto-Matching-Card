from pygame import *
from pygame import _view
from random import *

init()

size = width,height = 800,600
screen = display.set_mode(size)

bg1 = image.load(r"Pictures\\titlescreen.png").convert()
question_mark = image.load("Pictures\\question.jpg").convert()

card_images = [image.load(r"Pictures\\pic1.jpg").convert(),\
                image.load(r"Pictures\\pic2.jpg").convert(),\
                image.load(r"Pictures\\pic3.png").convert(),\
                image.load(r"Pictures\\pic4.jpg").convert(),\
                image.load(r"Pictures\\pic5.jpg").convert(),\
                image.load(r"Pictures\\pic6.jpg").convert(),\
                image.load(r"Pictures\\pic7.jpg").convert(),\
                image.load(r"Pictures\\pic8.jpg").convert(),\
                image.load(r"Pictures\\pic9.jpg").convert(),\
                image.load(r"Pictures\\pic10.jpg").convert()]

mismatch_images = [image.load(r"Mis Match Pics\\mis1.jpg").convert(),\
                    image.load(r"Mis Match Pics\\mis2.jpg").convert(),\
                    image.load(r"Mis Match Pics\\mis3.jpg").convert(),\
                    image.load(r"Mis Match Pics\\mis4.jpg").convert(),\
                    image.load(r"Mis Match Pics\\mis5.png").convert()]

class card():

    def __init__(self,c_type):

        self.c_type = c_type

        if c_type < 10:
            self.image = card_images[c_type]
        else:
            self.image = mismatch_images[c_type-10]

        self.matched = 0

    def get_c_type(self):

        return self.c_type

    def get_image(self):
        return self.image

    def set_matched(self):
        self.matched = 1

    def get_matched(self):
        return self.matched


p1_points = 0
p2_points = 0

player_turn = 1

choice = [0,0]

screentype = 'main'

font1 = font.Font('Fonts/BOOKOS.ttf',40)
font2 = font.Font('Fonts/BOOKOS.ttf',16)

cards = []
card_types = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,11,12,13,14]

for i in range(25):

    rand_card = card_types[randint(0,len(card_types)-1)]

    cards.append(card(rand_card))

    card_types.remove(rand_card)



while 1:

    event.pump()
    k = key.get_pressed()

    if k[K_ESCAPE]:
        break



    m = mouse.get_pressed()

    mx,my = mouse.get_pos()

    if screentype == 'main':

        screen.blit(transform.scale(bg1,size),(0,0))
        bg1 = image.load(r"Pictures\\titlescreen.png")

        if m[0] and 250 < mx < 550 and 150 < my < 250:
            screentype = 'game'
            time.wait(500)

        if m[0] and 200 < mx < 600 and 250 < my < 350:
            screentype = 'instructions'

    elif screentype == 'instructions':

        screen.fill((128,0,255))

        intro1 = font1.render('Welcome to the card matching game',1,(255,255,255))
        intro2 = font1.render('In this game two players take turns',1,(255,255,255))
        intro3 = font1.render('flipping cards to try to get matches.',1,(255,255,255))

        intro4 = font1.render('Watch out for 5 diff. cards!!',1,(255,255,255))
        intro5 = font1.render('Return.',1,(255,255,255))

        screen.blit(intro1,(50,50))
        screen.blit(intro2,(50,100))
        screen.blit(intro3,(50,150))
        screen.blit(intro4,(50,200))
        screen.blit(intro5,(300,500))

        if m[0] and 300 < mx < 700 and 500 < my < 550:
            screentype = 'main'

    elif screentype == 'game':

        screen.fill((255,255,255))
        screen.blit(transform.scale(bg1,size),(0,0))
        bg1 = image.load(r"Pictures\\display.jpg")

        msg_p1 = font2.render('Player 1 Points',1,(0,0,0))
        msg_p1p = font2.render(str(p1_points),1,(0,0,0))

        msg_p2 = font2.render('Player 2 Points',1,(0,0,0))
        msg_p2p = font2.render(str(p2_points),1,(0,0,0))

        screen.blit(msg_p1,(10,50))
        screen.blit(msg_p1p,(50,70))

        screen.blit(msg_p2,(660,50))
        screen.blit(msg_p2p,(700,70))

        msg_turn = font2.render('Your turn',1,(0,255,0))
        hero = image.load('Pictures\\Naruto Shippuden (4).png')
        if player_turn == 1:
            screen.blit(msg_turn,(25,10))
        if player_turn == 2:
            screen.blit(msg_turn,(675,10))

        for x in range(5):
            for y in range(5):
                if cards[x+y*5].get_matched() == 0:

                    if 150+x*100 < mx < 250+x*100 and y*120 < my < 120+y*120:

                        draw.rect(screen,(0,255,0),(150+x*100,y*120,100,120),3)

                        if m[0]:

                            if choice[0] == 0:
                                choice[0] = cards[x+y*5]

                            elif choice[1] == 0 and choice[0] != cards[x+y*5]:
                                choice[1] = cards[x+y*5]

                    else:
                        draw.rect(screen,(0,0,0),(150+x*100,y*120,100,120),3)

                    screen.blit(transform.scale(question_mark,(100,120)),(150+x*100,y*120))

                    if choice[0] == cards[x+y*5]:
                        screen.blit(transform.scale(choice[0].get_image(),(100,120)),(150+x*100,y*120))

                    if choice[1] == cards[x+y*5]:
                        screen.blit(transform.scale(choice[1].get_image(),(100,120)),(150+x*100,y*120))

        if choice[0] != 0 and choice[1] != 0:

            display.flip()
            time.wait(500)

            if choice[0].get_c_type() == choice[1].get_c_type():

                if player_turn == 1:
                    p1_points += 1

                elif player_turn == 2:
                    p2_points += 1

                choice[0].set_matched()
                choice[1].set_matched()

            if player_turn == 1:
                player_turn = 2

            elif player_turn == 2:
                player_turn = 1

            choice = [0,0]

        if p1_points > 5:
            screen.fill((255,255,255))
            screen.blit(transform.scale(bg1,size),(0,0))
            bg1 = image.load(r"Pictures\\display.jpg")
            print('Player 1 Wins!!!')
            break

        if p2_points > 5:
            print('Player 1 Wins!!!')
            break

        if p1_points+p2_points == 10:
            print('Draw Game!!!')
            break

    display.flip()

    time.delay(20)

quit()
