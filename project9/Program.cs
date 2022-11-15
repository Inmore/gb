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
