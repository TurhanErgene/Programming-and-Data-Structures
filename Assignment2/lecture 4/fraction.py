class Fraction:
  def __init__(self, numerator: int, denominator: int):
    self.numerator = numerator
    self.denominator = denominator
    self._simplify()


    if denominator == 0:
      raise ValueError("Cannot create a fraction with a zero numerator or denominator")
    

    if denominator < 0:
      numerator = -numerator
      denominator = -denominator
  
  def _simplify(self):
    common_divisor = gcd(self.numerator, self.denominator)
    self.numerator = self.numerator // common_divisor
    self.denominator = self.denominator // common_divisor

  def __add__(self, other):
    numerator = self.numerator * other.denominator + other.numerator * self.denominator
    denominator = self.denominator * other.denominator
    return Fraction(numerator, denominator)

  def __sub__(self, other):
    numerator = self.numerator * other.denominator - other.numerator * self.denominator
    denominator = self.denominator * other.denominator
    return Fraction(numerator, denominator)

  def __mul__(self, other):
    numerator = self.numerator * other.numerator
    denominator = self.denominator * other.denominator
    return Fraction(numerator, denominator)

  def __truediv__(self, other):
      if other.numerator == 0:
          raise ZeroDivisionError("Cannot divide by a fraction with numerator 0.")

      numerator = self.numerator * other.denominator
      denominator = self.denominator * other.numerator
      return Fraction(numerator, denominator)


  def __str__(self):
    return f"{self.numerator}/{self.denominator}"


    
def gcd(a, b):
  if(b == 0):
    return abs(a)
  else:
    return gcd(b, a % b)
  
  


f1 = Fraction(15, 45)
f2 = Fraction(5, 50)


print(f"f1: {f1}")
print(f"f2: {f2}")
print("\nCalculations:")
print(f"f1 + f2 = {f1 + f2}")
print(f"f1 - f2 = {f1 - f2}")
print(f"f1 * f2 = {f1 * f2}")
print(f"f1 / f2 = {f1 / f2}")








