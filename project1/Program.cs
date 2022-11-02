Console.WriteLine("Введите целое число");
int number = Convert.ToInt32(Console.ReadLine());
string result = "нет";

if (number % 2 == 0) {
    result = "да";
}

Console.WriteLine(result);