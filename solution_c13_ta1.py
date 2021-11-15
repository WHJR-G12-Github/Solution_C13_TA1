import pygame,random
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption('Infinite Flying Bird Game')
images={}
images["bg"] = pygame.image.load("bg1.png").convert_alpha()
images["ground"] = pygame.image.load("base.png").convert_alpha()
images["bird"] = pygame.image.load("bird.png").convert_alpha()
images["pipe"] = pygame.image.load("pipe.png").convert_alpha()
images["invertedpipe"]=pygame.transform.flip(images["pipe"], False, True)
groundx=0
speed=0
# Creating a variable 'score' and initializing it to 0
score=0
# Creating a variable 'state' and assigning the value "play" to it
state="play"
# Creating the font of style 'freesansbold.ttf' and size 20 and naming it 'score_font'
score_font=pygame.font.Font('freesansbold.ttf', 20)

class Bird:
    bird=pygame.Rect(100,250,30,30)
    

    def movedown(self):
        global speed
        gravity=0.2
        speed=speed+gravity
        self.bird.y=self.bird.y+speed
    def moveup(self):
        global speed
        speed=speed-5
    def display(self):
        screen.blit(images["bird"],self.bird)

class Pipe:
    def __init__(self,x):
        self.height=random.randint(150,400)
        self.tpipe=pygame.Rect(x,self.height-400,40,300)
        self.bpipe=pygame.Rect(x,self.height+150,40,300)
    def display(self):
      screen.blit(images["pipe"],self.bpipe)
      screen.blit(images["invertedpipe"],self.tpipe)
    def move(self):
        self.tpipe.x-=2
        self.bpipe.x-=2
        # Checking if 'self.tpipe.x' is less than -40
        if self.tpipe.x<-40:
            # Assigning a value greater than game screen width to 'self.tpipe.x'
            self.tpipe.x=450
            # Assigning a value greater than game screen width to 'self.bpipe.x'
            self.bpipe.x=450
            # Assigning a random value from 150 to 400 to 'self.height'
            self.height=random.randint(150,400)
            # Assigning 'self.height-400' to 'self.tpipe.y'
            self.tpipe.y=self.height-400
            # Assigning 'self.height+150' to 'self.bpipe.y'
            self.bpipe.y=self.height+150
bird1=Bird()
pipe1=Pipe(250)
while True:  
  
  screen.blit(images["bg"],[0,0])
  # Creating the text to be displayed for score using 'score_font' and naming it 'score_text'
  score_text=score_font.render("Score:"+str(score), True, (0,0,255))
  # Displaying 'score_text' at the location [10,10]
  screen.blit(score_text,[10,10])
  # The following code is moved inside the condition if state == "play":
  #groundx-=5
  #if groundx<-450:
      #groundx=0
  # The code till the previous line has been moved
  screen.blit(images["ground"],[groundx,550])
  bird1.movedown()
  bird1.display()
  pipe1.display()
  pipe1.move()
  # Checking if the value of 'state' is "play"
  if state=="play":
      # Moving the code to move the ground towards left infinitely
      groundx-=5
      if groundx<-450:
       groundx=0
      
      
         
  
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
        pygame.quit()
  
    if event.type==pygame.KEYDOWN:
        # Adding the condition to check whether the value of 'state' is "play"
        if event.key==pygame.K_SPACE and state=="play":
            bird1.moveup()  
  
  
  
  pygame.display.update()
  
  pygame.time.Clock().tick(30)
