Console.WriteLine("Введите целое число");
int number = Int32.Parse(Console.ReadLine());
string result = "нет";

if (number % 2 == 0) {
    result = "да";
}

Console.WriteLine(result);