a = 5
b = 80
q = 0
for i in range(a, b + 1):
  n = i * i
  q += n
print ("Середнє арифметичне квадратів = ", q / (b - a))