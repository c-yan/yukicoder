#include <bits/stdc++.h>
using namespace std;
using ll = long long;

ll isqrt(ll n) {
    ll ok = 0;
    ll ng = 3037000500;
    while (ng - ok > 1) {
        ll m = ok + (ng - ok) / 2;
        if (m * m <= n) {
            ok = m;
        } else {
            ng = m;
        }
    }
    return ok;
}

int main() {
    ll A, B;
    cin >> A >> B;

    ll X = gcd(A, B);

    if (isqrt(X) * isqrt(X) == X) {
        cout << "Odd" << endl;
    } else {
        cout << "Even" << endl;
    }

    return 0;
}
