# 🏴‍☠️ Caça ao Tesouro - Jogo de Tabuleiro com Pygame

Um jogo simples de tabuleiro, por turnos, para 2 jogadores, onde o objetivo é encontrar o máximo de tesouros (**T**) possível e evitar as bombas (**B**)

 🎓 **Projeto desenvolvido para a disciplina de Introdução à Programação (2025.2).**
 ## 👨‍💻 Autores

* Ciro
* Julia Rosa
* Liliana

## 🚀 Como Jogar

O jogo é jogado em um tabuleiro 4x4. A mecânica combina elementos de jogo de tabuleiro por turnos com a lógica de células vizinhas, similar ao Campo Minado.

1.  **Objetivo:** Obter a maior pontuação.
2.  **Turnos:** Os jogadores se revezam clicando em um quadrado no tabuleiro.
3.  **Quadrados e Pontuação:**
    * **Tesouro (T - Amarelo):** O jogador ganha **+100 pontos**.
    * **Bomba (B - Vermelho):** O jogador perde **-50 pontos** (a pontuação é limitada a 0, nunca ficando negativa).
    * **Números (Azul):** O número indica quantos tesouros (**T**) estão em quadrados **adjacentes** (vizinhos imediatos na horizontal ou vertical). Nenhuma pontuação é alterada.
    * **Quadrado Não Revelado (Azul Escuro):** Indica que a célula ainda não foi clicada.
4.  **Fim do Jogo:** O jogo termina quando todos os quadrados do tabuleiro forem revelados. Vence o jogador com a maior pontuação.
