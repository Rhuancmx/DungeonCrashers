from PPlay.window import *
from PPlay.sprite import *
from PPlay.collision import *
###################### Variables and Sprites ######################

############################################

###################### Collisions ######################

def sceneryCollision(objectPosX,objectPosY,actor):
    if objectPosX >= 573 and objectPosY >= 200 and objectPosY <= 315:
        return True
    if objectPosX >= 580 and objectPosY >= 315 and objectPosY <= 327:
        return True
    if objectPosX >= 593 and objectPosY >= 327 and objectPosY <= 380:
        return True
    if objectPosX >= 550 and objectPosY >= 186 and objectPosY <= 243:
        return True
    if objectPosX >= 561 and objectPosY >= 243 and objectPosY <= 257:
        return True
    if objectPosX >= 535 and objectPosY >= 176 and objectPosY <= 186:
        return True
    if objectPosX >= 521 and objectPosY <= 178:
        return True
    if objectPosX >= 508 and objectPosY <= 165:
        return True
    if objectPosX >= 499 and objectPosY <= 150:
        return True
    if objectPosX >= 486 and objectPosY <= 140:
        return True
    if objectPosX >= 479 and objectPosY <= 125:
        return True
    if objectPosX >= 519 and objectPosX <= 551 and objectPosY >= 234 and objectPosY <= 271:
        return True
    if objectPosY >= 338-actor.height and objectPosY<=418 and objectPosX<=135:
        return True
    if objectPosY<=305 and objectPosY>=300-actor.height and objectPosX >=100 and objectPosX<=140:
        return True
    if objectPosX>=128 and objectPosX<=148 and objectPosY>=280-actor.height and objectPosY<=294:
        return True
    if objectPosX<=140 and objectPosY<=280 and objectPosY>=260-actor.height:
        return True
    if objectPosX<=150 and objectPosY<=256 and objectPosY>=234-actor.height:
        return True
    if objectPosX<=210 and objectPosY<=234 and objectPosY>=160-actor.height:
        return True
    if objectPosX>=210 and objectPosX<=242 and objectPosY<=160:
        return True
    if objectPosX>=250 and objectPosX<=280 and objectPosY<=180 and objectPosY>=168-actor.height:
        return True
    if objectPosY-actor.height >= objectPosX +135 and objectPosX>=285 and objectPosX<=300 and objectPosY>=420 and objectPosY<=435:
        return True
    if objectPosX <= 100:
        return True
    if objectPosX >= 543 and objectPosX <= 600 and objectPosY >= 379:
        return True
    if objectPosY >= 401 and objectPosX <= 544:  ###Fundo
        return True
    if objectPosX >= 519 and objectPosX <= 551 and objectPosY >= 234 and objectPosY <= 271:
        return True
    if objectPosY<=105:
        return True
    if objectPosX>=272-actor.width and objectPosX<=302 and objectPosY>=134-actor.height and objectPosY<=160:
        return True
    if objectPosX>=240-actor.width and objectPosX<=265 and objectPosY>=140-actor.height and objectPosY<=157:
        return True
    if objectPosX>=356-actor.width and objectPosX<=395 and objectPosY>=127-actor.height and objectPosY<=130:
        return True
    if objectPosY <=147 and objectPosX>=400 and objectPosX<=463:
        return True
    if objectPosY <=137 and objectPosX>=460 and objectPosX<=487:
        return True
    if objectPosX>=418-actor.width and objectPosX<=438 and objectPosY>=321-actor.height and objectPosY<=344:
        return True
    if objectPosX>=488-actor.width and objectPosX<=508 and objectPosY>=361-actor.height and objectPosY<=379:
        return True
    if objectPosX>=568-actor.width and objectPosX<=590 and objectPosY>=329-actor.height and objectPosY<=349:
        return True
    if objectPosX>=239-actor.width and objectPosX<=268 and objectPosY>=280-actor.height and objectPosY<=344:
        return True
    if objectPosX>=215-actor.width and objectPosX<=227 and objectPosY>=281-actor.height and objectPosY<=340:
        return True
    if objectPosX>=239-actor.width and objectPosX<=262 and objectPosY>=259-actor.height and objectPosY<=283:
        return True
    if objectPosX >= 256 - actor.width and objectPosX <= 284 and objectPosY >= 279 - actor.height and objectPosY <= 287:
        return True
    if objectPosX >= 262 - actor.width and objectPosX <= 276 and objectPosY >= 274 - actor.height and objectPosY <= 279:
        return True
    if objectPosX >= 263 - actor.width and objectPosX <= 272-actor.width and objectPosY >= 260 - actor.height and objectPosY <= 268:
        return True
    if objectPosX >= 287 - actor.width and objectPosX <= 305 and objectPosY >= 309 - actor.height and objectPosY <= 333:
        return True
    if objectPosX >= 270 - actor.width and objectPosX <= 282 and objectPosY >= 295 - actor.height and objectPosY <= 335:
        return True
    if objectPosY <=133 and objectPosX<=285:
        return True
    if objectPosX >= 399 - actor.width and objectPosX <= 415 and objectPosY >= 143 - actor.height and objectPosY <= 147:
        return True
    if objectPosX >= 293 - actor.width and objectPosX <= 307 and objectPosY >= 256 - actor.height and objectPosY <= 255:
        return True
    
