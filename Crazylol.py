from ast import Break
import random
import PySimpleGUI as sg
import os
import emoji
import pygame
from time import sleep

class Crazylol:
    def __init__(self):
        #sg.theme('DarkBlack1')
        sg.theme('DarkBlack')
        layout = [
            [sg.Text(' NÃO USE ESSE PROGRAMA EM RANKEDS!'), sg.Text(emoji.emojize(":red_heart:"))],        
            [sg.Output(size=(50,4))],
            [sg.Text('                               '), sg.Button('Sortear')]
        ]  
        pygame.init()
        pygame.mixer.music.load('mario_full.mp3')
        pygame.mixer.music.play()
        self.janela = sg.Window('Crazy LoL', layout, size=(350,150))

    def Iniciar(self):
        while True:
            evento, valores = self.janela.read()
            if evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Sortear':
                pygame.init()
                pygame.mixer.music.load('mario_pulo.mp3')
                pygame.mixer.music.play()
                sorteio_champ = self.sortear(valores)
                sorteio_lane = self.sortear_lane(valores)
                sorteio_spell = self.sortear_spells(valores)
                print('Seu champ será: {}, \nSua lane: {}, \nSuas spells: {}.'.format(sorteio_champ, 
                sorteio_lane, sorteio_spell))
                sleep(1)
                pygame.init()
                pygame.mixer.music.load('mario_full.mp3')
                pygame.mixer.music.play()

    def sortear(self, valores):
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
        champ = ''.join(champ_escolhido)
        return champ

    def sortear_lane(self, valores):
        lanes = ['TOP', 'JUNGLE', 'MID', 'ADC', 'SUP']
        lane_escolhida = random.choice(lanes)
        lane = ''.join(lane_escolhida)
        return lane

    def sortear_spells(self, valores):
        spells = [' Flash ', ' Curar ', ' Purificar ', ' Ignite ', ' Exaustão ', ' Teleport ', ' Fantasma ', ' Barreira ']
        spell_escolhida = random.sample(spells, 2)
        spell = ''.join(spell_escolhida)
        return spell

gen = Crazylol()
gen.Iniciar()
