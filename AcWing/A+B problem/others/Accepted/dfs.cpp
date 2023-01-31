#include <iostream>
#include <math.h>
using namespace std;
#define safe 116
// safe 再小点的话...... Memory Limit Exceeded
int a, b;
int dfs(int x)
{
    if(x < 0)
    {
        return 0 - dfs(abs(x));
    }
    if(x == 0)
    {
        return dfs(x + dfs(1)) - dfs(1);
    }
    if(x < safe)
    {
        return x;
    }
    return dfs(x - safe) + safe;
}
int main(){
    cin >> a >> b;
    cout << dfs(dfs(a) + dfs(b));
    return dfs(0);
}
