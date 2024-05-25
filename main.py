import random as rand
player_point=0
comp_point=0
print('                                   SNAKE WATER GUN')
print()
print('first to 5 points wins')
print()
def game():
    global player_point
    global comp_point
    l=['SNAKE','WATER','GUN']
    while player_point or comp_point < 5:
        comp=rand.choice(l)
        #player=''
        def choice():
            global player
            player=input('Snake , Water or Gun : ')
            player=player.upper()
            if player not in l:
                print('invalid choice')
                choice()
        choice()
        if player==comp:
            print('Draw')
            print('points')
            print('player',player_point)
            print('comp',comp_point)
            print()
        else:
            if player=='SNAKE' and comp=='WATER':
                print('point to player')
                player_point+=1
                print('points')
                print('player',player_point)
                print('comp',comp_point)
            if player=='SNAKE' and comp=='GUN':
                print('point to comp')
                comp_point+=1
                print('points')
                print('player',player_point)
                print('comp',comp_point)
game()