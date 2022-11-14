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

// Задача 54: Задайте двумерный массив. Напишите программу, которая упорядочит по убыванию элементы каждой строки двумерного массива.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// В итоге получается вот такой массив:
// 7 4 2 1
// 9 5 3 2
// 8 4 4 2
 
// Задаем массив
int[,] array_54 = new int[,] {{1, 4, 7, 2}, {5, 9, 2, 3}, {8, 4, 2, 4}};
// Выводим его на экран
// Print2DIntArray(array_54);
// Выводим на экран отсортированный массив
// Console.WriteLine("Отсортированный массив");
// Print2DIntArray(SortLineInt2DArray(array_54));
 
int[,] SortLineInt2DArray(int[,] array) {
 
    for (int i = 0; i < array.GetLength(0); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            int min = array[i, j];
            int temp;
 
            for (int q = 0; q < array.GetLength(1); q++)
            {
                if (min > array[i, q])
                {
                    temp = array[i, q];
                    array[i, q] = min;
                    array[i, j] = temp;
                    min = temp;
                }
            }
        }
    }
    return array;
}

// Задача 56: Задайте прямоугольный двумерный массив. Напишите программу, которая будет 
// находить строку с наименьшей суммой элементов.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// 5 2 6 7
// Программа считает сумму элементов в каждой строке и выдаёт номер строки с наименьшей 
// суммой элементов: 1 строка
 
// Задаем массив
int[,] array_56 = new int[,] {{1, 4, 7, 2}, {5, 9, 2, 3}, {8, 4, 2, 4}, {5, 2, 6, 7}};
// Console.WriteLine(MinSumLine(array_56));
string MinSumLine(int[,] array) {
    int temp = 0;
    int line_number = 1;
 
    for (int i = 0; i < array.GetLength(0); i++)
    {
        int sum = 0;
 
        for (int j = 0; j < array.GetLength(1); j++)
        {
            sum = sum + array[i, j];
        }
 
        if (i == 0) {
            temp = sum;
        }
 
        if (sum < temp) {
            temp = sum;
            line_number = i + 1;
        }
    }
    return line_number + " строка";
}

// Задача 58: Задайте две матрицы. Напишите программу, которая будет находить произведение двух матриц.
// Например, даны 2 матрицы:
// 2 4 | 3 4
// 3 2 | 3 3
// Результирующая матрица будет:
// 18 20
// 15 18

int[,] matrix_1 = new int[,] {{2, 4}, {3, 2}};
int[,] matrix_2 = new int[,] {{3, 4}, {3, 3}};
// Console.WriteLine("Матрица 1");
// Print2DIntArray(matrix_1);
// Console.WriteLine("Матрица 2");
// Print2DIntArray(matrix_2);
// Console.WriteLine("Результирующая матрица");
// Print2DIntArray(MultiplyMatrix(matrix_1, matrix_2));

int[,] MultiplyMatrix(int[,] mA, int[,] mB) {

    int[,] matrix = new int[mA.GetLength(1), mB.GetLength(0)];

    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            for (int k = 0; k < matrix_1.GetLength(1); k++) {
                matrix[i, j] = matrix[i, j] + matrix_1[i, k] * matrix_2[k, j];
            }
        }
    }

    return matrix;
}

// Задача 60. ...Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. Напишите программу, которая будет построчно выводить массив, добавляя индексы каждого элемента.
// Массив размером 2 x 2 x 2
// 66(0,0,0) 25(0,1,0)
// 34(1,0,0) 41(1,1,0)
// 27(0,0,1) 90(0,1,1)
// 26(1,0,1) 55(1,1,1)

// Формируем массив
int[,,] array_60 = GenerateArray(2, 2, 2);
// Выводим массив построчно
// Print3DArray(array_60);

int[,,] GenerateArray(int a, int b, int c)
{
    int[,,] array = new int[a, b, c];
    int value = 0;
    Random rnd = new Random();

    for (int i = 0; i < a; i++)
    {
        for (int j = 0; j < b; j++)
        {
            for (int k = 0; k < c; k++)
            {
                do {
                    value = rnd.Next(10, 100);
                } while (FindEqual(array, value));

                array[i, j, k] = value;
            }
        }
    }

    bool FindEqual(int[,,] arr, int num)
    {
        bool result = false;
        for (int i = 0; i < arr.GetLength(2); i++)
        {
            for (int j = 0; j < arr.GetLength(1); j++)
            {
                for (int k = 0; k < arr.GetLength(0); k++)
                {
                    if (num == arr[i, j, k]) result = true;
                }
            }
        }
        return result;
    }

    return array;
}

void Print3DArray(int[,,] array)
{
    for (int i = 0; i < array.GetLength(2); i++)
    {
        for (int j = 0; j < array.GetLength(1); j++)
        {
            for (int k = 0; k < array.GetLength(0); k++)
            {
                Console.Write(array[i,j,k] + $"({i},{j},{k}) ");
            }
            Console.WriteLine("");
        }
    }
}

// Задача 62. Напишите программу, которая заполнит спирально массив 4 на 4.
// Например, на выходе получается вот такой массив:
// 01 02 03 04
// 12 13 14 05
// 11 16 15 06
// 10 09 08 07
 
// Задаем массив
int[,] array_62 = new int[4,4];
// Выводим на экран
Print2DIntArray(FillArray(array_62));

int[,] FillArray(int[,] array) {
    return array;
}

