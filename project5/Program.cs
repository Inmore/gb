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

