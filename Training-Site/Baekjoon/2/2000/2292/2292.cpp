#include <iostream>

using namespace std;

int main() {
    long long input = 0;
    long long sqrt = 1;
    float count = 1;

    cin>>input;

    while (true) {
        if (sqrt >= input)
            break;

        sqrt += 6 * count++;
    }

    cout<<count<<endl;
    return 0;
}