// boj_14225.cpp
// 부분수열의 합

#include <iostream>
#include <vector>
#define MAX_SIZE 2000000

using namespace std;

int n;
vector<int> s;
bool check[MAX_SIZE];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        s.push_back(x);
    }

    for (int i = 0; i < (1 << n); i++) {
        int sum = 0;
        for (int j = 0; j < n; j++) {
            if (i & (1 << j)) {
                sum += s[j];
            }
        }
        check[sum] = true;
    }

    for (int i = 1; i <= MAX_SIZE; i++) {
        if (!check[i]) {
            cout << i;
            return 0;
        }
    }

    return 0;
}