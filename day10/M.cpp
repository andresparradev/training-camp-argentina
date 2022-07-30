#include <bits/stdc++.h>
#include <cmath>

using namespace std;

bool isSquare(int n) {
    int raiz = sqrt(n);
    return raiz*raiz == n;
}

string solve(int n) {
    if (n % 2 == 0 && isSquare(n/2)) {
        return "YES";
    }

    if (n % 4 == 0 && isSquare(n/4)) {
        return "YES";
    }

    return "NO";
}

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        int n;
        cin >> n;
        cout << solve(n) << endl;
    }
}
