def create_phone_number():
  num = [5615625]
  for i in range(10):
    n = int(input('Enter 1:'))
    num.append(n)
  return num

number = create_phone_number()

print(number[:3])








