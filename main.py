import sys
from fractions import Fraction
from numpy import identity

determinant = 1
ask = ""
prin = 0
while ask != "1" and ask != "2":
    ask = input("1)system of equations\n2)Inverse Matrix\n3)Choose : ")
if ask == "1":

    n = int(input("number of equations : "))
    gauss = []
    output = []
    k = 0
    i = 0


    def printer():
        global prin
        print()
        while prin < len(output):
            for t in gauss:
                for b in t:
                    print(f"{str(Fraction(b).limit_denominator(max_denominator=10000)):6}", end=' ')
                print(f"∣   {str(Fraction(output[prin]).limit_denominator(max_denominator=10000))}")
                prin += 1
        prin = 0


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
        output.append(float(w))
        gauss.append(lines_list)
    printer()
    print("\n")
    # ready to start the calculations
    for p in range(1, n):
        for j in range(p, n):
            if gauss[i][p - 1] == 0:  # checking for Division By 0
                for d in range(i + 1, n):  # all lines
                    if gauss[d][p - 1] != 0:
                        determinant = determinant * -1
                        for m in range(n):  # swap
                            temp = gauss[i][m]
                            gauss[i][m] = gauss[d][m]
                            gauss[d][m] = temp
                        temp = output[i]
                        output[i] = output[d]
                        output[d] = temp
                        print(f"swapped between row {i + 1} and {d + 1}")
                        printer()
                        print("\n")
                        break

            if gauss[j][i] != 0:
                output[j] = output[p - 1] * (-gauss[j][i] / gauss[i][p - 1]) + output[j]
                temp = gauss[j][p - 1]
                for v in range(n):
                    gauss[j][v] = gauss[j][v] - ((temp * gauss[i][v]) / gauss[i][p - 1])
                print(
                    f"\nR{j + 1} -> R{j + 1} + ({str(Fraction(-temp / gauss[i][p - 1]).limit_denominator(max_denominator=10000))})xR{i + 1}\n")
                printer()
                print("\n")
        i += 1
    for det in range(n):
        determinant = determinant * gauss[det][det]

    for g in range(n):
        print(f"\nR{g + 1}/({str(Fraction(gauss[g][g]).limit_denominator(max_denominator=10000))})\n")
        try:
            output[g] = output[g] / gauss[g][g]
        except ZeroDivisionError:
            print("No Solutions")
            sys.exit()
        temp2 = gauss[g][g]
        for h in range(n):
            gauss[g][h] = gauss[g][h] / temp2

        printer()
        print("\n")
    print(f"determinant = {str(Fraction(determinant).limit_denominator(max_denominator=10000))}")
    j = ""
    while j.lower() != "yes" and j.lower() != "no":
        j = input("Jordan ? (Yes/No) : ")

    if j.lower() == "yes":
        for w in range(n - 1, 0, -1):
            o = 0
            for e in range(w - 1, -1, -1):
                o += 1
                print(
                    f"\nR{e + 1} -> R{e + 1} + (R{w + 1} * {str(Fraction(-gauss[e][w]).limit_denominator(max_denominator=10000))})\n")
                output[e] = output[e + o] * (-gauss[e][w]) + output[e]
                gauss[e][w] = gauss[e + o][e + o] * (-gauss[e][w]) + gauss[e][w]
                printer()
                print("\n")

else:
    n = int(input("Matrix Order: "))
    gauss = []
    output = identity(n)
    k = 0
    i = 0


    def printer():
        for i1, j1 in zip(gauss, output):
            for k1 in i1:
                print(f"{str(Fraction(k1).limit_denominator(max_denominator=10000)):6}", end=" ")
            print("∣   ", end="")
            for f in j1:
                print(f"{str(Fraction(f).limit_denominator(max_denominator=10000)):7}", end=" ")
            print()


    # making the matrix
    for lines in range(n):
        line_matrix = []
        for columns in range(n):
            line_matrix.append(int(input(f"Line {lines + 1} Column {columns + 1} : ")))
        gauss.append(line_matrix)

    printer()
    print("\n")
    for p in range(1, n):
        for j in range(p, n):
            if gauss[i][p - 1] == 0:  # checking for Division By 0
                for d in range(i + 1, n):  # all lines
                    if gauss[d][p - 1] != 0:
                        determinant = determinant * -1
                        for m in range(n):  # swap
                            temp = gauss[i][m]
                            gauss[i][m] = gauss[d][m]
                            gauss[d][m] = temp
                        temp = output[i]
                        output[i] = output[d]
                        output[d] = temp
                        print(f"swapped between row {i + 1} and {d + 1}")
                        printer()
                        print("\n")
                        break
            if gauss[j][i] != 0:
                temp = gauss[j][p - 1]
                for v in range(n):
                    output[j][v] = output[j][v] - ((temp * output[i][v]) / gauss[i][p - 1])
                    gauss[j][v] = gauss[j][v] - ((temp * gauss[i][v]) / gauss[i][p - 1])
                print(
                    f"\nR{j + 1} -> R{j + 1} + ({str(Fraction(-temp / gauss[i][p - 1]).limit_denominator(max_denominator=10000))})xR{i + 1}\n")
                printer()
                print("\n")
        i += 1
    for det in range(n):
        determinant = determinant * gauss[det][det]
    for g in range(n):
        print(f"\nR{g + 1}/({str(Fraction(gauss[g][g]).limit_denominator(max_denominator=10000))})\n")
        temp2 = gauss[g][g]
        for h in range(n):
            output[g][h] = output[g][h] / temp2
            gauss[g][h] = gauss[g][h] / temp2

        printer()
        print("\n")

    for w in range(n - 1, 0, -1):
        o = 0
        for e in range(w - 1, -1, -1):
            o += 1
            print(
                f"\nR{e + 1} -> R{e + 1} + (R{w + 1} * {str(Fraction(-gauss[e][w]).limit_denominator(max_denominator=10000))})\n")
            for r in range(n):
                output[e][r] = output[e + o][r] * (-gauss[e][w]) + output[e][r]

            gauss[e][w] = gauss[e + o][e + o] * (-gauss[e][w]) + gauss[e][w]
            printer()
            print("\n")
print(f"determinant = {str(Fraction(determinant).limit_denominator(max_denominator=10000))}")
