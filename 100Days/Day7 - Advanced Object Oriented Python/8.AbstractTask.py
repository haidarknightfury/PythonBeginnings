from abc import  ABC, abstractmethod


class Task(ABC):

    def execute(self):
        self.getReady()
        self.getUp()
        self.go()
    
    @abstractmethod
    def getReady(self):
        pass
    
    @abstractmethod
    def getUp(self):
        pass
    
    @abstractmethod
    def go(self):
        pass

class RunTask(Task):

    def getReady(self):
        print('Getting ready')
    
    def getUp(self):
        print('Getting up')
    
    def go(self):
        print('GO')

if __name__ == "__main__":
    runtask = RunTask()
    runtask.execute()

