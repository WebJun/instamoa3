from Model import Model
from dotmap import DotMap  # pip install dotmap

model = Model()
a = model.getUsers('ec959aee7a844f17b479fd92ed49ea6d')
print(a)

user = DotMap()
user.pks = '1'
model.saveUser(user)
