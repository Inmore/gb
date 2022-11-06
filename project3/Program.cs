// try
// {
//     Cubes(-3);
// }
// catch (Exception e) { Console.WriteLine(e.Message); };

// try
// {
//     AbsND();
// }
// catch (Exception e) { Console.WriteLine(e.Message); };

// Task 19
void IsPalindrom(int number) {
    int d1 = 0;
    int d2 = 0;
    string result = "да";
    
    for (int i = 0; i < 5; i++) {
        if (i == 0) {
            d1 = number % 10;
        }
        if (i == 1) {
            d2 = number % 10;
        }
        if (i == 3) {
            if (number % 10 != d2) {
                result = "нет";
                break;
            }
        }
        if (i == 4) {
            if (number % 10 != d1) {
                result = "нет";
            }
        }
        number = number / 10;
    }
    
    Console.WriteLine(result);
}

// Task 21
void Abs3D() {
    Console.WriteLine("Введите координаты точки A по очереди x, y и z");
    int a_x = Convert.ToInt32(Console.ReadLine());
    int a_y = Convert.ToInt32(Console.ReadLine());
    int a_z = Convert.ToInt32(Console.ReadLine());
    Console.WriteLine("Введите координаты точки B по очереди x, y и z");
    int b_x = Convert.ToInt32(Console.ReadLine());
    int b_y = Convert.ToInt32(Console.ReadLine());
    int b_z = Convert.ToInt32(Console.ReadLine());
    
    double result;
    
    result = System.Math.Sqrt(System.Math.Pow((a_x - b_x), 2) + System.Math.Pow((a_y - b_y), 2) + System.Math.Pow((a_z - b_z), 2));
    
    result = System.Math.Round(result, 2);
    
    Console.WriteLine(result);
}


// task 23
void Cubes(int number)
{
    if (number > 0)
    {
        string result = "";
        for (int i = 1; i <= number; i++)
        {
            result = result + System.Math.Pow(i, 3);
            if (number != i)
            {
                result = result + ", ";
            }
        }

        Console.WriteLine(result);
    }
    else
    {
        throw new ArgumentException("Введите целое число больше 0");
    }

}


// task 21 hard
void AbsND()
{
    Console.WriteLine("Введите мерность пространства");
    int dimension = Convert.ToInt32(Console.ReadLine());

    if (dimension > 0)
    {
        int[] coords_A = new int[dimension];
        int[] coords_B = new int[dimension];
        double summa = 0.0;
        double result = 0.0;

        Console.WriteLine("Введите по очереди координаты точки A");
        for (int i = 0; i < dimension; i++)
        {
            coords_A[i] = Convert.ToInt32(Console.ReadLine());
        }

        Console.WriteLine("Введите по очереди координаты точки B");
        for (int i = 0; i < dimension; i++)
        {
            coords_B[i] = Convert.ToInt32(Console.ReadLine());
        }

        for (int i = 0; i < dimension; i++)
        {
            summa = summa + System.Math.Pow((coords_A[i] - coords_B[i]), 2);
        }

        result = System.Math.Round(System.Math.Sqrt(summa), 2);

        Console.WriteLine(result);
    }
    else
    {
        throw new ArgumentException("Введите целое число больше 0");
    }
}

