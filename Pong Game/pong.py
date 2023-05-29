# Pong Mini Project

import pygame, random, math

# User-defined functions

def main():
    # initialize all pygame modules (some need initialization)
    pygame.init()
    # create a pygame display window
    pygame.display.set_mode((500, 400))
    # set the title of the display window
    pygame.display.set_caption('Pong')   
    # get the display surface
    w_surface = pygame.display.get_surface() 
    # create a game object
    game = Game(w_surface)
    # start the main game loop by calling the play method on the game object
    game.play() 
    # quit pygame and clean up the pygame window
    pygame.quit() 

# User-defined classes

class Game:
    # An object in this class represents a complete game.

    def __init__(self, surface):
        # Initialize a Game.
        # - self is the Game to initialize
        # - surface is the display window surface object

        # === objects that are part of every game that we will discuss
        self.surface = surface
        self.bg_color = pygame.Color('black')

        self.FPS = 60
        self.game_Clock = pygame.time.Clock()
        self.close_clicked = False
        self.continue_game = True

        # === game specific objects
        self.score = 0       
        self.score1 = 0
        
        # create the ball and paddles 
        self.create_dots()
        self.paddle_increment = 10
        self.paddle = Paddle(60,160,10,50,'white',self.surface)   
        self.paddle2 = Paddle(430,160,10,50,'white',self.surface) 

    def create_dots(self):
        # create the ball with its parameters 
        self.small_dot = Dot('white', 5, [250, 200], [2, 1], self.surface)  

    def play(self):
        # Play the game until the player presses the close box.
        # - self is the Game that should be continued or not.

        while not self.close_clicked:  # until player clicks close box
            # play frame
            self.handle_events()
            self.draw()            
            if self.continue_game:
                self.update()
                self.paddle_hit()
                self.gameover()
            self.game_Clock.tick(self.FPS) # run at most with FPS Frames Per Second 

    def handle_events(self):
        # Handle each user event by changing the game state appropriately.
        # - self is the Game whose events will be handled

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.close_clicked = True
            elif event.type == pygame.KEYDOWN:    
                self.handle_key_down(event)      
            elif event.type == pygame.KEYUP:     
                self.handle_key_up(event)
                
    def handle_key_down(self,event):
        # reponds to KEYDOWN event
        # - self is the Game object
        if event.key == pygame.K_a:      
            self.paddle.set_vertical_velocity(self.paddle_increment)     
        elif event.key == pygame.K_q:
            self.paddle.set_vertical_velocity(-self.paddle_increment)
        elif event.key == pygame.K_l:
            self.paddle2.set_vertical_velocity(self.paddle_increment) 
        elif event.key == pygame.K_p:
            self.paddle2.set_vertical_velocity(-self.paddle_increment)        
            
    def handle_key_up(self,event):
        # responds to KEYUP event
        # - self is the Game object
        if event.key == pygame.K_a:
            self.paddle.set_vertical_velocity(0)
        elif event.key == pygame.K_q:
            self.paddle.set_vertical_velocity(0)  
        elif event.key == pygame.K_l:
            self.paddle2.set_vertical_velocity(0)
        elif event.key == pygame.K_p:
            self.paddle2.set_vertical_velocity(0)        

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw

        self.surface.fill(self.bg_color) # clear the display surface first
        self.small_dot.draw()
        self.draw_score()
        self.paddle.draw()
        self.paddle2.draw()
        pygame.display.update() # make the updated surface appear on the display

    def draw_score(self):
        score_string = str(self.score)
        score_string1 = str(self.score1)
        
        # step 1 create a font object
        font_size = 60
        fg_color = pygame.Color('white')
        font = pygame.font.SysFont('',font_size)
        
        # step 2 render the font
        text_box = font.render(score_string1, True,fg_color,self.bg_color)
        text_box1 = font.render(score_string, True,fg_color,self.bg_color)
        
        # step 3  compute the location 
        location = (0,0)
        location1 = (460, 0)
        
        # step 4 blit the source surface on the target surface at the specified location
        self.surface.blit(text_box,location)
        self.surface.blit(text_box1,location1)

    def update(self):
        # Update the game objects for the next frame.
        # - self is the Game to update

        self.small_dot.move()
        self.paddle.move()
        self.paddle2.move()
        
        # update the score if ball hit left or right edge
        if (self.small_dot.move() == True):
            self.score = self.score + 1
        if (self.small_dot.move() == False):
            self.score1 = self.score1 + 1        

    def paddle_hit(self):
        # Check if the paddles hit the ball
        # Reverse the x direction of the ball if hit
        if self.paddle2.collide(self.small_dot.centerc()):
            self.small_dot.reverse()
        if self.paddle.collide(self.small_dot.centerc()):
            self.small_dot.reverse()      
    
    def gameover(self):
        # Check if any player has won by scoring 11 points
        if (self.score == 11 or self.score1 == 11):
            self.continue_game = False 

class Dot:
    # An object in this class represents a Dot that moves 

    def __init__(self, dot_color, dot_radius, dot_center, dot_velocity, surface):
        # Initialize a Dot.
        # - self is the Dot to initialize
        # - color is the pygame.Color of the dot
        # - center is a list containing the x and y int
        #   coords of the center of the dot
        # - radius is the int pixel radius of the dot
        # - velocity is a list containing the x and y components
        # - surface is the window's pygame.Surface object

        self.color = pygame.Color(dot_color)
        self.radius = dot_radius
        self.center = dot_center
        self.velocity = dot_velocity
        self.surface = surface         

    def centerc(self):
        return (self.center[0] , self.center[1])
    
    def reverse(self):
        self.velocity[0] = -self.velocity[0]            

    def move(self):
        # Change the location of the Dot by adding the corresponding 
        # speed values to the x and y coordinate of its center
        # - self is the Dot

        size = self.surface.get_size()        
        for i in range(0,2):
            self.center[i] = (self.center[i] + self.velocity[i])
            if self.center[i] <= self.radius :       
                self.velocity[i] = -self.velocity[i]
                if (i == 0 and self.center[0] <= self.radius):
                    return True
                    
            if self.center[i] + self.radius >= size[i]:       
                self.velocity[i] = - self.velocity[i]
                if (i == 0 and self.center[0] + self.radius >= size[0]):
                    return False

    def draw(self):
        # Draw the dot on the surface
        # - self is the Dot
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)

class Paddle:
    # An object in this class represents a Paddle that moves

    def __init__(self,x,y,width,height,color,surface):
        # - self is the Paddle object
        # - x, y are the top left corner coordinates of the rectangle of type int
        # - width is the width of the rectangle of type int
        # - height is the heightof the rectangle of type int
        # - surface is the pygame.Surface object on which the rectangle is drawn

        self.rect = pygame.Rect(x,y,width,height)
        self.color = pygame.Color(color)
        self.surface = surface
        self.vertical_velocity = 0  
        
    def draw(self):
        # -self is the Paddle object to draw
        pygame.draw.rect(self.surface,self.color,self.rect)
        
    def set_vertical_velocity(self,vertical_distance):
        self.vertical_velocity = vertical_distance
        
    def move(self):
        # moves the paddle such that paddle does not move outside the window
        # - self is the Paddle object
        self.rect.move_ip(0 , self.vertical_velocity)
        if self.rect.bottom >= self.surface.get_height():     
            self.rect.bottom = self.surface.get_height()
        elif self.rect.top  <= 0:       
            self.rect.top = 0

    def collide(self,dot):
        # check if ball collides with paddle
        if (self.rect.collidepoint(dot[0], dot[1])):
            return True
        else:
            return False
    
main()