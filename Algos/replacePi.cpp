#include <iostream>

using namespace std;

void replacePi(char input[]) {
	// Write your code here
    int size = 0;
    while(input[size] != '\0') {
        ++size;
    }

    if(size <= 1){
        return;
    }

    replacePi(input+1);

    size = 0;
    while(input[size] != '\0') {
        ++size;
    }

    if(input[0] == 'p' && input[1] == 'i'){
        //two space shifting
        for(int i = size-1; i >= 0; i--){
            input[i+2] = input[i];
        }
        input[0] = '3';
        input[1] = '.';
        input[2] = '1';
        input[3] = '4';
    }
}

int main()
{
    char input[10000];
    cin.getline(input, 10000);
    replacePi(input);
    cout << input << endl;
}
