result_1 = 'результат операции: 42'
index = result_1.index(':')
number = int(result_1[index + 1:].strip())
print (number + 10)

result_2 = 'результат операции: 514'
index = result_2.index(':')
number = int(result_2[index + 1:].strip())
print (number + 10)

result_3 = 'результат работы программы: 9'
index = result_3.index(':')
number = int(result_3[index + 1:].strip())
print (number + 10)
