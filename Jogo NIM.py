def computador_escolhe_jogada(n,m):
    if n%(m+1) == 0:
        e = m
    else:
        e = n%(m+1)
        
    if e == 1:
            print('O computador tirou uma peça.')
    else:
            print('O computador tirou %d peças' %(e))
    
    return e
    

def usuario_escolhe_jogada(n,m):
    e = int(input('Quantas peças você vai tirar? '))
    
    while e > m:
        print()
        print('Oops! Jogada inválida! Tente de novo.')
        print()
        e = int(input('Quantas peças você vai tirar? '))
        
    if e == 1:
        print('Você tirou uma peça.')
    else:
        print('Voce tirou %d peças.' %(e))
    
    return e
        
            
def partida():
    vencedor = 0
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    
    while m > n:
        print('O limite de pecas tem que ser menor que o total de pecas! Tente Novamente:')
        n = int(input('Quantas peças? '))
        m = int(input('Limite de peças por jogada? '))
        print()
        
    if n % (m + 1) == 0:
        print('Voce começa!')
        print()
        
    else:
        print('Computador começa!')
        print()


    while n > 0:
       if n % (m + 1) != 0:
           n = n - (computador_escolhe_jogada(n, m))
           if n == 1:
               print('Agora resta apenas uma peça no tabuleiro.')
           elif n == 0:
               print('Fim do jogo! O computador ganhou!')
               vencedor += 1
               break    
           else:    
               print('Agora restam', n , 'peças no tabuleiro.')
           print()
               
           n = n - (usuario_escolhe_jogada(n, m))
           if n == 1:
               print('Agora resta apenas uma peça no tabuleiro.')
           elif n == 0:
               print('Fim do jogo! Voce ganhou!')
               vencedor += 2
               break    
           else:    
               print('Agora restam', n , 'peças no tabuleiro.')
           print()
           
           
       elif n % (m + 1) == 0:
           n = n - (usuario_escolhe_jogada(n, m))
           if n == 1:
               print('Agora resta apenas uma peça no tabuleiro.')
           elif n == 0:
               print('Fim do jogo! Voce ganhou!')
               vencedor += 2
               break    
           else:    
               print('Agora restam', n , 'peças no tabuleiro.')
           print()
           
           n = n - (computador_escolhe_jogada(n, m))
           if n == 1:
               print('Agora resta apenas uma peça no tabuleiro.')
           elif n == 0:
               print('Fim do jogo! O computador ganhou!')
               vencedor += 1
               break    
           else:    
               print('Agora restam', n , 'peças no tabuleiro.')
           print()

    return vencedor           
             
        
def campeonato():
    computador = 0
    usuario = 0
    print('Voce escolheu um campeonato!')
    print()
    print('**** Rodada 1 ****')
    print()
    
    if partida() == 1:
        computador += 1
    elif partida() == 2:
        usuario += 1
        
    print()
    print('**** Rodada 2 ****')
    print()
    
    if partida() == 1:
        computador += 1
    elif partida() == 2:
        usuario += 1
        
    print()
    print('**** Rodada 3 ****')
    print()
    
    if partida() == 1:
        computador += 1
    elif partida() == 2:
        usuario += 1
    
    print('**** Final do campeonato! ****')
    print()
    print('Placar: Você %d X %d Computador' %(usuario, computador))

#-----------------------------------------------------------------------------------------------------------------------------------------------#

def menu():
    while True:
        print('Bem-vindo ao jogo do NIM! Escolha:')
        print()
        P = int(input('1 - para jogar uma partida isolada \n'
                  '2 - para jogar um campeonato '))
        while P != 1 and P != 2:
            print('Opcao Invalida! Tente Novamente:')
            P = int(input('1 - para jogar uma partida isolada \n'
                      '2 - para jogar um campeonato '))
        print()    
        if P == 1:
            print('Voce escolheu uma partida isolada!')
            print()
            partida()
        elif P == 2:
            campeonato()
            
        replay = str(input('Deseja jogar novamente? '))
        if replay == "y" or replay == "Y":
            return True
        else:
            return1 False
        
menu()