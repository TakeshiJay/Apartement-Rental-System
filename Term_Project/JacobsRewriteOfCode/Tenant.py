from TIS import TIS

class Tenant:
    def __init__(self):
        tis = TIS.user_inp()
        self.__Apt_No, self.__Name = tis.get_input()   
    
    def get_Apt(self):
        return self.__Apt_No
    
    def get_Tenant(self):
        return self.__Name