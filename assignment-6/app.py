a = [1,2,3,4,5]

square = lambda x: x * x
result = list(map(square, a))
print(result)

result = list(map(lambda x : x * x, a))

print(result)