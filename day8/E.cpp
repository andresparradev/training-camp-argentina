#include <algorithm>
#include <bits/stdc++.h>
#include <cstdlib>
#include <functional>
#include <string>
#include <vector>

using namespace std;

int main() {
  int k;
  cin >> k;

  for (int i = 0; i < k; i++) {
    long p;
    int n;
    cin >> p >> n;
    vector<long> amounts;
    vector<long> result;
    long sumTotal = 0;

    for (int j = 0; j < n; j++) {
      long el;
      cin >> el;
      amounts.push_back(el);
      result.push_back(0);
      sumTotal += el;
    }

    if (sumTotal < p) {
      cout << "IMPOSSIBLE" << endl;
      continue;
    }

    while (p > 0) {
      if (p < n) {
        long minNumber = amounts[0];
        for (int j = 0; j < n; j++) {
          if (amounts[j] != 0) {
            minNumber = min(minNumber, amounts[j]);
          }
        }

        for (int j = 0; j < n; j++) {
          if (p > 0) {
            if (amounts[j] > minNumber) {
              amounts[j] -= 1;
              result[j] += 1;
              p--;
            }
          }
        }

        for (int j = 0; j < n; j++) {
          if (p > 0 && amounts[j] == minNumber) {
            amounts[j] -= 1;
            result[j] += 1;
            p--;
          }
        }
      } else {
        for (int j = 0; j < n; j++) {
          if (amounts[j] != 0 && p > 0) {
            amounts[j] -= 1;
            result[j] += 1;
            p--;
          }
        }
      }
    }

    for (long j = 0; j < n; j++) {
      cout << result[j];
      if (j < n) {
          cout << " ";
      }
    }
    cout << endl;
  }

  return 0;
}
