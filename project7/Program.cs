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