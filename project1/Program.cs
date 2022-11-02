Console.WriteLine("Введите целое число");
int number = Convert.ToInt32(Console.ReadLine());

int i = 1;

while (i <= number) {
    if (i % 2 == 0) {
        if (i == number || i == number - 1) {
            Console.WriteLine(i);
        } else {
            Console.Write(i + ", ");
        }
    }
    i++;
}