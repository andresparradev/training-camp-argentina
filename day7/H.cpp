#include <bits/stdc++.h>
#include <type_traits>

using namespace std;

int main() {
    string m, word;
    long l;
    getline(cin, m);
    cin >> l;

    word = m;

    for (long i = 0; i < l; i++) {
        long x;
        cin >> x;

        string pre = word.substr(0, x);
        string suf = word.substr(x, word.size());

        reverse(pre.begin(), pre.end());
        reverse(suf.begin(), suf.end());

        word = pre.append(suf);
    }

    cout << word;

    return 0;
}
