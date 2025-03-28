"""
oblicz tekst zapisany w ONP
jest to sposób zapisu wyrażeń arytmetycznych, w którym znak
wykonywanej operacji umieszczony jest po operandach
Przyklad:
(2+3)×5
mozna w ONP zapisac jako
2 3 + 5 × = 25
"""

input1 = "2 3 + 5 *"  # 25
input2 = "3 4 + 5 2 - * 8 4 / 6 1 + * + 9 -"  # 26
stack = []

input2 = input2.replace(" ", "")
for elem in input2:
    if "0" <= elem <= '9':
        stack.append(int(elem))
    else:
        a = stack.pop()
        b = stack.pop()
        match elem:
            case "+":
                stack.append(a + b)
                continue
            case '-':
                stack.append(b - a)
                continue
            case '*':
                stack.append(a * b)
                continue
            case '/':
                stack.append(b / a)
                continue
    # print(stack)
print(stack)
# solution = ?