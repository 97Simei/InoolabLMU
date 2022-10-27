def value_check(value):
  if value < 0:
    raise Exception("Sorry, no numbers below zero")
def my_kaya_equation(pop,gdp,enInt,carbInt):
  """
  Input Example for my_kaya_equation
  • pop (mio): 82.4
  • gdp (in $1000/person): 44
  • enInt (in GJ/$1000GDP): 5
  • carbInt (in tonnes CO2/GJ): 0.05
  """
  """check if the value is smaller than zero"""
  value_check(pop)
  value_check(gdp)
  value_check(enInt)
  value_check(carbInt)
  co2 = pop * gdp * enInt * carbInt
  return co2


