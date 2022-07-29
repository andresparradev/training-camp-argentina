#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, a, b, c = 0;
    cin >> n >> a >> b;
    int count = 0;
    int clients = 0;

    for (int i = 0; i < n; i++) {
        int sizeGroup;
        cin >> sizeGroup;
        clients += sizeGroup;

        if (sizeGroup == 1) {
            if (a > 0) {
                a--;
            } else {
                if (b > 0) {
                    b--;
                    c++;
                } else {
                    if (c > 0) {
                        c--;
                    } else {
                        count++;
                    }
                }
            }
        } else {
            if (b > 0) {
                b--;
            } else {
                count += 2;
            }
        }
    }

    cout << count;

    return 0;
}
