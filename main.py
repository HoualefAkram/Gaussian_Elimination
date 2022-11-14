n = int(input("number of equations : "))
gauss = []
output = []
k = 0
i = 0


def bad_row(row):
    try:
        if gauss[row][0] == 0:
            return True
        return False
    except:
        return False


def printer():
    for lists, values in zip(gauss, output):
        lists = list(map(lambda x: round(x, 3), lists))
        print(lists, round(values, 3))


# making the matrix
for lines in range(n):
    lines_list = []
    equations = input(f"Equation {lines + 1} = ")
    for columns in range(n):
        if columns == 0:
            v = equations[0: equations.index("x")]
        else:
            v = equations[
                equations.index("xyzabcdefghijklmnopqrstuvw"[columns - 1]) + 1: equations.index(
                    "xyzabcdefghijklmnopqrstuvw"[columns])]

        lines_list.append(int(v))
    w = equations[equations.index("=") + 1::]
    output.append(int(w))
    gauss.append(lines_list)
printer()
print("\n")
# finding a row without 0s
while bad_row(k):
    k += 1
# change line 1 with line k
if k != 0 and k != n:
    for m in range(n):
        temp = gauss[0][m]
        gauss[0][m] = gauss[k][m]
        gauss[k][m] = temp
        temp = output[0]
        output[0] = output[k]
        output[k] = temp
    print(f"swapped between row 1 and {k + 1}")
    printer()
    print("\n")
# ready to start the calculations
for p in range(1, n):
    for j in range(p, n):
        if gauss[j][i] != 0:
            output[j] = output[p - 1] * (-gauss[j][i] / gauss[i][p - 1]) + output[j]
            temp = gauss[j][p - 1]
            for v in range(n):
                gauss[j][v] = gauss[j][v] - ((temp * gauss[i][v]) / gauss[i][p - 1])
            print(f"\nR{j + 1} -> R{j + 1} + ({round(-temp / gauss[i][p - 1], 3)})xR{i + 1}\n")
            printer()
            print("\n")
    i += 1

for g in range(n):
    print(f"\nR{g + 1}/{round(gauss[g][g], 3)}\n")
    output[g] = output[g] / gauss[g][g]
    temp2 = gauss[g][g]
    for h in range(n):
        gauss[g][h] = gauss[g][h] / temp2

    printer()
    print("\n")
j = ""
while j.lower() != "yes" and j.lower() != "no":
    j = input("Jordan ? (Yes/No) : ")

if j.lower() == "yes":
    for w in range(n - 1, 0, -1):
        o = 0
        for e in range(w - 1, -1, -1):
            o += 1
            print(f"\nR{e + 1} -> R{e + 1} + (R{w + 1} * {round(-gauss[e][w], 3)})\n")
            output[e] = output[e + o] * (-gauss[e][w]) + output[e]
            gauss[e][w] = gauss[e + o][e + o] * (-gauss[e][w]) + gauss[e][w]
            printer()
            print("\n")
