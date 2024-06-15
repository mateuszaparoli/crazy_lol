import random
import tkinter as tk
from tkinter import messagebox
import os
import emoji
import pygame
from time import sleep

class Crazylol:
    def __init__(self, root):
        self.root = root
        self.root.title('Crazy LoL')
        
        self.label1 = tk.Label(root, text='NÃO USE ESSE PROGRAMA EM RANKEDS!')
        self.label1.pack()
        
        self.label2 = tk.Label(root, text=emoji.emojize(":red_heart:"))
        self.label2.pack()
        
        self.output_text = tk.Text(root, height=4, width=50)
        self.output_text.pack()
        
        self.button_sortear = tk.Button(root, text='Sortear', command=self.sortear_campos)
        self.button_sortear.pack()
        
        pygame.init()
        pygame.mixer.music.load('mario_full.mp3')
        pygame.mixer.music.play()

    def sortear_campos(self):
        pygame.init()
        pygame.mixer.music.load('mario_pulo.mp3')
        pygame.mixer.music.play()
        
        sorteio_champ = self.sortear()
        sorteio_lane = self.sortear_lane()
        sorteio_spell = self.sortear_spells()
        
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, 'Seu champ será: {}, \nSua lane: {}, \nSuas spells: {}.'.format(sorteio_champ, sorteio_lane, sorteio_spell))
        
        sleep(1)
        
        pygame.init()
        pygame.mixer.music.load('mario_full.mp3')
        pygame.mixer.music.play()

    def sortear(self):
        champs = ['Aatrox', 'Ahri', 'Akali', 'Akshan', 'Alsitar', 'Amumu', 'Anivia', 'Annie', 'Aphelius', 'Ashe',
                  'Aurelion Sol', 'Azir', 'Bardo', 'Blitzcrank', 'Brand', 'Braum', 'Caitlyn', 'Camille', 'Cassiopeia', "Cho'Gath",
                  'Corki', 'Darius', 'Diana', 'Dr. Mundo', 'Draven', 'Ekko', 'Elise', 'Evelynn', 'Ezreal', 'Fiddlesticks', 'Fiora',
                  'Fizz', 'Galio', 'Gangplank', 'Garen', 'Gnnar', 'Gragas', 'Graves', 'Gwen', 'Hecarim', 'Heimerdinger',
                  'Jax', 'Jayce', 'Jhin', 'Jinx', "Kai'sa", 'Kalista', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kayle',
                  'Kayn', 'Kennen', "Kha'Zix", 'Kindred', 'Kled', "Kog'Maw", 'Leblanc', 'Lee Sin', 'Leona', 'Lillia', 'Lissandra',
                  'Lucian', 'Lulu', 'Lux', 'Malphite', 'Malzahar', 'Maokai', 'Master Yi', 'Miss Fortune', 'Morderkaiser', 'Morgana',
                  'Nami', 'Nasus', 'Nautilus', 'Neeko', 'Needalee', 'Nocturne', 'Nunu e Willump', 'Olaf', 'Orianna', 'Ornn', 'Pantheon',
                  'Poppy', 'Pyke', 'Qiyana', 'Quinn', 'Rakan', 'Rammus', "Rek'Sai", 'Rell', 'Renata Glasc', 'Renekton', 'Rengar',
                  'Riven', 'Rumble', 'Ryze', 'Samira', 'Sejuani', 'Senna', 'Seraphine', 'Sett', 'Shaco', 'Shen', 'Shyvana', 'Singed',
                  'Sion', 'Sivir', 'Skarner', 'Sona', 'Soraka', 'Swain', 'Sylas', 'Syndra', 'Tahm Kench', 'Taliyah', 'Talon', 'Taric',
                  'Teemo', 'Thresh', 'Tristana', 'Trundle', 'Tryndamere', 'Twisted Fate', 'Twitch', 'Udyr', 'Urgot', 'Varus', 'Vayne',
                  'Veigar', "Vel'Koz", 'Vex', 'Vi', 'Viego', 'Viktor', 'Vladimir', 'Volibear', 'Warwick', 'Wukong', 'Xayah', 'Xerath',
                  'Xin Zhao', 'Yasuo', 'Yone', 'Yorick', 'Yummi', 'Zac', 'Zed', 'Zeri', 'Ziggs', 'Zilean', 'Zoe', 'Zyra']
        champ_escolhido = random.choice(champs)
        return champ_escolhido

    def sortear_lane(self):
        lanes = ['TOP', 'JUNGLE', 'MID', 'ADC', 'SUP']
        lane_escolhida = random.choice(lanes)
        return lane_escolhida

    def sortear_spells(self):
        spells = [' Flash ', ' Curar ', ' Purificar ', ' Ignite ', ' Exaustão ', ' Teleport ', ' Fantasma ', ' Barreira ']
        spell_escolhida = random.sample(spells, 2)
        return ' e '.join(spell_escolhida)

if __name__ == "__main__":
    root = tk.Tk()
    app = Crazylol(root)
    root.mainloop()
