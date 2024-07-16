# ABSTRACTION : hiding the details and showing what is required.
# ABSTRACTION can be achieved by importing ABC and abstractmethod

from abc import ABC, abstractmethod
class pyATB(ABC):

    @abstractmethod
    def payFEE(self):
        pass

    def enrolled(self):
        print("enrolled")


class himanth(pyATB):
    def payFEE(self):
        print("paid")



H = himanth()
print(H.enrolled())

