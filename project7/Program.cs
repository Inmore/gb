// Задача 47. Задайте двумерный массив размером m×n, заполненный случайными вещественными числами.
// m = 3, n = 4.
// 0,5 7 -2 -0,2
// 1 -3,3 8 -9,9
// 8 7,8 -7,1 9
int m = 3;
int n = 4;
 
double[,] array = GenerateArray(m, n);
// Print2DArray(array);
 
double[,] GenerateArray(int m, int n)
{
    double[,] array = new double[m, n];
    Random rnd = new Random();
 
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            array[i, j] = Math.Round(rnd.NextDouble() * 20 - 10, 1);
        }
    }
 
    return array;
}

void Print2DArray(double[,] array)
{
    
    for (int i = 0; i < m; i++)
    {
        string result = "";
        int resultLength = 7;
        for (int j = 0; j < n; j++)
        {
            result = $"{array[i, j]}";
            int k = 0;
            int resLen = result.Length;
        
            while (k < resultLength - resLen) {
                result = " " + result; 
                k++;
            }

            Console.Write(result);
        }
        Console.WriteLine("");
    }
}

// Задача 50. Напишите программу, которая на вход принимает значение элемента в двумерном 
// массиве, и возвращает позицию этого элемента или же указание, что такого элемента нет.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// 17 -> такого числа в массиве нет
 
int[,] array_50 = new int[,] {{1, 4, 7, 2}, {5, 9, 2, 3}, {8, 4, 2, 4}};
 
string InArray(int num, int[,] array) {
    string result = "такого числа в массиве нет";
 
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            if (num == array[i, j]) {
                result = $"({i},{j})";
                break;
            }
        }
    }
 
    return result;
}
// Console.WriteLine(InArray(17, array_50));

// Задача 52. Задайте двумерный массив из целых чисел. Найдите среднее арифметическое элементов 
// в каждом столбце.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// Среднее арифметическое каждого столбца: 4,6; 5,6; 3,6; 3.
// Console.WriteLine(ColumnsAverage(array_50));
string ColumnsAverage(int[,] array) {
    string result = "";
 
    for (int i = 0; i < array.GetLength(1); i++)
    {
        double sum = 0.0;
        for (int j = 0; j < array.GetLength(0); j++)
        {
            sum = sum + array[j, i];
        }
 
        double average = Math.Round(sum / array.GetLength(0), 1);
 
        result = result + $"{average}";
        if (i != array.GetLength(1) - 1) result = result + "; ";
    }
 
    return "Среднее арифметическое каждого столбца: " + result + ".";
}

// Задача HARD SORT необязательная. Считается за три обязательных
// Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. 
// Отсортировать элементы по возрастанию слева направо и сверху вниз.
// Например, задан массив:
// 1 4 7 2
// 5 9 10 3
// После сортировки
// 1 2 3 4
// 5 7 9 10

// Генерируем массив
// int[,] intArray = GenerateIntArray();
// Выводим его на экран
// Print2DIntArray(intArray);
// Выводим на экран отсортированный массив
// Console.WriteLine("Отсортированный массив");
// Print2DIntArray(SortIntArray(intArray));

int[,] SortIntArray(int[,] array) {

    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            int min = array[i, j];
            int temp;
            
            for (int p = 0; p < array.GetLength(0); p++)
            {
                for (int q = 0; q < array.GetLength(1); q++)
                {
                    if (min < array[p, q])
                    {
                        temp = array[p, q];
                        array[p, q] = min;
                        array[i, j] = temp;
                        min = temp;
                    }
                }
            }
        }
    }
    return array;
}
 
int[,] GenerateIntArray()
{
    Console.WriteLine("Введите количество строк");
    int m = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Введите количество столбцов");
    int n = Convert.ToInt32(Console.ReadLine());
    int[,] array = new int[m, n];
    Random rnd = new Random();
 
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            array[i, j] = rnd.Next(1, 11);
        }
    }
 
    return array;
}

void Print2DIntArray(int[,] array)
{
    int resultLength = 7;
    
    for (int i = 0; i < array.GetLength(0); i++)
    {
        string result = "";
        
        for (int j = 0; j < array.GetLength(1); j++)
        {
            result = $"{array[i, j]}";
            int k = 0;
            int resLen = result.Length;
        
            while (k < resultLength - resLen) {
                result = " " + result; 
                k++;
            }

            Console.Write(result);
        }
        Console.WriteLine("");
    }
}