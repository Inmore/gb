Console.WriteLine("Введите целое число");
int number = Convert.ToInt32(Console.ReadLine());
int tempNumber = number;
int result = 0;
int digits = 10;

if (number > 9)
{
    while (tempNumber > 0)
    {

        int temp = tempNumber % 10;
        tempNumber = tempNumber / 10;

        if (tempNumber > 0 && tempNumber < 10)
        {
            result = number - tempNumber * digits - (temp - tempNumber) * digits / 10;
        }

        digits = digits * 10;
    }
}


Console.WriteLine(result);