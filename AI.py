import random


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

def points_table():
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
    if (table[0]) != 'taken':
        print('1.ones =' + str(score1))
    if (table[1]) != 'taken':
        print('2.twos =' + str(score2))
    if (table[2]) != 'taken':
        print('3.threes =' + str(score3))    
    if (table[3]) != 'taken':
        print('4. Fours =' + str(score4))
    if (table[4]) != 'taken':
        print('5.Fives =' + str(score5))
    if (table[5]) != 'taken':
        print('6.Sixes=' + str(score6))
    if (table[6]) != 'taken':
        print('7.Two in a row=' + str(score7))
    if (table[7]) != 'taken':
        print('8.Three in a row=' + str(score8))
    if (table[8]) != 'taken':
        print('9.Small Straigth=' + str(score9))
    if (table[9]) != 'taken':
        print('10.Large Straigth=' + str(score10))
    if (table[10]) != 'taken':
        print('11.Chance=' + str(score))
    if (table[11]) != 'taken':
        print('12.Four of a kind=' + str(score12))
        

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
    #print(score7)
    #print(c1)
    #print(c2)
    #print(c3)
    #print(c4)
    #print(c5)
    #print(c6)
    
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
    
    points = []
    points.append(score1 / 40)
    points.append(score2 / 40)
    points.append(score3 / 40)
    points.append(score4 / 40)
    points.append(score5 / 40)
    points.append(score6 / 40)
    points.append(score7 / 40)
    points.append(score8 / 40)
    points.append(score9 / 40)
    points.append(score10 / 40)
    points.append(score / 40)
    points.append(score12 / 40)
    
    
    
    print(points)
    
    prob = []
    prob.append(score1 * 381 / 1296)
    prob.append(score2 * 381 / 1296)
    prob.append(score3 * 381 / 1296)
    prob.append(score4 * 381 / 1296)
    prob.append(score5 * 381 / 1296)
    prob.append(score6 * 381 / 1296)
    prob.append(score7 * 1080 / 1296)
    prob.append(score8 * 144 / 1296)
    prob.append(score9 * 216 / 1296)
    prob.append(score10 * 72 / 1296)
    prob.append(score)
    prob.append(score12 * 6 / 1296)
    
    print(prob)
    
   
    
    
    
    z = 0
    max = -0.0
    for j in range(len(points)):
         if points[j] > max:
             max = points[j]
             z = j 
         elif points[j] == max:
             if prob[j] < prob[z]:
                 max = points[j]
             
             
         
             
            
                 
    print(max)
    print(z+1)
               
    z = z + 1

       
        
       
        
    
    
    
    
        #z = int(input('pick???'))

    if z != 1:
        score1 = 0
    elif z == 1:
        total_score = total_score + score1
        score1 = 0
    if z != 2:
        score2 = 0
    elif z == 2:
        total_score = total_score + score2
        score2 = 0
    if z != 3:
        score3 = 0
    elif z == 3:
        total_score = total_score + score3
        score3 = 0
    if z != 4:
        score4 = 0
    elif z == 4:
        total_score = total_score + score4
        score4 = 0
    if z != 5:
        score5 = 0
    elif z == 5:
        total_score = total_score + score5
        score5 = 0
    if z != 6:
        score6 = 0
    elif z == 6:
        total_score = total_score + score6
        score6 = 0
    if z != 7:
        score7 = 0
    if z == 7:
        total_score = total_score + score7
        score7 = 0
        
    if z != 8:
        score8 = 0
    if z == 8:
        total_score = total_score + score8
        score8 = 0
    if z != 9:
        score9 = 0
    if z == 9:
        total_score = total_score + score9
        score9 = 0
    if z != 10:
        score10 = 0
    if z == 10:
        total_score = total_score + score10
        score10 = 0
    if z != 11:
        score = 0
    if z == 11:
        total_score = total_score + score
        score11 = 0
    if z != 12:
        score12 = 0
    if z == 12:
        total_score = total_score + score12
        score12 = 0
        
    dice.clear()
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    score = 0
              

        
       
    

print(total_score)