def collidedLake(objectPosX,objectPosY,actor):
    if objectPosX>=264-actor.width and objectPosX<=416 and objectPosY>=205-actor.height and objectPosY<=229:
        return True
    if objectPosX >= 277 - actor.width and objectPosX <= 403 and objectPosY >= 192 - actor.height and objectPosY <= 200:
        return True
    if objectPosX >= 288 - actor.width and objectPosX <= 350 and objectPosY >= 184 - actor.height and objectPosY <= 188:
        return True
    if objectPosX >= 301 - actor.width and objectPosX <= 336 and objectPosY >= 167 - actor.height and objectPosY <= 179:
        return True
    if objectPosX >= 285 - actor.width and objectPosX <= 427 and objectPosY >= 235 - actor.height and objectPosY <= 246:
        return True
    if objectPosX >= 310 - actor.width and objectPosX <= 395 and objectPosY >= 259 - actor.height and objectPosY <= 258:
        return True
    if objectPosX >= 362 - actor.width and objectPosX <= 382 and objectPosY >= 262 - actor.height and objectPosY <= 270:
        return True
    if objectPosX >= 300 - actor.width and objectPosX <= 370 and objectPosY >= 270 - actor.height and objectPosY <= 260:
        return True
############################################

###################### Drawing ######################

def drawScene(objects):
    for item in objects:
        item.draw()
        item.update()

############################################

###################### Player mechanics ######################
class player:
    def __init__(self,life):
        self.parado_direita = Sprite("Actors/player_parado_direita.png",2)
        self.parado_esquerda = Sprite("Actors/player_parado_esquerda.png",2)
        self.andando_direita = Sprite("Actors/player_walk_direita.png",8)
        self.andando_esquerda = Sprite("Actors/player_walk_esquerda.png",8)
        self.life = life

        # Player invencível
        self.parado_direitaI = Sprite("Actors/player_parado_direita_Inv.png", 4)
        self.parado_esquerdaI = Sprite("Actors/player_parado_esquerda_Inv.png", 4)
        self.andando_direitaI = Sprite("Actors/player_andando_direita_Inv.png", 16)
        self.andando_esquerdaI = Sprite("Actors/player_andando_esquerda_Inv.png", 16)
        self.invincible = 0
        self.time_invincible = 0

