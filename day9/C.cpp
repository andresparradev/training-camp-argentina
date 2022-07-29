#include <bits/stdc++.h>
#include <cstring>
#include <functional>
#include <string>

using namespace std;

vector<string> subs;

void getSubs(string str, string out) {
    if (str.empty()) {
        subs.push_back(out);
        return;
    }

    getSubs(str.substr(1), out + str[0]);
    getSubs(str.substr(1), out);
}

bool compare(string a, string b) {
    return a.length() < b.length();
}

int main() {
    string a, b;
    getline(cin, a);
    getline(cin, b);
    int i;

    if (a.length() >= b.length()) {
        getSubs(a, "");
        sort(subs.begin(), subs.end(), compare);

        for (i = subs.size()-1; i >= 0; i--) {
            if (b.find(subs[i]) == ::string::npos) {
                cout << subs[i].length();
                return 0;
            }
        }
    } else {
        getSubs(b, "");
        sort(subs.begin(), subs.end(), compare);
        for (i = subs.size()-1; i >= 0; i--) {
            if (a.find(subs[i]) == ::string::npos) {
                cout << subs[i].length();
                return 0;
            }
        }
    }
    
    cout << -1;
    return 0;
}
