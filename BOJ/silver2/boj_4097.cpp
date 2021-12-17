// boj_4097.cpp
// 수익

#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    while (true) {
        int n;
        cin >> n;
        if (n == 0) {
            return 0;
        }
        int total = 0;
        int ans = -10000;
        while (n--) {
            int x;
            cin >> x;
            total += x;
            ans = max(ans, total);
            if (total < 0)
                total = 0;
        }

        cout << ans << '\n';
    }
    return 0;
}
