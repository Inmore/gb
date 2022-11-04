Console.WriteLine("Введите целое число");
int number = Convert.ToInt32(Console.ReadLine());

int digit = 0;

if (number / 100 > 0)
{
    if (number < 1000) {
        digit = number / 100;
    } else {
        digit = (number / 100) % 10;
    }
    Console.WriteLine(digit);
}
else
{
    Console.WriteLine("третьей цифры нет");
}