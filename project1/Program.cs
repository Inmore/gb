Console.WriteLine("Введите целое число");
int number = Int32.Parse(Console.ReadLine());

int i = 1;

while (i <= number) {
    if (i % 2 == 0) {
        if (i == number) {
            Console.WriteLine(i);
        } else {
            Console.Write(i + ", ");
        }
    }
    i++;
}