# Calculadora de Partidas Rankeadas
[GFT Start #6 - Lógica de Programação](https://www.dio.me/users/dognew)

## Descrição

Este projeto é uma calculadora de partidas rankeadas, desenvolvida para determinar o saldo de vitórias e derrotas de um jogador e calcular seu nível em um jogo baseado nesse saldo. Através de uma interface de terminal interativa e refinada, o programa solicita ao usuário o número de vitórias e derrotas, calcula o saldo de partidas e determina o nível do jogador com base nas vitórias.

## Funcionalidades

- Recebe as vitórias e derrotas do jogador.
- Calcula o saldo de partidas (vitórias - derrotas).
- Classifica o jogador em diferentes níveis baseados no número de vitórias.
- Exibe o resultado de maneira clara e interativa, utilizando a biblioteca **curses** para uma interface mais profissional.

## Níveis

- Ferro: Menos de 10 vitórias.
- Bronze: Entre 11 e 20 vitórias.
- Prata: Entre 21 e 50 vitórias.
- Ouro: Entre 51 e 80 vitórias.
- Diamante: Entre 81 e 90 vitórias.
- Lendário: Entre 91 e 100 vitórias.
- Imortal: 101 vitórias ou mais.

## Como rodar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/douglas-student/dio-rank-calculator
   ```

2. Instale o Python e as dependências (caso necessário).

3. Execute o programa:
   ```bash
   python3 calculadora_rankeadas.py
   ```

4. Siga as instruções no terminal para fornecer as vitórias e derrotas.

## Tecnologias Utilizadas

- **Python 3.x**
- **curses**: Para criar uma interface de terminal interativa e profissional.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.


