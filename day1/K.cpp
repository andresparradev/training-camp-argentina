#include <iostream>

using namespace std;

int main() {
	int n, c = 0, m;
	cin >> n;
	
	m = n/2;

	if(n % 2 == 0) {
		for(int i = 1; i < m; i++) {
			if((m-i) != (m-(m-i)) && (m-i) > (m-(m-i))) {
				c++;
			}
		}
	}

	cout << c;
	return 0;
}
