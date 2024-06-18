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

# Função para atualizar o desenho baseado no ângulo de incidência e índices de refração
def update_drawing(angle, n1, n2, n3):
    angle_of_incidence = float(angle)
    indice_refra_m1 = float(n1)
    indice_refra_m2 = float(n2)
    indice_refra_m3 = float(n3)

    angle_of_incidence_rad = ToRads(angle_of_incidence)  # Conversão para radianos

    # Cálculo do ângulo de refração no segundo meio usando a lei de Snell
    try:
        angle_of_incidence_2_rad = math.asin((indice_refra_m1 * math.sin(angle_of_incidence_rad)) / indice_refra_m2)
        angle_of_incidence_2 = ToGlaus(angle_of_incidence_2_rad)  # Conversão para graus
    except ValueError:
        angle_of_incidence_2 = 90  # Se a refração total interna ocorrer

    # Cálculo do ângulo de refração no terceiro meio usando a lei de Snell
    try:
        angle_of_incidence_3_rad = math.asin((indice_refra_m2 * math.sin(angle_of_incidence_2_rad)) / indice_refra_m3)
        angle_of_incidence_3 = ToGlaus(angle_of_incidence_3_rad)  # Conversão para graus
    except ValueError:
        angle_of_incidence_3 = 90  # Se a refração total interna ocorrer

    # Posições de origem e direções corrigidas para os vetores das ondas
    x_origem_wave = -300 * math.sin(angle_of_incidence_rad)  # Cálculo da posição x de origem da onda
    y_origem_wave = 300 * math.cos(angle_of_incidence_rad)   # Cálculo da posição y de origem da onda

    # Cálculo das direções das ondas refratadas
    x_direcao_wave2 = 200 * math.sin(angle_of_incidence_2_rad)
    y_direcao_wave2 = 200 * math.cos(angle_of_incidence_2_rad)

    x_direcao_wave3 = 200 * math.sin(angle_of_incidence_3_rad)
    y_direcao_wave3 = 200 * math.cos(angle_of_incidence_3_rad)

    # Atualização das coordenadas dos vetores das ondas
    vetor_onda1 = [x_pos_geral + x_origem_wave, y_division1 - y_origem_wave, x_pos_geral, y_division1]
    vetor2 = [x_pos_geral, y_division1, x_pos_geral + x_direcao_wave2, y_division2]
    vetor3 = [x_pos_geral + x_direcao_wave2, y_division2, x_pos_geral + x_direcao_wave3, y_division2 + y_direcao_wave3]

    # Atualização do vetor normal no meio 2
    vetor_normal2 = [x_pos_geral + x_direcao_wave2, y_division2-200, x_pos_geral + x_direcao_wave2, 600]

    # Limpeza do canvas e redesenho dos elementos
    ambiente.delete('all')
    ambiente.create_rectangle(meio_2, outline='', fill='#C8C8FF', width=2)
    normal.clear()
    reta.clear()
    normal.append(ambiente.create_line(vetor_normal1, fill="gray", width=1))
    normal.append(ambiente.create_line(vetor_normal2, fill="gray", width=1))
    reta.append(ambiente.create_line(vetor_onda1, fill="green", width=2))
    reta.append(ambiente.create_line(vetor2, fill="yellow", width=2))
    reta.append(ambiente.create_line(vetor3, fill="blue", width=2))

# Função para ler os valores dos campos de entrada e atualizar o desenho
def set_values():
    angle = float(angle_entry.get())
    n1 = float(n1_entry.get())
    n2 = float(n2_entry.get())
    n3 = float(n3_entry.get())
    angle_slider.set(angle)
    n1_slider.set(n1)
    n2_slider.set(n2)
    n3_slider.set(n3)
    update_drawing(angle, n1, n2, n3)

# Criação da janela principal
janela = Tk()
janela.title('Wave Refraction')
janela["background"] = rgb_color((RED, GREEN, BLUE))
janela.geometry('800x600+0+0')

# Criação do canvas para desenho
ambiente = Canvas(janela, width=600, height=600, background='white')
ambiente.pack(side='left')

# Coordenadas gerais e divisões para os meios
x_pos_geral = 300
y_division1 = 200
y_division2 = 400

# Criação dos vetores normais
vetor_normal1 = [x_pos_geral, y_division2, x_pos_geral, 0]
vetor_normal2 = [x_pos_geral, y_division1, x_pos_geral, 600]

# Desenho do retângulo que representa o segundo meio
meio_2 = [0, y_division1, 600, y_division2]
ambiente.create_rectangle(meio_2, outline='', fill='#C8C8FF', width=2)

# Inicialização das listas para armazenar os elementos gráficos
normal = []
reta = []

# Adição do vetor normal inicial
normal.append(ambiente.create_line(vetor_normal1, fill="gray", width=1))
normal.append(ambiente.create_line(vetor_normal2, fill="gray", width=1))

# Criação do frame para os controles
control_frame = Frame(janela, background=rgb_color((RED, GREEN, BLUE)))
control_frame.pack(side='right', fill='both', expand=True)

# Criação da barra deslizante para ajustar o ângulo de incidência
angle_slider = Scale(control_frame, from_=-90, to=90, orient=HORIZONTAL, label='Ângulo de Incidência', command=lambda val: update_drawing(val, n1_slider.get(), n2_slider.get(), n3_slider.get()))
angle_slider.pack(padx=20, pady=10)

# Criação das barras deslizantes para ajustar os índices de refração
n1_slider = Scale(control_frame, from_=0, to=2, resolution=0.01, orient=HORIZONTAL, label='Índice de Refração M1', command=lambda val: update_drawing(angle_slider.get(), val, n2_slider.get(), n3_slider.get()))
n1_slider.pack(padx=20, pady=10)

n2_slider = Scale(control_frame, from_=0, to=2, resolution=0.01, orient=HORIZONTAL, label='Índice de Refração M2', command=lambda val: update_drawing(angle_slider.get(), n1_slider.get(), val, n3_slider.get()))
n2_slider.pack(padx=20, pady=10)

n3_slider = Scale(control_frame, from_=0, to=2, resolution=0.01, orient=HORIZONTAL, label='Índice de Refração M3', command=lambda val: update_drawing(angle_slider.get(), n1_slider.get(), n2_slider.get(), val))
n3_slider.pack(padx=20, pady=10)

# Criação das caixas de entrada para o ângulo de incidência e índices de refração
angle_entry = Entry(control_frame)
angle_entry.pack(padx=20, pady=10)

n1_entry = Entry(control_frame)
n1_entry.pack(padx=20, pady=10)

n2_entry = Entry(control_frame)
n2_entry.pack(padx=20, pady=10)

n3_entry = Entry(control_frame)
n3_entry.pack(padx=20, pady=10)

# Criação do botão de confirmação para ajustar o ângulo de incidência e índices de refração
set_button = Button(control_frame, text='Set Values', command=set_values)
set_button.pack(padx=20, pady=10)

# Início do loop principal da janela Tkinter
janela.mainloop()
