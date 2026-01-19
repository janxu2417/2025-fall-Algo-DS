#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> prm;
vector<bool> is_prm(3170, true);
vector<int> d1, d2;
unordered_map<int, pair<int, int>> dic;

void divide(int x) {
    int y = x;
    bool flag = false;
    // 检查是否已经计算过
    if (dic.find(x) != dic.end()) {
        d1.push_back(dic[x].first);
        d2.push_back(dic[x].second);
        return;
    }
    
    // 尝试分解质因数
    for (int i : prm) {
        if (i * i > x) break;
        if (y % i == 0) {
            int tmp = 1;
            while (y % i == 0) {
                y /= i;
                tmp *= i;
            }
            if (tmp == x) continue;
            dic[x] = make_pair(tmp, x / tmp);
            d1.push_back(tmp);
            d2.push_back(x / tmp);
            flag = true;
            break;
        }
    }
    // 如果无法分解，标记为-1,-1
    if (!flag) {
        dic[x] = make_pair(-1, -1);
        d1.push_back(-1);
        d2.push_back(-1);
    }
}

int main() {
    int n;
    cin >> n;
    
    vector<int> a(n);
    for (int i = 0; i < n; ++i) 
        cin >> a[i];
    
    // 生成质数表（埃拉托斯特尼筛法）
    for (int i = 2; i < 3170; ++i) {
        if (is_prm[i]) {
            prm.push_back(i);
        }
        for (int j : prm) {
            if (i * j >= 3170) break;
            is_prm[i * j] = false;
            if (i % j == 0) break;
        }
    }
    
    for (int x : a)
        divide(x);
    
    for (int i : d1)
        cout << i << " ";
    cout << endl;
    
    for (int i : d2)
        cout << i << " ";
    return 0;
}
