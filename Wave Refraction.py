from functools import partial
from tkinter import *
from base64 import b16encode
import math

# Constantes de cores
RED = 25
GREEN = 25
BLUE = 24

# Função para converter RGB para uma string hexadecimal
def rgb_color(rgb):
    return b'#' + b16encode(bytes(rgb))

# Função para converter radianos para graus
def ToGlaus(rads):
    return (rads * 360) / (math.pi * 2)

# Função para converter graus para radianos
def ToRads(angle):
    return (angle * math.pi * 2) / 360

# Função para corrigir o ângulo adicionando 90 graus (não utilizado)
def corretionAngle(angle):
    return angle + 90

# Criação da janela principal
janela = Tk()
janela.title('Wave Refraction')
janela["background"] = rgb_color((RED, GREEN, BLUE))
janela.geometry('800x600+0+0')

# Criação do canvas para desenho
ambiente = Canvas(janela, width=600, height=600, background='white')
ambiente.pack(side='left')

# Índices de refração dos meios
indice_refra_m1 = 1
indice_refra_m2 = 1.5
indice_refra_m3 = 1

# Ângulo de incidência no primeiro meio em graus
angle_of_incidence = 85
angle_of_incidence_rad = ToRads(angle_of_incidence)  # Conversão para radianos

# Cálculo do ângulo de refração no segundo meio usando a lei de Snell
angle_of_incidence_2_rad = math.asin((indice_refra_m1 * math.sin(angle_of_incidence_rad)) / indice_refra_m2)
angle_of_incidence_2 = ToGlaus(angle_of_incidence_2_rad)  # Conversão para graus

# Cálculo do ângulo de refração no terceiro meio usando a lei de Snell
angle_of_incidence_3_rad = math.asin((indice_refra_m2 * math.sin(angle_of_incidence_2_rad)) / indice_refra_m3)
angle_of_incidence_3 = ToGlaus(angle_of_incidence_3_rad)  # Conversão para graus

# Impressão dos ângulos calculados
print('Ângulo de incidência no meio 1 é de', angle_of_incidence, 'graus')
print('Ângulo de incidência dentro do meio 2 é de', angle_of_incidence_2, 'graus')
print('Ângulo de incidência dentro do meio 3 é de', angle_of_incidence_3, 'graus')

# Posições de origem e direções corrigidas para os vetores das ondas
y_origem_wave = 300
x_origem_wave = -300 * math.sin(angle_of_incidence_rad)  # Cálculo da posição x de origem da onda
y_origem_wave = 300 * math.cos(angle_of_incidence_rad)   # Cálculo da posição y de origem da onda

# Cálculo das direções das ondas refratadas
x_direcao_wave2 = 200 * math.sin(angle_of_incidence_2_rad)
y_direcao_wave2 = 200 * math.cos(angle_of_incidence_2_rad)

x_direcao_wave3 = 200 * math.sin(angle_of_incidence_3_rad)
y_direcao_wave3 = 200 * math.cos(angle_of_incidence_3_rad)

# Coordenadas gerais e divisões para os meios
x_pos_geral = 300
y_division1 = 200
y_division2 = 400

# Criação dos vetores normais
vetor_normal1 = [x_pos_geral, y_division2, x_pos_geral, 0]
vetor_normal2 = [x_pos_geral + x_direcao_wave2, y_division1, x_pos_geral + x_direcao_wave2, 600]

# Criação dos vetores das ondas
vetor_onda1 = [x_pos_geral + x_origem_wave, y_division1 - y_origem_wave, x_pos_geral, y_division1]
vetor2 = [x_pos_geral, y_division1, x_pos_geral + x_direcao_wave2, y_division2]
vetor3 = [x_pos_geral + x_direcao_wave2, y_division2, x_pos_geral + x_direcao_wave3, y_division2 + y_direcao_wave3]

# Desenho do retângulo que representa o segundo meio
meio_2 = [0, y_division1, 600, y_division2]
ambiente.create_rectangle(meio_2, outline='', fill='#C8C8FF', width=2)

# Inicialização das listas para armazenar os elementos gráficos
normal = []
reta = []

# Desenho das normais e das ondas no canvas
normal.append(ambiente.create_line(vetor_normal1, fill="gray", width=1))
normal.append(ambiente.create_line(vetor_normal2, fill="gray", width=1))
reta.append(ambiente.create_line(vetor_onda1, fill="green", width=2))
reta.append(ambiente.create_line(vetor2, fill="yellow", width=2))
reta.append(ambiente.create_line(vetor3, fill="blue", width=2))

# Início do loop principal da janela Tkinter
janela.mainloop()
