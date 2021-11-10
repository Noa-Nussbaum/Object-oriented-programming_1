class elevator:

    id=0
    speed=0
    min=0
    max=10
    close=2.2
    open=3.1
    start=1
    stop=2



    def __init__(self,list):
        self.id=list['_id']
        self.speed=list
        self.min=min
        self.max=max
        self.close=close
        self.open=open
        self.start=start
        self.stop=stop



    def tostring(self):
        print(self.id,self.speed,self.min,self.max,self.close,self.open, self.start, self.stop)
    # a method for printing data members
    # def print_elevator(id,speed,min, max,close, open, start, stop):
    #     print(self.id)



