#include <iostream>
#include <vector> 

using namespace std;

int main() {
	int n, k;
	cin >> n >> k;
	int matriz[k][n];

	for(int i = 0; i < k; i++) {
		for(int j = 0; j < n; i++) {
			int a = 0;
			cin >> a;
			matriz[i][j] = a;
		}
	}

	vector<int> sequence;

	for(int i = 0; i < k; i++) {
		for(int j = 0; j < n; j++) {
			int el = matriz[i][j];
		}
	}

	return 0;
}
