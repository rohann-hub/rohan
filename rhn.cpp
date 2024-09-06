// #pattern program to print even and odd numbere
// 1
// 2 4
// 3 5 7
// 6 8 10 12
#include <iostream>
using namespace std;

int main() {
    int rows, odd = 1, even = 2;

    cout << "Enter the number of rows: ";
    cin >> rows;

    
    for (int i = 1; i <= rows; i++) {
        
        for (int j = 1; j <= i; j++) {
            if (i % 2 == 0) { 
                cout << even << " ";
                even += 2;
            } else { 
                cout << odd << " ";
                odd += 2;
            }
        }
        cout << endl; 
    }

    return 0;
}
