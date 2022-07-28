#include <bits/stdc++.h>

using namespace std;

long long getSmallestDivisor(long long n) {
    if (n % 2 == 0) {
        return 2;
    }

    for (long long i = 3; i*i <= n; i+=2) {
        if (n % i == 0) {
            return i;
        }
    }

    return n;
}

int main() {
    long long n;
    long long count = 0;
    cin >> n;

    while (n != 0) {
        n -= getSmallestDivisor(n);
        count++;

        if (n % 2 == 0) {
            cout << (n/2) + count;
            return 0;
        }
    }

    cout << count;
}
