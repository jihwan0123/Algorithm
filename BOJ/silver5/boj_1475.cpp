#include <bits/stdc++.h>
using namespace std;
int arr[11];
int main(void) {
    ios::sync_with_stdio(0);
    cin.tie(0);
    string s;
    cin >> s;
    for (int i=0; i<s.size();i++) {
        arr[s[i]-'0']++;
    }
    int temp = arr[6]+arr[9];
    if (temp % 2 == 1) temp++;
    temp /= 2;
    arr[6] = temp;
    arr[9] = temp;
    cout << *max_element(arr, arr+10);
}