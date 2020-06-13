#include <iostream>
#include <string>

using namespace std;

int main() {
    int _input = 0;
    cin >> _input;
    for (int i = 1; i <= 9; i++) {
        printf("%d * %d = %d\n", _input, i, _input * i);
    }
}