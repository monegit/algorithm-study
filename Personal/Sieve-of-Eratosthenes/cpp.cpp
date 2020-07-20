#include <iostream>

using namespace std;

void Eratosthenes(int n) {
    if(n<=1) return;

    bool* PrimeArray = new bool[n + 1];

    for (int i = 2; i <= n; i++)
        // PrimeArray의 모든 값들을 소수로 임시 정의
        PrimeArray[i] = true;

    for (int i = 2; i * i <= n; i++)
        if (PrimeArray[i])
            for (int j = i * i; j <= n; j+=i)
                // 소수 j의 PrimeArray는 소수로 바꿈
                PrimeArray[j] = false;

    for (int i = 0; i <= n; i++) {
        if (PrimeArray[i])
            cout<< i << ", ";
    }
}

int main() {
    Eratosthenes(100);

    return 0;
}