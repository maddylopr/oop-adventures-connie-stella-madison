import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Beat 'Em Up - Street Fighter Clone")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Clock to control FPS
clock = pygame.time.Clock()

# Load assets (placeholder for sprites)
def load_sprite(color, width, height):
    sprite = pygame.Surface((width, height))
    sprite.fill(color)
    return sprite

# Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, controls):
        super().__init__()
        self.image = load_sprite(RED, 50, 100)  # Placeholder player sprite
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Movement and state
        self.speed = 5
        self.dx = 0
        self.dy = 0
        self.controls = controls
        self.is_attacking = False

        # Health
        self.health = 100

    def handle_input(self, keys):
        # Movement keys
        self.dx, self.dy = 0, 0
        if keys[self.controls['left']]:
            self.dx = -self.speed
        if keys[self.controls['right']]:
            self.dx = self.speed
        if keys[self.controls['up']]:
            self.dy = -self.speed
        if keys[self.controls['down']]:
            self.dy = self.speed

        # Attack key
        if keys[self.controls['attack']]:
            self.is_attacking = True
        else:
            self.is_attacking = False

    def update(self, keys):
        self.handle_input(keys)
        self.rect.x += self.dx
        self.rect.y += self.dy

# Health Bar Function
def draw_health_bar(surface, x, y, health):
    pygame.draw.rect(surface, BLACK, (x, y, 200, 20))
    pygame.draw.rect(surface, RED, (x, y, 2 * health, 20))  # Scale health to bar length

# Game Loop
def main():
    # Player controls
    controls_p1 = {'left': pygame.K_a, 'right': pygame.K_d, 'up': pygame.K_w, 'down': pygame.K_s, 'attack': pygame.K_SPACE}
    controls_p2 = {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'up': pygame.K_UP, 'down': pygame.K_DOWN, 'attack': pygame.K_RETURN}

    # Create players
    player1 = Player(100, SCREEN_HEIGHT - 150, controls_p1)
    player2 = Player(600, SCREEN_HEIGHT - 150, controls_p2)

    # Sprite group
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player1, player2)

    # Main loop
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get key states
        keys = pygame.key.get_pressed()

        # Update
        all_sprites.update(keys)

        # Collision Detection (simple placeholder for hitboxes)
        if player1.is_attacking and player1.rect.colliderect(player2.rect):
            player2.health -= 1  # Reduce player 2 health

        if player2.is_attacking and player2.rect.colliderect(player1.rect):
            player1.health -= 1  # Reduce player 1 health

        # Draw
        screen.fill(WHITE)  # Clear screen
        all_sprites.draw(screen)

        # Draw health bars
        draw_health_bar(screen, 50, 50, player1.health)
        draw_health_bar(screen, 550, 50, player2.health)

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

if __name__ == "__main__":
    main()
