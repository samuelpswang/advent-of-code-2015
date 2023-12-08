#include <iostream>
#include <fstream> 
#include <string>
#include <set>
using namespace std;

int main() {
    ifstream ifs("input.txt");
    if (!ifs) exit(1);

    string dir;
    getline(ifs, dir);
    ifs.close();
    
    int x = 0, y = 0;
    set<pair<int,int>> s = {{0, 0}};
    for (char step: dir) {
        switch (step) {
            case '<':
                --x;
                break;
            case '>':
                ++x;
                break;
            case '^':
                ++y;
                break;
            case 'v':
                --y;
                break;
        }
        pair<int,int> p = {x, y};
        if (!s.count(p)) s.insert(p);
    }

    cout << s.size() << endl;
}