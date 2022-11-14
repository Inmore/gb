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