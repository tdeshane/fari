import pygame
import random
import time

WIDTH = 1040
HEIGHT = 720

LEVEL_2_SCORE = 9000
LEVEL_3_SCORE = 12000
LEVEL_4_SCORE = 18000
LEVEL_5_SCORE = 24000
LEVEL_6_SCORE = 30000
LEVEL_7_SCORE = 37000
LEVEL_17_SCORE = 45000
LEVEL_956842987_SCORE = 50000
MAGMA_MONSTER_LEVEL = 52965000000000000000000


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

dragonX = 0
dragonY = 100

fireballX = 0
fireballY = 100

giant_catX = 0
giant_catY = 100

ghostX = 0
ghostY = 100

vortexX = 0
vortexY = 100

dark_conveyorX = 0
dark_conveyorY = 100

demon_of_the_darkX = 0
demon_of_the_darkY = 100
demon_of_the_dark_health = 2000

magma_monsterX = 0
magma_monsterY = 100
magma_monster_difficulty = "hard"
magma_monster_age = 5
magma_monster_level = MAGMA_MONSTER_LEVEL
magma_monster_health = 50000

last_shield_spawn_time = 0
shield_spawn_interval = 1000  # 10 seconds in milliseconds
shield_active = True
shieldX = -1
shieldY = -1
sonic_blastX = -1
sonic_blastY = -1


#initilize health
health = 100

#initilize score
score = 0


MAX_SCREEN_X = 1040
MAX_SCREEN_Y = 720

level = 1
level = MAGMA_MONSTER_LEVEL



ball_speed = 5
ball_radius = 10
balls = []
skulls = []

player_width = 5
player_height = 5




