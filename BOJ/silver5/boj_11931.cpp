// boj_11931.cpp
// 수 정렬하기 4

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int n;
vector<int> arr;

int main()
{
    ios::sync_with_stdio(false); 
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n;
    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        arr.push_back(temp);
    }
    sort(arr.begin(), arr.end(), greater<int>());
    for (int a: arr) {
        cout << a << '\n';
    }
}