import json

class UI: #user interface
  def __init__(self):
    f = open('login.json',)
    self.__dic = json.load(f)
    self.flag = False
    self.__expenses_List = self.__dic["Expenses"]
    self.__loged_user_idx = -1
    self.__tenants_list = self.__dic["TenantList"][self.__loged_user_idx]
    self.__rent_records = self.__dic["RentRecord"][self.__loged_user_idx]
    self.__tenant_input = TIS()
  
  def nu_user(self, user, passw):
    if user not in self.__dic["Username"]:
      self.__dic["Username"].append(user)
      self.__dic["Password"].append(passw)
      self.__dic["TenantList"].append(dict())
      self.__dic["RentRecord"].append([0]*12)
      self.__dic["Expenses"].append(dict())
    if user in self.__dic["Username"]:
      print("Invalid: Username taken")
  
  def get_dict(self):
    return(self.__dic)

  def get_indx(self):
    return(self.__loged_user_idx)

  def validate_user(self, user, passw):
    if user not in self.__dic["Username"]:
      print("Invalid Username")
      return 0 
    for i in self.__dic["Username"]:
      if i == user:
        idx = self.__dic["Username"].index(i)
    for j in self.__dic["Password"]:
      if self.__dic["Password"].index(j) == idx:
        if j == passw:
          self.flag = True
          self.__loged_user_idx = idx
          print("Password successful")
          return 0 
        else:
          print("Invalid Password")
          return 0
  
  def store_to_file(self):
    js = json.dumps(self.__dic)
    f = open("login.json","w")
    f.write(js)
    f.close()

class TIS: #Tenant input screen
  def __init__(self, __tenant_list):
    self.__Name = None 
    self.__ApaNo = None
    self.__tenant_list = __tenant_list

  def get_Tenant(self):
    return(self.__tenant_name, self.__apt_Num)

  @classmethod
  def user_inp(cls):
    return cls(
      input("Tenant Name:"),
      input("Tenant Apartment_No: ")
    )
class Tenant:
  def __init__(self, __Apt_No, __Name):
    self.__Apt_No = __Apt_No
    self.__Name = __Name
  
  def get_Apt(self):
    return(self.__Apt_No)
  
  def get_Tenant(self):
    return(self.__Name)
  
class Tenant_List:
  def __init__(self, __tenant_list):
    self.__tenant_list = __tenant_list
    self.__tenant_pos = -1
  
  def add_nu_tenant(self, name, Apa_no):
    if name not in self.__tenant_list:
      self.__tenant_list[name] = Apa_no

  def count_tenants(self):
    return(len(self.__tenant_list))

