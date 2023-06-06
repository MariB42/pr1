def gauss_method(c, A, B):
#Прямой ход.
#Выбор максимальных элементов строки по модулю для сортировки по ним.
    for i in range(c):
        max_el = abs(A[i][i])
        max_row = i
        for k in range(i + 1, c):
            if abs(A[k][i]) > max_el:
                max_el = abs(A[k][i])
                max_row = k
#Сортировка строк.
        A[i], A[max_row] = A[max_row], A[i]
        B[i], B[max_row] = B[max_row], B[i]
#Приведение к ступенчатой или треугольной форме.
        for k in range(i + 1, c):
            f = -A[k][i] / A[i][i]
            for j in range(i, c):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += f * A[i][j]
            B[k] += f * B[i]
#Округление слишком маленьких елементов системы для корректной работы.
#(только в случае если елемент меньше чем 10^(-10))
    for i in range(c):
        for j in range(c):
            if abs(A[i][j])<10**(-10):
                A[i][j]=0
        if abs(B[i])<10**(-10):
                B[i]=0
#Проверка системы на несовместность.   
    prov=0
    for i in range(c):
        for j in range(c):
            prov+=abs(A[i][j])
        if prov==0 and B[i]!=0:
            print("Решений нет.")
            prov=-1
            break
        prov=0
#Обратный ход.
    if prov!=-1:
        x = [0 for _ in range(c)]
        for i in range(c - 1, -1, -1):
            if (B[i]!=0 or A[i][i]!=0) and (B[i]!=0 and A[i][i]!=0):
                x[i] = B[i] / A[i][i]
                for k in range(i - 1, -1, -1):
                    B[k] -= A[k][i] * x[i]
        return x

print("Введите размер матрицы:")
a, b = map(int,input().split( ))
print("Введите матрицу построчно посимвольно:")
#Введение матрицы с дополнительным построением до квадратной матрицы.
c=max(a,b)
A = []
for i in range(c):
    row = []
    if i<a:
        for j in range(c):
            if j<b:
                e = float(input())
            else: e = 0
            row.append(e)
    else:
        for j in range(c):
            e = 0
            row.append(e)
    A.append(row)
print("Введите неизвестные величины посимвольно")
#Введение неизвестных величин с доп. постр. в соответствии с квадратной матрицей.
B = []
for i in range(c):
    if i<a:
        e = float(input())
    else: e = 0
    B.append(e)
print("СЛАУ:",A,B)
#Вызов функции выполняющей метод Гаусса.
result = gauss_method(c, A, B)
#Вывод результата решения с учётом вводимого размера системы.
if result!=None:
    print("Решение:")
    for i in range(a):
        print("x", i+1, " = ", "%.5f" % result[i])
