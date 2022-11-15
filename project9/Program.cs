// Задача 64: Задайте значение N. Напишите программу, которая выведет все 
// натуральные числа в промежутке от N до 1. Выполнить с помощью рекурсии.
// N = 5 -> "5, 4, 3, 2, 1"
// N = 8 -> "8, 7, 6, 5, 4, 3, 2, 1"

// Console.WriteLine("Введите натуральное число");
// int n = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine(PrintNumbers(n));

string PrintNumbers(int n)
{
    string result = "";
    string comma = ", ";

    if (n == 0) return result;

    if (n == 1) comma = "";

    return result = n + comma + PrintNumbers(n - 1);
}

// Задача 66: Задайте значения M и N. Напишите программу, которая 
// найдёт сумму натуральных элементов в промежутке от M до N.
// M = 1; N = 15 -> 120
// M = 4; N = 8. -> 30

// Console.WriteLine("Введите натуральное число");
// int m = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine("Введите натуральное число");
// int n = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine(NumbersSum(m, n));

int NumbersSum(int m, int n) {
    if (m < 1) m = 1;
    if (n < 1) n = 1;

    if (m == n) return m;

    int temp = 0;

    if (m > n) {
        temp = m;
        m = n;
        n = temp;
    }

    return n + NumbersSum(m, n - 1);
}

// Задача 68: Напишите программу вычисления функции Аккермана
// с помощью рекурсии. Даны два неотрицательных числа m и n.
// m = 2, n = 3 -> A(m,n) = 9
// m = 3, n = 2 -> A(m,n) = 29

// Console.WriteLine("Введите неотрицательное число");
// int m = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine("Введите неотрицательное число");
// int n = Convert.ToInt32(Console.ReadLine());
// Console.WriteLine(Akkerman(m, n));

int Akkerman(int m, int n)
{
    if (m == 0)
    {
        return n + 1;
    }
    else
    {
        if (m > 0 && n == 0)
        {
            return Akkerman(m - 1, 1);
        }
        else
        {
            return Akkerman(m - 1, Akkerman(m, n - 1));
        }
    }
}
