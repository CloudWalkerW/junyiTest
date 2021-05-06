def nonfactors_calculate(n):
	count = 0
	for i in range(1 , n + 1):
		if i % 15 == 0:
			count += 1
		elif i % 3 != 0 and i % 5 != 0:
			count += 1
	return count

n = int(input("請輸入數字："))

print(nonfactors_calculate(n))