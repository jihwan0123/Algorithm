#include <vector>
#include <algorithm>
using namespace std;

int student[31];

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    
    sort(reserve.begin(), reserve.end());
    
    for (int i: lost) student[i] = 1;
    for (int i: reserve){
        if (student[i] == 1) 
            student[i] = -1;
    }
    
    for (int i: reserve){
        if (student[i] == -1) continue;
        if (student[i-1] == 1) {
            student[i-1] = 0;
        }
        else if (student[i+1] == 1) {
            student[i+1] = 0;
        }
    }
    
    for (int i=1;i<=n;i++){
        if (student[i] == 0 || student[i] == -1){
            answer++;
        }
    }
    
    
    return answer;
}