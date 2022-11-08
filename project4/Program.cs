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

// Задача 27: Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе. Через строку решать нельзя.
// 452 -> 11
// 82 -> 10
// 9012 -> 12
int FiguresSum(int a)
{

    int result = 0;

    while (a > 0)
    {
        result = result + a % 10;
        a = a / 10;
    }
    return result;
}

// Задача 29: Напишите программу, которая задаёт массив из 8 элементов с клавиатуры и выводит массив на экран.
void PrintArray()
{
    string?[] array = new string[8];
    Console.WriteLine("Введите по очереди восемь элементов для создания массива");
    for (int i = 0; i < array.Length; i++)
    {
        string? value = Console.ReadLine();
        if (!string.IsNullOrEmpty(value)) {
            array[i] = value;
        } else {
            Console.WriteLine("Вы ничего не ввели, требуется значение");
            i--;
        }
    }

    for (int i = 0; i < array.Length; i++) {
        Console.Write(array[i]);
        if (i != array.Length - 1) Console.Write(", ");
    }
    Console.WriteLine("");
}
