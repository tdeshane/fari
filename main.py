import pygame
import random

WIDTH = 1040
HEIGHT = 720

enemies = []

#pygame setup
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

file = 'battle.mp3'

try:
    pygame.mixer.music.load(file)
    print("Music file {} loaded!".format(file))
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

except pygame.error:
    print("File {} not found! ({})".format(file, pygame.get_error()))
    raise SystemExit


#initialize player position to be on the grass
playerX = 0
playerY = 255


#initilize blob position to be on the grass
blobX = 0
blobY = 100

#put blob coordinates in the enemies list
enemies.append((blobX, blobY))

snipper_copterX = 0
snipper_copterY = 100

#put snipper copter coordinates in the enemies list
enemies.append((snipper_copterX, snipper_copterY))

smasherX = 0
smasherY = 100
# put smasher coordinates in the enemies list
enemies.append((smasherX, smasherY))

#initilize health
health = 100

#initilize score
score = 0

MAX_SCREEN_X = 1040
MAX_SCREEN_Y = 720

level = 1
#score = 246000
teleport = False


# Game loop
running = True
while running:
    # Process input (events)
    for event in pygame.event.get():
        # Check for closing the window
        if event.type == pygame.QUIT:
            running = False
    # Update
    # Draw / render
    screen.fill((0, 0, 0))
    # *after* drawing everything, flip the display


    #fill bottom third with green relative to MAX_SCREEN_X and MAX_SCREEN_Y
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(0, (2*MAX_SCREEN_Y)/3, MAX_SCREEN_X, MAX_SCREEN_Y/3))

    #pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(0, 480, MAX_SCREEN_X, 240))

    #fill top two thirds with blue relative to MAX_SCREEN_X and MAX_SCREEN_Y
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(0, 0, MAX_SCREEN_X, (2*MAX_SCREEN_Y)/3))
    #pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(0, 0, MAX_SCREEN_X, 480))


    #if level 1, blob is the enemy
    if level == 1:
        #draw a semi circle blob
        pygame.draw.circle(screen, (255, 255, 255), (blobX, blobY), 60)

        #move the blob closer to the player
        if blobX < playerX:
            blobX += 1
        elif blobX > playerX:
            blobX -= 1
        elif blobY < playerY:
            blobY += 1
        elif blobY > playerY:
            blobY -= 1

       
    elif level == 2:
        #snipper copters are the enemy
        #rectagle for the body
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(snipper_copterX, snipper_copterY, 30, 50))
        #circle for the head
        pygame.draw.circle(screen, (255, 255, 255), (snipper_copterX+15, snipper_copterY), 15)

        #move the snipper copter closer to the player diagonally
        if snipper_copterX < playerX and snipper_copterY < playerY:
            snipper_copterX += 1
            snipper_copterY += 1
        elif snipper_copterX > playerX and snipper_copterY > playerY:
            snipper_copterX -= 1
            snipper_copterY -= 1
        elif snipper_copterX < playerX and snipper_copterY > playerY:
            snipper_copterX += 1
            snipper_copterY -= 1
        elif snipper_copterX > playerX and snipper_copterY < playerY:
            snipper_copterX -= 1
            snipper_copterY += 1
    elif level == 3:
        #enemy is a smasher
        #draw a rectangle
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(smasherX, smasherY, 30, 50))

        #move the smasher closer to the player horizontally and vertically by 2 units
        #if smasher is to the left of the player, move right
        if smasherX < playerX:
            smasherX += 2
        #if smasher is to the right of the player, move left
        elif smasherX > playerX:
            smasherX -= 2
        #if smasher is above the player, move down
        elif smasherY < playerY:
            smasherY += 2
        #if smasher is below the player, move up
        elif smasherY > playerY:
            smasherY -= 2

        #in level 3, when different scores are reached, add teleports for the player
        # if score is greater than 12000 and is a multiple of 1000, draw a teleport
        if score > 246000 and score % 1000 == 0:
            #draw teleport in random location
            randX = random.randint(0, MAX_SCREEN_X)
            randY = random.randint(0, MAX_SCREEN_Y)
            
            #set teleport values to randX and randY
            teleportX = randX
            teleportY = randY
            teleport = True

        if(teleport == True):
            #draw teleport
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(teleportX, teleportY, 30, 30))
 
            #if player touches teleport, move player to random location
            if playerX == randX and playerY == randY:
                playerX = random.randint(0, MAX_SCREEN_X)
                playerY = random.randint(0, MAX_SCREEN_Y)
                #increase score by 100244
                print("teleport")
                print(playerX)
                print(playerY)
                print(randX)
                print(randY)
                print(score)
     






    #loop through enemies list and if any enemy is touching the edge of the screen, move it to the other side of the screen
    for enemyX,enemyY in enemies:
        #if enemy reaches right edge of screen, move to other left side of screen
        if enemyX > MAX_SCREEN_X:
            enemyX = 0
        #if enemy reaches bottom edge of screen, move to top of screen
        elif enemyY > MAX_SCREEN_Y:
            enemyY = 0
        #if enemy reaches right edge of screen, move to other left side of screen
        elif enemyX < 0:
            enemyX = MAX_SCREEN_X
        #if enemy reaches top edge of screen, move to bottom of screen
        elif enemyY < 0:
            enemyY = MAX_SCREEN_Y

        
    #same edge movement for player
    if playerX > MAX_SCREEN_X:
        playerX = 0
    elif playerY > MAX_SCREEN_Y:
        playerY = 0
    elif playerX < 0:
        playerX = MAX_SCREEN_X
    elif playerY < 0:
        playerY = MAX_SCREEN_Y

    #update enemy positions in enemies list
    
    if level == 1:
        enemies[0] = (blobX, blobY)
    elif level == 2:
        enemies[1] = (snipper_copterX, snipper_copterY)
    elif level == 3:
        enemies[2] = (smasherX, smasherY)


    #if enemy is touching player, decrease health
    #enemies are stored as coordinates in a list
   
    for enemyX,enemyY in enemies:
        if enemyX == playerX and enemyY == playerY:
            health -= 1
            #print(health)
    

    #draw health bar
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 0, health*10, 30))

    #draw score
    display_text = pygame.font.Font(None, 36).render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(display_text, (0, 0))



    #if health is 0, game over
    if health == 0:
        display_text = pygame.font.Font(None, 36).render("Game Over", True, (255, 255, 255))
        #sleep in pygame
        screen.blit(display_text, (WIDTH/2, HEIGHT/2))
        pygame.display.flip()
        pygame.time.wait(3000)
        
        pygame.quit()    


    #add keyboard controls
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        playerY -= 1
        
    if pressed[pygame.K_DOWN]:
        playerY += 1

    if pressed[pygame.K_LEFT]:
        playerX -= 1
  
    if pressed[pygame.K_RIGHT]:
        playerX += 1
        

    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(playerX, playerY, 30, 30))
    pygame.display.flip()
    
    # keep loop running at the right speed
    clock.tick(60)
    score += 1

    #if score is 9000, go to level 2
    if score == 9000:
        level = 2
    elif score == 246000:
        level = 3



pygame.quit()

