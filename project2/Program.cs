Console.WriteLine("Введите целое число");
int number = Convert.ToInt32(Console.ReadLine());

int count = 0;
int i = 0;
int temp1 = number;
int temp2 = number;
int result = 0;

if (number / 100 > 0)
{
    do {
        count++;
        temp1 = temp1 / 10;
    }
    while (temp1 > 0);

    while (i < count - 3) {
        temp2 = temp2 / 10;
        i++;
    }

    result = temp2 % 10;

    Console.WriteLine(result);
}
else
{
    Console.WriteLine("третьей цифры нет");
}