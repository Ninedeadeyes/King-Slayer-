import pygame, math,random

pygame.init()

class Game:
    def __init__(self):
        self.gold=0
        self.damage=0
        self.gold_per_click=1
        self.damage_per_click=1
        self.castle_new_hp=5000
        self.castle_defeated=0
        self.castle_hitpoints=5000
        self.castle_image=pygame.image.load("assets/castle.png").convert_alpha()
        self.castle_rect=self.castle_image.get_rect(center=(screen.get_width()/2-15,screen.get_height()/2+150))

        self.good_ending=pygame.image.load("assets/good_ending.jpg").convert_alpha()
        self.bad_ending=pygame.image.load("assets/bad_ending.jpg").convert_alpha()

        #scale down 
        self.good_ending = pygame.transform.smoothscale(self.good_ending, 
            (self.good_ending.get_width() // 3, self.good_ending.get_height() // 3))
        
        self.bad_ending = pygame.transform.smoothscale(self.bad_ending, 
            (self.bad_ending.get_width() // 3, self.bad_ending.get_height() // 3))


        self.good_ending_rect=self.castle_image.get_rect(center=(screen.get_width()/2-50,screen.get_height()/2+50))
        self.bad_ending_rect=self.castle_image.get_rect(center=(screen.get_width()/2-50,screen.get_height()/2+50))


        self.health_bar_x = 130  # Position of health bar
        self.health_bar_y = 815  # Position below castle info
        self.health_bar_w = 200  # Width of health bar
        self.health_bar_h = 18   # Height of health bar
        
        # Castle shake properties
        self.castle_shake_intensity = 0
        self.castle_shake_duration = 0
        self.original_castle_pos = None

        self.button_font=pygame.font.Font("assets/font2.ttf",16)
        self.button_title_font=pygame.font.Font("assets/font3.ttf",16)
        self.current_castle_name= " War Fortress of the Mad Goblin King "

        self.clicked=False

        self.weapon_upgrade_rect=pygame.Rect(270,100,260,140)
        self.weapon_upgrade_cost=5
        self.weapon_upgrade_count=0

        self.demon_passive_income_rect = pygame.Rect(270, 250, 260, 120)  # Position left of weapon upgrade
        self.demon_passive_income_cost = 40  # Starting cost
        self.demon_damage_per_second = 0      # Current passive income rate

        self.orc_passive_income_rect = pygame.Rect(570, 100, 220, 120)  # Position left of weapon upgrade
        self.orc_passive_income_cost = 5  # Starting cost
        self.orc_damage_per_second = 0      # Current passive income rate
        self.orcs=0

        self.goblin_passive_income_rect = pygame.Rect(10, 100, 220, 120)  # Position left of weapon upgrade
        self.goblin_passive_income_cost = 10  # Starting cost
        self.goblin_gold_per_second = 0      # Current passive income rate
        self.goblins=0

        self.ratling_passive_income_rect = pygame.Rect(10, 230, 220, 120)  # Position left of weapon upgrade
        self.ratling_passive_income_cost = 2000  # Starting cost
        self.ratling_gold_per_second = 0      # Current passive income rate
        self.ratlings=0

        self.kobold_passive_income_rect = pygame.Rect(10, 360, 220, 120)  # Position left of weapon upgrade
        self.kobold_passive_income_cost = 22000  # Starting cost
        self.kobold_gold_per_second = 0      # Current passive income rate
        self.kobolds=0

        self.troll_passive_income_rect = pygame.Rect(570, 230, 220, 120)  # Position left of weapon upgrade
        self.troll_passive_income_cost = 400  # Starting cost
        self.troll_damage_per_second = 0      # Current passive income rate
        self.trolls=0

        self.knight_passive_income_rect = pygame.Rect(570, 360, 220, 120)  # Position left of weapon upgrade
        self.knight_passive_income_cost = 25000  # Starting cost
        self.knight_damage_per_second = 0      # Current passive income rate
        self.knights=0

        self.lesser_demon_passive_income_rect = pygame.Rect(570, 490, 220, 120)  # Position left of weapon upgrade
        self.lesser_demon_passive_income_cost = 2  # Starting cost
        self.lesser_demon_passive_gold_income_cost = 100000  # Starting cost
        self.lesser_demon_damage_per_second = 0      # Current passive income rate
        self.lesser_demons=0


        self.game_over=False
        self.unhappy_ending=False

    
    def instruction(self):
         instrut=self.button_title_font.render("Press SpaceBar to Pause Music",True,"black")
         screen.blit(instrut,(480,850))

    def display_lesser_demon_passive_damage_upgrade(self):
        lesser_demon_title = self.button_title_font.render("Hastur: The King in Yellow ", True, "black")

        lesser_demon_passive_cost_display = self.button_font.render(
            "Blessing/Curse Cost: ", True, "black")
        
        lesser_demon_passive_cost_display2 = self.button_font.render(
            f"King Skulls: {int(self.lesser_demon_passive_income_cost)} ", True, "black")
        
        lesser_demon_passive_cost_display3 = self.button_font.render(
            f"Gold: {int(self.lesser_demon_passive_gold_income_cost)}", True, "black")
        
        lesser_demon_passive_cost_display4 = self.button_font.render(
            "Effect: ???", True, "black")
        
        pygame.draw.rect(screen, "grey", self.lesser_demon_passive_income_rect, border_radius=(15))
        screen.blit(lesser_demon_title,(575,500))
        screen.blit(lesser_demon_passive_cost_display, (575, 520))
        screen.blit(lesser_demon_passive_cost_display2, (575, 540))
        screen.blit(lesser_demon_passive_cost_display3, (575, 560))
        screen.blit(lesser_demon_passive_cost_display4, (575, 580))


    def display_demon_passive_damage_upgrade(self):
        demon_title = self.button_title_font.render("Azathoth: The 'Blind Idiot God'", True, "black")
        demon_passive_attack_display = self.button_font.render(
            f"DPS: {self.demon_damage_per_second}", True, "black")
        
        demon_passive_cost_display = self.button_font.render(
            f"Summon Cost: {int(self.demon_passive_income_cost)} King Skulls", True, "black")
        
        
        pygame.draw.rect(screen, "grey", self.demon_passive_income_rect, border_radius=(15))
        screen.blit(demon_title,(275,280))
        screen.blit(demon_passive_attack_display, (275, 310))
        screen.blit(demon_passive_cost_display, (275, 340))
    
    def display_orc_passive_damage_upgrade(self):
        orc_title = self.button_title_font.render("Orc Berserker War Camp", True, "black")
        orc_count=self.button_font.render( 
             f"Orcs: {self.orcs}", True, "black")
        orc_passive_attack_display = self.button_font.render(
            f"DPS: {self.orc_damage_per_second}", True, "black")
        orc_passive_cost_display = self.button_font.render(
            f"Hire Cost: {int(self.orc_passive_income_cost)}", True, "black")
        
        pygame.draw.rect(screen, "grey", self.orc_passive_income_rect, border_radius=(15))
        screen.blit(orc_title,(575,120))
        screen.blit(orc_count,(575,140))
        screen.blit(orc_passive_attack_display, (575, 160))
        screen.blit(orc_passive_cost_display, (575, 180))

    def display_troll_passive_damage_upgrade(self):
        troll_title = self.button_title_font.render("Doom Troll Hideout", True, "black")
        troll_count=self.button_font.render( 
             f"Trolls: {self.trolls}", True, "black")
        troll_passive_attack_display = self.button_font.render(
            f"DPS: {self.troll_damage_per_second}", True, "black")
        troll_passive_cost_display = self.button_font.render(
            f"Hire Cost: {int(self.troll_passive_income_cost)}", True, "black")
        
        pygame.draw.rect(screen, "grey", self.troll_passive_income_rect, border_radius=(15))
        screen.blit(troll_title,(575,250))
        screen.blit(troll_count,(575,270))
        screen.blit(troll_passive_attack_display, (575, 290))
        screen.blit(troll_passive_cost_display, (575, 310))

    def display_knight_passive_damage_upgrade(self):
        knight_title = self.button_title_font.render("Death Knight Stronghold", True, "black")
        knight_count=self.button_font.render( 
             f"Knights: {self.knights}", True, "black")
        knight_passive_attack_display = self.button_font.render(
            f"DPS: {self.knight_damage_per_second}", True, "black")
        knight_passive_cost_display = self.button_font.render(
            f"Hire Cost: {int(self.knight_passive_income_cost)}", True, "black")
        
        pygame.draw.rect(screen, "grey", self.knight_passive_income_rect, border_radius=(15))
        screen.blit(knight_title,(575,380))
        screen.blit(knight_count,(575,400))
        screen.blit(knight_passive_attack_display, (575, 420))
        screen.blit(knight_passive_cost_display, (575,440))

    def display_kobold_passive_income_upgrade(self):
        kobold_title = self.button_title_font.render("Kobold Gold Mine", True, "black")
        kobold_count=self.button_font.render( 
             f"Kobolds: {self.kobolds}", True, "black")
        kobold_passive_income_display = self.button_font.render(
            f"Gold per second: {self.kobold_gold_per_second}", True, "black")
        kobold_passive_cost_display = self.button_font.render(
            f"Hire Cost: {int(self.kobold_passive_income_cost)}", True, "black")
        
        pygame.draw.rect(screen, "grey", self.kobold_passive_income_rect, border_radius=(15))
        screen.blit(kobold_title,(15, 380))
        screen.blit(kobold_count,(15,400))
        screen.blit(kobold_passive_income_display, (15, 420))
        screen.blit(kobold_passive_cost_display, (15, 440))

    def display_ratling_passive_income_upgrade(self):
        ratling_title = self.button_title_font.render("Ratling Loan Shark Den", True, "black")
        ratling_count=self.button_font.render( 
             f"Ratlings: {self.ratlings}", True, "black")
        ratling_passive_income_display = self.button_font.render(
            f"Gold per second: {self.ratling_gold_per_second}", True, "black")
        ratling_passive_cost_display = self.button_font.render(
            f"Hire Cost: {int(self.ratling_passive_income_cost)}", True, "black")
        
        pygame.draw.rect(screen, "grey", self.ratling_passive_income_rect, border_radius=(15))
        screen.blit(ratling_title,(15, 250))
        screen.blit(ratling_count,(15,270))
        screen.blit(ratling_passive_income_display, (15, 290))
        screen.blit(ratling_passive_cost_display, (15, 310))
    
    def display_goblin_passive_income_upgrade(self):
        goblin_title = self.button_title_font.render("Goblin Fungus Farm", True, "black")
        goblin_count=self.button_font.render( 
             f"Goblins: {self.goblins}", True, "black")
        goblin_passive_income_display = self.button_font.render(
            f"Gold per second: {self.goblin_gold_per_second}", True, "black")
        goblin_passive_cost_display = self.button_font.render(
            f"Hire Cost: {int(self.goblin_passive_income_cost)}", True, "black")
        
        pygame.draw.rect(screen, "grey", self.goblin_passive_income_rect, border_radius=(15))
        screen.blit(goblin_title,(15, 120))
        screen.blit(goblin_count,(15,140))
        screen.blit(goblin_passive_income_display, (15, 160))
        screen.blit(goblin_passive_cost_display, (15, 180))

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
        self.weapon_title=self.button_title_font.render("Broken Hatchet",True,"black")
        if self.weapon_upgrade_count==2 or self.weapon_upgrade_count==3:
                            self.weapon_title=self.button_title_font.render("Rusty Hand Axe",True,"black")
        elif self.weapon_upgrade_count==4 or self.weapon_upgrade_count==5:
                            self.weapon_title=self.button_title_font.render("Chipped Wood Axe",True,"black")
        elif self.weapon_upgrade_count==6 or self.weapon_upgrade_count==7:
                            self.weapon_title=self.button_title_font.render("Crude Orc Axe",True,"black")
        elif self.weapon_upgrade_count==8 or self.weapon_upgrade_count==9:
                            self.weapon_title=self.button_title_font.render("Plain Steel Axe",True,"black")
        elif self.weapon_upgrade_count>=10 and self.weapon_upgrade_count<=12:
                            self.weapon_title=self.button_title_font.render("Two Handed War Axe",True,"black")
        elif self.weapon_upgrade_count>=13 and self.weapon_upgrade_count<=15:
                            self.weapon_title=self.button_title_font.render("Oakwood Battle Axe",True,"black")
        elif self.weapon_upgrade_count>=16 and self.weapon_upgrade_count<=18:
                            self.weapon_title=self.button_title_font.render("Great Axe of EverFrost ",True,"black")
        elif self.weapon_upgrade_count>=19:
                            self.weapon_title=self.button_title_font.render("The Doom Axe",True,"black")


        self.weapon_upgrade_msg=self.button_title_font.render("Weapon Upgrade",True,"black")
        self.weapon_damage_display=self.button_font.render(f"Damage per click: {str(self.damage_per_click)}",True,"black")
        self.weapon_gold_display=self.button_font.render(f"Gold per click: {str(self.gold_per_click)}",True,"black")
        self.weapon_cost_display=self.button_font.render(f"Upgrade Cost: {int(self.weapon_upgrade_cost)}",True,"black")

        pygame.draw.rect(screen,"grey",self.weapon_upgrade_rect,border_radius=(15))
        screen.blit(self.weapon_upgrade_msg,(290,120))
        screen.blit(self.weapon_title,(290,150))
        screen.blit(self.weapon_damage_display,(290,170))
        screen.blit(self.weapon_gold_display,(290,190))
        screen.blit(self.weapon_cost_display,(290,210))

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
            destroy_sound.play()
            self.castle_defeated+=1
            self.gold+=500

            if self.castle_defeated==50:
                self.game_over=True
                 
            self.castle_new_hp=math.floor(self.castle_new_hp*1.2)
            self.castle_hitpoints=self.castle_new_hp

            prefixes = [
                "Elven", "Knight Templer", "Goblins", "Iron Hand ", "Greyborn",
                "Dwarven", "Ratling", "Blood", "Shadow Mage ", "Dragon"
            ]

            bases = [
                "Castle", "Keep", "Tower", "Fortress", "Stronghold",
                "Citadel", "Manor", "Hall", "Spire", "Bastion"
            ]

            suffixes = [
                "Peak", "Heights", "Vale", "Reach", "Fall",
                "Watch", "Dawn", "Night", "Crown", "Shield"
]
            if self.castle_defeated==1:
                self.current_castle_name= "Black Stone Castle of the Iron Dwarves  "
            elif self.castle_defeated==2:
                self.current_castle_name= "Fort of Angot, He Who Dwells in the Shadows" 
            elif self.castle_defeated==3:
                self.current_castle_name= "Stronghold of the Serpent Doom Cult " 
            
            else:
                self.current_castle_name= f"{random.choice(prefixes)} {random.choice(bases)} of the  {random.choice(suffixes)}"

    def ending (self):

            self.ending_rect = pygame.Rect(0, 0, 1250, 950)  # Position left of weapon upgrade
            pygame.draw.rect(screen, "black", self.ending_rect)
            self.ending3_msg = self.button_title_font.render( "Press Escape Key to Exit Game ", True,  "white")
            
            if self.unhappy_ending:

                self.ending1_msg = self.button_title_font.render("You have unleashed Azathoth !! You have slain all the Kings ", True,  "white")
                self.ending2_msg = self.button_title_font.render( "as well as everything else !!  ", True,  "white")
                
                screen.blit(self.bad_ending,self.bad_ending_rect)

                
            else:
                 self.ending1_msg= self.button_title_font.render(" You have slain all the Kings of the World !! ", True,  "white")
                 self.ending2_msg = self.button_title_font.render ( " You Win King Slayer !!  ", True, "white")


                 screen.blit(self.good_ending,self.good_ending_rect)
            
            
            screen.blit(self.ending1_msg,(100,200))
            screen.blit(self.ending2_msg,(100,220))
            screen.blit(self.ending3_msg,(220,840))
               
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
                        click_sound.play()
                        self.destroyed_castle()

            screen.blit(self.castle_image,self.castle_rect)

            if self.weapon_upgrade_rect.collidepoint(self.mouse_pos):
                    if pygame.mouse.get_pressed()[0]:
                        self.clicked=True
                    
                    else:
                        if self.clicked:

                            if self.gold>=self.weapon_upgrade_cost:
                                self.gold-=self.weapon_upgrade_cost
                                self.weapon_upgrade_cost*=1.2
                                self.damage_per_click+=4
                                self.gold_per_click+=1
                                self.weapon_upgrade_count+=1
                                self.clicked=False
                                upgrade_sound.play()
                                

            if self.goblin_passive_income_rect.collidepoint(self.mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                else:
                    if self.clicked:
                        if self.gold >= self.goblin_passive_income_cost:
                            self.gold -= self.goblin_passive_income_cost
                            self.goblin_passive_income_cost *= 1.05   #  cost for next upgrade
                            self.goblin_gold_per_second+= 1     # Increase passive income 
                            self.goblins+=1
                            hire_sound.play()
                            self.clicked = False


            if self.ratling_passive_income_rect.collidepoint(self.mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                else:
                    if self.clicked:
                        if self.gold >=self.ratling_passive_income_cost:
                            self.gold -=self.ratling_passive_income_cost
                            self.ratling_passive_income_cost *= 1.05   #  cost for next upgrade
                            self.ratling_gold_per_second+= 25     # Increase passive income 
                            self.ratlings+=1
                            hire_sound.play()
                            self.clicked = False

            if self.kobold_passive_income_rect.collidepoint(self.mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                else:
                    if self.clicked:
                        if self.gold >=self.kobold_passive_income_cost:
                            self.gold -=self.kobold_passive_income_cost
                            self.kobold_passive_income_cost *= 1.05   #  cost for next upgrade
                            self.kobold_gold_per_second+= 300     # Increase passive income 
                            self.kobolds+=1
                            hire_sound.play()
                            self.clicked = False

            if self.orc_passive_income_rect.collidepoint(self.mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                else:
                    if self.clicked:
                        if self.gold >= self.orc_passive_income_cost:
                            self.gold -= self.orc_passive_income_cost
                            self.orc_passive_income_cost *= 1.05  # Double cost for next upgrade
                            self.orc_damage_per_second+= 10     # Increase passive income by 1 gold/sec
                            self.orcs+=1
                            hire_sound.play()
                            self.clicked = False

            if self.troll_passive_income_rect.collidepoint(self.mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                else:
                    if self.clicked:
                        if self.gold >= self.troll_passive_income_cost:
                            self.gold -= self.troll_passive_income_cost
                            self.troll_passive_income_cost *= 1.05  # Double cost for next upgrade
                            self.troll_damage_per_second+= 200     # Increase passive income by 1 gold/sec
                            self.trolls+=1
                            hire_sound.play()
                            self.clicked = False

            if self.knight_passive_income_rect.collidepoint(self.mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                else:
                    if self.clicked:
                        if self.gold >= self.knight_passive_income_cost:
                            self.gold -= self.knight_passive_income_cost
                            self.knight_passive_income_cost *= 1.02  # Double cost for next upgrade
                            self.knight_damage_per_second+= 1600    # Increase passive income by 1 gold/sec
                            self.knights+=1
                            hire_sound.play()
                            self.clicked = False

            if self.demon_passive_income_rect.collidepoint(self.mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                else:
                    if self.clicked:
                        if self.castle_defeated >= self.demon_passive_income_cost:
                            self.castle_defeated -= self.demon_passive_income_cost
                            self.unhappy_ending=True
                            self.demon_damage_per_second=99999999999999     # Increase passive income by 1 gold/sec
                            self.demon_passive_income_cost=99
                            self.clicked = False


            if self.lesser_demon_passive_income_rect.collidepoint(self.mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                else:
                    if self.clicked:
                        if self.castle_defeated >= self.lesser_demon_passive_income_cost and self.gold >= self.lesser_demon_passive_gold_income_cost:
                            self.castle_defeated -= self.lesser_demon_passive_income_cost
                            self.gold -= self.lesser_demon_passive_gold_income_cost
                            self.damage_per_click+=7000
                            self.gold_per_click+=5000
                            self.lesser_demon_passive_income_cost+=1
                            self.lesser_demon_passive_gold_income_cost+=100000
                            self.clicked = False

     
    def render(self):
        if self.game_over==True:
            pygame.mixer.music.pause()
            self.ending()


        else:
            self.destroyed_castle()
            self.update_castle_shake()
            self.click_button()
            self.gold+=self.ratling_gold_per_second/60
            self.gold += self.goblin_gold_per_second/60  #The passive income is calculated by dividing the per-second rate by 60 (frames per second)
            self.gold += self.kobold_gold_per_second/60  #The passive income is calculated by dividing the per-second rate by 60 (frames per second)
            self.castle_hitpoints-=self.orc_damage_per_second/60
            self.castle_hitpoints-=self.troll_damage_per_second/60
            self.castle_hitpoints-=self.knight_damage_per_second/60
            self.castle_hitpoints-=self.demon_damage_per_second/60
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
            self.display_lesser_demon_passive_damage_upgrade()  
            self.display_weapon_upgrade()
            self.axe_cursor()
            self.display_castle_defeated()
            self.display_castle_info()
            self.draw_health_bar(screen) 
            self.instruction()

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
click_sound=pygame.mixer.Sound("assets/click.flac")
destroy_sound=pygame.mixer.Sound("assets/destroy.wav")
upgrade_sound=pygame.mixer.Sound("assets/upgrade.wav")
hire_sound=pygame.mixer.Sound("assets/hire.wav")


click_sound.set_volume(0.5)
destroy_sound.set_volume(0.6) 
upgrade_sound.set_volume(0.6)

pygame.mixer.init()

music_tracks = [
    'assets/bg1.mp3',
    'assets/bg2.mp3',
    'assets/bg3.mp3',
    'assets/bg4.mp3',
    'assets/bg5.mp3'
]
    
pygame.mixer.music.load(music_tracks[0])
pygame.mixer.music.play()
pygame.mixer.music.set_endevent(pygame.USEREVENT)  # Set event for when music ends
current_track = 0
play_once=False
run=True

while run:

    screen.fill("light grey")

    if game.game_over==True and play_once==False:
        if game.unhappy_ending:
            bad_ending_sound=pygame.mixer.Sound("assets/bad_ending.wav")
            bad_ending_sound.play()
        else:
            good_ending_sound=pygame.mixer.Sound("assets/good_ending.wav")
            good_ending_sound.play()
        play_once=True

             
    for event in pygame.event.get():

        if event.type==pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run=False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Toggle music play/pause
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            if event.key == pygame.K_ESCAPE:
                 run=False

        if event.type == pygame.USEREVENT and game.game_over==False:
            # When music ends, play next track
            current_track = (current_track + 1) % len(music_tracks)
            pygame.mixer.music.load(music_tracks[current_track])
            pygame.mixer.music.play()

    screen.blit(title,title_rect)
    game.render()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
