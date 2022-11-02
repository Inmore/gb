Console.WriteLine("Введите первое число из трех");
int a = Int32.Parse(Console.ReadLine());
Console.WriteLine("Введите второе число из трех");
int b = Int32.Parse(Console.ReadLine());
Console.WriteLine("Введите третье число из трех");
int c = Int32.Parse(Console.ReadLine());

int max = a;

if (max < b) {
    max = b;
}
if (max < c) {
    max = c;
}

Console.WriteLine(max);