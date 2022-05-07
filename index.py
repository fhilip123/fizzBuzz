ninput = int(input('n = '))
def fizz_buzz(n):
    answer = []
    x = ''
    for i in range(1, n+1):
        answer.append(i)
    for i in answer:
        if i%3 == 0 and i%5 != 0:
            x = 'Fizz'
        elif i%3 != 0 and i%5 == 0:
            x = 'Buzz'
        elif i%3 == 0 and i%5 == 0:
            x = 'FizzBuzz'
        else:
            x = i
        if x != '':
            answer[i-1] = x
    for i in answer:
        if str(type(i)) != "<class 'str'>":
            answer[i-1] = str(i)
    return answer

print(fizz_buzz(ninput))