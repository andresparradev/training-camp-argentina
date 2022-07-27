#include <bits/stdc++.h>

using namespace std;
 
int main() {
    long long n;
    cin >> n;

    vector<long long> d;
    long long best = 0;

    long long i = 1;
    while (i*i <= n) {
        if (n % i == 0) {
            d.push_back(i);
            d.push_back(n/i);
        }
        i++;
    }

    sort(d.begin(), d.end());

    for (long long j = d.size()-1; j >= 0; j--) {
        bool divi = false;

        for (long long k = 2; k*k <= d[j]; k++) {
            if (d[j] % (k*k) == 0) {
                divi = true;
                break;
            }
        }

        if (divi == false) {
            best = d[j];
            break;
        }
    }

    cout << best;
 
    return 0;
}
