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
        Console.Write(arr[i] + " / ");
        if (i % 2 != 0) {
            result = result + arr[i];
        }
    }

    return result;
}

