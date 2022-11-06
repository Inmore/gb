isPalindrom(21512);

// Task 19
void isPalindrom(int number) {
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
void abs3D() {
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

