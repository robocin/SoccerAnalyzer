#Código adaptado do repositório https://github.com/fnalmeidap/robocin-projects, originalmente por Felipe Nunes

#Funções do analyzer module para para modalidade 2D

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.patches as patches
import matplotlib.pyplot as plt
import seaborn as sns

log = pd.read_csv('./t1.rcg.csv1')

def placar(log):
    #Gráfico coluna do placar entre os times
    placar = [log['team_score_l'].max(),log['team_score_r'].max()]

    team_left = log.iloc[0].team_name_l
    team_right = log.iloc[0].team_name_r
    equipes = [team_left,team_right]

    eixox = np.arange(len(equipes))
    plt.bar(eixox,placar)
    plt.title('PLACAR')
    plt.xlabel('TIMES')
    plt.ylabel('GOLS')
    plt.ylim(0,5)
    plt.xticks(eixox,equipes)
    plt.show()

def playmodes(log):
    #Gráfico coluna da ocorrência dos playmodes
    modos = pd.value_counts(log['playmode']).plot.bar()

def faltas(log):
    #Gráfico coluna do total de faltas por time
    faltas_r = (log['playmode'] == 'foul_charge_r').sum()
    faltas_l = (log['playmode'] == 'foul_charge_l').sum()

    vetor = [faltas_l, faltas_r]
    eixox = equipes
    y_pos = np.arange(len(eixox))
    plt.bar(y_pos, vetor)

    plt.title('foul_charge_l x foul_charge_r')
    plt.xlabel('teams')
    plt.ylabel('values')
    plt.ylim(0,faltas_l+50)
    plt.xticks(y_pos, eixox)
    plt.show()

def penalidades(log):
    #Gráfico coluna do total de penalidades por time
    penaltis = [log['team_pen_score_l'].max(),log['team_pen_score_r'].max()]

    plt.bar(eixox,penaltis)
    plt.title('PENALTIS')
    plt.xlabel('TIMES')
    plt.ylabel('GOLS')
    plt.ylim(0,10)
    plt.xticks(eixox,equipes)
    plt.show()

def analise_detalhada_faltas(log):
    #Gráfico setor da porcentagem de ações que causaram faltas
    fcl = log['playmode'].str.count('foul_charge_l').sum()
    fcr = log['playmode'].str.count('foul_charge_r').sum()
    fkl = log['playmode'].str.count('free_kick_l').sum()
    fkr = log['playmode'].str.count('free_kick_r').sum()

    labels = ['foul_charge_l', 'foul_charge_r', 'free_kick_l', 'free_kick_r']
    sizes = [fcl, fcr, fkl, fkr]
    colors = ['#83fc5b','#66b3ff','#439129','#5bcdf0']
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',shadow=True, startangle=90, pctdistance = 0.85)

    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    ax1.axis('equal')
    plt.tight_layout()
    plt.show()

def mapaDeCalor_v1(log):
    #Gráfico simples de todas as posições ocupadas pela bola ao longo da partida (TODO: é isso mesmo?)
    mostly_x = log['ball_x'].mean()
    mostly_y = log['ball_y'].mean()

    log.plot(x='ball_x', y='ball_y')

def mapaDeCalor_seaborn(log):
    #Gráfico seaborn representando o mapa de calor da posição da bola 
    ig, ax = plt.subplots()
    fig.set_size_inches(7, 5)

    sns.kdeplot(pp['ball_x'], pp['ball_y'], shade = "True", color = "green", n_levels =10)
    plt.title('POSIÇÃO DE BOLA')
    plt.ylim(-35,35)
    plt.xlim(-55,55)
    plt.show()

def posicaoBola(log):
    #(TODO: posse de bola ou posição referente à qual metade do campo?)
    percentage = log[log['ball_x'] < 0 & (log['playmode'] == 'play_on')]
    left_time = (percentage['ball_x'] < 0).sum()
    right_time = (percentage['ball_y'] > 0).sum()

    labels = ['RoboCIn','ADV']
    sizes = [left_time,right_time]
    colors = ['#23a634','#2aa3db']
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',shadow=True, startangle=90)
    ax1.axis('equal')
    plt.tight_layout()
    plt.title('POSIÇÃO DE BOLA')
    plt.show()

def graficoFaltas(log):
    #Gráfico das posições das faltas, com distinção entre times 
    free_kicks = t1_df[['playmode','ball_x','ball_y']]
    fk_r = free_kicks[free_kicks['playmode']=='free_kick_r']
    fk_l = free_kicks[free_kicks['playmode']=='free_kick_l']
    fk_l.head()
    rx = fk_r['ball_x']
    ry = fk_r['ball_y'
    lx = fk_l['ball_x']
    ly = fk_l['ball_y']
    plt.plot(rx,ry,'o',color='green')
    plt.plot(lx,ly,'o',color='red')

def tacklesTime(log):
    #Tomadas de bola por jogador por time (TODO: é isso mesmo?)
    N = 11

    ind = np.arange(N) 
    width = 0.35       
    plt.bar(ind, tck_l, width, label= equipes[0], color ='green')
    plt.bar(ind + width, tck_r, width,
        label= equipes[1], color = 'red')

    plt.ylabel('TACKLES')
    plt.title('TACKLES DE CADA TIME')

    plt.xticks(ind + width / 2, ('1', '2', '3', '4', '5','6','7','8','9','10','11'))
    plt.show()