def getLife(life):
    lifePNG = Sprite("Actors/Life.png",1)
    if life > 1:
        prim = Sprite("Actors/Life-full.png",1)
    elif life == 1:
        prim = Sprite("Actors/Life-half.png", 1)
    else:
        prim = Sprite("Actors/Life-Empty.png", 1)
    if life > 3:
        seg = Sprite("Actors/Life-full.png",1)
    elif life == 3:
        seg = Sprite("Actors/Life-half.png", 1)
    else:
        seg = Sprite("Actors/Life-Empty.png", 1)
    if life > 5:
        ter = Sprite("Actors/Life-full.png",1)
    elif life == 5:
        ter = Sprite("Actors/Life-half.png", 1)
    else:
        ter = Sprite("Actors/Life-Empty.png", 1)
    prim.y = seg.y = ter.y = lifePNG.y = 25
    prim.x = 50 + prim.width
    seg.x = 100 + prim.width
    ter.x = 150 + prim.width
    lifePNG.x = 10
    prim.draw()
    seg.draw()
    ter.draw()
    lifePNG.draw()


    return prim,seg, ter

def playerCollideEnemies(player,sprite,enemies,janela):
    if player.invincible:
        if player.time_invincible > 2:
            player.invincible = 0
            player.time_invincible = 0
        else:
            player.time_invincible += janela.delta_time()
    else:
        for enemy in enemies:
            if Collision.collided(sprite,enemy[2]):
                player.life -= 1
                player.invincible = 1
                
def getPlayerSprite(direction, player, teclado):
    if not player.invincible:
        if teclado.key_pressed("LEFT"):
            return (player.andando_esquerda)
        elif teclado.key_pressed("RIGHT"):
            return (player.andando_direita)
        else:
            if direction == "r":
                return (player.parado_direita)
            elif direction == "l":
                return (player.parado_esquerda)
    else:
        if teclado.key_pressed("LEFT"):
            return (player.andando_esquerdaI)
        elif teclado.key_pressed("RIGHT"):
            return (player.andando_direitaI)
        else:
            if direction == "r":
                return (player.parado_direitaI)
            elif direction == "l":
                return (player.parado_esquerdaI)

def getLastDirection(direction, teclado):
    if teclado.key_pressed("LEFT"):
        direction = "l"
    elif teclado.key_pressed("RIGHT"):
        direction = "r"
    return direction

def movePlayer(initialx, initialy, player, janela, teclado):
    player_pos_x = initialx
    player_pos_y = initialy
    if teclado.key_pressed("LEFT"):
        player_vel_x = -100
    elif teclado.key_pressed("RIGHT"):
        player_vel_x = 100
    else:
        player_vel_x = 0
    if teclado.key_pressed("UP"):
        player_vel_y = -100
    elif teclado.key_pressed("DOWN"):
        player_vel_y = 100
    else:
        player_vel_y = 0
    if not sceneryCollision(player_pos_x + player_vel_x * janela.delta_time(), player_pos_y, player) and not collidedLake(player_pos_x + player_vel_x * janela.delta_time(), player_pos_y, player):
        player_pos_x = player_pos_x + player_vel_x*janela.delta_time()
    if not sceneryCollision(player_pos_x, player_pos_y + player_vel_y * janela.delta_time(), player) and not collidedLake(player_pos_x, player_pos_y + player_vel_y * janela.delta_time(), player):
        player_pos_y = player_pos_y + player_vel_y*janela.delta_time()
    return([player_pos_x,player_pos_y])

def shoot(initialx,initialy,direction, teclado, tiros):
    tiroX = initialx
    tiroY = initialy
    if teclado.key_pressed("UP"):
        direction = "u"
        tiro = Sprite("Actors/tiroVerticalCima.png", 4)
    elif teclado.key_pressed("DOWN"):
        direction = "d"
        tiro = Sprite("Actors/tiroVerticalBaixo.png",4)
    else:
        direction = getLastDirection(direction, teclado)
        if direction == "r":
            tiro = Sprite("Actors/tiroLateralDireita.png", 4)
        else:
            tiro = Sprite("Actors/tiroLateralEsquerda.png", 4)
    tiros.append([tiro, tiroX, tiroY, direction])
    return (tiros)

def explosaoGen(posX,posY,explosoes):
    explosao = Sprite("Actors/explosao.png", 8)
    explosao.set_total_duration(1000)
    explosao.set_position(posX,posY)
    explosoes.append([explosao,0])

