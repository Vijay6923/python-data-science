class Planet:
    count=0
    def revolutions(self):
        self.count=self.count+1
        print(self.count)

x=Planet()
print(x.count)
x.revolutions()
x.revolutions()
x.revolutions()
Planet.revolutions(x)