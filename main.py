from random import randint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def ver(jogador):
  if jogador == 'p':
    return False
  elif jogador == 'a':
    return False
  elif jogador == 't':
    return False
  else:
    return True

def ascii(jogador):
  asc = str('')
  if jogador == 'p':
    asc = '@'
    return asc
  elif jogador == 'a':
    asc = '___'
    return asc
  else:
    asc = '8<'
    return asc

def jogo(c,j):
  jogador = str(input('Pedra (p), Papel (a), Tesoura (t)? ')).lower()
  if jogador == "" or ver(jogador):
    print("{}Por favor digitar uma alternativa!{}".format(bcolors.WARNING,bcolors.ENDC))
    print('============================================')
    jogo(c,j)
  else:
    scoreC = int(c)
    scoreJ = int(j)
    print(ascii(jogador),'vs', end='  ')
    escolhido = randint(1,3)

 
    #print(escolhido)
   
    if escolhido == 1:
    	computador = 'p'
    elif escolhido == 2:
    	computador = 'a'
    else:
    	computador = 't'
    print(ascii(computador))
 
    if jogador == computador:
    	print('{}EMPATE{}'.format(bcolors.OKBLUE,bcolors.ENDC))
    elif jogador =='p' and computador =='t':
      scoreJ += 1
      print('{}O jogador ganhou!{} O jogador está com: {}'.format(bcolors.OKGREEN,bcolors.ENDC,scoreJ))
    elif jogador =='p' and computador =='a':
      scoreC += 1
      print('{}O computador ganhou!{} O Computador está com: {}'.format(bcolors.FAIL,bcolors.ENDC,scoreC))
    elif jogador =='a' and computador =='p':
      scoreJ += 1
      print('{}O jogador ganhou!{} O jogador está com: {}'.format(bcolors.OKGREEN,bcolors.ENDC,scoreJ))
    elif jogador =='a' and computador =='t':
      scoreC += 1
      print('{}O computador ganhou!{} O Computador está com: {}'.format(bcolors.FAIL,bcolors.ENDC,scoreC))
    elif jogador =='t' and computador =='a':
      scoreJ += 1
      print('{}O jogador ganhou!{} O jogador está com: {}'.format(bcolors.OKGREEN,bcolors.ENDC,scoreJ))
    elif jogador =='t' and computador =='p':
      scoreC += 1
      print('{}O computador ganhou!{} O Computador está com: {}'.format(bcolors.FAIL,bcolors.ENDC,scoreC))
   
    print('============================================')
    jogo(scoreC,scoreJ)
jogo(0,0)
