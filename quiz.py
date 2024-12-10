import pygame
pygame.init()
screen = pygame.display.set_mode((1000, 600))
screen.fill((255,255,255))
pygame.display.update()

Brazil = pygame.image.load("Brazil.jpg")
Brazilimg = pygame.transform.scale(Brazil, (100,70))

Italy = pygame.image.load("Italy.jpg")
Italyimg = pygame.transform.scale(Italy, (100,70))

Uruguay = pygame.image.load("Uruguay.png")
Uruguayimg = pygame.transform.scale(Uruguay, (100,70))

America= pygame.image.load("America.png")
Americaimg = pygame.transform.scale(America, (100,70))

screen.blit(Uruguayimg,(150,100))
screen.blit(Americaimg,(150,200))
screen.blit(Brazilimg,(150,300))
screen.blit(Italyimg,(150,400))

while True:
    pygame.display.update()    

    font = pygame.font.SysFont("Times New Roman", 30)
    text = font.render("Which country has won the most world cups?", True,(0,0,0))
    text1 = font.render("Which country has won the 2020 euro cup?", True,(0,0,0))
    text2 = font.render("Which coutry has won the first world cup?", True,(0,0,0))
    text3 = font.render("Which country is going to host the 2026 world cup?", True,(0,0,0))

    screen.blit(text,(350,100))
    screen.blit(text1,(350,200))
    screen.blit(text2,(350,300))
    screen.blit(text3,(350,400))
    pygame.display.update()

    while 1:

        event = pygame.event.poll()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen,(0,0,0), (pos), 20, 0)
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            pos2 = pygame.mouse.get_pos()
            pygame.draw.line(screen,(0,0,0), (pos), (pos2), 3)
            pygame.draw.circle(screen,(0,0,0), (pos2), 20, 0)
            pygame.display.update()
            
        elif event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
  







