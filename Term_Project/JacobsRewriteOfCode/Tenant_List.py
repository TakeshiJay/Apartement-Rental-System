class Tenant_List:
    
    def __init__(self, __tenant_list, __rent_list):
        self.__tenant_list = __tenant_list
        self.__tenant_pos = -1
        self.__rental_list = [0] * 12
        self.__rent_list = __rent_list

    def add_nu_tenant(self, name, Apa_no):
        if Apa_no not in self.__tenant_list:
            self.__tenant_list[Apa_no] = name
            self.__rent_list.append(self.__rental_list)
        else:
            print('Apartment Taken, User Not Added')
