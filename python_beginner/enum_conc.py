#enums are readable names that are bounds
#to constant value
#we use enum to create contant value in python
#then nobody can reassign the value
from enum import Enum
class State(Enum):
    ACTIVE=1
    INACTIVE=0

print(State.ACTIVE.value)
print(State(1))
print(State['ACTIVE'].value)