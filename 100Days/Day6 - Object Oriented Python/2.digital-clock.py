from time import sleep

class Clock(object):

    def __init__(self, hour, minute, second):
        self._hour = hour
        self._minute = minute
        self._second = second

    def increment(self):
        self._second += 1
        if(self._second == 60):
            self._second = 0
            self._minute += 1
            if(self._minute == 60):
                self._minute = 0
                self._hour += 1
                if(self._hour == 24):
                    self._hour = 0

    # To String function
    def __str__(self):
        return '%0.2d hour %0.2d minute %0.2d second' % (self._hour, self._minute, self._second)

if __name__ == "__main__":
    clock = Clock(23,58,0)
    while(True):
        print(clock)
        sleep(1)
        clock.increment()

