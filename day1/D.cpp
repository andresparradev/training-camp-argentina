#include <iostream>
#include <vector>

using namespace std;

int main() {
	int n, m, min = 0, max = 0;
	cin >> n;
	cin >> m;
	int teams[m];
	
	for(int i = 0; i < n; i++) {
		if(!teams[i]) {
			teams[i] = 0;
		} else {
			teams[i] = teams[i] + 1;
		}
	}

	for(int i = 0; i < m; i++) {
		cout << teams[i] << endl;
	}

	cout << "\n";

	
	/* cout << min << " " << max; */

	return 0;
}
