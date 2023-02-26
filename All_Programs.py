import random


class All_prog():


    def Harmonic_num(self):
        H_range = int(input("Enter the range : "))
        H_number = 0
        for i in range (1,H_range+1):
            if H_range == 0:
                print("Enter the valid number")
            else:
                H_number += 1 / i
        print("the Nth Harmonic number is",H_number) 


  
    def Flip_The_Coin(self):
        number_flip=int(input("Enter the number of flips: "))
        head=0
        tail=0
        for i in range(number_flip):
            face=random.randint(0,1)
            if face == 0:
                # print("head")
                head = head+1
            else:
                # print("tail")
                tail = tail+1

        # print("count of haed is: ",head)  
        # print("count of tail is :",tail)      
            
        Head_percentage=(head*100)/number_flip
        Tail_percentage=100-Head_percentage      

        print("percetage of Head: ",Head_percentage,"\n","percentage of tail: ",Tail_percentage )


    def Leap_Year_prog(self):
        year=int(input("inter the Year : "))
        if (year % 4 ==0) and (year % 100 != 0):
            print("it's a leap Year")
        else:
            print("it's not a leap year")

    def Power_of_Two(self):
        power_of_2=int(input("Enter the number: "))

        if (0 <= power_of_2 < 31):
            for i in range(power_of_2):
                print(i," ",pow(2,i))
        else:
            print("Enter the valid number")        


    def Replace_the_name(self):
        name=input("Enter the Username : ")

        print("Hello "+name+" ,How are you?")        
        
    
        








     