
import random
import pandas as pd
from collections import Counter

table = [0] * 12 #for points table

table1 = [0] * 12 #for points table computer


def points_table(z):
    if (table[z-1]) != 'taken':
       table[z-1] = 'taken'
       #print(table)
#for computer
def points_table_comp(z):
    if (table1[z-1]) != 'taken':
       table1[z-1] = 'taken'
#rolling four dice      
def dice_rolls():
    dice1 = []
    for i in range(4):
        dice1.append(random.randint(1,6))
    print('The dice rolls are: ')
    dce(dice1)
    #print()
    #dice1.sort()
    return dice1

def re_rolled(dice):
    print("Do you want to roll dices again? (Y/N)")
    choice = input()
   
    if choice == 'Y' or choice == 'y':
        print("Choose dices")
        a = [int(a) for a in input().split()]
        for j in a:
            dice[j-1] = random.randint(1,6)
        print('The dice rolls are: ')
        dce(dice)
        print()
        #dice.sort()
   
    return dice
    
            
#visualizing a dice
def dce(l):
    for a in l:
        if a == 1:
            print(' ______ \n|      |\n|      |\n|  ◆  |\n|      |\n|______|')
        elif a == 2:
            print(' _____ \n|     |\n| ◆  |\n|     |\n|   ◆|\n|_____|')
        elif a == 3:
            print(' ______ \n|      |\n|◆    |\n|  ◆  |\n|    ◆|\n|______|')
        elif a == 4:
            print(' _____ \n|     |\n|◆ ◆|\n|     |\n|◆ ◆|\n|_____|')
        elif a == 5:
            print(' ______ \n|      |\n|◆  ◆|\n|  ◆  |\n|◆  ◆|\n|______|')
        else:
            print(' _____ \n|     |\n|◆ ◆|\n|◆ ◆|\n|◆ ◆|\n|_____|')


#for user points table        
def avail_table(s):
    d = {}
    l = []
    name = []
    p = []
    print('...........Points Table...........')
    if (table[0]) != 'taken':
        l.append(1)
        name.append('ones')
        p.append(s[0])
    if (table[1]) != 'taken':
        l.append(2)
        name.append('twos') 
        p.append(s[1])
    if (table[2]) != 'taken':
        l.append(3)
        name.append('threes')
        p.append(s[2])
    if (table[3]) != 'taken':
        l.append(4)
        name.append('Fours')
        p.append(s[3])
    if (table[4]) != 'taken':
        l.append(5)
        name.append('Fives')
        p.append(s[4])
    if (table[5]) != 'taken':
        l.append(6)
        name.append('Sixes')
        p.append(s[5])
    if (table[6]) != 'taken':
        l.append(7)
        name.append('Two in a row')
        p.append(s[6])
    if (table[7]) != 'taken':
        l.append(8)
        name.append('Three in a row')
        p.append(s[7])
    if (table[8]) != 'taken':
        l.append(9)
        name.append('Small Straigth')
        p.append(s[8])
    if (table[9]) != 'taken':
        l.append(10)
        name.append('Large Straigth')
        p.append(s[9])
    if (table[10]) != 'taken':
        l.append(11)
        name.append('Chance')
        p.append(s[10])
    if (table[11]) != 'taken':
        l.append(12)
        name.append('Four of a kind')
        p.append(s[11])
    d = {'number' : l , 'catagories' : name , 'points': p}
    
    
    df = pd.DataFrame(d)
    df = df.set_index('number')
    print(df)
  

#for computers points table

def avail_table_comp(r):
    dc = {}
    lc = []
    namec = []
    pc = []
    if (table1[0]) != 'taken':
        lc.append(1)
        namec.append('ones')
        pc.append(r[0])
    if (table1[1]) != 'taken':
        lc.append(2)
        namec.append('twos') 
        pc.append(r[1])
    if (table1[2]) != 'taken':
        lc.append(3)
        namec.append('threes')
        pc.append(r[2])
    if (table1[3]) != 'taken':
        lc.append(4)
        namec.append('Fours')
        pc.append(r[3])
    if (table1[4]) != 'taken':
        lc.append(5)
        namec.append('Fives')
        pc.append(r[4])
    if (table1[5]) != 'taken':
        lc.append(6)
        namec.append('Sixes')
        pc.append(r[5])
    if (table1[6]) != 'taken':
        lc.append(7)
        namec.append('Two of a kind')
        pc.append(r[6])
    if (table1[7]) != 'taken':
        lc.append(8)
        namec.append('Three of a kind')
        pc.append(r[7])
    if (table1[8]) != 'taken':
        lc.append(9)
        namec.append('Small Straight')
        pc.append(r[8])
    if (table1[9]) != 'taken':
        lc.append(10)
        namec.append('Large Straight')
        pc.append(r[9])
    if (table1[10]) != 'taken':
        lc.append(11)
        namec.append('Chance')
        pc.append(r[10])
    if (table1[11]) != 'taken':
        lc.append(12)
        namec.append('Four of a kind')
        pc.append(r[11])
    dc = {'number' : lc , 'catagories' : namec , 'points': pc}
    
    dfc = pd.DataFrame(dc)
    dfc = dfc.set_index('number')
    print(dfc)
  
       
