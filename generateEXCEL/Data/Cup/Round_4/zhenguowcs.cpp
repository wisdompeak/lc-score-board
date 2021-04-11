#include<iostream>
using namespace std;
using ll = long long;

ll a, b, n;
int cnt;

int f(ll n, ll a, ll b)
{
//	printf("calculating: f(%lld, %lld, %lld)\n", n, a, b);
//	if(++cnt == 10) exit(0);
	if(!a) return 1000;
	if(a + b > n + 1) return f(n, n + 1 - a, n + 1 - b);
	if(a > b) swap(a, b);
	if(b > n / 2)
	{
		if(a + b == n + 1) return 1;
		if(a + b < n) return 2;
		ll m = (n + 1) / 2;
		return 1 + min(f(m, (a + 1) / 2, m - a / 2), f(m, (a - 1) / 2, m - 1 - a / 2));
	}
	else
	{
		ll m = (n + 1) / 2;
		if(m > a + b) return 1 + f(m, a, b);
		else if(m == a + b) return 1 + min(f(m, a, b), f(m, a - 1, b + 1));
		if(m == a + b - 1 || b > a + 1 || m % 2 == 0) return 2;
		return 1 + f(m, (m + 1)/2, (m + 3)/2);
	}
}

int g(ll n, ll a, ll b)
{
	if(a + b > n + 1) return g(n, n + 1 - a, n + 1 - b);
	if(a > b) swap(a, b);
	ll m = (n + 1) / 2;
	if(b > n / 2)
	{
		if(a + b == n + 1) return 1;
		else return 1 + g(m, 1, b + 1 - n / 2);
	}
	else return 1 + g(m, 1, 2);
}

void test()
{
	for(int i = 1; i <= 11; ++i) for(int j = 1; j <= 11; ++j) if(i != j)
		printf("%d, %d :%d %d\n", i, j, f(11, i, j), g(11, i, j));
}

int main()
{
	scanf("%lld%lld%lld", &n, &a, &b);
//	test();
	printf("%d %d\n", f(n, a, b), g(n, a, b));
}
