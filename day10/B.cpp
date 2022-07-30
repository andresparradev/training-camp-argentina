#include <bits/stdc++.h>
using namespace std;

#define forn(i, n) for (ll i = 0; i < n; i++)
#define ll long long

int main() {
  ll n, m, l;
  ll ans = 0;
  cin >> n >> m;
  char o;

  forn(i, n) {
    cin >> o;
    cin >> l;
    if (o == '+') {
      m += l;
    } else {
      if (m < l) {
        ans++;
      } else {
        m -= l;
      }
    }
  }

  cout << m << " " << ans << endl;
  return 0;
}
