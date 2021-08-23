import random 

print("Давайте узнаем что случилось с вашим персонажем")

X = 0 # X это показатель обозначающийся отрицательное значение броска
Y = 0 # Y это показатель обозначающийся положительное значение броска
Z = 0 # Z это флаг прекращения while 
Ti = int(input("что вы хотите узнать,\n 0 для броска \n 1 для судьбы или \n 2 для настраимового броска: "))
I = 0 # I это какой гранник бы выббираите 
D = 0 # D это число броска кубика

KGran = [4,6,8,10,12]

if Ti == 1 :
    while Z != 1 :
        d20 = random.randint(1,20)
        print(d20)
        input("press enter")

        if d20 == 1:
            X = X + 2;
        elif 1 < d20 < 11:
            X = X + 1;

        if X >= 3: 
            print("ваш персонаж погиб")
            Z = Z + 1

        if d20 == 20:
            Y = Y + 2;
        elif 20 > d20 > 10:
            Y = Y + 1;

        if Y >= 3:
            print("С вами всё хорошо")
            Z = Z + 1

elif Ti == 2 :  
    while Z != 1:
        I = int(input("Какой гранник вы выбирите? \n '4' - 1 \n '6' - 2 \n '8' - 3 \n '10' - 4 \n '12' - 5 : "))
        I = I - 1
        V = int(input("Сколько бросков сделать?: "))
        if -1 < I < 5:
            for i in range(V):
                D = random.randint(1, KGran[I])
                print(D)
        else :
            print("!!!вы ввели не верное число!!!")
        input("enter: ")
        Z = Z + 1

else :
    while Z != 1:
        input("нажмите enter для броска:")
        d20 = random.randint(1,20)
        print(d20)

        if d20 == 1: 
            print("критическая неудача")
            Z = Z + 1
        elif d20 == 20: 
            print("критическая удача")
            Z = Z + 1
        else :
            Z = Z + 1

T = input()