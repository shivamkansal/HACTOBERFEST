#include <iostream>

using namespace std;

int stringToNumber(char input[]) {
    // Write your code here
    int size = 0;
    while(input[size] != '\0') {
        ++size;
    }

    if(size == 1) {
        int a = input[0];
        cout << "a: " << a - 48 << endl;
        return a - 48;
    }

    int smallNumber = stringToNumber(input+1);
   int b = input[0] - 48;

    int multiplier = 1;
    for(int i = 0; i < size-1; i++) {
        multiplier *= 10;
    }
    cout << "Multiplier: " << multiplier << endl;
    return b*multiplier + smallNumber;
}

int main()
{
    char input[50];
    cin >> input;
    cout << stringToNumber(input) << endl;
}
