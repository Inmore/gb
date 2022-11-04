Console.WriteLine("Введите номер дня недели от 1 до 7");
int dayNum = Convert.ToInt32(Console.ReadLine());
string message = "";

if (dayNum > 0 && dayNum <= 7)
{
    if (dayNum == 6 || dayNum == 7)
    {
        message = "да";
    } else {
        message = "нет";
    }
    Console.WriteLine(message);
}

