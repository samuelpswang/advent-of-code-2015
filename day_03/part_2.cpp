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
    
    bool is_santa = true;
    int x = 0, y = 0, rx = 0, ry = 0;
    set<pair<int,int>> s = {{0, 0}};
    for (char step: dir) {
        switch (step) {
            case '<':
                if (is_santa) --x;
                else --rx;
                break;
            case '>':
                if (is_santa) ++x;
                else ++rx;
                break;
            case '^':
                if (is_santa) ++y;
                else ++ry;
                break;
            case 'v':
                if (is_santa) --y;
                else --ry;
                break;
        }
        if (is_santa) {
            pair<int,int> p = {x, y};
            if (!s.count(p)) s.insert(p);
        } else {
            pair<int,int> rp = {rx, ry};
            if (!s.count(rp)) s.insert(rp);
        }
        is_santa = !is_santa;
    }

    cout << s.size() << endl;
}