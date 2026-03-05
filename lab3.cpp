#include <iostream>
using namespace std;

int main() {
    // Task 1 (Hailstone Sequence (Collatz Conjecture)

    int n;
    cout << "Please enter a positive int greater than 1: ";
    cin >> n;

    while (n <= 1) {
        cout << "Please enter a positive int greater than 1: ";
        cin >> n;
    }

    int steps = 0;
    cout << n;

    while (n != 1) {

        if (n % 2 == 0) {
            n = n / 2;
        } else {
            n = n * 3 + 1;
        }

        cout << " -> " << n;
        steps++;
    }

    cout << "\nTotal steps: " << steps << endl;
    cout << "Now we are continuing with FizzBuzz game." << endl;

    // Task 2 (FizzBuzz Counter)

    cout << "\nPlease enter a number between 10 and 100: ";
    cin >> n;

    while (n < 10 || n > 100) {
        cout << "Invalid input." << endl;
        cout << "Please enter a number between 10 and 100: ";
        cin >> n;
    }
    int fizz = 0;
    int buzz = 0;
    int fizzbuzz = 0;

    for (int i = 1; i <= n; i++) {

        if (i % 7 == 0) {
            cout << i << " is skipped" << endl;
        }

        if (i % 3 == 0 && i % 5 == 0) {
            cout << "FizzBuzz" << endl;
            fizzbuzz++;
        }

        else if (i % 3 == 0) {
            cout << "Fizz" << endl;
            fizz++;
        }

        else if (i % 5 == 0) {
            cout << "Buzz" << endl;
            buzz++;
        }

        else {
            cout << i << endl;
        }
    }

    cout << "Fizz counter: " << fizz << endl;
    cout << "Buzz counter: " << buzz << endl;
    cout << "FizzBuzz counter: " << fizzbuzz << endl;


    //TaSK 3:
    int x;
    cout << "Please enter a number between 3 and 9: ";
    cin >> x;

    for (int i = 1; i < 2 * x; i++) {
        int k = x - abs(x - i);

        for (int j = 0; j < k; j++) {
            cout << "*";
        }

        cout << endl;
    }

    return 0;
}