def tirosUpdate(tiros, velTiro, janela, explosoes, enemies):
    for tiro in tiros:
        tiro[0].set_position(tiro[1], tiro[2])
        tiro[0].set_total_duration(1000)
        tiro[0].update()
        tiro[0].draw()
        if tiro[3] == "u":
            tiro[2] = tiro[2] - velTiro * janela.delta_time()
        elif tiro[3] == "d":
            tiro[2] = tiro[2] + velTiro * janela.delta_time()
        elif tiro[3] == "l":
            tiro[1] = tiro[1] - velTiro*janela.delta_time()
        elif tiro[3] == "r":
            tiro[1] = tiro[1] + velTiro * janela.delta_time()
        if sceneryCollision(tiro[1], tiro[2], tiro[0]):
            explosaoGen(tiro[1],tiro[2], explosoes)
            tiros.remove(tiro)

def explosoesUpdate(explosoes, janela):
    for explosao in explosoes:
        explosao[1] += janela.delta_time()
        explosao[0].draw()
        explosao[0].update()
        if explosao[1]>=1:
            explosoes.remove(explosao)

############################################

###################### Enemy mechanics ######################
class enemy:
    def __init__(self, direita, esquerda):
        self.direita = direita
        self.esquerda = esquerda
        self.height = direita.height
        self.width = direita.width

def getMaximum(initialEnemyX,initialEnemyY, playerX, playerY, Enemy):
    enemyPosXMaximum = initialEnemyX
    enemyPosYMaximum = initialEnemyY
    while (not sceneryCollision(enemyPosXMaximum, enemyPosYMaximum, Enemy)):
        if initialEnemyX > playerX:
            enemyPosXMaximum = enemyPosXMaximum - 40
            if enemyPosXMaximum < playerX:
                break
        elif initialEnemyX < playerX:
            enemyPosXMaximum = enemyPosXMaximum + 40
            if enemyPosXMaximum > playerX:
                break
        if initialEnemyY > playerY:
            enemyPosYMaximum = enemyPosYMaximum -40
            if enemyPosYMaximum < playerY:
                break
        elif initialEnemyY < playerY:
            enemyPosYMaximum = enemyPosYMaximum + 40
            if enemyPosYMaximum > playerY:
                break
    return([enemyPosXMaximum,enemyPosYMaximum])

def moveEnemy(playerX, playerY, initialEnemyX, initialEnemyY, Enemy, janela):
    enemyPosX = initialEnemyX
    enemyPosY = initialEnemyY
    if initialEnemyX >= playerX:
        velX = -40
        sprite = Enemy.esquerda
    elif initialEnemyX < playerX:
        velX = 40
        sprite = Enemy.direita
    if initialEnemyY >= playerY:
        velY = -40
    elif initialEnemyY < playerY:
        velY = 40
    if not sceneryCollision(enemyPosX + velX * janela.delta_time(), enemyPosY, Enemy) and not collidedLake(enemyPosX + velX * janela.delta_time(), enemyPosY, Enemy):
        enemyPosX = enemyPosX + velX*janela.delta_time()
    if not sceneryCollision(enemyPosX, enemyPosY + velY * janela.delta_time(), Enemy) and not collidedLake(enemyPosX, enemyPosY + velY * janela.delta_time(), Enemy):
        enemyPosY = enemyPosY+ velY*janela.delta_time()
    return([enemyPosX, enemyPosY, sprite, Enemy])

def updateEnemyPosition(initialx,initialy,enemies, tiros, explosoes, janela):
    for enemy in enemies:
        enemy[0], enemy[1], enemy[2] = moveEnemy(initialx,initialy,enemy[0],enemy[1], enemy[3],janela)[0], moveEnemy(initialx,initialy,enemy[0],enemy[1],enemy[3],janela)[1], moveEnemy(initialx,initialy,enemy[0],enemy[1],enemy[3], janela)[2]
        enemy[2].set_position(enemy[0],enemy[1])
        enemy[2].set_total_duration(1000)
        enemy[2].draw()
        enemy[2].update()
        for tiro in tiros:
            if Collision.collided(enemy[2], tiro[0]):
                tiros.remove(tiro)
                enemies.remove(enemy)
                explosaoGen(enemy[0], enemy[1], explosoes)
