from pygame import*

game = True
okno = display.set_mode((900,700), FULLSCREEN)
clock = time.Clock()

font.init()
wr = font.Font(None, 50)

fon = transform.scale(image.load('ABCD.jpg'),(900,700))
pers = transform.scale(image.load('kir.png'),(50,50))

from random import randint

class gameobject(sprite.Sprite):
    def __init__(self, pikt, x,y):
        self.image = transform.scale(image.load(pikt),(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def ris(self):
        okno.blit(self.image, (self.rect.x,self.rect.y))
    def control(self):
        kn = key.get_pressed()
        if kn[K_LEFT]:
            self.rect.x -= 5
        if kn[K_RIGHT]:
            self.rect.x += 5
    def fall(self):
        self.rect.y += 5
        if self.rect.y > 700:
            self.rect.y = 30
            self.rect.x = randint(25,840)
        if sprite.collide_rect(self, pers):
            self.rect.y = -30
            self.rect.x = randint(25,840)
            global points
            points += 1


pers = gameobject('kir.png', 300,450)
star = gameobject('ab.jpeg', 300,30)
points = 0



while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
        if i.type == KEYDOWN:
            if i.key == K_ESCAPE:
                game =False
    okno.blit(fon, (0,0))
    pers.ris()
    pers.control()
    star.ris()
    star.fall()
    score = wr.render(str(points), True, (255,0,0))
    okno.blit(score, (10,10))
    clock.tick(60)
    display.update()