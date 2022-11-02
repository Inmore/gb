Console.WriteLine("Введите первое целое число");
int a = Int32.Parse(Console.ReadLine());
Console.WriteLine("Введите второе целое число");
int b = Int32.Parse(Console.ReadLine());

int max = a;

if (a < b) {
    max = b;
}

Console.WriteLine("max = " + max);