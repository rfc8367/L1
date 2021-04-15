#Количество введённых чисел (завершающий 0 не считается)

def num_count():
  
    init_num = int(input("Введите число: "))
    
    count = 0

    while init_num != 0:
      
        count += 1
        init_num = int(input())
        
    print('Количество: ', count )

num_count()



#Сумма

def count_sum():
  
    init_num = int(input("Введите число: "))
    
    sum_num = 0

    while init_num != 0:
      
        sum_num += init_num
        init_num = int(input())
        
    print(sum_num)

count_sum()



#Произведение

def multiplication():
  
    init_num = int(input("Введите число: "))
    
    mul_num = 0

    while init_num != 0:
      
        mul_num *= init_num
        init_num = int(input())
        
    print(mul_num)

multiplication()




#Среднее арифметическое (не считая завершающего числа 0)

def average():
  
    init_num = int(input("Введите число: "))
    
    sum_num = 0
    count = 0
    avg = 0

    while init_num != 0:
      
        sum_num += init_num
        
        init_num = int(input())
        count += 1

    avg = (sum_num / count)
    print(avg)

average()



#Определить значение и порядковый номер наибольшего элемента последовательности. Если наибольших элементов несколько, выведите порядковый номер первого из них.

def maximum():

   init_num = int(input("Введите число: "))
    
    first_max = 0
    ordinal = 0

    while init_num != 0:
      if init_num > first_max:
          
            first_max = init_num
            
        init_num = int(input())
        ordinal += 1
        
    print(ordinal)

maximum()



#Определить количество чётных и не чётных элементов в последовательности

def even_odd():
  
   init_num = int(input("Введите число: "))

    even_count = 0
    odd_count = 0

    while init_num != 0:
        if init_num % 2 == 0:
          
            even_count += 1

        else:
          
            odd_count += 1
        init_num = init_num // 10
    print("Even: %d, Odd: %d" % (even_count, odd_count))

even_odd()



#Определить значение второго по величине элемента в этой последовательности

def second_maximum():
  
    init_num = int(input("Введите число: "))
    
    first_max = 0
    second_max = 0

    while init_num != 0:
        if init_num > first_max:
          
            second_max = first_max
            first_max = init_num 
            
        elif init_num > second_max:
          
            second_max = init_num
        init_num = int(input())

    print(second_max)

second_maximum()



#Определите, сколько элементов этой последовательности равны ее наибольшему элементу

def max_element():
    init_num = int(input("Введите число: "))

    first_max = 0
    element_count = 1

    while init_num != 0:
        if init_num > first_max:

            first_max = init_num
            element_count = 1

        elif init_num == first_max:

            element_count += 1
        init_num = int(input())

    print(element_count)

max_element()
