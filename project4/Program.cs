// Задача 25: Напишите цикл, который принимает на вход два числа (A и B) и возводит число A в натуральную степень B.
// 3, 5 -> 243 (3⁵)
// 2, 4 -> 16
int ToExtent(int a, int b)
{
    if (b > 0)
    {
        int result = 1;

        for (int i = 0; i < b; i++)
        {
            result = result * a;
        }

        return result;
    }
    else
    {
        throw new ArgumentException("В качестве второго аргумента ожидается натуральное число");
    }
}
