import sys
import fs
import os.path
import pygame
import random
import sqlite3
from PyQt5 import QtWidgets

length = 400
width = 80

class Blocks:
    def __init__(self, screen):
        self.block_list = list()
        self.block_dict = {}
        self.current_level = 5
        self.screen = screen

    def get_blocks(self):
        return self.block_list

    def get_blocks_dict(self):
        return self.block_dict

    def delete_last(self):
        last_index = self.current_level * 3 - 1
        print("last_index:", last_index)
        print("current_level:", self.current_level)
        self.block_list.remove(self.block_list[last_index])
        self.block_list.remove(self.block_list[last_index - 1])
        self.block_list.remove(self.block_list[last_index - 2])
        self.current_level -= 1


    def set_up(self, secret_list, connect):
        cursor = connect.cursor()
        temp_whole_words = list()

        for sel in secret_list:
            cursor.execute(f"SELECT * FROM {sel}")
            fetchone = cursor.fetchone()
            while fetchone is not None:
                temp_whole_words.append(fetchone)
                fetchone = cursor.fetchone()
        n = 0
        x = 0
        y = 0
        while n < 15:
            choice = random.choice(temp_whole_words)
            temp_whole_words.remove(choice)
            word = None
            pronounce = None
            memo = None
            if len(choice) == 6:
                memo = 1
                pronounce = 4
            elif len(choice) == 7:
                pronounce = 5
                memo = 2
            elif len(choice) == 8:
                pronounce = 6
                memo = 3
            if n%3 == 0:
                if n!=0:
                    y += width
                x = 0
            if type(choice[2]) == int() and (choice[2].lower() == "der" or
                                             choice[2].lower() == "die" or choice[2].lower() == "das"):
                word = choice[2].lower() + " " + choice[0]
            else:
                word = choice[0]
            if choice[2] in ["die", "das", "der"]:
                word = choice[2] + " " + word
                self.block_list.append(Block(length, width, (x, y), word, choice[1],
                                             choice[pronounce], choice[memo],
                                             choice[-1], 9, self.screen, n / 3, "die " + choice[3]))
            else:
                self.block_list.append(Block(length, width, (x, y), word, choice[1],
                                             choice[pronounce], choice[memo],
                                             choice[-1], 9, self.screen, n / 3))
            self.block_dict[word] = choice[1]
            n += 1
            x += length


    def draw(self):
        level = None
        for block in self.block_list:
            if block.pressed:
                self.delete_last()
            else:
                block.draw()

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        icon = pygame.image.load("bullet.png")
        self.bullet_icon = pygame.transform.scale(icon, (20, 20))
        self.start_off = False

    def set_player(self, screen):
        screen.blit(self.bullet_icon, (self.x, self.y))


class Block:
    def __init__(self, width, height, pos, word, meaning, pronounce, extra,
                 col, elev, screen, level, artikel=None):
        self.single_or_plural = 0 # single as a default
        self.pronounce = pronounce
        self.summarize = extra
        self.level = level
        self.artikel = artikel
        self.width = width
        self.height = height
        self.word = word
        self.meaning = meaning
        self.col = get_color(col)
        self.pos = pos
        self.elev = elev
        self.pressed = False
        self.dynamic_elev = elev
        self.original_pos = pos[1]
        self.gui_font = pygame.font.Font(None, 25)
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = self.col
        self.old_color = self.col
        self.text_surf = None
        self.screen = screen
        self.still_click = False
        self.is_known = False
        self.text_rect = None
        self.text_surf = self.gui_font.render(self.word, True, "#FFFFFF")
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        self.top_rect.y = self.original_pos - self.dynamic_elev
        self.text_rect.center = self.top_rect.center
        r = int(self.top_color[0])
        g = int(self.top_color[1])
        b = int(self.top_color[2])
        if self.single_or_plural == 0:
            self.text_surf = self.gui_font.render(self.word, True, "#FFFFFF")
            self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
            pygame.draw.rect(self.screen, (r, g, b), self.top_rect, border_radius=2)
            self.screen.blit(self.text_surf, self.text_rect)
        else:
            if self.artikel is not None:
                self.text_surf = self.gui_font.render(self.artikel, True, "#FFFFFF")
                self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
                pygame.draw.rect(self.screen, (r, g, b), self.top_rect, border_radius=2)
                self.screen.blit(self.text_surf, self.text_rect)
            else:
                self.text_surf = self.gui_font.render(self.word, True, "#FFFFFF")
                self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
                pygame.draw.rect(self.screen, (r, g, b), self.top_rect, border_radius=2)
                self.screen.blit(self.text_surf, self.text_rect)
        self.check_click()


    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = (180, 30, 40)
            if pygame.mouse.get_pressed()[0]:
                if self.summarize != 0 and self.summarize != "-":
                    print(self.pronounce + " : " + self.summarize)
                else:
                    print(self.pronounce)
                if not self.still_click:
                    if self.single_or_plural == 0:
                        self.single_or_plural = 1
                    else:
                        self.single_or_plural = 0
                    self.still_click = True
            else:
                self.dynamic_elev = self.elev
                self.still_click = False
        else:
            self.dynamic_elev = self.elev
            self.top_color = self.old_color


