Total = [j for j in range(1,31)]
Class = []
for i in range(28):
    student = int(input())
    Class.append(student)
for j in Total:
    if j not in Class:
        print(j)   