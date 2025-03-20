import pygame
from math import sin,cos,floor
from  random import choice
import asyncio

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

        self.mouse_pos = pygame.mouse.get_pos()

        self.good_ending=pygame.image.load("assets/good_ending.jpg").convert_alpha()
        self.bad_ending=pygame.image.load("assets/bad_ending.jpg").convert_alpha()

        #scale down 
        self.good_ending = pygame.transform.smoothscale(self.good_ending, 
            (self.good_ending.get_width() // 3, self.good_ending.get_height() // 3))
        
        self.bad_ending = pygame.transform.smoothscale(self.bad_ending, 
            (self.bad_ending.get_width() // 3, self.bad_ending.get_height() // 3))

        self.good_ending_rect=self.castle_image.get_rect(center=(screen.get_width()/2-50,screen.get_height()/2+50))
        self.bad_ending_rect=self.castle_image.get_rect(center=(screen.get_width()/2-50,screen.get_height()/2+50))

        #images # screen.blit(self.orc_image,self.orc_rect)  ( for my own personal reference, can delete)

        self.hover_scale_factor = 0.95 # Makes image 5% smaller on hover

        self.orc_image=pygame.image.load("assets/orc_img.jpg").convert_alpha()

        self.orc_image = pygame.transform.smoothscale(self.orc_image, 
            (self.orc_image.get_width() // 2.7, self.orc_image.get_height() // 2.7))
        
        self.orc_rect=self.orc_image.get_rect(topleft=(1000,120))

        self.troll_image=pygame.image.load("assets/troll_img.jpg").convert_alpha()
        self.troll_rect=self.troll_image.get_rect(topleft=(1000,250))

        self.troll_image = pygame.transform.smoothscale(self.troll_image, 
             (self.troll_image.get_width() // 2.7, self.troll_image.get_height() // 2.7))
        
        self.troll_rect=self.troll_image.get_rect(topleft=(1000,250))

        self.knight_image=pygame.image.load("assets/knight_img.jpg").convert_alpha()

        self.knight_image = pygame.transform.smoothscale(self.knight_image, 
             (self.knight_image.get_width() // 2.7, self.knight_image.get_height() // 2.7))
        
        self.knight_rect=self.knight_image.get_rect(topleft=(1000,380))

        self.hastur_image=pygame.image.load("assets/hastur_img.jpg").convert_alpha()

        self.hastur_image = pygame.transform.smoothscale(self.hastur_image, 
             (self.hastur_image.get_width() // 2.7, self.hastur_image.get_height() // 2.7))
        
        self.hastur_rect=self.hastur_image.get_rect(topleft=(1000,510))
        
        self.goblin_image=pygame.image.load("assets/goblin_img.jpg").convert_alpha()

        self.goblin_image = pygame.transform.smoothscale(self.goblin_image, 
        (self.goblin_image.get_width() // 2.7, self.goblin_image.get_height() // 2.7))    

        self.goblin_rect=self.goblin_image.get_rect(topleft=(330,120))    

        self.ratling_image=pygame.image.load("assets/ratling_img.jpg").convert_alpha()

        self.ratling_image = pygame.transform.smoothscale(self.ratling_image, 
        (self.ratling_image.get_width() // 2.7, self.ratling_image.get_height() // 2.7))   

        self.ratling_rect=self.ratling_image.get_rect(topleft=(330,250))

        self.kobold_image=pygame.image.load("assets/kobold_img.jpg").convert_alpha()

        self.kobold_image = pygame.transform.smoothscale(self.kobold_image, 
        (self.kobold_image.get_width() // 2.7, self.kobold_image.get_height() // 2.7))   

        self.kobold_rect=self.kobold_image.get_rect(topleft=(330,380))


        self.orc_hover_image = pygame.transform.smoothscale(self.orc_image,
                                                           (int(self.orc_image.get_width() * self.hover_scale_factor),
                                                            int(self.orc_image.get_height() * self.hover_scale_factor)))
    
        self.goblin_hover_image = pygame.transform.smoothscale(self.goblin_image,
                                                           (int(self.goblin_image.get_width() * self.hover_scale_factor),
                                                            int(self.goblin_image.get_height() * self.hover_scale_factor)))
        
        self.troll_hover_image = pygame.transform.smoothscale(self.troll_image,
                                                           (int(self.troll_image.get_width() * self.hover_scale_factor),
                                                            int(self.troll_image.get_height() * self.hover_scale_factor)))
        

        self.knight_hover_image = pygame.transform.smoothscale(self.knight_image,
                                                           (int(self.knight_image.get_width() * self.hover_scale_factor),
                                                            int(self.knight_image.get_height() * self.hover_scale_factor)))
        
        self.kobold_hover_image = pygame.transform.smoothscale(self.kobold_image,
                                                           (int(self.kobold_image.get_width() * self.hover_scale_factor),
                                                            int(self.kobold_image.get_height() * self.hover_scale_factor)))
        
        self.hastur_hover_image = pygame.transform.smoothscale(self.hastur_image,
                                                           (int(self.hastur_image.get_width() * self.hover_scale_factor),
                                                            int(self.hastur_image.get_height() * self.hover_scale_factor)))
        
        self.ratling_hover_image = pygame.transform.smoothscale(self.ratling_image,
                                                           (int(self.ratling_image.get_width() * self.hover_scale_factor),
                                                            int(self.ratling_image.get_height() * self.hover_scale_factor)))

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

        self.weapon_upgrade_rect=pygame.Rect(470,100,260,140)
        self.weapon_upgrade_cost=5
        self.weapon_upgrade_count=0

        self.demon_passive_income_rect = pygame.Rect(470, 250, 260, 160)  
        self.demon_passive_income_cost = 30 # Starting cost
        self.demon_passive_gold_income_cost = 500000
        self.demon_damage_per_second = 0      

        self.orc_passive_income_rect = pygame.Rect(770, 100, 220, 120) 
        self.orc_passive_income_cost = 5  # Starting cost
        self.orc_damage_per_second = 0      
        self.orcs=0

        self.goblin_passive_income_rect = pygame.Rect(100, 100, 220, 120)  
        self.goblin_passive_income_cost = 10  # Starting cost
        self.goblin_gold_per_second = 0      
        self.goblins=0

        self.ratling_passive_income_rect = pygame.Rect(100, 230, 220, 120)  
        self.ratling_passive_income_cost = 2000  # Starting cost
        self.ratling_gold_per_second = 0      
        self.ratlings=0

        self.kobold_passive_income_rect = pygame.Rect(100, 360, 220, 120) 
        self.kobold_passive_income_cost = 22000  # Starting cost
        self.kobold_gold_per_second = 0      
        self.kobolds=0

        self.troll_passive_income_rect = pygame.Rect(770, 230, 220, 120)  
        self.troll_passive_income_cost = 300  # Starting cost
        self.troll_damage_per_second = 0     
        self.trolls=0

        self.knight_passive_income_rect = pygame.Rect(770, 360, 220, 120) 
        self.knight_passive_income_cost = 25000  # Starting cost
        self.knight_damage_per_second = 0      
        self.knights=0

        self.lesser_demon_passive_income_rect = pygame.Rect(770, 490, 220, 120)  
        self.lesser_demon_passive_gold_income_cost = 75000  # Starting cost
        self.lesser_demon_passive_income_cost = 1  # Starting cost
        self.lesser_demon_damage_per_second = 0     
        self.lesser_demons=0

        self.game_over=False
        self.unhappy_ending=False

        self.start_time = None
        self.end_time = None
        self.is_running = False
         
    def start_timer(self):
        """Start the game timer"""
        if not self.is_running:
            self.start_time = pygame.time.get_ticks()
            self.is_running = True
            
    def stop_timer(self):
        """Stop the game timer"""
        if self.is_running:
            self.end_time = pygame.time.get_ticks()
            self.is_running = False
            
    def get_elapsed_time(self):
        """Calculate elapsed time based on current state"""
        if self.is_running:
            current_time = pygame.time.get_ticks()
            return (current_time - self.start_time) / 1000
        elif self.end_time is not None:
            return (self.end_time - self.start_time) / 1000
        return 

    def story(self):
         
        story1=self.button_font.render("Raise your army of Doom",True,"black")
        story2=self.button_font.render("and bringforth your (un)divine justice. ",True,"black")        
        story3=self.button_font.render("When the last King draws his final breath,",True,"black")
        story4=self.button_font.render("Vengeance will be yours... King Slayer.",True,"black")

        screen.blit(story1,(100,510))
        screen.blit(story2,(100,530))
        screen.blit(story3,(100,550))
        screen.blit(story4,(100,570))
    
    def instruction(self):
         instrut=self.button_title_font.render("Press SpaceBar to Pause Music",True,"black")
         screen.blit(instrut,(860,850))

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
        screen.blit(lesser_demon_title,(775,500))
        screen.blit(lesser_demon_passive_cost_display, (775, 520))
        screen.blit(lesser_demon_passive_cost_display2, (775, 540))
        screen.blit(lesser_demon_passive_cost_display3, (775, 560))
        screen.blit(lesser_demon_passive_cost_display4, (775, 580))

        if self.hastur_rect.collidepoint(self.mouse_pos):
            screen.blit(self.hastur_hover_image, self.hastur_rect)
        else:
            screen.blit(self.hastur_image, self.hastur_rect)

    def display_demon_passive_damage_upgrade(self):
        demon_title = self.button_title_font.render("Azathoth: The 'Blind Idiot God'", True, "black")
        demon_passive_attack_display = self.button_font.render(
            f"DPS: {self.demon_damage_per_second}", True, "black")
        
        demon_passive_cost_display1 = self.button_font.render(
            "Summon Cost:", True, "black")
        
        demon_passive_cost_display2 = self.button_font.render(
            f"King Skulls: {int(self.demon_passive_income_cost)}", True, "black")

        demon_passive_cost_display3 = self.button_font.render(
            f"Gold: {int(self.demon_passive_gold_income_cost)}", True, "black")    
        
        if self.demon_passive_income_rect.collidepoint(self.mouse_pos):

            pygame.draw.rect(screen, "dark grey", self.demon_passive_income_rect, border_radius=(15))
        else:
            pygame.draw.rect(screen, "grey", self.demon_passive_income_rect, border_radius=(15))
        
        screen.blit(demon_title,(475,280))
        screen.blit(demon_passive_attack_display, (475, 310))
        screen.blit(demon_passive_cost_display1, (475, 340))
        screen.blit(demon_passive_cost_display2, (475, 360))
        screen.blit(demon_passive_cost_display3, (475, 380))

    def display_orc_passive_damage_upgrade(self):

        orc_title = self.button_title_font.render("Orc Berserker War Camp", True, "black")
        orc_count=self.button_font.render( 
             f"Orcs: {self.orcs}", True, "black")
        orc_passive_attack_display = self.button_font.render(
            f"DPS: {self.orc_damage_per_second}", True, "black")
        orc_passive_cost_display = self.button_font.render(
            f"Hire Cost: {int(self.orc_passive_income_cost)}", True, "black")
        
        pygame.draw.rect(screen, "grey", self.orc_passive_income_rect, border_radius=(15))
        screen.blit(orc_title,(775,120))
        screen.blit(orc_count,(775,140))
        screen.blit(orc_passive_attack_display, (775, 160))
        screen.blit(orc_passive_cost_display, (775, 180))
        
        if self.orc_rect.collidepoint(self.mouse_pos):
            screen.blit(self.orc_hover_image, self.orc_rect)
        else:
            screen.blit(self.orc_image, self.orc_rect)
       
    def display_troll_passive_damage_upgrade(self):
        troll_title = self.button_title_font.render("Bog Troll Hideout", True, "black")
        troll_count=self.button_font.render( 
             f"Trolls: {self.trolls}", True, "black")
        troll_passive_attack_display = self.button_font.render(
            f"DPS: {self.troll_damage_per_second}", True, "black")
        troll_passive_cost_display = self.button_font.render(
            f"Hire Cost: {int(self.troll_passive_income_cost)}", True, "black")
        
        pygame.draw.rect(screen, "grey", self.troll_passive_income_rect, border_radius=(15))
        screen.blit(troll_title,(775,250))
        screen.blit(troll_count,(775,270))
        screen.blit(troll_passive_attack_display, (775, 290))
        screen.blit(troll_passive_cost_display, (775, 310))
        
        if self.troll_rect.collidepoint(self.mouse_pos):
            screen.blit(self.troll_hover_image, self.troll_rect)
        else:
            screen.blit(self.troll_image, self.troll_rect)

    def display_knight_passive_damage_upgrade(self):
        knight_title = self.button_title_font.render("Death Knight Stronghold", True, "black")
        knight_count=self.button_font.render( 
             f"Knights: {self.knights}", True, "black")
        knight_passive_attack_display = self.button_font.render(
            f"DPS: {self.knight_damage_per_second}", True, "black")
        knight_passive_cost_display = self.button_font.render(
            f"Hire Cost: {int(self.knight_passive_income_cost)}", True, "black")
        
        pygame.draw.rect(screen, "grey", self.knight_passive_income_rect, border_radius=(15))
        screen.blit(knight_title,(775,380))
        screen.blit(knight_count,(775,400))
        screen.blit(knight_passive_attack_display, (775, 420))
        screen.blit(knight_passive_cost_display, (775,440))

        if self.knight_rect.collidepoint(self.mouse_pos):
            screen.blit(self.knight_hover_image, self.knight_rect)
        else:
            screen.blit(self.knight_image, self.knight_rect)

    def display_kobold_passive_income_upgrade(self):
        kobold_title = self.button_title_font.render("Kobold Gold Mine", True, "black")
        kobold_count=self.button_font.render( 
             f"Kobolds: {self.kobolds}", True, "black")
        kobold_passive_income_display = self.button_font.render(
            f"Gold per second: {self.kobold_gold_per_second}", True, "black")
        kobold_passive_cost_display = self.button_font.render(
            f"Hire Cost: {int(self.kobold_passive_income_cost)}", True, "black")
        
        pygame.draw.rect(screen, "grey", self.kobold_passive_income_rect, border_radius=(15))
        screen.blit(kobold_title,(105, 380))
        screen.blit(kobold_count,(105,400))
        screen.blit(kobold_passive_income_display, (105, 420))
        screen.blit(kobold_passive_cost_display, (105, 440))

        if self.kobold_rect.collidepoint(self.mouse_pos):
            screen.blit(self.kobold_hover_image, self.kobold_rect)
        else:
            screen.blit(self.kobold_image, self.kobold_rect)

    def display_ratling_passive_income_upgrade(self):
        ratling_title = self.button_title_font.render("Ratling Loan Shark Den", True, "black")
        ratling_count=self.button_font.render( 
             f"Ratlings: {self.ratlings}", True, "black")
        ratling_passive_income_display = self.button_font.render(
            f"Gold per second: {self.ratling_gold_per_second}", True, "black")
        ratling_passive_cost_display = self.button_font.render(
            f"Hire Cost: {int(self.ratling_passive_income_cost)}", True, "black")
        
        pygame.draw.rect(screen, "grey", self.ratling_passive_income_rect, border_radius=(15))
        screen.blit(ratling_title,(105, 250))
        screen.blit(ratling_count,(105,270))
        screen.blit(ratling_passive_income_display, (105, 290))
        screen.blit(ratling_passive_cost_display, (105, 310))


        if self.ratling_rect.collidepoint(self.mouse_pos):
            screen.blit(self.ratling_hover_image, self.ratling_rect)
        else:
            screen.blit(self.ratling_image, self.ratling_rect)

    def display_goblin_passive_income_upgrade(self):
        goblin_title = self.button_title_font.render("Goblin Fungus Farm", True, "black")
        goblin_count=self.button_font.render( 
             f"Goblins: {self.goblins}", True, "black")
        goblin_passive_income_display = self.button_font.render(
            f"Gold per second: {self.goblin_gold_per_second}", True, "black")
        goblin_passive_cost_display = self.button_font.render(
            f"Hire Cost: {int(self.goblin_passive_income_cost)}", True, "black")
        
        pygame.draw.rect(screen, "grey", self.goblin_passive_income_rect, border_radius=(15))
        screen.blit(goblin_title,(105, 120))
        screen.blit(goblin_count,(105,140))
        screen.blit(goblin_passive_income_display, (105, 160))
        screen.blit(goblin_passive_cost_display, (105, 180))


        if self.goblin_rect.collidepoint(self.mouse_pos):
            screen.blit(self.goblin_hover_image, self.goblin_rect)
        else:
            screen.blit(self.goblin_image, self.goblin_rect)

    def update_castle_shake(self):
        if self.castle_shake_duration > 0:
            # Calculate shake offset using sine waves for smooth motion
            x_offset = sin(pygame.time.get_ticks() * 0.1) * self.castle_shake_intensity
            y_offset = cos(pygame.time.get_ticks() * 0.05) * self.castle_shake_intensity
            
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
        if self.weapon_upgrade_count>=3 and self.weapon_upgrade_count<=8:
                            self.weapon_title=self.button_title_font.render("Rusty Hand Axe",True,"black")
        elif self.weapon_upgrade_count>=9 and self.weapon_upgrade_count<=14:
                            self.weapon_title=self.button_title_font.render("Chipped Wood Axe",True,"black")
        elif self.weapon_upgrade_count>=15 and self.weapon_upgrade_count<=20:
                            self.weapon_title=self.button_title_font.render("Crude Axe",True,"black")
        elif self.weapon_upgrade_count>=21 and self.weapon_upgrade_count<=26:
                            self.weapon_title=self.button_title_font.render("Steel Axe",True,"black")
        elif self.weapon_upgrade_count>=27 and self.weapon_upgrade_count<=32:
                            self.weapon_title=self.button_title_font.render("Two Handed War Axe",True,"black")
        elif self.weapon_upgrade_count>=33 and self.weapon_upgrade_count<=38:
                            self.weapon_title=self.button_title_font.render("Oakwood Battle Axe",True,"black")
        elif self.weapon_upgrade_count>=39 and self.weapon_upgrade_count<=42:
                            self.weapon_title=self.button_title_font.render("Dragon Tooth Axe ",True,"black")        
        elif self.weapon_upgrade_count>=43 and self.weapon_upgrade_count<=45:
                            self.weapon_title=self.button_title_font.render("Great Axe of EverFrost ",True,"black")
        elif self.weapon_upgrade_count>=46:
                            self.weapon_title=self.button_title_font.render("Axe of Consuming Darkness",True,"black")

        self.weapon_upgrade_msg=self.button_title_font.render("Weapon Upgrade",True,"black")
        self.weapon_damage_display=self.button_font.render(f"Damage per click: {str(self.damage_per_click)}",True,"black")
        self.weapon_gold_display=self.button_font.render(f"Gold per click: {str(self.gold_per_click)}",True,"black")
        self.weapon_cost_display=self.button_font.render(f"Upgrade Cost: {int(self.weapon_upgrade_cost)}",True,"black")

        if self.weapon_upgrade_rect.collidepoint(self.mouse_pos):
            pygame.draw.rect(screen,"dark grey",self.weapon_upgrade_rect,border_radius=(15))
        else:
            pygame.draw.rect(screen,"grey",self.weapon_upgrade_rect,border_radius=(15))     
        
        screen.blit(self.weapon_upgrade_msg,(480,120))
        screen.blit(self.weapon_title,(480,150))
        screen.blit(self.weapon_damage_display,(480,170))
        screen.blit(self.weapon_gold_display,(480,190))
        screen.blit(self.weapon_cost_display,(480,210))

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
            self.gold+=450

            if self.castle_defeated==35:
                self.game_over=True
                 
            self.castle_new_hp=floor(self.castle_new_hp*1.20)
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
            elif self.castle_defeated==4:
                self.current_castle_name= "The War Fortress of the Mountain Orcs " 
            elif self.castle_defeated==5:
                self.current_castle_name= "The Red House 'Here Lies The Consuming Darkness' "             
            else:
                self.current_castle_name= f"{choice(prefixes)} {choice(bases)} of the  {choice(suffixes)}"

    def ending (self):

            self.ending_rect = pygame.Rect(0, 0, 1250, 950) 
            pygame.draw.rect(screen, "black", self.ending_rect)
            self.ending3_msg = self.button_title_font.render( "Press Escape Key to Exit Game ", True,  "white")
            pygame.mixer.music.stop()
            
            if self.unhappy_ending:

                self.ending0_msg = self.button_title_font.render("Bad Ending", True,  "white")
                self.ending1_msg = self.button_title_font.render("You have unleashed Azathoth !! You have slain all the Kings ", True,  "white")
                self.ending2_msg = self.button_title_font.render( "as well as everything else !! Contemplate your foolish actions in silence..  ", True,  "white")
                self.ending4_msg = self.button_title_font.render ( "Play again to redeem yourself or see how quick you can destroy the world ..Again.  ", True, "white")
                self.ending5_msg = self.button_title_font.render ("Attempt to get a completion time below 12 minutes. ", True, "white")
                screen.blit(self.bad_ending,self.bad_ending_rect)

            else:
                 self.ending0_msg = self.button_title_font.render("Good Ending", True,  "white")
                 self.ending1_msg= self.button_title_font.render("You have ended the royal bloodline.", True,  "white")
                 self.ending2_msg = self.button_title_font.render ("Vengeance is yours !! All hail the King Slayer !!   ", True, "white")
                 self.ending4_msg = self.button_title_font.render ("Congratulation !! Can you get a better completion time ?   ", True, "white")
                 self.ending5_msg = self.button_title_font.render ("Attempt to get a completion time below 14 minutes. ", True, "white")

                 screen.blit(self.good_ending,self.good_ending_rect)

            elapsed_time = self.get_elapsed_time()
            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)
            completion_time = self.button_title_font.render(
            f"Completion Time: {minutes:02d}:{seconds:02d}",True,"white")

            screen.blit(self.ending0_msg,(320,160))
            screen.blit(self.ending1_msg,(320,200))
            screen.blit(self.ending2_msg,(320,220))
            screen.blit(self.ending4_msg,(320,260))
            screen.blit(self.ending5_msg,(320,280))
            screen.blit(self.ending3_msg,(410,840))
            screen.blit(completion_time, (440,800))
               
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

            if self.goblin_rect.collidepoint(self.mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                else:
                    if self.clicked:
                        if self.gold >= self.goblin_passive_income_cost:
                            self.gold -= self.goblin_passive_income_cost
                            self.goblin_passive_income_cost *= 1.05   
                            self.goblin_gold_per_second+= 1    
                            self.goblins+=1
                            hire_sound.play()
                            self.clicked = False

            if self.ratling_rect.collidepoint(self.mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                else:
                    if self.clicked:
                        if self.gold >=self.ratling_passive_income_cost:
                            self.gold -=self.ratling_passive_income_cost
                            self.ratling_passive_income_cost *= 1.05  
                            self.ratling_gold_per_second+= 25     
                            self.ratlings+=1
                            hire_sound.play()
                            self.clicked = False

            if self.kobold_rect.collidepoint(self.mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                else:
                    if self.clicked:
                        if self.gold >=self.kobold_passive_income_cost:
                            self.gold -=self.kobold_passive_income_cost
                            self.kobold_passive_income_cost *= 1.05  
                            self.kobold_gold_per_second+= 300    
                            self.kobolds+=1
                            hire_sound.play()
                            self.clicked = False

            if self.orc_rect.collidepoint(self.mouse_pos):

                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                    
                else:
                    if self.clicked:
                        if self.gold >= self.orc_passive_income_cost:
                            self.gold -= self.orc_passive_income_cost
                            self.orc_passive_income_cost *= 1.05  
                            self.orc_damage_per_second+= 10     
                            self.orcs+=1
                            hire_sound.play()
                            self.clicked = False
                 

            if self.troll_rect.collidepoint(self.mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                else:
                    if self.clicked:
                        if self.gold >= self.troll_passive_income_cost:
                            self.gold -= self.troll_passive_income_cost
                            self.troll_passive_income_cost *= 1.05  
                            self.troll_damage_per_second+= 90     
                            self.trolls+=1
                            hire_sound.play()
                            self.clicked = False

            if self.knight_rect.collidepoint(self.mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                else:
                    if self.clicked:
                        if self.gold >= self.knight_passive_income_cost:
                            self.gold -= self.knight_passive_income_cost
                            self.knight_passive_income_cost *= 1.02  
                            self.knight_damage_per_second+= 1050   
                            self.knights+=1
                            hire_sound.play()
                            self.clicked = False

            if self.demon_passive_income_rect.collidepoint(self.mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                else:
                    if self.clicked:
                        if self.castle_defeated >= self.demon_passive_income_cost and self.gold >= self.demon_passive_gold_income_cost:
                            self.castle_defeated -= self.demon_passive_income_cost
                            self.gold -= self.demon_passive_gold_income_cost
                            self.unhappy_ending=True
                            self.demon_damage_per_second=99999999999999     
                            self.demon_passive_income_cost=99
                            demon_sound.play()
                            self.clicked = False


            if self.hastur_rect.collidepoint(self.mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                else:
                    if self.clicked:
                        if self.castle_defeated >= self.lesser_demon_passive_income_cost and self.gold >= self.lesser_demon_passive_gold_income_cost:
                            self.castle_defeated -= self.lesser_demon_passive_income_cost
                            self.gold -= self.lesser_demon_passive_gold_income_cost
                            self.damage_per_click+=1600
                            self.gold_per_click+=900
                            self.lesser_demon_passive_gold_income_cost+=15000
                            hastur_sound.play()
                            self.clicked = False
     
    def render(self):
        if self.game_over==True:
            
            self.stop_timer()
            self.ending()
            self.get_elapsed_time()

        else:
            self.click_button()
            self.start_timer()
            self.destroyed_castle()
            self.update_castle_shake()
            self.click_button()
            self.gold+=self.ratling_gold_per_second/60
            self.gold += self.goblin_gold_per_second/60  #The passive income is calculated by dividing the per-second rate by 60 (frames per second)
            self.gold += self.kobold_gold_per_second/60  
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
            self.story()
            self.axe_cursor()

screen_width=1200
screen_height=900

screen=pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("King Slayer")

text_font=pygame.font.Font("assets/font.ttf",20)
title_font=pygame.font.Font("assets/font.ttf",40)
title=title_font.render("King Slayer",True,"black")
title_rect=title.get_rect(center=(screen.get_width()/2,70))

game=Game()
clock=pygame.time.Clock()
click_sound=pygame.mixer.Sound("assets/click.ogg")
destroy_sound=pygame.mixer.Sound("assets/destroy.ogg")
upgrade_sound=pygame.mixer.Sound("assets/upgrade.ogg")
hire_sound=pygame.mixer.Sound("assets/hire.ogg")
hastur_sound=pygame.mixer.Sound("assets/hastur.ogg")
demon_sound=pygame.mixer.Sound("assets/demon.ogg")

click_sound.set_volume(0.5)
destroy_sound.set_volume(0.6) 
upgrade_sound.set_volume(0.6)

async def main():
    pygame.mixer.init(44100, -16, 2, 2048)
    
    music_tracks = [
        'assets/bg1.ogg',
        'assets/bg2.ogg',
        'assets/bg3.ogg',
        'assets/bg4.ogg',
        'assets/bg5.ogg'
    ]
    pygame.mixer.music.load(music_tracks[0])
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    current_track = 0
    
    run = True
    play_once = False

    while run:
        screen.fill("light grey")
        
        if game.game_over == True and play_once == False:
            good_ending_sound = pygame.mixer.Sound("assets/good_ending.ogg")
            good_ending_sound.play()
            play_once = True
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if pygame.mixer.music.get_busy():
                        pygame.mixer.music.pause()
                    else:
                        pygame.mixer.music.unpause()
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.USEREVENT and game.unhappy_ending == False:
                current_track = (current_track + 1) % len(music_tracks)
                pygame.mixer.music.load(music_tracks[current_track])
                pygame.mixer.music.play()

        pygame.draw.rect(screen, "white", (447, 40, 300, 40), border_radius=15)
        screen.blit(title, title_rect)
        
        game.render()
        pygame.display.flip()
        clock.tick(60)
        await asyncio.sleep(0)  # Critical for browser compatibility
        
    pygame.quit()

if __name__ == "__main__":
    asyncio.run(main())
