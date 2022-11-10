// Задача 41: Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь.
// 0, 7, 8, -2, -2 -> 2
// 1, -7, 567, 89, 223-> 3


int CountPositive(int m)
{
    if (m > 0)
    {
        Console.WriteLine($"Введите {m} чисел");

        int[] array = new int[m];
        int count = 0;

        for (int i = 0; i < m; i++)
        {
            array[i] = Convert.ToInt32(Console.ReadLine());

            if (array[i] > 0) count++;
        }

        return count;
    } else {
        throw new ArgumentException("Ожидается натуральное число");
    }

}
Console.WriteLine("Введено чисел больше 0: " + CountPositive(5));