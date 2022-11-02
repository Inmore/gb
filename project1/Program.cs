Console.WriteLine("Введите первое число из трех");
int a = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите второе число из трех");
int b = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите третье число из трех");
int c = Convert.ToInt32(Console.ReadLine());

int max = a;

if (max < b) {
    max = b;
}
if (max < c) {
    max = c;
}

Console.WriteLine("Max = " + max);