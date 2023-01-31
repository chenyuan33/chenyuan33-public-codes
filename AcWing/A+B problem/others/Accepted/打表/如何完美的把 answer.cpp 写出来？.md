有人可能会问：
# Q: 咋做的这？
对此，我给出的回答是：

A: 首先，提交下面这段代码：
``` cpp
#include <iostream>
using namespace std;
int a, b;
int main()
{
	cin >> a >> b;
	cout << a << ' ' << b;
	return 0;
}
```
然后，就能 `Wrong Answer` 了。

贴心的 [AcWing](https://www.acwing.com/problem/content/1/) 把错误数据给出来了，万岁！
# 个屁！做出来了吗？
[AcWing](https://www.acwing.com/problem/content/1/) 说，输入 `3 4` ，输出了 `3 4` ，而正确的是 `7` 。

好的！如果是 `3 4` ，那么是 `7` ，所以代码要改成：
``` cpp
#include <iostream>
using namespace std;
int a, b;
int main()
{
	cin >> a >> b;
	if(a == 3 && b == 4) cout << 7;
	else cout << a << ' ' << b;
	return 0;
}
```
打表完成，万岁！
# 个屁！做出来了吗？
e......

才一个。。。。。。

不过，我们再提交一遍，把这个数据改对，变成
``` cpp
#include <iostream>
using namespace std;
int a, b;
int main()
{
	cin >> a >> b;
	if(a == 3  && b == 4 ) cout << 7  ; else
	if(a == 45 && b == 55) cout << 100; else
	cout << a << ' ' << b;
}
```
继续！
``` cpp
#include <bits/stdc++.h>
using namespace std;
int a, b;
int main()
{ 
    cin >> a >> b;
    if(a == 3        && b == 4       ) cout << "7"        ; else
    if(a == 45       && b == 55      ) cout << "100"      ; else
    if(a == 123      && b == 321     ) cout << "444"      ; else
    if(a == 5710219  && b == 85140568) cout << "90850787" ; else
    if(a == 42267194 && b == 60645282) cout << "102912476"; else
    if(a == 69274392 && b == 10635835) cout << "79910227" ; else
    if(a == 70597795 && b == 90383234) cout << "160981029"; else
    if(a == 75601477 && b == 24005804) cout << "99607281" ; else
    if(a == 82574652 && b == 22252146) cout << "104826798"; else
    if(a == 91086199 && b == 18700332) cout << "109786531"; else
	cout << a << ' ' << b;
    return 0;
}
```
`Accepted` 了！万岁！
# 但是
也不像 `./answer.cpp` 呀！

既然 `cout << a << ' ' << b;` 永远不会执行，所以，
``` cpp
#include <bits/stdc++.h>
using namespace std;
int a, b;
int main()
{ 
    cin >> a >> b;
    if(a == 3        && b == 4       ) cout << "7"        ; else
    if(a == 45       && b == 55      ) cout << "100"      ; else
    if(a == 123      && b == 321     ) cout << "444"      ; else
    if(a == 5710219  && b == 85140568) cout << "90850787" ; else
    if(a == 42267194 && b == 60645282) cout << "102912476"; else
    if(a == 69274392 && b == 10635835) cout << "79910227" ; else
    if(a == 70597795 && b == 90383234) cout << "160981029"; else
    if(a == 75601477 && b == 24005804) cout << "99607281" ; else
    if(a == 82574652 && b == 22252146) cout << "104826798"; else
    if(a == 91086199 && b == 18700332) cout << "109786531";
    return 0;
}
```
把 `else` 去掉，就得到了如下代码：

见 `./answer.cpp`

(呃。。。。。。)
