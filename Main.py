from  All_Programs import All_prog

if __name__ == "__main__":

        # Harmonic = All_prog()  
        # Harmonic.Harmonic_num()

        # Flip_coin = All_prog()
        # Flip_coin.Flip_The_Coin()

        # Leap_Year = All_prog()
        # Leap_Year.Leap_Year_prog()

        # power_of_2 = All_prog()
        # power_of_2.Power_of_Two()

        # replace = All_prog()
        # replace.Replace_the_name()


    obj = All_prog()

    while True:

        print("\n Enter Your Option\n\n1 : Program For The Harmonic Number\n2 : Program For The Flip The Coin\n3 : Program For the Leap Year\n4 : Program For Power Of TWo\n5 : Program For the Replacing The name\n")

        select_option = int(input())
        if select_option == 1:
            obj.Harmonic_num()

        elif select_option == 2:
            obj.Flip_The_Coin()  

        elif select_option == 3:
            obj.Leap_Year_prog()

        elif select_option == 4:
            obj.Power_of_Two()    

        elif select_option == 5:
            obj.Replace_the_name()

        else:
            print("Enter The Valid Number")






