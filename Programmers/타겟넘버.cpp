#include <string>
#include <vector>
#include <algorithm>

using namespace std;
int ans;

void dfs(int total, int target, int cnt, vector<int> num) {
    if (cnt > num.size()) return;
    
    if ((cnt == num.size()) && (total == target)){
        ans++;
        return;
    }
    
    dfs(total+num[cnt], target, cnt+1, num);
    dfs(total-num[cnt], target, cnt+1, num);
}


int solution(vector<int> numbers, int target) {
    dfs(0, target, 0, numbers);
    
    return ans;
}