def calc_points(dice1):
    dice = dice1.copy()
    dice.sort()
    p = [0] * 12
    score = sum(dice)
    p[10] = score
    a = Counter(dice)
 #first six points   
    p[0] = a[1] * 1
    p[1] = a[2] * 2
    p[2] = a[3] * 3
    p[3] = a[4] * 4
    p[4] = a[5] * 5
    p[5] = a[6] * 6
#special points    
    b , c = a.most_common()[0]
    if c >= 3:
        p[7] = score
    if c >= 2:
        p[6] = score
    if c == 4:
        p[11] = 40
        
    
        
 #straight points   
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
        p[8] = 25
    if straight == 4:
        p[9] = 30
    return p
#total score count
total = [0 , 0]
def total_score(z , point):
    total[0] = total[0] + point[z - 1]
    #print(total[0])

#for computer
def total_score_comp(z , point):
    total[1] = total[1] + point[z - 1]
    #print(total[1])



def ai(l):
    points = []
    points.append(l[0] / 40)
    points.append(l[1] / 40)
    points.append(l[2] / 40)
    points.append(l[3] / 40)
    points.append(l[4] / 40)
    points.append(l[5] / 40)
    points.append(l[6] / 40)
    points.append(l[7] / 40)
    points.append(l[8] / 40)
    points.append(l[9] / 40)
    points.append(l[10] / 40)
    points.append(l[11] / 40)
    
    
    
    #print(points)
    
    prob = []
    prob.append(l[0] * 381 / 1296)
    prob.append(l[1] * 381 / 1296)
    prob.append(l[2] * 381 / 1296)
    prob.append(l[3] * 381 / 1296)
    prob.append(l[4] * 381 / 1296)
    prob.append(l[5] * 381 / 1296)
    prob.append(l[6] * 1080 / 1296)
    prob.append(l[7] * 144 / 1296)
    prob.append(l[8] * 216 / 1296)
    prob.append(l[9] * 72 / 1296)
    prob.append(l[10])
    prob.append(l[11] * 6 / 1296)
    
    #print(prob)
    
   
    
    
    
    z = 0
    mx = -0.0
    for j in range(len(points)):
         if points[j] > mx and table1[j] != 'taken':
             mx = points[j]
             z = j 
             #print('vERy')
         elif points[j] == mx and table1[j] != 'taken':
             if prob[j] < prob[z]:
                 mx = points[j]
                 z = j 
                 #print('NO')
         
             
             
         
             
            
                 
    #print(max)
    #print(z+1)
               
    z = z + 1
    return z

      
   
#main function  
for i in range(12):
    dice1 = dice_rolls()
    calc1 = calc_points(dice1)
    avail1 = avail_table(calc1)
    dice_human = re_rolled(dice1)
    calc2 = calc_points(dice_human)
    avail2 = avail_table(calc2)
    #in case user choose a same number twice or number outside the table
    a = 1
    while(a == 1):
        z = int(input('pick???'))
        if z < 1 or z > 12 or (table[z-1]) == 'taken':
             print("you have chosen wrong number. Please choose only the given number")
             a = 1
            
        else:
            table[z-1] = 'taken'
            #print(table)
            a = 2
    points_table(z)
    total_score(z , calc2)
    #For computer
    dice2 = dice_rolls()
    calc2 = calc_points(dice2)
    #dice_computer = re_rolled(dice2)
    #calc2 = calc_points(dice_computer)
    avail2 = avail_table_comp(calc2)
    a = ai(calc2)
    print('........................................')
    print('Computer has chosen number ' + str(a) )
    print('.........................................')
    tab = points_table_comp(a)
    total_score_comp(a , calc2)
    print('..............................................')
    print('USER: ' +str(total[0]) + '   COMPUTER: ' + str(total[1]) )
    print('..............................................')
if total[0] > total[1]:
    print('USER')
else:
    print('COMPUTER')
    
    
    
    
    
    
    
    
    
    



