teleport = False
teleportX = -1
teleportY = -1

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
        if score > LEVEL_3_SCORE and score % 1000 == 0 and teleport == False:
            #draw teleport in random location
            randX = random.randint(0, MAX_SCREEN_X)
            randY = random.randint(0, MAX_SCREEN_Y)
            
            #set teleport values to randX and randY
            teleportX = randX
            teleportY = randY
            teleport = True
            print("teleportX: " + str(teleportX))
            print("teleportY: " + str(teleportY))

        if(teleport == True):
            #draw teleport
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(teleportX, teleportY, 30, 30))
 
            #if player touches teleport, move player to random location
            if playerX == teleportX and playerY == teleportY:
                playerX = random.randint(0, MAX_SCREEN_X)
                playerY = random.randint(0, MAX_SCREEN_Y)
                #increase score by 1024
                score += 1024
                print("teleport")
                print(playerX)
                print(playerY)
                print(score)
                teleportX = -1
                teleportY = -1
                teleport = False
    elif level == 4:
        #dragon enemy
        #draw a triangle for the entire dragon using dragonX and dragonY
        pygame.draw.polygon(screen, (255, 255, 255), [(dragonX, dragonY), (dragonX+30, dragonY), (dragonX+15, dragonY-30)])
        
        #make the dragon shoot fireballs
        #draw a circle for the fireball shooting from the dragon's mouth
        pygame.draw.circle(screen, (255, 0, 0), (fireballX+15, fireballY-30), 5)
        #move the fireball closer to the player based on the player's position
        if fireballX < playerX:
            fireballX += 4
        if fireballX < 0 or fireballX > MAX_SCREEN_X:
            fireballX = dragonX
        if fireballY < playerY:
            fireballY += 4
        if fireballY < 0 or fireballY > MAX_SCREEN_Y:
            fireballY = dragonY

        #move the dragon closer to the player horizontally and vertically by 2 units
        #if dragon is to the left of the player, move right
        if dragonX < playerX:
            dragonX += 2
        #if dragon is to the right of the player, move left
        elif dragonX > playerX:
            dragonX -= 2
        #if dragon is above the player, move down
        elif dragonY < playerY:
            dragonY += 2
        #if dragon is below the player, move up
        elif dragonY > playerY:
            dragonY -= 2

        #if fireball touches player, decrease health
        if fireballX == playerX and fireballY == playerY:
            health -= 1
            print(health)

        #if dragon touches player, decrease health
        if dragonX == playerX and dragonY == playerY:
            health -= 1
            print(health)
    elif level == 5:
        #giant cat enemy
        #draw a very large circle for the cat
        pygame.draw.circle(screen, (255, 255, 255), (giant_catX, giant_catY), 100)

        #move the giant cat closer to the player diagonally
        if giant_catX < playerX and giant_catY < playerY:
            giant_catX += 1
            giant_catY += 1
        elif giant_catX > playerX and giant_catY > playerY:
            giant_catX -= 1
            giant_catY -= 1
        elif giant_catX < playerX and giant_catY > playerY:
            giant_catX += 1
            giant_catY -= 1
        elif giant_catX > playerX and giant_catY < playerY:
            giant_catX -= 1
            giant_catY += 1

        #if giant cat touches player, decrease health
        if giant_catX == playerX and giant_catY == playerY:
            health -= 1
            print(health)
    elif level == 6:
        #ghost enemy
        #draw a triangle for the ghost
        pygame.draw.polygon(screen, (255, 255, 255), [(ghostX, ghostY), (ghostX+30, ghostY), (ghostX+15, ghostY-30)])
        

        #move the ghost closer to the player diagonally
        if ghostX < playerX and ghostY < playerY:
            ghostX += 1
            ghostY += 1
        elif ghostX > playerX and ghostY > playerY:
            ghostX -= 1
            ghostY -= 1
        elif ghostX < playerX and ghostY > playerY:
            ghostX += 1
            ghostY -= 1
        elif ghostX > playerX and ghostY < playerY:
            ghostX -= 1
            ghostY += 1

        #if ghost touches player, decrease health
        if ghostX == playerX and ghostY == playerY:
            health -= 1
            print(health)
    elif level == 7:
        #vortex enemy as square
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(vortexX, vortexY, 30, 30))

        #move the vortex closer to the player horizontally by 2 units
        #if vortex is to the left of the player, move right
        if vortexX < playerX:
            vortexX += 2
        #if vortex is to the right of the player, move left
        elif vortexX > playerX:
            vortexX -= 2

        #if vortex touches player, decrease health
        if vortexX == playerX and vortexY == playerY:
            health -= 100
            print(health)
    elif level == 17:
        #draw a dark conveyor as a rectangle for the body
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(dark_conveyorX, dark_conveyorY, 30, 50))
        #draw a circle for the head
        pygame.draw.circle(screen, (255, 255, 255), (dark_conveyorX+15, dark_conveyorY), 15)
        #draw triangles for arms
        pygame.draw.polygon(screen, (255, 255, 255), [(dark_conveyorX, dark_conveyorY), (dark_conveyorX-15, dark_conveyorY+15), (dark_conveyorX, dark_conveyorY+30)])
        pygame.draw.polygon(screen, (255, 255, 255), [(dark_conveyorX+30, dark_conveyorY), (dark_conveyorX+45, dark_conveyorY+15), (dark_conveyorX+30, dark_conveyorY+30)])

        #draw cirles for eyes
        pygame.draw.circle(screen, (255, 255, 255), (dark_conveyorX+5, dark_conveyorY-10), 5)
        pygame.draw.circle(screen, (255, 255, 255), (dark_conveyorX+25, dark_conveyorY-10), 5)

        #move the dark conveyor closer to the player horizontally and vertically by 2 units
        #if dark conveyor is to the left of the player, move right
        if dark_conveyorX < playerX:
            dark_conveyorX += 2
        #if dark conveyor is to the right of the player, move left
        elif dark_conveyorX > playerX:
            dark_conveyorX -= 2
        #if dark conveyor is above the player, move down
        elif dark_conveyorY < playerY:
            dark_conveyorY += 2
        #if dark conveyor is below the player, move up
        elif dark_conveyorY > playerY:
            dark_conveyorY -= 2

        #if dark conveyor touches player, decrease health
        if dark_conveyorX == playerX and dark_conveyorY == playerY:
            health -= 5
            print(health)

    elif level == LEVEL_956842987_SCORE:


        #add upgrades for player
        #set position of shield to random location
        if shieldX == -1 and shieldY == -1:
            shieldX = random.randint(0, MAX_SCREEN_X)
            shieldY = random.randint(0, MAX_SCREEN_Y)
            shield_active = True
       

        if sonic_blastX == -1 and sonic_blastY == -1:
            sonic_blastX = random.randint(0, MAX_SCREEN_X)
            sonic_blastY = random.randint(0, MAX_SCREEN_Y)
            sonic_blast_active = True
            

       #add sonic blast upgrade, when player touches it, it shots out at the demon of the dark and causes damage
        #draw a circle for the sonic blast
        if sonic_blast_active:
            pygame.draw.circle(screen, (255, 255, 255), (sonic_blastX, sonic_blastY), 5)
        #if player within hitbox of sonic blast, shoot it at the demon of the dark
        hitbox = 30
        if playerX - hitbox < sonic_blastX < playerX + hitbox and playerY - hitbox < sonic_blastY < playerY + hitbox:
            #draw sonic blast emanating from the circle
            #draw a line from the circle to the demon of the dark
            pygame.draw.line(screen, (255, 255, 255), (playerX, playerY), (sonic_blastX, sonic_blastY), 1)

     
            #descrease demon of the dark health by 100
            demon_of_the_dark_health -= 100
            #if demon of the dark health is 0, display you win!
            if demon_of_the_dark_health == 0:
                display_text = pygame.font.Font(None, 36).render("You Win!", True, (255, 255, 255))
                screen.blit(display_text, (WIDTH/2, HEIGHT/2))
                pygame.display.flip()
                pygame.time.wait(3000)
                pygame.quit()

            sonic_blastX = -1
            sonic_blastY = -1



        
        #draw shield
        if shield_active:
            pygame.draw.rect(screen, (15, 30, 255), pygame.Rect(shieldX, shieldY, 30, 30))
    
        #if player is within hitbox of the shield, increase health
        hitbox = 30
        if playerX - hitbox < shieldX < playerX + hitbox and playerY - hitbox < shieldY < playerY + hitbox:
            health += 10 ** 1000
            print(health)
            shield_active = False
            shieldX = -1
            shieldY = -1




        # Create the demon of the dark
        pygame.draw.polygon(screen, (0,0,0), [(demon_of_the_darkX, demon_of_the_darkY), (demon_of_the_darkX + 30, demon_of_the_darkY + 50), (demon_of_the_darkX+15, demon_of_the_darkY-30), (demon_of_the_darkX + 30, demon_of_the_darkY + 50)])

        # Additional setup for giant skulls
        skull_width = 20
        skull_height = 30

        # Attack player with balls and giant skulls
        if random.randint(1, 60) == 1:
            new_ball = {"x": demon_of_the_darkX, "y": demon_of_the_darkY, "dx": random.choice([-1, 1]), "dy": random.choice([-1, 1])}
            balls.append(new_ball)
        
        if random.randint(1, 60) == 1:
            new_skull = {"x": demon_of_the_darkX, "y": demon_of_the_darkY, "dx": random.choice([-1, 1]), "dy": random.choice([-1, 1])}
            skulls.append(new_skull)

        # Update ball and skull positions and check for collisions with the player
        for ball in balls:
            ball["x"] += ball["dx"] * ball_speed
            ball["y"] += ball["dy"] * ball_speed

            # Check for collision with player
            if playerX - ball_radius < ball["x"] < playerX + ball_radius and playerY - ball_radius < ball["y"] < playerY + ball_radius:
                health -= 10  # Decrease health by 10
                balls.remove(ball)  # Remove the ball that collided

            # Draw the ball
            pygame.draw.circle(screen, (255, 0, 0), (ball["x"], ball["y"]), ball_radius)

        for skull in skulls:
            skull["x"] += skull["dx"] * ball_speed
            skull["y"] += skull["dy"] * ball_speed

            # Check for collision with player
            if playerX - skull_width < skull["x"] < playerX + skull_width and playerY - skull_height < skull["y"] < playerY + skull_height:
                health -= 10  # Decrease health by 10
                skulls.remove(skull)  # Remove the skull that collided

            # Draw the skull (simplified, you might want to create a more detailed representation)
            pygame.draw.rect(screen, (150, 150, 150), (skull["x"], skull["y"], skull_width, skull_height))
            pygame.draw.circle(screen, (150, 150, 150), (skull["x"] + skull_width // 2, skull["y"] - skull_height // 2), skull_width // 2)

        # Add code to remove skulls and balls that are off-screen (to save memory)
        balls = [ball for ball in balls if 0 <= ball["x"] <= WIDTH and 0 <= ball["y"] <= HEIGHT]
        skulls = [skull for skull in skulls if 0 <= skull["x"] <= WIDTH and 0 <= skull["y"] <= HEIGHT]

        # Move the demon of the dark closer to the player
        # ... (retain your existing code for moving the demon)


    
    elif level == MAGMA_MONSTER_LEVEL:
        #make the magma monster
        #draw a circle for the magma monster's head
        pygame.draw.circle(screen, (255, 255, 255), (magma_monsterX, magma_monsterY), 100)
        #draw a rectangle for the magma monster's body
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(magma_monsterX-100, magma_monsterY, 200, 200))
        #draw a circle for the magma monster's left eye
        pygame.draw.circle(screen, (255, 255, 255), (magma_monsterX-50, magma_monsterY-50), 20)
        #draw a circle for the magma monster's right eye
        pygame.draw.circle(screen, (255, 255, 255), (magma_monsterX+50, magma_monsterY-50), 20)
        #draw a circle for the magma monster's left pupil
        pygame.draw.circle(screen, (0, 0, 0), (magma_monsterX-50, magma_monsterY-50), 10)
        #draw a circle for the magma monster's right pupil
        pygame.draw.circle(screen, (0, 0, 0), (magma_monsterX+50, magma_monsterY-50), 10)
        #draw a circle for the magma monster's mouth
        pygame.draw.circle(screen, (255, 0, 0), (magma_monsterX, magma_monsterY+50), 30)

        #move the magma monster closer to the player diagonally
        if magma_monsterX < playerX and magma_monsterY < playerY:
            magma_monsterX += 1
            magma_monsterY += 1
        elif magma_monsterX > playerX and magma_monsterY > playerY:
            magma_monsterX -= 1
            magma_monsterY -= 1
        elif magma_monsterX < playerX and magma_monsterY > playerY:
            magma_monsterX += 1
            magma_monsterY -= 1
        elif magma_monsterX > playerX and magma_monsterY < playerY:
            magma_monsterX -= 1
            magma_monsterY += 1
        #also move horizontally and vertically
        elif magma_monsterX < playerX:
            magma_monsterX += 1
        elif magma_monsterX > playerX:
            magma_monsterX -= 1
        elif magma_monsterY < playerY:
            magma_monsterY += 1
        elif magma_monsterY > playerY:
            magma_monsterY -= 1

        #if magma monster touches player, decrease health
        if magma_monsterX == playerX and magma_monsterY == playerY:
            health -= 5
            print(health)     

        #display magma monster health near the bottom of the screen
        display_text = pygame.font.Font(None, 36).render("Magma Monster Health: " + str(magma_monster_health), True, (255, 255, 255))
        screen.blit(display_text, (0, MAX_SCREEN_Y-66))
        







        #move the demon of the dark closer to the player horizontally and vertically and diagonally by 3 units
        if demon_of_the_darkX < playerX and demon_of_the_darkY < playerY:
            demon_of_the_darkX += 3
            demon_of_the_darkY += 3
        elif demon_of_the_darkX > playerX and demon_of_the_darkY > playerY:
            demon_of_the_darkX -= 3
            demon_of_the_darkY -= 3
        elif demon_of_the_darkX < playerX and demon_of_the_darkY > playerY:
            demon_of_the_darkX += 3
            demon_of_the_darkY -= 3
        elif demon_of_the_darkX > playerX and demon_of_the_darkY < playerY:
            demon_of_the_darkX -= 3
            demon_of_the_darkY += 3
        elif demon_of_the_darkX < playerX:
            demon_of_the_darkX += 3
        elif demon_of_the_darkX > playerX:
            demon_of_the_darkX -= 3
        elif demon_of_the_darkY < playerY:
            demon_of_the_darkY += 3
        elif demon_of_the_darkY > playerY:
            demon_of_the_darkY -= 3

       

        #add health bar for demon of the dark
        

        pygame.draw.rect(screen, (0, 100, 0), pygame.Rect(0, MAX_SCREEN_Y-30, demon_of_the_dark_health/10, 30))

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
    print_health = health
    max_print_health = 100
    if health > max_print_health:
        print_health = max_print_health
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(0, 0, print_health*10, 30))

    #draw score
    display_text = pygame.font.Font(None, 36).render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(display_text, (0, 0))

    #draw level
    display_text = pygame.font.Font(None, 36).render("Level: " + str(level), True, (255, 255, 255))
    screen.blit(display_text, (0, 30))

    

    




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

    #set level based on score
    if score == LEVEL_2_SCORE:
        level = 2
    elif score == LEVEL_3_SCORE:
        level = 3
    elif score == LEVEL_4_SCORE:
        level = 4
    elif score == LEVEL_5_SCORE:
        level = 5
    elif score == LEVEL_6_SCORE:
        level = 6
    elif score == LEVEL_7_SCORE:
        level = 7
    elif score == LEVEL_17_SCORE:
        level = 17
    elif score == LEVEL_956842987_SCORE:
        level = 956842987
    elif score == MAGMA_MONSTER_LEVEL:
        level = MAGMA_MONSTER_LEVEL

print(level)

pygame.quit()