class Player:
    def __init__(self):
        icon = pygame.image.load("player1.png")
        self.player_icon = pygame.transform.scale(icon, (70, 70))
        self.x = 590
        self.y = 630
        self.is_known = True
        self.meaning = None

    def set_player(self, screen, block_dict, bullet_list):
        screen.blit(self.player_icon, (self.x, self.y))

        if self.is_known:
            temp = random.choice(bullet_list[len(bullet_list)-3:len(bullet_list)])
            self.meaning = temp.meaning
            top_rect = pygame.Rect((self.x - 166, self.y + 65), (length, width))
            pygame.draw.rect(screen, (90, 90, 90), top_rect, border_radius=2)
            gui_font = pygame.font.Font(None, 20)
            text_surf = gui_font.render(temp.meaning, True, "#FFFFFF")
            text_rect = text_surf.get_rect(center=top_rect.center)
            screen.blit(text_surf, text_rect)
            self.is_known = False
        else:
            top_rect = pygame.Rect((self.x - 166, self.y + 65), (length, width))
            pygame.draw.rect(screen, (90, 90, 90), top_rect, border_radius=2)
            gui_font = pygame.font.Font(None, 20)
            text_surf = gui_font.render(self.meaning, True, "#FFFFFF")
            text_rect = text_surf.get_rect(center=top_rect.center)
            screen.blit(text_surf, text_rect)

    def get_meaning(self):
        return self.meaning


class MainPanel:
    def __init__(self):
        self.blocks = None
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        background = pygame.image.load("game1.jpg")
        self.back_img = pygame.transform.scale(background, (1200, 800))

    def set_up(self, selected, data, n = 0):
        result = 0
        pygame.display.set_caption("Game")
        icon = pygame.image.load("gamepad.png")
        pygame.display.set_icon(icon)
        clock = pygame.time.Clock()
        player = Player()
        self.block_manager = Blocks(self.screen)
        self.blocks = self.block_manager.get_blocks()
        self.block_manager.set_up(selected, data)
        self.block_dict = self.block_manager.get_blocks_dict()
        bullets = list()
        current_level = 5
        while True:
            self.screen.blit(self.back_img, (0, 0))
            player.set_player(self.screen, self.block_manager.block_dict,
                              self.block_manager.block_list[:current_level*3])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        player.x -= 40
                    if event.key == pygame.K_RIGHT:
                        player.x += 40
                    if event.key == pygame.K_SPACE:
                        bullet = Bullet(player.x+25, player.y)
                        bullet.start_off = True
                        bullets.append(bullet)
            self.block_manager.draw()
            if len(bullets) > 0:
                word = update(bullets, self.blocks)
                if word is not None:
                    if self.block_dict[word] == player.meaning:
                        player.is_known = True
                        current_level -= 1
                        if current_level == 0:
                            result = 500
                            if os.path.exists("score.txt"):
                                with open("score.txt", "r", encoding="utf-8") as score:
                                    result += int(score.readline())
                                with open("score.txt", "w", encoding="utf-8") as score:
                                    score.write(str(result))
                            else:
                                with open("score.txt", "w", encoding="utf-8") as score:
                                    score.write(str(result))
                            n += 1
                            if n < 3:
                                self.set_up(selected, data, n)
                            else:
                                app = QtWidgets.QApplication(sys.argv)
                                ui = fs.Ui_MainWindow()
                                fs.main(ui, "SUCCESS!!")
                                app.exec_()
                                break
                    else:
                        app = QtWidgets.QApplication(sys.argv)
                        ui = fs.Ui_MainWindow()
                        result = (player.meaning, get_word(player.meaning, self.block_dict), word)
                        fs.main(ui, "FAIL!!")
                        app.exec_()
                        break
            if len(bullets) > 0:
                for bullet in bullets:
                    if bullet.start_off:
                        bullet.set_player(self.screen)
            pygame.display.update()
            clock.tick(60)



class Main:
    def __init__(self):
        self.panel = MainPanel()

    def set_up(self, selected, data):
        self.panel.set_up(selected, data)

def get_selected_words(temp):
    result = ""
    for w in temp:
        result += "'" + w + "', "
    return result[:-2]

def get_color(col):
    temp = col[1:-1]
    temp_list = temp.split(",")
    r = int(temp_list[0])
    g = int(temp_list[1])
    b = int(temp_list[2])
    return (r, g, b)

def get_word(meaning, diction):
    for i in diction.keys():
        if meaning == diction[i]:
            return i

def update(bullets, blocks):
    result = None
    rev = blocks
    for bullet in bullets:
        for block in rev:
            block_pos_left = 0
            block_pos_right = block.pos[0] + 398 #TODO: Look that one !!
            if block.pos[0] - 250 > 0:
                block_pos_left = block.pos[0] - 100
            if (bullet.y in range(block.pos[1]+10, block.pos[1] + 13)) and \
                    (block_pos_left < bullet.x < block_pos_right):
                result = block.word
                block.pressed = True
                bullet.start_off = False
                break
        if bullet.start_off:
            bullet.y -= 5
    return result
