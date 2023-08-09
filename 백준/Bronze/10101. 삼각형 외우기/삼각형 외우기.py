tri_degree = []
for _ in range(3):
  degree = int(input())
  tri_degree.append(degree)
if sum(tri_degree) != 180:
  print('Error')
elif len(set(tri_degree)) == 1:
  print('Equilateral')
elif len(set(tri_degree)) == 2:
  print('Isosceles')
elif len(set(tri_degree)) == 3:
  print('Scalene')