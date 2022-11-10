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
// Console.WriteLine("Введено чисел больше 0: " + CountPositive(5));

// Задача 43: Напишите программу, которая найдёт точку пересечения двух прямых, заданных уравнениями 
// y = k1 * x + b1, y = k2 * x + b2; значения b1, k1, b2 и k2 задаются пользователем.
// b1 = 2, k1 = 5, b2 = 4, k2 = 9 -> (-0,5; -0,5)

// CrossPoint();

void CrossPoint()
{
    double crossPoint_x = 0.0;
    double crossPoint_y = 0.0;

    int[] line_1 = new int[2];
    Console.WriteLine("Введите по очереди b1 и k1 для первой линии");
    for (int i = 0; i < line_1.Length; i++)
    {
        line_1[i] = Convert.ToInt32(Console.ReadLine());
    }
    int[] line_2 = new int[2];
    Console.WriteLine("Введите по очереди b2 и k2 для второй линии");
    for (int i = 0; i < line_2.Length; i++)
    {
        line_2[i] = Convert.ToInt32(Console.ReadLine());
    }

    crossPoint_x = (double)(line_2[0] - line_1[0]) / (line_1[1] - line_2[1]);
    crossPoint_y = line_1[1] * crossPoint_x + line_1[0];

    Console.WriteLine($"({crossPoint_x}; {crossPoint_y})");
}