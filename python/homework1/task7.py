# 2.Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
def test_expression():
    for x in range(2):
        for y in range(2):
            for z in range(2):
                left = not (x and y and z)
                right = not x or not y or not z
                print(left == right)


test_expression()