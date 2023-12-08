import pygame
import pygame.mixer as pygmixer
import sys
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, img_path, posx, posy, width, height, ratio_x, ratio_y):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.scale(self.image, (width, height)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = int(posx * ratio_x)
        self.rect.y = int(posy * ratio_y)
        self.rect.width = width
        self.rect.height = height
class Game:
    def __init__(self):
        pygame.init()
        pygmixer.init()

        self.screen_info = pygame.display.Info()
        self.screen_WIDTH, self.screen_HEIGHT = 1280, 720
        self.monitor_WIDTH, self.monitor_HEIGHT = self.screen_info.current_w, self.screen_info.current_h
        print(f"Current screen resolution of monitor:{self.monitor_WIDTH}x{self.monitor_HEIGHT}")
        print(f"Current game resolution:1280x720")

        self.gamefps = 60
        self.clock = pygame.time.Clock()
        self.fullscreen = False

        self.Window = pygame.display.set_mode((self.screen_WIDTH, self.screen_HEIGHT))
        pygame.display.set_caption("Super Mario Bros by Arhan Jain/FallDrop[ch] in pygame")

        self.bgimg = pygame.image.load("background1.png").convert()
        self.bgimgwidth = self.bgimg.get_width()
        self.biggerbgimg = pygame.transform.scale(self.bgimg, (self.monitor_WIDTH, self.monitor_HEIGHT))
        self.biggerbgimgwidth = self.biggerbgimg.get_width()
        self.smallerbgimg = pygame.transform.scale(self.bgimg, (1280, 720))
        self.current_bgimg = self.smallerbgimg
        self.scroll = 0
        self.playermoving = False
        self.playerrunning = False
        self.playerjumping = False
        self.playergroundpos = 515
        self.gravity = 16
        self.jump_height = 250
        self.jump_count = 0
        self.player_y_velocity = 0
        self.player_y = self.playergroundpos
        self.jump_key_pressed = False
        self.jump_max_count = 20
        self.on_ground = True

        self.bgmusic = True

        pygmixer.music.load("bgmusictheme.mp3")
        pygmixer.music.set_volume(1)

        if self.bgmusic:
            pygmixer.music.play(-1)
        elif not self.bgmusic:
            print("No background music to be played, reason: self.bgmusic set to false")

        self.jmpsndeffx = pygmixer.Sound("mariojump.mp3")
        self.jmpsndeffx.set_volume(0.05)

        self.coincllcteffx = pygmixer.Sound("mariocoincollect.mp3")
        self.coincllcteffx.set_volume(0.4)

        if self.fullscreen == False:
            self.tiles = math.ceil(self.screen_WIDTH / self.bgimgwidth) + 1
            print(f"tiles for background: {math.ceil(self.tiles)}")
        else:
            self.tiles = math.ceil(self.screen_WIDTH / self.biggerbgimgwidth) + 1

        self.mysteryboximg = "mysterybox.png"
        self.marioidleimg = "marioidle.png"
        self.mariomovingimgs = ["mariomove1.png", "mariomove2.png", "mariomove3.png"]
        self.moveimgindex = 0

        self.last_sprite_update = pygame.time.get_ticks()
        self.sprite_update_interval = 100

        self.player = Player("marioidle.png", 200, self.playergroundpos, 60, 70, 1, 1)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

    def changespriteandredraw(self):            
        current_time = pygame.time.get_ticks()

        if current_time - self.last_sprite_update >= self.sprite_update_interval:
            if self.moveimgindex > 2:
                self.moveimgindex = 0
            
            self.mario = self.draw_mario(self.mariomovingimgs[self.moveimgindex], 200, self.player_y, 60, 70)
            pygame.display.update()

            self.moveimgindex += 1
            self.last_sprite_update = current_time
        
    def gamerun(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit(0)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F11:
                        self.fullscreentoggle()
                    elif event.key == pygame.K_d:
                        self.playermoving = True
                    elif event.key == pygame.K_l:
                        self.playerrunning = True
                    elif event.key == pygame.K_k and self.on_ground:
                        self.jmpsndeffx.play()
                        self.playerjumping = True
                        self.jump_key_pressed = True
                        self.on_ground = False

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        self.playermoving = False
                    elif event.key == pygame.K_l:
                        self.playerrunning = False
                    elif event.key == pygame.K_k and self.playerjumping:
                        self.jump_key_pressed = False
                        self.jump_count = 0
                        self.playerjumping = False

            if self.playermoving or self.playerrunning:
                if self.playermoving:
                    self.scroll -= 4
                    self.changespriteandredraw()
                if self.playerrunning:
                    self.scroll -= 8
                    self.changespriteandredraw()
            else:
                self.mario = self.draw_mario(self.marioidleimg, 200, self.player_y, 60, 70)

            if self.playerjumping:
                if self.jump_count == 0:
                    self.player_y_velocity = -0.1

                if self.jump_count < self.jump_max_count:
                    self.displacement = self.player_y_velocity * self.jump_count + 0.5 * self.gravity * self.jump_count ** 2
                    self.player_y = self.playergroundpos - min(self.displacement, self.jump_height)
                    self.jump_count += 1
                else:
                    self.jump_count = 0
                    self.playerjumping = False
            else:
                if self.player_y < self.playergroundpos:
                    self.player_y += self.gravity
                else:
                    self.player_y = self.playergroundpos
                    self.on_ground = True

            for i in range(0, self.tiles):
                if self.fullscreen == False:
                    self.Window.blit(self.current_bgimg, (i * self.bgimgwidth + self.scroll, 0))
                else:
                    self.Window.blit(self.current_bgimg, (i * self.biggerbgimgwidth + self.scroll, 0))

            if self.fullscreen == False:
                if abs(self.scroll) > self.bgimgwidth:
                    self.scroll = 0
            else:
                if abs(self.scroll) > self.biggerbgimgwidth:
                    self.scroll = 0

            self.draw_squarectangleimg(self.mysteryboximg, 90, 90, 60, 60)
            self.draw_squarectangleimg(self.mysteryboximg, 330, 20, 60, 60)
            self.draw_squarectangleimg(self.mysteryboximg, 730, 130, 60, 60)
            self.draw_squarectangleimg(self.mysteryboximg, 1030, 230, 60, 60)

            self.all_sprites.draw(self.Window)
            
            pygame.display.update()
            self.clock.tick(self.gamefps)
    
    def fullscreentoggle(self):
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            self.Window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.current_bgimg = self.biggerbgimg
            print(f"Current game resolution: {self.monitor_WIDTH}x{self.monitor_HEIGHT}")
        else:
            self.Window = pygame.display.set_mode((self.screen_WIDTH, self.screen_HEIGHT))
            self.current_bgimg = self.smallerbgimg
            print(f"Current game resolution: 1280x720")

    def bgimgresize(self):
        if self.fullscreen == False:
            self.Window.blit(self.smallerbgimg, (0,0))
        elif self.fullscreen == True:
            self.Window.blit(self.biggerbgimg, (0,0))

    def draw_mario(self, img_path, posx, posy, width, height):
        self.player.image = pygame.image.load(img_path)
        ratio_x = self.Window.get_width() / self.screen_WIDTH
        ratio_y = self.Window.get_height() / self.screen_HEIGHT
        width = int(width * ratio_x)
        height = int(height * ratio_y)
        self.player.image = pygame.transform.scale(self.player.image, (width, height)).convert_alpha()
        self.player.rect = self.player.image.get_rect()
        self.player.rect.x = int(posx * ratio_x)
        self.player.rect.y = int(posy * ratio_y)
        self.player.rect.width = width
        self.player.rect.height = height
        self.all_sprites.draw(self.Window)
    
    def draw_squarectangleimg(self, img_path, posx, posy, width, height):
        self.img = pygame.image.load(img_path)
        ratio_x = self.Window.get_width() / self.screen_WIDTH
        ratio_y = self.Window.get_height() / self.screen_HEIGHT
        width = int(width * ratio_x)
        height = int(height * ratio_y)
        self.img = pygame.transform.scale(self.img, (width, height)).convert_alpha()
        self.rect = self.img.get_rect()
        self.rect.x = int(posx * ratio_x)
        self.rect.y = int(posy * ratio_y)
        self.rect.width = width
        self.rect.height = height
        self.Window.blit(self.img, (self.rect.x, self.rect.y))

if __name__ == "__main__":
    game = Game()
    game.gamerun()
    pygame.quit()
    quit()
    sys.exit(0)
