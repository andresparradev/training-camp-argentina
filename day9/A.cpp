#include <bits/stdc++.h>

using namespace std;

int main() {
    long long n;
    long long countA = 0, countB = 0;
    int currentA = 0, currentB = 0;
    string a, b;
    cin >> n;
    cin >> a;
    cin >> b;
    int menor = 0;

    if (a.length() < b.length()) menor = a.length();
    else menor = b.length();

    for (int i = 0; i < menor; i++) {
        char electionA = a[currentA];
        char electionB = b[currentB];

        if (electionA != electionB) {
            if ((electionA == 'R' && electionB == 'S') || (electionA == 'P' && electionB == 'R') || (electionA == 'S' && electionB == 'P')) {
                countB++;
            }
 
            if ((electionB == 'R' && electionA == 'S') || (electionB == 'P' && electionA == 'R') || (electionB == 'S' && electionA == 'P')) {
                countA++;
            }
        }

        if (currentA == int(a.length())-1) {
            currentA = 0;
        } else {
            currentA++;
        }
 
        if (currentB == int(b.length())-1) {
            currentB = 0;
        } else {
            currentB++;
        }
    }

    countA *= round(n/menor);
    countB *= round(n/menor);

    cout << countA << " " << countB;

    return 0;
}
