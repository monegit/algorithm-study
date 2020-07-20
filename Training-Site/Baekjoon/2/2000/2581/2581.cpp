#include <iostream>

using namespace std;

void Eratos(int n, int m) {
    long result = 0;
    int minor = 0;

    bool* array = new bool[m+1];

    for (int i = 2; i <= m; i++)
        array[i] = true;

    for (int i = 2; i * i <= m; i++)
        if (array[i])
            for (int j = i * i; j <= m; j+=i) {
                array[j] = false;
            }

    for (int i = n; i <= m; i++) {
        if (array[i])
        result += i;
    }        

    for (int i = n; i <= m; i++) {
        if (array[i]) {
            minor = i;
            break;
        }
    }

    if (result >= 1) {
        cout<<result<<endl;
        cout<<minor<<endl;
    } else {
        cout<<-1<<endl;
    }
}

int main() {
    int x;
    int y;

    cin>>x;
    cin>>y;

    Eratos(x, y);

    return 0;
}