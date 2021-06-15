import json

class login:
  def __init__(self):
    f = open('login.json',)
    self.__dic = json.load(f)
    self.flag = False
    self.__loged_user_idx = -1
  
  def nu_user(self, user, passw):
    if user not in self.__dic["Username"]:
      self.__dic["Username"].append(user)
      self.__dic["Password"].append(passw)
      self.__dic["TenantList"].append(dict())
  
  def get_dict(self):
    return(self.__dic)

  def get_indx(self):
    return(self.__loged_user_idx)

  def validate(self, user, passw):
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
  def __init__(self, __tenant_name, __apt_Num):
    self.lg = login()
    f = open(login.json,)
    self.__dic = json.load(f)
    self.__tenant_name = __tenant_name
    self.__apt_Num = __apt_Num




# lg = login()

# x = input("Username:")
# y = input("Password:")
# lg.validate(x,y)
# a = lg.get_dict()

# if lg.flag == True:
#   new_ten = input("Enter Tenant Name")
#   apt_No = input("Enter apartment no.:")
# b = lg.get_indx()
# a["TenantList"][new_ten].append(apt_No)


# if lg.flag == False:
#   nu_u = input("Do you want to enter a new user?(Y/N):")
#   if nu_u.lower() == 'y':
#     x = input("Enter a New Username:")
#     y = input("Enter a New Password:")
#     lg.nu_user(x,y)

# lg.store_to_file()

item = [{}]
x = 515
item[0].append(x)
print(x)
