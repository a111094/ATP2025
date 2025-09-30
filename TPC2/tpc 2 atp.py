import random
soma = 21
print("Jogo dos fósforos, número inicial de fósforos é 21. Cada jogador pode tirar entre 1 a 4 fósforos. Quem tirar o último perde!")

play = int(input("Quem começa? (1=tu, 2=computador):"))

if play == 1:

    while soma > 1:
        n = int(input("Escolhe um número de fósforos (1-4):"))
        while n < 1 or n > 4 or n > soma:
            print("Número inválido, escolhe entre 1 e 4, e não maior que o número de fósforos que restam. ")
            n=int(input("Diz me um número de fósforos de (1-4)"))

        soma -= n
        print(f"Tiraste {n} fósforos. Faltam {soma} fósforos.")

        if soma == 1:
            print("Ganhaste, o computador perdeu")
            break

        comp = min(5-n, soma -1)
        soma -= comp 
        print(f"O computador tirou {comp} fósforos. Faltam {soma} fósforos.")

        if soma == 1:
            print("Perdeste, o computador ganhou")
            break

else:

    comp = random.randint(1,4)
    soma -= comp
    print(f"O computador tirou {comp} fósforos. Faltam {soma} fósforos.")

    while soma > 1:
        n = int(input("Diz um número de fósforos de (1-4):"))
        while n < 1 or n > 4 or n > soma:
            print("Número inválido, escolhe entre 1 e 4, e não maior que os fósforos restantes.")
            n = int(input("Diz um número de fósforos (1-4):"))

            soma -= n 
            print(f"Tiraste {n} fósforos. Faltam {soma} fósforos.")

            if soma == 1:
                print("Ganhaste, o computador perdeu!")
                break

            if soma % 5 !=1:
                comp = (soma -1) %5
                if comp == 0:
                    comp = random.randint(1, min(4, soma-1))
            else:
                comp = random.randint(1, min(4, soma -1))
            
            soma -= comp
            print(f"O computador tirou {comp} fósforos. Faltam {soma}fósforos.")

            if soma == 1:
                print("Perdeste, o computador ganhou!")
                break