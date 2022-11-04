Console.WriteLine("Введите целое трехзначное число");
int number = Convert.ToInt32(Console.ReadLine());

int result = 0;
result = (number / 10) % 10;

Console.WriteLine(result);