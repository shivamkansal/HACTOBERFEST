#include <iostream>
#include <string>
using namespace std;

void helper(string input, string output) {
    if(input.length() == 0) {
        cout << output << endl;
        return;
    }

    string newOut, newOut2;

    int i = 0;
    for(; i < output.length(); i++) {
        newOut[i] = output[i];
        newOut2[i] = output[i];
    }
    cout << "newOut: "<< newOut << endl;
    cout << "newOut2: "<< newOut2 << endl;
    int firstNumber = input[0] - 48;
    newOut[i] = 'a' + firstNumber - 1;


    int tens = input[0] - 48;
    int ones = input[1] - 48;
    int firstTwo = (tens*10) + ones;
    newOut2[i] = 'a' + firstTwo - 1;

    cout << "newOut: "<< newOut << endl;
    cout << "newOut2: "<< newOut2 << endl;

    helper(input.substr(1), newOut);
    if(input.length() >= 2)
        helper(input.substr(2), newOut2);
}


void printAllPossibleCodes(string input) {
    /*
    Given the input as a string, print all its possible combinations. You do not need to return anything.
    */
    if(input.length() == 0) {
        return;
    }

    string output;
    helper(input, output);
}

int main()
{
    string input;
    cin >> input;

    printAllPossibleCodes(input);
    return 0;
}
