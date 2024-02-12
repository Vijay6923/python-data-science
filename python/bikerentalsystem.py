class bikeshop:
    def __init__(self,stock):
        self.stock=stock
        def displaybike(self):
            print("total bikes",self.stock)
        def rentforbikes(self,q):
            if q<=0:
                print("enter the positive value or greater the 0")
            elif q>self.stock:
                print("enter the value less than stock")
            else:
                self.stock=self.stock-q
                print("total price",q*100)
                print("total bikes",self.stock)
        while True:
            obj=bikeshop(100)
            uc=int(input())('''
            1 Display Stock
            2 Rent a Bike 
            3 Exit ''')
                
            if uc==1:
                obj.displaybike()
            elif uc==2:
                n=int(input("enter the quantity: "))
                obj.rentforbike(n)
            else:
                break
