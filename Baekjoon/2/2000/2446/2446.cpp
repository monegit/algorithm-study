#include <iostream>

using namespace std;

int main()
{
    int _input = 0;
    cin >> _input;

    int reverse_star_count = (_input*2)-1;

    for (int i = 0; i <= _input - 1; i++)
    {
        for (int space = 0; space <= i - 1; space++)
            cout<<' ';
        
        for (int star = 1; star <= reverse_star_count; star++)
            cout<<'*';
        reverse_star_count-=2;

        cout<<endl;
    }


    int star_count = 2;
    int space_count = (_input - 1);

    for (int i = 1; i <= _input - 1; i++)
    {
        for (int space = space_count - 1; space >= 1; space--)
            cout<<' ';
        space_count-=1;

        for (int star = 0; star <= star_count; star++)
            cout<<'*';
        star_count+=2;

        cout<<endl;
    }
}