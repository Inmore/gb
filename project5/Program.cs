// Задача 34: Задайте массив заполненный случайными положительными трёхзначными числами. 
// Напишите программу, которая покажет количество чётных чисел в массиве.
// [345, 897, 568, 234] -> 2
int[] array = new int[4];
for (int i = 0; i < array.Length; i++)
{
    array[i] = new Random().Next(100, 1000);
}

int CountEven(int[] arr)
{
    int count = 0;
    for (int i = 0; i < arr.Length; i++)
    {
        if (arr[i] % 2 == 0) {
            count++;
        }
    }
    return count;
}

// Задача 36: Задайте одномерный массив, заполненный случайными числами. 
// Найдите сумму элементов, стоящих на нечётных позициях.
// [3, 7, 23, 12] -> 19
// [-4, -6, 89, 6] -> 0
int[] randomNumbers = new int[4];
for (int i = 0; i < randomNumbers.Length; i++)
{
    randomNumbers[i] = new Random().Next(-99, 100);
}

int OddPositionItemsSum(int[] arr) {
    int result = 0;

    for (int i = 0; i < arr.Length; i++)
    {
        if (i % 2 != 0) {
            result = result + arr[i];
        }
    }

    return result;
}

// Задача 38: Задайте массив вещественных чисел. 
// Найдите разницу между максимальным и минимальным элементов массива.

double[] realArray = new double[5];

for (int i = 0; i < realArray.Length; i++)
{
    realArray[i] = new Random().NextDouble();
}
DifferenceBetweenMinAndMax(realArray);
double DifferenceBetweenMinAndMax(double[] array)
{
    double diff = 0;
    double min = array[0];
    double max = array[0];

    for (int i = 0; i < array.Length; i++)
    {
        if (min > array[i]) min = array[i];
        if (max < array[i]) max = array[i];
    }

    diff = max - min;

    return diff;
}

// Задача HARD STAT необязательная: Задайте массив случайных целых чисел. 
// Найдите максимальный элемент и его индекс, минимальный элемент и его индекс, 
// среднее арифметическое всех элементов. Сохранить эту инфу в отдельный массив и вывести 
// на экран с пояснениями. Найти медианное значение первоначалального массива , возможно 
// придется кое-что для этого дополнительно выполнить.

int[] rndNums = new int[7];
for (int i = 0; i < rndNums.Length; i++)
{
    rndNums[i] = new Random().Next(-99, 100);
}
string[] res = AnalizeArray(rndNums);
for (int i = 0; i < res.Length; i++) {
    Console.WriteLine(res[i]);
}

string[] AnalizeArray(int[] array) {
    string[] result = new string[3];
    int min = array[0];
    int max = array[0];
    int index_min = 0;
    int index_max = 0;
    int sum = 0;
    int average = 0;
    int count = 0;

    for (int i = 0; i < array.Length; i++)
    {
        if (min > array[i]) {
            min = array[i];
            index_min = i;
        }
        if (max < array[i]) {
            max = array[i]; 
            index_max = i;
        }
        sum = sum + array[i];
        count++;
    }
    average = sum / count;

    for (int i = 0; i < result.Length; i++)
    {
        if (i == 0) result[i] = $"максимальный элемент {max} с индексом {index_max}";
        if (i == 1) result[i] = $"минимальный элемент {min} с индексом {index_min}";
        if (i == 2) result[i] = $"среднее арифметическое всех элементов {average}";
    }
    return result;
}
// Console.WriteLine(" Median: " + ArrayMedian(rndNums));
double ArrayMedian(int[] array)
{
    double result = 0.0;
    int temp;

    for (int i = 0; i < array.Length - 1; i++)
    {
        for (int j = i + 1; j < array.Length; j++)
        {
            if (array[i] > array[j])
            {
                temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
    }

    if (array.Length % 2 > 0) {
        result = array[array.Length / 2];
    } else {
        result = (array[array.Length / 2 - 1] + array[array.Length / 2]) / 2;
    }

    return result;
}


