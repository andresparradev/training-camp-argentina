#include <iostream>
using namespace std;
 
int main() {
	int n;
	int r = 0;
	int vector [n];
	cin >> n;

	for(int i=0; i < n; i++){
		cin >> vector[i];
	}

	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++){
			if(i != j && vector[j] <= n && vector[i] != vector[j]){
				r++;
				j = n;
			}
		}
	}
	
	if(r == 3){
		cout << "YES" << endl;
	}else{
		cout << "NO" << endl;
	}

	return 0;
}
