import math

class rectangle:

  def __init__(self,l,b):
    self.length=l
    self.width=b
    print('hello world')
  
  def __str__(self) -> str:
    return '{}  {}'.format(self.length,self.width)
  
  def area(self):
    return self.length*self.width
  
  def perimeter(self):
    return 2*self.length+2*self.width

  def diagonal(self):
    return math.sqrt(self.length*self.length+self.width*self.width)

  def is_square(self):
    if self.length==self.width:
      return True
    else:
      return False
    
  def resize(self,l,b):
    self.length=l
    self.width=b

  def scale(self,l,b):
    self.length=self.length*l
    self.width=self.width*b


obj = rectangle(2,3)
a=obj.area()
print(a)
