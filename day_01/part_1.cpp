#include <iostream>
#include <fstream>
using namespace std;

int main() {
    ifstream ifs("input.txt");
    if (!ifs) exit(1);
    
    string dir;
    getline(ifs, dir);

    int floor = 0;
    for (char c: dir) {
        switch (c) {
            case '(':
                ++floor;
                break;
            case ')':
                --floor;
                break;
        }
    }
    
    cout << floor << endl;
}