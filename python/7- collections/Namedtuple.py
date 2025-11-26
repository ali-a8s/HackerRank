from collections import namedtuple

size, fields = int(input()), input().split()

Student = namedtuple('Student', fields)

print(f"{sum(int(Student(*input().split()).MARKS) for _ in range(size)) / size}")