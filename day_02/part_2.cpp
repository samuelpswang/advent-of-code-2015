#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int ribbon_length(int l, int w, int h) {
    int min_side = min(l+w, min(w+h, h+l));
    return l*w*h + 2*min_side;
}

int main() {
    ifstream ifs("input.txt");
    if (!ifs) exit(1);
    
    string line;
    size_t pos1, pos2;
    int l, w, h;
    long sum = 0;
    while (getline(ifs, line)) {
        pos1 = line.find('x');
        pos2 = line.find('x', pos1+1);
        l = stoi(string(line.begin(), line.begin()+pos1));
        w = stoi(string(line.begin()+pos1+1, line.begin()+pos2));
        h = stoi(string(line.begin()+pos2+1, line.end()));
        sum += ribbon_length(l, w, h);
    }

    cout << sum << endl;
}