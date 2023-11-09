#Тема 1: Возможности Python. Типы и операции. Условные конструкции.
#Задания по лекции
# График
x=int(input("Введите значение x: "))
y=int(input("Введите значение y: "))

if (x>0) and (y>0):
    print ("I четверть")
elif (x<0) and (y>0):
    print ("II четверть")
elif (x<0) and (y<0):
    print ("III четверть")
elif (x>0) and (y<0):
    print("IV четверть")
else:
    print ("Оси")
