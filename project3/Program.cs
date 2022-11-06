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


