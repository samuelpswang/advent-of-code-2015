#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int wrapping_paper_area(int l, int w, int h) {
    int min_side = min(l*w, min(w*h, h*l));
    return 2*l*w + 2*w*h + 2*h*l + min_side;
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
        sum += wrapping_paper_area(l, w, h);
    }

    cout << sum << endl;
}