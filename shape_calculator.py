class Rectangle: 
  def __init__(self, width, height):
    self.width=width
    self.height=height
    
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
  def get_picture(self):
    if(self.width>50 or self.height>50):
      return "Too big for picture."
    else:
      toprint=""
      for i in range(self.height):
        printRow=""
        for j in range(self.width):
          printRow+="*"      
        toprint+=printRow + "\n"  
      return toprint
    
  def set_width(self, width):
    self.width=width
  def set_height(self, height):
    self.height=height
  def get_area(self):
    self.area =self.width * self.height
    return self.area
  def get_perimeter(self):
    self.p = 2*(self.width + self.height)
    return  self.p
  def get_diagonal(self):
    diagonal = (self.width**2 + self.height**2)**0.5
    print (diagonal)
    return diagonal
  def get_amount_inside(self, shape):
    print(self.height, shape.height)
    height_coef = self.height / shape.height
    width_coef = self.width / shape.width
    return int(height_coef * width_coef)
    
class Square(Rectangle):
  def __init__(self, side):
    self.width=side
    self.height=side
  def __str__(self):
    return f"Square(side={self.width})"
  def set_side(self, side):
    self.width=side
    self.height=side