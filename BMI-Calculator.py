#BMI Calculator
def calc_bmi(w,h):
  bmi = w/(h**2)
  if bmi<18.5:
    return f"Underweight"
  elif 18.5 <= bmi < 24.9:
    return f"Normal Weight"
  elif 25 <= bmi < 29.9:
    return f"Overweight"
  else:
    return f"Obesity"
w = float(input('Enter your weight in KG: '))
h = float(input('Enter your height in meter: '))
print(calc_bmi(w,h))