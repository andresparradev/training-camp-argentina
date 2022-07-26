#include <iostream>
#include <math.h>

using namespace std;

int main() {
	int n, k, count = 0;
	float note = 0;
	cin >> n >> k;
	count = n;

	int elements[n];

	for(int i = 0; i < n; i++) {
		int a;
		cin >> a;
		elements[i] = a;
		note += a;
	}

	while(round(note/count) < k) {
		if(round(note/count) < k) {
			note += k;
			count++;
		}
	}

	count -= n;

	cout << count;

	return 0;
}
