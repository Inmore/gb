string[] FilterArray()
{
    Console.WriteLine("Введите количество элементов массива");
    int m = Convert.ToInt32(Console.ReadLine());
 
    if (m > 0)
    {
        string[] array = new string[m];
 
        Console.WriteLine($"Введите поочередно элементы массива");
 
        for (int i = 0; i < array.Length; i++)
        {
            array[i] = Console.ReadLine();
        }
 
        int count = 0;
 
        for (int i = 0; i < array.Length; i++)
        {
            if (array[i].Length <= 3) {
                count++;
            } 
        }
 
        string[] result = new string[count];
        int k = 0;
 
        for (int i = 0; i < array.Length; i++)
        {
            if (array[i].Length <= 3) {
                result[k] = array[i];
                k++;
            } 
        }
 
        return result;
    } else {
        throw new ArgumentException("Ожидается натуральное число");
    }
 
}
string[] array = FilterArray();
PrintStringArray(array);
void PrintStringArray(string[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        string result = "";
 
        result = $"{array[i]}";
        Console.Write(result);
 
        if (i != array.Length - 1) Console.Write(", "); 
    }
    Console.WriteLine("");
}