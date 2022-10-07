#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
#define ordered_set tree<int, null_type, less_equal<int>, rb_tree_tag, tree_order_statistics_node_update>
#define int long long
using namespace std;
#define Y cout << "YES\n";
#define N cout << "NO\n";
// this works as multiset,for erasing dont directly erase use iterater and find that by upper bound not lower as they act vice versa here.
// find by order: returns number present at kth pasition with 0 based indexing
// syntax=> int j=*s.find_by_order(3);  j stores 4th element present in the ordered set.
// order of key: return number of elements strictly smaller than the given element
// syntax: int j=s.order_of_key(5); returns number of elements smaller than 5;
#define endl "\n"
#define lowestbit(x) __builtin_ffs(x)           // returns 1+index of(lowest bit)
#define numberofbits(x) __builtin_popcountll(x) // returns number of set bits
#define highestbit(x) __builtin_clz(x)          // returns number of 0's to left of MST
#define is(x) cerr << #x << " is " << x << "\n";
#define full(v1) v1.begin(), v1.end()
#define pb push_back
#define loop(i, a, b) for (int i = (a); i < (b); i++)
#define inputarr loop(i, 0, n) cin >> ar[i];
int mod = 1e9 + 7;
int inf = 9e18;
int mx = -1;
int mn = 9e18;
int calpow(int x, int y, int md)
{
    int res = 1;

    x = x % md;
    if (x == 0)
        return 0;

    while (y > 0)
    {
        if (y & 1)
            res = ((res % md) * (x % md)) % md;
        y = y >> 1;
        x = ((x % md) * (x % md)) % md;
    }

    return res;
}
/*vector<int> fac(3e5 + 5);
vector<int> inv(3e5 + 5);
int j;
void facm()
{
  fac[0] = 1;
  loop(i, 1, 300002)
  {
    fac[i] = ((i) % mod * fac[i - 1]) % mod;
  }
  inv[300001]=calpow(fac[300001],mod-2,mod);
  for(int i=300000;i>=0;i--)
  {
     inv[i]=((i+1)*inv[i+1])%mod;
  }
}
int ncr(int n, int r, int mod)
{
  if(r>n)
  return 0;
  return ((fac[n]*inv[r])%mod*inv[n-r])%mod;
}*/
/*vector<int> v;
bool p[32004];
void pre()
{
  for (int i = 2; i <= 32000; i++)
  {
    if (!p[i])
    {
      v.pb(i);
      for (int j = i * i; j <= 32000; j += i)
        p[j] = 1;
    }
  }
}*/
void solve()
{
    int i, j, n, t, q, a, b, m, k, ct = 0, sum = 0, flag = 0;
    //Printing hello world in my very own standard template
    cout<<"Hello World!";
}
signed main()
{
    // freopen("lineup.in","r",stdin);
    // freopen("lineup.out","w",stdout);
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    // WATCH FOR SAME VARIABLE USAGE CLEARLY!!!
    // MAKE SURE TO MAKE A DUPLICATE OF ANYTHING IF PERFORMING OPERATION DIRECTLY ON SOMETHING !!!
    int t = 1;
    // cin>>t;
    while (t--)
    {
        solve();
        cout << "\n";
    }

    cerr << clock() * 1000.0 / CLOCKS_PER_SEC << 'm' << 's';
    return 0;
}
