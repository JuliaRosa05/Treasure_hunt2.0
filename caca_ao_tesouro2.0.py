import pygame
import random
import sys

pygame.init()

pygame.mixer.music.load("musica_jogo.mp3") 
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.40)

largura = 700
altura = 700
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Caça ao Teseouro - Ciro, Julia Rosa, Liliana")
fonte_letra = pygame.font.SysFont(None, 40)

azul = (117,121,146)
amarelo = (238, 139, 26)
vermelho = (164,25,23)
bege = (109,160,225)
preto = (14,15,21)

linhas = colunas = 4
tamanho = 120
margem = 10
tabuleiro = [["" for _ in range(colunas)] for _ in range(linhas)]
revelado = [[False] * colunas for _ in range(linhas)]

def vizinhos(linha, coluna):
    vizinho = []
    if linha > 0: 
        vizinho.append((linha - 1, coluna)) 
    if linha < linhas - 1: 
        vizinho.append((linha + 1, coluna))
    if coluna > 0: 
        vizinho.append((linha, coluna - 1))
    if coluna < colunas - 1:
        vizinho.append((linha, coluna + 1))
    return vizinho

posição = [(linha, coluna) for linha in range(linhas) for coluna in range (colunas)]
random.shuffle(posição)
for linha, coluna in posição[:6]:
    tabuleiro[linha][coluna] = "T"
for linha, coluna in posição[6:9]:
    tabuleiro[linha][coluna] = "B"
    for l in range(linhas):
        for c in range(colunas):
            if tabuleiro[l][c] == "":
                num_tesouros_vizinhos = 0
                for v_l, v_c in vizinhos(l, c):
                    if tabuleiro[v_l][v_c] == "T":
                        num_tesouros_vizinhos += 1
                tabuleiro[l][c] = str(num_tesouros_vizinhos)

pontos = [0,0]
jogador = 0
fim = False

def clicar(mx,my, jogador_atual, estado_fim):

    for linha in range(linhas):
        for coluna in range(colunas):
            x = 50 + coluna * (tamanho + margem)
            y = 100 + linha * (tamanho + margem)
            retangulo = pygame.Rect(x,y, tamanho, tamanho)

            if retangulo.collidepoint(mx,my) and not revelado[linha][coluna]:
                revelado[linha][coluna] = True
                vizinho = tabuleiro[linha][coluna]
                if vizinho == "T":
                    pontos[jogador_atual]+= 100
                elif vizinho == "B":
                    novo_placar = pontos[jogador_atual] - 50
                    if novo_placar < 0:
                        pontos[jogador_atual] = 0
                    else:
                        pontos[jogador_atual] = novo_placar

                jogo_terminou = True
                

                for linha_checado in range(linhas):
                    for coluna_checado in range(linhas):
                        if revelado[linha_checado][coluna_checado] is False:
                            jogo_terminou = False
                            break
                estado_fim = jogo_terminou
                return 1 - jogador_atual,estado_fim
    return jogador_atual, estado_fim


def desenhar():
    tela.fill(bege)
    player1 = fonte_letra.render(f"Jogador 1: {pontos[0]}", True, preto)
    player2 = fonte_letra.render(f"Jogador 2: {pontos[1]}", True, preto)
    tela.blit(player1, (50, 30))
    tela.blit(player2, (largura-250, 30))

    for l in range(linhas):
        for c in range(colunas):
            x = 50 + c * (tamanho + margem) 
            y = 100 + l * (tamanho + margem)
            retangulo = pygame.Rect(x,y, tamanho, tamanho)
            pygame.draw.rect(tela, preto, retangulo, 2)
            if revelado[l][c]:
                if tabuleiro[l][c] == "T":
                    pygame.draw.rect(tela, amarelo, retangulo)
                    texto = fonte_letra.render ("T", True, preto)
                elif tabuleiro[l][c] == "B":
                    pygame.draw.rect(tela, vermelho, retangulo)
                    texto = fonte_letra.render ("B", True, preto)
                else:
                    pygame.draw.rect(tela, azul, retangulo)
                    texto = fonte_letra.render(tabuleiro[l][c], True, preto)
                tela.blit(texto, (x+ tamanho/2-10, y + tamanho/2-20))
            else:
                pygame.draw.rect(tela, azul, retangulo)
    if fim:
        if pontos[0] > pontos[1]:
            mensagem = "Jogador 1 venceu!"
        elif pontos[1] > pontos[0]:
            mensagem = "Jogador 2 venceu!"
        else:
            mensagem = "Empate!!!"
        tipo_texto = fonte_letra.render(mensagem,True, (preto))
        tela.blit(tipo_texto, (largura/2 - 150, altura - 60))
    pygame.display.flip()

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            jogador, fim = clicar(*event.pos, jogador, fim)
    desenhar()
    clock.tick(30)
    


