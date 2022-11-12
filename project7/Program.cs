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
