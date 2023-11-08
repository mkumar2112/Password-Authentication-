import random

class Password_Generator:
    code = "abcdefghijklmnopqrstuvwxyz@#$%&*_ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    password = ""
    t=0
    def __new__(cls,lenght):
        p = 5
        while len(cls.password)!=lenght:
            if lenght%(cls.t+1)==0:
                p= random.randint(0,26)
            elif lenght%(cls.t+1)==1:
                p= random.randint(26,33)
            elif lenght%(cls.t+1)==2:
                p= random.randint(33,59)
            elif lenght%(cls.t)==3:
                p= random.randint(59,69)
            else:
                p= random.randint(0,69)

            cls.password = cls.password[:cls.t]+cls.code[p]+cls.password[cls.t+1:]
            cls.t = cls.t +1
        return  cls.password
            

# pa = Password_Generator()
# Password = pa.Password_Generator(6)
# print(Password)










