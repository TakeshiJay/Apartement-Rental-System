class User:
    def __init__(self, un, passw):
        self.__un = un
        self.__passw = passw
    
    def get_user(self):
        return(self.__un, self.__passw)
    
    @classmethod
    def user_new(cls):
        return(cls(
            input('Enter a New Username:'),
            input('Enter a Password:'))
        )
    
    @classmethod
    def user_wb(cls):
        return(cls(
            input('Enter a Valid Username:'),
            input('Enter a Password:'))
        )