#include <algorithm>
#include <bits/stdc++.h>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<vector<int>> fractions;
    vector<int> numerators;
    vector<int> denominators;
    int minNumerator = 0, maxNumerator = 0, minDenominator = 0, maxDenominator = 0;

    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        fractions.push_back({a,b});
        numerators.push_back(a);
        denominators.push_back(b);
    }

    minNumerator = *min_element(numerators.begin(), numerators.end());
    maxNumerator = *max_element(numerators.begin(), numerators.end());
    minDenominator = *min_element(denominators.begin(), denominators.end());
    maxDenominator = *max_element(denominators.begin(), denominators.end());

    for (int i = minNumerator; i <= maxNumerator; i++) {
        for (int j = minDenominator; j <= maxDenominator; j++) {

        }
    }


    // Print
    for(vector<int> i : fractions) {
        for (int j : i) {
            cout << j << " ";
        }
        cout << "\n";
    }

    return 0;
}
