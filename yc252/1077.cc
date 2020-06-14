#include <cstdio>
#include <vector>
#include <algorithm>
#define rep(i, a) for (int i = (int)0; i < (int)a; ++i)
template<class T> inline void chmin(T& a, T b) { if (a > b) { a = b; } }
using ll = long long;
using namespace std;

int main()
{
	ll N;
	scanf("%lld", &N);
	vector<ll> Y(N), a(N);
	rep(i, N) {
		scanf("%lld", &Y[i]);
		a[i] = Y[i];
	}
	sort(a.begin(), a.end());
	a.erase(unique(a.begin(), a.end()), a.end());
	vector<ll> dp(a.size(), 0);
	rep(i, N){
		ll t = 1LL << 60;
		rep(j, a.size()){
			chmin(t, dp[j] + abs(Y[i] - a[j]));
			dp[j] = t;
		}
	}
	printf("%lld\n", *min_element(dp.begin(), dp.end()));
	return 0;
}
