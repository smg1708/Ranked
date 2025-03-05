while True:
    vitorias = int(input("Quantas vitorias o jogador obteve? "))
    derrotas = int(input("Quantas derrotas o jogador obteve? "))
    saldo = vitorias - derrotas
    if saldo <= 10:
            print("Se vitórias for menor do que 10 = Ferro")
            break
    if 11 <= saldo <= 20:
        print("Se vitórias for entre 11 e 20 = Bronze")
        break
    if 21 <= saldo <= 50:
        print("Se vitórias for entre 21 e 50 = Prata")
        break
    if 51 <= saldo <= 80:
        print("Se vitórias for entre 51 e 80 = Ouro")
        break
    if 81 <= saldo <= 90:
        print("Se XP for entre 81 e 90 = Diamante")
        break
    if 91 <= saldo <= 100:
        print("Se XP for entre 91 e 100 = Lendário")
        break
    if 101 <= saldo:
        print("Se XP for maior ou igual a 101 = Imortal")
        break