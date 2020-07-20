#include <iostream>

using namespace std;

void Eratosthenes(int n) {
    if(n<=1) return;

    bool* PrimeArray = new bool[n + 1];
    
    // 0과 1은 소수가 아니므로 2부터 n까지 반복
    for (int i = 2; i <= n; i++)
        // 2~n까지 PrimeArray의 모든 값들을 소수로 임시 정의
        PrimeArray[i] = true;

    // root(n)이상의 소수는 필요없으므로 i * i = n까지만 반복한다
    for (int i = 2; i * i <= n; i++)
        // i가 2일때는 2의 배수, 3일때는 3의 배수로 소수가 아닌 숫자를 거름
        for (int j = i * i; j <= n; j+=i)
            // j는 소수가 아니므로 값 변경
            PrimeArray[j] = false;

    // 출력
    for (int i = 0; i <= n; i++) {
        if (PrimeArray[i])
            cout<< i << ", ";
    }
}

int main() {
    Eratosthenes(1000);

    return 0;
}