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
            [sg.Text(' ESCOLHAS DO DIA SURIKATY'), sg.Text(emoji.emojize(":red_heart:"))],        
            [sg.Output(size=(50,4))],
            [sg.Text('                               '), sg.Button('Sortear')]
        ]  
        pygame.init()
        pygame.mixer.music.load('mario_full.mp3')
        pygame.mixer.music.play()
        self.janela = sg.Window('Sorteio Surikaty', layout, size=(350,150))

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
                #sorteio_spell = self.sortear_spells(valores)
                print('O QUIZ DO DIA É SOBRE: {}, \nA recompensa: {}.'.format(sorteio_champ, 
                sorteio_lane))
                sleep(1)
                pygame.init()
                pygame.mixer.music.load('mario_full.mp3')
                pygame.mixer.music.play()

    def sortear(self, valores):
        champs = ['Ballet', 'Letras', 'Surikaty', 'Linguas', 'Arquitetura', 'Conhecimentos Gerais',
        'Harry Potter', '1 Banda famosa Atualmente']
        champ_escolhido = random.choice(champs)
        champ = ''.join(champ_escolhido)
        return champ

    def sortear_lane(self, valores):
        lanes = ['10 Perguntas sobre o Mundo', '7 perguntas sobre Idiomas', 
        '+1 Doce de leite quando nos vermos', '1 mordida', '10 perguntas SIM OU NÃO', 'Curiosidade linguísticas'
        'Curiosidades sobre Países', 'Planos para próximos passeios/encontros/viagens']
        lane_escolhida = random.choice(lanes)
        lane = ''.join(lane_escolhida)
        return lane

#def sortear_spells(self, valores):
        #spells = [' Flash ', ' Curar ', ' Purificar ', ' Ignite ', ' Exaustão ', ' Teleport ', ' Fantasma ', ' Barreira ']
        #spell_escolhida = random.sample(spells, 2)
        #spell = ''.join(spell_escolhida)
        #return spell

gen = Crazylol()
gen.Iniciar()
