#include <bits/stdc++.h>

using namespace std;

int main() {
    long x,y,z;
    long a,b,c;
    long count = 0;
    cin >> x >> y >> z;
    cin >> a >> b >> c;

    if ((a-x) >= 0) {
        a -= x;
        count++;
    }
    
    long k = (a+b) - y;
    if (k >= 0) {
        count++;

        for (int i = 1; i <= (y); i++) {
            if (i%2 != 0) {
                a--;
            } else {
                b--;
            }
        }
    }
    
    k = (a+b+c) - z;
    if (k >= 0) {
        count++;
    }

    if (count == 3) {
        cout << "YES";
    } else {
        cout << "NO";
    }

    return 0;
}
