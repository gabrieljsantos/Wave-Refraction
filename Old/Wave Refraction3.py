from functools import partial
from tkinter import*
from base64 import b16encode
import math
 
RED = 25
GREEN = 25
BLUE = 24
def rgb_color(rgb):
    return(b'#' + b16encode(bytes(rgb)))
def ToGlaus(rads):
    return ((rads*360)/(math.pi*2))
def ToRads(angle):
    return((angle*math.pi*2)/360)
def corretionAngle(angle):
    return angle+90

janela = Tk()
janela.title('Wave Refraction')
janela["background"]= rgb_color((RED, GREEN, BLUE))
janela.geometry('800x600+1500+20')

ambiente = Canvas(janela, width=600, height=600, background='white')
ambiente.pack(side='left')
indice_refra_m1 = 1
indice_refra_m2 = 1.5
indice_refra_m3 = 1
reta = []
normal =[]

angle_of_incidence = 85
angle_of_incidence_rad = ToRads(angle_of_incidence)
angle_of_incidence_2_rad = (math.asin(((indice_refra_m1*math.sin(angle_of_incidence_rad))/indice_refra_m2)))
angle_of_incidence_2 = ToGlaus(angle_of_incidence_2_rad)
angle_of_incidence_3_rad = (math.asin(((indice_refra_m2*math.sin(angle_of_incidence_2_rad))/indice_refra_m3)))
angle_of_incidence_3 = ToGlaus(angle_of_incidence_3_rad)
print('angulo de incidencia no meio 1 é de ',(angle_of_incidence),'graus')
print('angulo de incidencia dentro do meio 2 é de',(angle_of_incidence_2),'graus')
print('angulo de incidencia dentro do meio 3 é de',(angle_of_incidence_3),'graus')

y_origem_wave=300
if angle_of_incidence != 0:
    x_origem_wave=-300*math.sin(angle_of_incidence_rad)
else :
    x_origem_wave=0
y_origem_wave=300*math.cos(angle_of_incidence_rad)
if angle_of_incidence_2_rad != 0:
    x_direcao_wave2= math.sqrt(((1/(math.sin(angle_of_incidence_2_rad+ (math.pi/2))**2))*200**2)-200**2)
else :
    x_direcao_wave2=0

if angle_of_incidence_3_rad != 0:
    x_direcao_wave3= math.sqrt(((1/(math.sin(angle_of_incidence_3_rad)**2))*200**2)-200**2)
else :
    x_direcao_wave3=0

y_direcao_wave= 200*math.cos(angle_of_incidence_2_rad) 
x_pos_geral=300
y_division1=200
y_division2=400
print(x_origem_wave)
print(y_origem_wave)

vetor_normal1 = [x_pos_geral,y_division2,x_pos_geral,0]
vetor_normal2 = [x_pos_geral+x_direcao_wave3,y_division1,x_pos_geral+x_direcao_wave3,600]

vetor_onda1 = [x_pos_geral+x_origem_wave,y_division1-y_origem_wave,x_pos_geral,y_division1]
print(vetor_onda1)
vetor2 = [300,200,x_direcao_wave2,400]
vetor3 = [x_direcao_wave2,400,x_direcao_wave3,600]

meio_2 = [0,y_division1,600,y_division2] #x0, y0, x1, y1, (x0, y0) é o canto superior esquerdo e (x1, y1) é a localização do pixel fora do canto inferior direito.
ambiente.create_rectangle(meio_2, outline='', fill='#C8C8FF', width=2)

ambiente.create_rectangle([300,100,200,200], outline='', fill='#FFC8FF', width=2)
normal.append(ambiente.create_polygon(vetor_normal1, outline="gray", fill='yellow', width=1))
normal.append(ambiente.create_polygon(vetor_normal2, outline="gray", fill='yellow', width=1))
reta.append(ambiente.create_polygon(vetor_onda1, outline="green", fill='yellow', width=2))
reta.append(ambiente.create_polygon(vetor2, outline="yellow", fill='yellow', width=2))
reta.append(ambiente.create_polygon(vetor3, outline="blue", fill='yellow', width=2))


#def draw (vetor1):

    

 #, 
#ambiente.place(relx=1.0, rely=1.0, anchor=)
 # , fill="both" , expand=True


janela.mainloop()

