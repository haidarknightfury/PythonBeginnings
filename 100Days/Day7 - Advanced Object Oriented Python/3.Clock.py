from time import time, localtime, sleep


class Clock(object):

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    # Class method - return an instance of the class
    # cls is the constructor method
    @classmethod
    def now(cls):
        currenttime = localtime(time())
        return cls(currenttime.tm_hour, currenttime.tm_min, currenttime.tm_sec)

    def run(self):
        self ._second += 1
        if self ._second == 60:
            self ._second = 0
            self ._minute += 1
            if self ._minute == 60:
                self ._minute = 0
                self ._hour += 1
                if self ._hour == 24:
                    self ._hour = 0
    
    def __str__(self):
        return ' %02d : %02d : %02d ' % \
               (self ._hour, self ._minute, self ._second)


def main():
    clock = Clock.now()
    while(True):
        sleep(1)
        clock.run()
        print(clock)

if __name__ == '__main__':
    main()
