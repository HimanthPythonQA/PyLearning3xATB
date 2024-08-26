from abc import ABC, abstractmethod
class ATB(ABC):

     @abstractmethod
     def perform_task1(self):
         pass

     @abstractmethod
     def perform_task2(self):
         pass


class hemanth(ATB):

    def perform_task1(self):
        return "done1"
    def perform_task2(self):
        return "done2"

G = hemanth()
print(G.perform_task1())
print(G.perform_task2())

