#include <iostream>
#include <fstream>
using namespace std;

// implement your own md5 -
#include "md5.hpp"

bool is_valid(const string& key, long num) {
    string hash = md5(key+to_string(num));
    for (int i = 0; i < 5; i++) {
        if (hash.at(i) != '0') return false;
    }
    return true;
}

long linear_search(const string& key) {
    long first = 0;
    while (!is_valid(key, first)) { ++first; }
    return first;
}

int main() {
    ifstream ifs("input.txt");
    string key;
    getline(ifs, key);
    ifs.close();
    cout << linear_search(key) << endl;
}