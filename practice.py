import random
import pandas as pd

table = [1,2,3,4,5,6,7,8,9,10,11,12]
#print(table)
score = 0
score1 = 0
score2 = 0
score3 = 0
score4 = 0
score5 = 0
score6 = 0
score7 = 0
score8 = 0
score9 = 0
score10 = 0

score12 = 0
dice = []
total_score = 0
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0

def points_table(z):
    if (table[z-1]) != 'taken':
       table[z-1] = 'taken'
       print(table)

def dice_rolls():
    for i in range(4):
        dice.append(random.randint(1,6))
    print('The dice rolls are: ', end = '')
    for d in dice:
        print(str(d) + '  ' ,end = '')
    print()
    dice.sort()


def tabl():
    d = {}
    p = []
    name = []
    l = []
    if (table[0]) != 'taken':
        l.append(1)
        name.append('ones')
        p.append(score1)
    if (table[1]) != 'taken':
        l.append(2)
        name.append('twos') 
        p.append(score2)
    if (table[2]) != 'taken':
        l.append(3)
        name.append('threes')
        p.append(score3)
    if (table[3]) != 'taken':
        l.append(4)
        name.append('Fours')
        p.append(score4)
    if (table[4]) != 'taken':
        l.append(5)
        name.append('Fives')
        p.append(score5)
    if (table[5]) != 'taken':
        l.append(6)
        name.append('Sixes')
        p.append(score6)
    if (table[6]) != 'taken':
        l.append(7)
        name.append('Two in a row')
        p.append(score7)
    if (table[7]) != 'taken':
        l.append(8)
        name.append('Three in a row')
        p.append(score8)
    if (table[8]) != 'taken':
        l.append(9)
        name.append('Small Straigth')
        p.append(score9)
    if (table[9]) != 'taken':
        l.append(10)
        name.append('Large Straigth')
        p.append(score10)
    if (table[10]) != 'taken':
        l.append(11)
        name.append('Chance')
        p.append(score)
    if (table[11]) != 'taken':
        l.append(12)
        name.append('Four of a kind')
        p.append(score12)
    d = {'number' : l , 'catagories' : name , 'points': p}
    #t = pd.Series(d)
    
    df = pd.DataFrame(d)
    df = df.set_index('number')
    print(df)
        

for i in range(3):
    dice_rolls()
    for d in dice:
        if d == 1:
            score1 = score1 + d 
            c1 = c1 + 1
            score = score + d
            
        elif d == 2:
            score2 = score2 + d
            c2 = c2 + 1
            score = score + d
        
        elif d == 3:
            score3 = score3 + d
            c3 = c3 + 1
            score = score + d
        
        elif d == 4:
            score4 = score4 + d
            c4 = c4 + 1
            score = score + d
        
        elif d == 5:
            score5 = score5 + d
            c5 = c5 + 1
            score = score + d
        
        
        elif d == 6:
            score6 = score6 + d
            c6 = c6 + 1
            score = score + d
    
    if c1 >= 3 or c2 >= 3 or c3 >= 3 or c4 >= 3 or c5 >= 3 or c6 >= 3:
        score8 = score
    else:
        score8 == 0
        
    if c1 >= 2 or c2 >= 2 or c3 >= 2 or c4 >= 2 or c5 >= 2 or c6 >= 2:
        score7 = score
    else:
        score7 == 0
        
    if c1 == 4 or c2 == 4 or c3 == 4 or c4 == 4 or c5 == 4 or c6 == 4:
        score12 = 40
    else:
        score12 == 40
        
    
        
    #score = 0
    straight = 1
    for index in range(len(dice)):
        current = index
        count = 1
        while(current != -1):
            if current + 1 < len(dice):
                if dice[current + 1] - dice[current] == 1:
                    current = current + 1
                    count = count + 1
                    #print('yes')
                elif dice[current + 1] == dice[current]:
                    current = current + 1
                else:
                    current = -1
            else:
                 current = -1
                  
            if count > straight:
                 straight = count
    if straight == 3:
        score9 = 25
    if straight == 4:
        score10 = 30
            
            
        
            
        
    
            
            
    tabl()
    a = 1
    while(a == 1):
        z = int(input('pick???'))
        if (table[z-1]) == 'taken':
             print("you have chosen same number. Please choose another")
             a = 1
            
        else:
            table[z-1] = 'taken'
            print(table)
            a = 2
            
       
        
       
        
    
    
    
    
        #z = int(input('pick???'))
    if z != 1:
        score1 = 0
    elif z == 1:
        total_score = total_score + score1
    if z != 2:
        score2 = 0
    elif z == 2:
        total_score = total_score + score2
    if z != 3:
        score3 = 0
    elif z == 3:
        total_score = total_score + score3
    if z != 4:
        score4 = 0
    elif z == 4:
        total_score = total_score + score4
    if z != 5:
        score5 = 0
    elif z == 5:
        total_score = total_score + score5
    if z != 6:
        score6 = 0
    elif z == 6:
        total_score = total_score + score6
    if z != 7:
        score7 = 0
    if z == 7:
        total_score = total_score + score7
        
    if z != 8:
        score8 = 0
    if z == 8:
        total_score = total_score + score8
    if z != 9:
        score9 = 0
    if z == 9:
        total_score = total_score + score9
    if z != 10:
        score10 = 0
    if z == 10:
        total_score = total_score + score10
    if z != 11:
        score = 0
    if z == 11:
        total_score = total_score + score
    if z != 12:
        score12 = 0
    if z == 12:
        total_score = total_score + score12
        
        
    dice.clear()
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    score = 0
print(total_score)



