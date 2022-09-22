import random


table = [1,2,3,4,5,6]
#print(table)
score1 = 0
score2 = 0
score3 = 0
score4 = 0
score5 = 0
score6 = 0
dice = []
dice1 = []

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
    
"""        
print("1..." + str(score1))
print("2..." + str(score2))
print("3..." + str(score3))
print("4.." + str(score4))
print("5.." + str(score5))
print("6.." + str(score6))
"""
    
print(dice)    


    

   
dice_rolls()   

for d in dice:
    if d == 1:
        score1 = score1 + d
        
    elif d == 2:
        score2 = score2 + d
        
    elif d == 3:
        score3 = score3 + d
        
    elif d == 4:
        score4 = score4 + d
        
    elif d == 5:
        score5 = score5 + d
        
        
    elif d == 6:
        score6 = score6 + d
"""       
print("1..." + str(score1))
print("2..." + str(score2))
print("3..." + str(score3))
print("4.." + str(score4))
print("5.." + str(score5))
print("6.." + str(score6))

"""    
"""        
def straight(dice):
    straight = 1
    for index in range(len(dice)):
        current = index
        count = 1
        while(current != -1):
            if current + 1 < len(dice):
                if int(dice[current + 1]) - int(dice[current]) == 1:
                    current = current + 1
                    count = count + 1
                elif int(dice[current + 1]) == int(dice[current]):
                    current = current + 1
                else:
                    current = -1
            else:
                current = -1
            if count > straight:
                straight = count
    if straight == 2:
        print("Small Straight: 30 points.")
        return 30
    else:
        return 0
"""

straight = 1
for index in range(len(dice)):
    current = index
    count = 1
    while(current != -1):
        if current + 1 < len(dice):
            if dice[current + 1] - dice[current] == 1:
                current = current + 1
                count = count + 1
                print('yes')
            elif dice[current + 1] == dice[current]:
                current = current + 1
            else:
                current = -1
        else:
            current = -1
        if count > straight:
            straight = count
if straight >= 3:
    print("Small Straight: 30 points.")

        
                    
                
            
        
        
       
       
       
        
def tabl():
    if (table[0]) != 'taken':
        print('1.ones =' + str(score1))
    if (table[1]) != 'taken':
        print('2.twos =' + str(score2))
    if (table[2]) != 'taken':
        print('3.threes' + str(score3))    
    if (table[3]) != 'taken':
        print('4. Fours =' + str(score4))
    if (table[4]) != 'taken':
        print('5.Fives =' + str(score5))
    if (table[5]) != 'taken':
        print('6.Sixes' + str(score6))  
        
        
    
tabl()


#z = int(input("pick?"))
#points_table()

    



"""    
for j in range(3):
    z = 0
    dice_rolls()
    
    tabl()
    points_table()
    dice.clear()
    z = int(input("pick?"))
"""

    
    
    
    
    
    


        
    
