// boj_7682.cpp : 이 파일에는 'main' 함수가 포함됩니다. 거기서 프로그램 실행이 시작되고 종료됩니다.
//

#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cstdlib>
using namespace std;

char arr[3][3];
string input;
int o_cnt, x_cnt;

bool check_x() {
    int chk = 0;
    for (int i = 0; i < 3; i++) {
        chk = 0;
        for (int j = 0; j < 3; j++) {
            if (arr[i][j] == 'X') {
                chk++;
            }
        }
        if (chk == 3) {
            return true;
        }
    }
    for (int i = 0; i < 3; i++) {
        chk = 0;
        for (int j = 0; j < 3; j++) {
            if (arr[j][i] == 'X') {
                chk++;
            }
        }
        if (chk == 3) {
            return true;
        }
    }

    if (arr[1][1] == 'X') {
        if ((arr[0][0] == 'X') && (arr[2][2] == 'X')) { // 대각
            return true;
        }
        else if ((arr[0][2] == 'X') && (arr[2][0] == 'X')) { // 대각
            return true;
        }
    }
    return false;
}

bool check_o() {
    int chk = 0;
    for (int i = 0; i < 3; i++) {
        chk = 0;
        for (int j = 0; j < 3; j++) {
            if (arr[i][j] == 'O') {
                chk++;
            }
        }
        if (chk == 3) {
            return true;
        }
    }
    for (int i = 0; i < 3; i++) {
        chk = 0;
        for (int j = 0; j < 3; j++) {
            if (arr[j][i] == 'O') {
                chk++;
            }
            else {
                chk = 0;
                break;
            }
        }
        if (chk == 3) {
            return true;
        }
    }

    if (arr[1][1] == 'O') {
        if ((arr[0][0] == 'O') && (arr[2][2] == 'O')) { // 대각
            return true;
        }
        else if ((arr[0][2] == 'O') && (arr[2][0] == 'O')) { // 대각
            return true;
        }
    }
    return false;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    while (true) {
        cin >> input;
        o_cnt = 0;
        x_cnt = 0;
        if (input == "end") {
            break;
        }
        else {
            for (int i = 0; i < 9; i++) {
                arr[i/3][i%3] = input[i];
                if (input[i] == 'O') {
                    o_cnt++;
                }
                else if (input[i] == 'X') {
                    x_cnt++;
                }
            }
        }
        if (!((x_cnt-o_cnt == 1) || (x_cnt - o_cnt == 0))) {
            cout << "invalid" << "\n";
            continue;
        }

        bool x = false;
        bool o = false;
        x = check_x();
        o = check_o();
        // 둘다 불가능한데 9개를 다 놨으면 valid
        if ((!x && !o) && (x_cnt + o_cnt == 9)) {
            cout << "valid" << "\n";
            continue;
        }
        else {
            // 동시에 성공 불가능
            if ((x && o) || (!x && !o)) {
                cout << "invalid" << "\n";
                continue;
            }
            // X가 3개가 연결되었을 경우
            // X의 수 = Y의 수 + 1 이어야한다.
            if (x && (x_cnt != (o_cnt+1))) {
                cout << "invalid" << "\n";
                continue;
            }

            // O가 3개 연결되었을 경우
            // X 수가 더 많으면 invalid
            if (o && (x_cnt > o_cnt)) {
                cout << "invalid" << "\n";
                continue;
            }
        }
        cout << "valid" << "\n";
    }
    return 0;
}