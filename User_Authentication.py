'''## Description
About       :-'These the Password Authentication Program where a user comes and autherized the              appplication after the verification of there identity.'
Features    :-'Features are following...
                1. You cannot access the application without proper verication.
                2. If you have no user Id than you will create for you.
                3. When creating password for a new user there are two option 
                    a. Computer Generated Password
                    b. Manually Typed Password
                4.'
Usage       :-'For Creating a user access application after verification '
Contact     :-'
                Created By  :- Monu Kumar
                Email Id    :- monukumar20238@gmail.com
                '
    '''


import getpass
import Random_Password_Genertor as Pg

class PasswordAutentication:
    
    database={'user':'password',
                  'ok':'6789'}
        
    def __init__(self) :
        # print(self.database.keys())
        userName= input("Enter Your username :")
        if userName in self.database:
            password = getpass.getpass("enter Your Password :")
            while password != self.database.get(userName):
                password = getpass.getpass('Enter Your Password Again :')
                print(self.database.get(userName))
            print('Verified')
        else :
            self.Create_user()

    def Create_user(self):
            flag = int(input('User is Not found in Data\nWant to make it. Press 1 for Yes 0 For No.'))
            user_flag = False
            if flag == True:
                while user_flag == False:
                    userName = input("Enter Your username :")

                    if userName not in self.database:
                        pass_Flag_val = int(input("Want to Random Generated Password...\n Press 1 for Yes, 0 For No!"))
                        if pass_Flag_val == 1:
                            password = Pg.Password_Generator(25)
                            C_password=password
                            print("Your password is ", C_password)

                        else:
                            password = getpass.getpass("Enter Your Password :")
                            C_password = getpass.getpass("enter Your Password :")
                            while password != C_password:
                                password = getpass.getpass("Cannot Create User. Your Password is wrong...       \nEnter    Your   Password :")
                                C_password = getpass.getpass("enter Your Password :")
                        updated_Data = {
                                userName : password
                        }
                        self.database.update(updated_Data)
                        user_flag = True
                        print('user Created !!!!!')
                    else :
                        print('Username already created Try with different username...')


         
