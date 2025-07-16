#include <iostream>
#include <string>
using namespace std;

void helloWorld() {
    cout << "\n--- Hello World ---\n";
    cout << "Hello, GitHub!" << endl;
}

void bubbleSort() {
    cout << "\n--- Bubble Sort ---\n";
    int arr[] = {5, 2, 9, 1, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);

    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }

    cout << "Sorted array: ";
    for (int i = 0; i < n; i++) cout << arr[i] << " ";
    cout << endl;
}

void palindromeChecker() {
    cout << "\n--- Palindrome Checker ---\n";
    string str;
    cout << "Enter a word: ";
    cin >> str;

    string reversed = string(str.rbegin(), str.rend());

    if (str == reversed)
        cout << "It's a palindrome!" << endl;
    else
        cout << "Not a palindrome." << endl;
}

void simpleCalculator() {
    cout << "\n--- Simple Calculator ---\n";
    double a, b;
    char op;
    cout << "Enter two numbers: ";
    cin >> a >> b;
    cout << "Enter operator (+, -, *, /): ";
    cin >> op;

    switch (op) {
        case '+': cout << "Result: " << a + b << endl; break;
        case '-': cout << "Result: " << a - b << endl; break;
        case '*': cout << "Result: " << a * b << endl; break;
        case '/': 
            if (b != 0)
                cout << "Result: " << a / b << endl;
            else
                cout << "Cannot divide by zero!" << endl;
            break;
        default: cout << "Invalid operator!" << endl;
    }
}

void trianglePattern() {
    cout << "\n--- Triangle Pattern ---\n";
    int rows;
    cout << "Enter number of rows: ";
    cin >> rows;

    for (int i = 1; i <= rows; ++i) {
        for (int j = 1; j <= i; ++j)
            cout << "* ";
        cout << endl;
    }
}

int main() {
    int choice;
    do {
        cout << "\n=========== Menu ===========" << endl;
        cout << "1. Hello World" << endl;
        cout << "2. Bubble Sort" << endl;
        cout << "3. Palindrome Checker" << endl;
        cout << "4. Simple Calculator" << endl;
        cout << "5. Triangle Pattern" << endl;
        cout << "0. Exit" << endl;
        cout << "Choose an option: ";
        cin >> choice;

        switch (choice) {
            case 1: helloWorld(); break;
            case 2: bubbleSort(); break;
            case 3: palindromeChecker(); break;
            case 4: simpleCalculator(); break;
            case 5: trianglePattern(); break;
            case 0: cout << "Exiting program..." << endl; break;
            default: cout << "Invalid option. Try again.\n";
        }

    } while (choice != 0);

    return 0;
}
