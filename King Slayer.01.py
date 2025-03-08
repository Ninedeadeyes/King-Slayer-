import pygame, math,random

pygame.init()

class Game:
    def __init__(self):
        self.gold=0
        self.damage=0
        self.gold_per_click=1
        self.damage_per_click=1
        self.castle_new_hp=300
        self.castle_defeated=0
        self.castle_hitpoints=300
        self.castle_image=pygame.image.load("assets/castle.png").convert_alpha()
        self.castle_rect=self.castle_image.get_rect(center=(screen.get_width()/2,screen.get_height()/2+150))
        
        self.health_bar_x = 130  # Position of health bar
        self.health_bar_y = 815  # Position below castle info
        self.health_bar_w = 200  # Width of health bar
        self.health_bar_h = 18   # Height of health bar
        
        # Castle shake properties
        self.castle_shake_intensity = 0
        self.castle_shake_duration = 0
        self.original_castle_pos = None

        self.button_font=pygame.font.Font("assets/font2.ttf",18)
        self.button_title_font=pygame.font.Font("assets/font3.ttf",18)
        self.current_castle_name= " War Fortress of the Mad Goblin King "

        self.clicked=False

        self.weapon_upgrade_rect=pygame.Rect(270,110,260,140)
        self.weapon_upgrade_cost=5
        self.weapon_upgrade_count=0

        self.demon_passive_income_rect = pygame.Rect(270, 270, 260, 140)  # Position left of weapon upgrade
        self.demon_passive_income_cost = 15  # Starting cost
        self.demon_damage_per_second = 0      # Current passive income rate

        self.orc_passive_income_rect = pygame.Rect(570, 110, 220, 140)  # Position left of weapon upgrade
        self.orc_passive_income_cost = 10  # Starting cost
        self.orc_damage_per_second = 0      # Current passive income rate
        self.orcs=0

        self.goblin_passive_income_rect = pygame.Rect(10, 110, 220, 140)  # Position left of weapon upgrade
        self.goblin_passive_income_cost = 10  # Starting cost
        self.goblin_gold_per_second = 0      # Current passive income rate
        self.goblins=0

        self.ratling_passive_income_rect = pygame.Rect(10, 270, 220, 140)  # Position left of weapon upgrade
        self.ratling_passive_income_cost = 1000  # Starting cost
        self.ratling_gold_per_second = 0      # Current passive income rate
        self.ratlings=0

        self.kobold_passive_income_rect = pygame.Rect(10, 430, 220, 140)  # Position left of weapon upgrade
        self.kobold_passive_income_cost = 10000  # Starting cost
        self.kobold_gold_per_second = 0      # Current passive income rate
        self.kobolds=0

        self.orc_passive_income_rect = pygame.Rect(570, 110, 220, 140)  # Position left of weapon upgrade
        self.orc_passive_income_cost = 2   # Starting cost
        self.orc_damage_per_second = 0      # Current passive income rate
        self.orcs=0

        self.troll_passive_income_rect = pygame.Rect(570, 270, 220, 140)  # Position left of weapon upgrade
        self.troll_passive_income_cost = 100  # Starting cost
        self.troll_damage_per_second = 0      # Current passive income rate
        self.trolls=0

        self.knight_passive_income_rect = pygame.Rect(570, 430, 220, 140)  # Position left of weapon upgrade
        self.knight_passive_income_cost = 12000  # Starting cost
        self.knight_damage_per_second = 0      # Current passive income rate
        self.knights=0

        self.game_over=False

    def display_demon_passive_damage_upgrade(self):
        demon_title = self.button_title_font.render(" Azathoth: The 'Blind Idiot God'", True, "black")
        demon_passive_attack_display = self.button_font.render(
            f"DPS: {self.demon_damage_per_second}", True, "black")
        
        demon_passive_cost_display = self.button_font.render(
            f"Summon Cost: {int(self.demon_passive_income_cost)} Kings Skulls", True, "black")
        
        pygame.draw.rect(screen, "grey", self.demon_passive_income_rect, border_radius=(15))
        screen.blit(demon_title,(270,280))
        screen.blit(demon_passive_attack_display, (270, 310))
        screen.blit(demon_passive_cost_display, (270, 340))
    
    def display_orc_passive_damage_upgrade(self):
        orc_title = self.button_title_font.render("Orc Berserker", True, "black")
        orc_count=self.button_font.render( 
             f"Orcs: {self.orcs}", True, "black")
        orc_passive_attack_display = self.button_font.render(
            f"DPS: {self.orc_damage_per_second}", True, "black")
        orc_passive_cost_display = self.button_font.render(
            f"Upgrade Cost: {int(self.orc_passive_income_cost)}", True, "black")
        
        pygame.draw.rect(screen, "grey", self.orc_passive_income_rect, border_radius=(15))
        screen.blit(orc_title,(575,130))
        screen.blit(orc_count,(575,180))
        screen.blit(orc_passive_attack_display, (575, 200))
        screen.blit(orc_passive_cost_display, (575, 220))

    def display_troll_passive_damage_upgrade(self):
        troll_title = self.button_title_font.render("Doom Troll", True, "black")
        troll_count=self.button_font.render( 
             f"Trolls: {self.trolls}", True, "black")
        troll_passive_attack_display = self.button_font.render(
            f"DPS: {self.troll_damage_per_second}", True, "black")
        troll_passive_cost_display = self.button_font.render(
            f"Upgrade Cost: {int(self.troll_passive_income_cost)}", True, "black")
        
        pygame.draw.rect(screen, "grey", self.troll_passive_income_rect, border_radius=(15))
        screen.blit(troll_title,(575,280))
        screen.blit(troll_count,(575,320))
        screen.blit(troll_passive_attack_display, (575, 340))
        screen.blit(troll_passive_cost_display, (575, 360))

    def display_knight_passive_damage_upgrade(self):
        knight_title = self.button_title_font.render("Death Knight", True, "black")
        knight_count=self.button_font.render( 
             f"knights: {self.knights}", True, "black")
        knight_passive_attack_display = self.button_font.render(
            f"DPS: {self.knight_damage_per_second}", True, "black")
        knight_passive_cost_display = self.button_font.render(
            f"Upgrade Cost: {int(self.knight_passive_income_cost)}", True, "black")
        
        pygame.draw.rect(screen, "grey", self.knight_passive_income_rect, border_radius=(15))
        screen.blit(knight_title,(575,450))
        screen.blit(knight_count,(575,490))
        screen.blit(knight_passive_attack_display, (575, 510))
        screen.blit(knight_passive_cost_display, (575,530))

    def display_kobold_passive_income_upgrade(self):
        kobold_title = self.button_title_font.render("Kobold Gold Miner", True, "black")
        kobold_count=self.button_font.render( 
             f"kobolds: {self.kobolds}", True, "black")
        kobold_passive_income_display = self.button_font.render(
            f"Gold per second: {self.kobold_gold_per_second}", True, "black")
        kobold_passive_cost_display = self.button_font.render(
            f"Upgrade Cost: {int(self.kobold_passive_income_cost)}", True, "black")
        
        pygame.draw.rect(screen, "grey", self.kobold_passive_income_rect, border_radius=(15))
        screen.blit(kobold_title,(15, 450))
        screen.blit(kobold_count,(15,490))
        screen.blit(kobold_passive_income_display, (15, 510))
        screen.blit(kobold_passive_cost_display, (15, 530))

    def display_ratling_passive_income_upgrade(self):
        ratling_title = self.button_title_font.render("Ratling Loan Shark", True, "black")
        ratling_count=self.button_font.render( 
             f"Ratlings: {self.ratlings}", True, "black")
        ratling_passive_income_display = self.button_font.render(
            f"Gold per second: {self.ratling_gold_per_second}", True, "black")
        ratling_passive_cost_display = self.button_font.render(
            f"Upgrade Cost: {int(self.ratling_passive_income_cost)}", True, "black")
        
        pygame.draw.rect(screen, "grey", self.ratling_passive_income_rect, border_radius=(15))
        screen.blit(ratling_title,(15, 280))
        screen.blit(ratling_count,(15,320))
        screen.blit(ratling_passive_income_display, (15, 340))
        screen.blit(ratling_passive_cost_display, (15, 360))
    
    def display_goblin_passive_income_upgrade(self):
        goblin_title = self.button_title_font.render("Goblin Fungus", True, "black")
        goblin_title2 = self.button_title_font.render("Farmer", True, "black")
        goblin_count=self.button_font.render( 
             f"Goblins: {self.goblins}", True, "black")
        goblin_passive_income_display = self.button_font.render(
            f"Gold per second: {self.goblin_gold_per_second}", True, "black")
        goblin_passive_cost_display = self.button_font.render(
            f"Upgrade Cost: {int(self.goblin_passive_income_cost)}", True, "black")
        
        pygame.draw.rect(screen, "grey", self.goblin_passive_income_rect, border_radius=(15))
        screen.blit(goblin_title,(15, 130))
        screen.blit(goblin_title2,(15, 150))
        screen.blit(goblin_count,(15,180))
        screen.blit(goblin_passive_income_display, (15, 200))
        screen.blit(goblin_passive_cost_display, (15, 220))

    def update_castle_shake(self):
        if self.castle_shake_duration > 0:
            # Calculate shake offset using sine waves for smooth motion
            x_offset = math.sin(pygame.time.get_ticks() * 0.1) * self.castle_shake_intensity
            y_offset = math.cos(pygame.time.get_ticks() * 0.05) * self.castle_shake_intensity
            
            # Apply shake offset to castle position
            new_center = (
                self.original_castle_pos[0] + x_offset,
                self.original_castle_pos[1] + y_offset
            )
            self.castle_rect.center = new_center
            
            # Reduce shake intensity over time
            self.castle_shake_intensity *= 0.95
            self.castle_shake_duration -= 1
            
            # Reset position when shake ends
            if self.castle_shake_duration <= 0:
                self.castle_rect.center = self.original_castle_pos
                self.castle_shake_intensity = 0

    def draw_health_bar(self, surface):
        # Calculate health ratio
        ratio = self.castle_hitpoints / self.castle_new_hp
        
        # Draw background red rectangle
        pygame.draw.rect(surface, "red", 
                        (self.health_bar_x, self.health_bar_y, 
                         self.health_bar_w, self.health_bar_h,),border_radius=(5))
        
        # Draw green health bar based on current hp
        pygame.draw.rect(surface, "green",
                        (self.health_bar_x, self.health_bar_y,
                         self.health_bar_w * ratio, self.health_bar_h),border_radius=(5))

    def axe_cursor(self):
        pygame.mouse.set_visible(False)
        original_cursor = pygame.image.load("assets/axe.png").convert_alpha()
        if self.castle_rect.collidepoint(self.mouse_pos):
             if pygame.mouse.get_pressed()[0]:
                 original_cursor = pygame.image.load("assets/axe2.png").convert_alpha()

        width = int(original_cursor.get_width() /3)
        height = int(original_cursor.get_height() /3)
        
        self.new_cursor = pygame.Surface((width, height), pygame.SRCALPHA)  
           
        scaled_surface = pygame.transform.smoothscale(                  
            original_cursor,                                            
            (width, height),
            self.new_cursor                                             
        )
        
        self.new_cursor.blit(scaled_surface, (0, 0))   # sticker (scaled_surface) on a peice of paper (self.new_cursor)
        screen.blit(self.new_cursor, self.mouse_pos)   # putting that piece of paper with the sticker onto the screen 

    def display_weapon_upgrade(self):
        self.weapon_title=self.button_title_font.render("Rusty Hand Axe",True,"black")
        if self.weapon_upgrade_count>=2 and self.weapon_upgrade_count<=5:
                            self.weapon_title=self.button_title_font.render("Wood Axe",True,"black")
        elif self.weapon_upgrade_count>=6 and self.weapon_upgrade_count<=10:
                            self.weapon_title=self.button_title_font.render("Steel Axe",True,"black")
        elif self.weapon_upgrade_count>=6 and self.weapon_upgrade_count<=10:
                            self.weapon_title=self.button_title_font.render("War Axe",True,"black")
        self.weapon_upgrade_msg=self.button_title_font.render("Weapon Upgrade",True,"black")
        self.weapon_damage_display=self.button_font.render(f"Damage per click: {str(self.damage_per_click)}",True,"black")
        self.weapon_gold_display=self.button_font.render(f"Gold per click: {str(self.gold_per_click)}",True,"black")
        self.weapon_cost_display=self.button_font.render(f"Upgrade Cost: {int(self.weapon_upgrade_cost)}",True,"black")

        pygame.draw.rect(screen,"grey",self.weapon_upgrade_rect,border_radius=(15))
        screen.blit(self.weapon_upgrade_msg,(310,130))
        screen.blit(self.weapon_title,(310,160))
        screen.blit(self.weapon_damage_display,(310,180))
        screen.blit(self.weapon_gold_display,(310,200))
        screen.blit(self.weapon_cost_display,(310,220))

    def display_castle_info(self):
        castle_name_text = self.button_font.render(f"Castle: {self.current_castle_name}", True, "black")
        screen.blit(castle_name_text, (50, 780))

    def display_castle_hp(self):
        self.total_hp=self.button_font.render("Castle HP",True,"black")
        screen.blit(self.total_hp,(50,810))

    def display_gold(self):
        self.total_gold=self.button_font.render(f"Gold:{int(self.gold)}",True,"black")
        screen.blit(self.total_gold,(50,840))

    def display_castle_defeated(self):
        self.total_defeated=self.button_font.render(f"Kings Skull Count:{str(self.castle_defeated)}",True,"black")
        screen.blit(self.total_defeated,(50,870))

    def destroyed_castle(self):
         
        if self.castle_hitpoints<=0:
            self.castle_defeated+=1

            if self.castle_defeated>=30:
                 self.game_over=True
                 
            self.castle_new_hp=math.floor(self.castle_new_hp*1.5)
            self.castle_hitpoints=self.castle_new_hp

            prefixes = [
                "Dark", "Shadow", "Storm", "Moon", "Star",
                "Dragon", "Eagle", "Wolf", "Iron", "Black"
            ]

            bases = [
                "castle", "keep", "tower", "fortress", "stronghold",
                "citadel", "manor", "hall", "spire", "bastion"
            ]

            suffixes = [
                "peak", "heights", "vale", "reach", "fall",
                "watch", "gate", "wall", "crown", "shield"
]
            if self.castle_defeated==1:
                self.current_castle_name= "Black Stone Castle of the Iron Dwarves  "
            elif self.castle_defeated==2:
                self.current_castle_name= "Fort of Angot, He Who Dwells in the Shadows" 
            elif self.castle_defeated==3:
                self.current_castle_name= "Stronghold of the Serpent Doom Cult " 
            
            else:
            
                self.current_castle_name= f"{random.choice(prefixes)} {random.choice(bases)} {random.choice(suffixes)}"

    def ending (self):

            self.ending_rect = pygame.Rect(0, 0, 800, 900)  # Position left of weapon upgrade
            self.ending_msg= self.button_title_font.render("you win !! ", True, "white")
            pygame.draw.rect(screen, "black", self.ending_rect)

            screen.blit(self.ending_msg,(400,450))

    def click_button(self):

        if self.game_over==False:
            self.mouse_pos=pygame.mouse.get_pos()
            if self.castle_rect.collidepoint(self.mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked=True

                else:
                    if self.clicked:
                        self.castle_shake_intensity = 5  # Adjust this value to control shake intensity
                        self.castle_shake_duration = 10   # Number of frames to shake

                    # Store original position for shaking
                        if self.original_castle_pos is None:
                            self.original_castle_pos = self.castle_rect.center

                        self.castle_hitpoints-=self.damage_per_click
                        self.gold+=self.gold_per_click
                        self.clicked=False
                        self.destroyed_castle()

            screen.blit(self.castle_image,self.castle_rect)

            if self.weapon_upgrade_rect.collidepoint(self.mouse_pos):
                    if pygame.mouse.get_pressed()[0]:
                        self.clicked=True
                    
                    else:
                        if self.clicked:

                            if self.gold>=self.weapon_upgrade_cost:
                                self.gold-=self.weapon_upgrade_cost
                                self.weapon_upgrade_cost*=2
                                self.damage_per_click+=2
                                self.gold_per_click+=1
                                self.weapon_upgrade_count+=1
                                self.clicked=False

            if self.goblin_passive_income_rect.collidepoint(self.mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                else:
                    if self.clicked:
                        if self.gold >= self.goblin_passive_income_cost:
                            self.gold -= self.goblin_passive_income_cost
                            self.goblin_passive_income_cost *= 1.2   #  cost for next upgrade
                            self.goblin_gold_per_second+= 1     # Increase passive income 
                            self.goblins+=1
                        self.clicked = False

            if self.ratling_passive_income_rect.collidepoint(self.mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                else:
                    if self.clicked:
                        if self.gold >=self.ratling_passive_income_cost:
                            self.gold -=self.ratling_passive_income_cost
                            self.ratling_passive_income_cost *= 1.2   #  cost for next upgrade
                            self.ratling_gold_per_second+= 15     # Increase passive income 
                            self.ratlings+=1
                        self.clicked = False

            if self.kobold_passive_income_rect.collidepoint(self.mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                else:
                    if self.clicked:
                        if self.gold >=self.kobold_passive_income_cost:
                            self.gold -=self.kobold_passive_income_cost
                            self.kobold_passive_income_cost *= 1.2   #  cost for next upgrade
                            self.kobold_gold_per_second+= 300     # Increase passive income 
                            self.kobolds+=1
                        self.clicked = False

            if self.orc_passive_income_rect.collidepoint(self.mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                else:
                    if self.clicked:
                        if self.gold >= self.orc_passive_income_cost:
                            self.gold -= self.orc_passive_income_cost
                            self.orc_passive_income_cost *= 1.1  # Double cost for next upgrade
                            self.orc_damage_per_second+= 2     # Increase passive income by 1 gold/sec
                            self.orcs+=1
                        self.clicked = False

            if self.troll_passive_income_rect.collidepoint(self.mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                else:
                    if self.clicked:
                        if self.gold >= self.troll_passive_income_cost:
                            self.gold -= self.troll_passive_income_cost
                            self.troll_passive_income_cost *= 1.2  # Double cost for next upgrade
                            self.troll_damage_per_second+= 30     # Increase passive income by 1 gold/sec
                            self.trolls+=1
                        self.clicked = False

            if self.knight_passive_income_rect.collidepoint(self.mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                else:
                    if self.clicked:
                        if self.gold >= self.knight_passive_income_cost:
                            self.gold -= self.knight_passive_income_cost
                            self.knight_passive_income_cost *= 1.2  # Double cost for next upgrade
                            self.knight_damage_per_second+= 300    # Increase passive income by 1 gold/sec
                            self.knights+=1
                        self.clicked = False

            if self.demon_passive_income_rect.collidepoint(self.mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                else:
                    if self.clicked:
                        if self.castle_defeated >= self.demon_passive_income_cost:
                            self.castle_defeated -= self.demon_passive_income_cost
                            self.demon_damage_per_second=99999999999     # Increase passive income by 1 gold/sec
                            self.demon_passive_income_cost=666
                        self.clicked = False
     
    def render(self):
        if self.game_over==False:
            self.update_castle_shake()
            self.click_button()
            self.gold+=self.ratling_gold_per_second/60
            self.gold += self.goblin_gold_per_second/60  #The passive income is calculated by dividing the per-second rate by 60 (frames per second)
            self.gold += self.kobold_gold_per_second/60  #The passive income is calculated by dividing the per-second rate by 60 (frames per second)
            self.castle_hitpoints-=self.orc_damage_per_second/60
            self.castle_hitpoints-=self.troll_damage_per_second/60
            self.castle_hitpoints-=self.knight_damage_per_second/60
            self.castle_hitpoints-=self.demon_damage_per_second/60
            self.destroyed_castle()
            self.display_gold()
            self.display_castle_hp()
            self.display_weapon_upgrade()
            self.display_goblin_passive_income_upgrade()
            self.display_ratling_passive_income_upgrade()
            self.display_kobold_passive_income_upgrade()
            self.display_orc_passive_damage_upgrade()
            self.display_troll_passive_damage_upgrade()  
            self.display_knight_passive_damage_upgrade()  
            self.display_demon_passive_damage_upgrade()       
            self.display_weapon_upgrade()
            self.axe_cursor()
            self.display_castle_defeated()
            self.display_castle_info()
            self.draw_health_bar(screen) 
            print(self.castle_hitpoints)
        else:
             self.ending()

screen_width=800
screen_height=900

screen=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("King Slayer")

text_font=pygame.font.Font("assets/font.ttf",20)
title_font=pygame.font.Font("assets/font.ttf",40)
title=title_font.render("King Slayer",True,"black")
title_rect=title.get_rect(center=(screen.get_width()/2,80))

game=Game()
clock=pygame.time.Clock()

run=True

while run:

    screen.fill("light grey")

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    screen.blit(title,title_rect)

    game.render()
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
