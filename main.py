import pygame
import player


BLACK = (255,255,255)

WHITE = (255, 255, 255)
WIDTH = 800
HEIGHT = 300
FPS = 3



class Game:
    def __init__(self):
        pygame.init()
        # Images
        self.background_img = pygame.image.load("assets/images/bg2.png")
        self.bg = pygame.image.load('assets/images/bg3.png')
        # Init
        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('FIGHTER')
        # Players
        self.player = player.Player(120, 85, 'player', 'scorpion_red_sprites', flip=False)
        self.all_sprite_list = pygame.sprite.Group()
        self.all_sprite_list.add(self.player)

    def run(self):
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_a:
                        self.player.go_left()
                        self.player.move = True
                    if event.key == pygame.K_d:
                        self.player.move = True
                        self.player.go_right()
                    if event.key == pygame.K_SPACE:
                        self.player.attack = True
                    if event.key == pygame.K_b:
                        self.player.ultra_attack = True

                if event.type == pygame.KEYUP:
                    if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                        self.player.stop()
            
            self.screen.fill(BLACK)
            self.screen.blit(self.background_img, [0, 0])

            self.screen.blit(self.bg, (0, 0))
            self.all_sprite_list.draw(self.screen)

            self.all_sprite_list.update()
            pygame.display.update()
            self.clock.tick(FPS)
        pygame.quit()


game = Game()
game.run()
