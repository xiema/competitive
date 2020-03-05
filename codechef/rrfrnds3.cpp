#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef string st;
typedef vector<int> vi;
typedef vector<vi> vii;
typedef vector<pii> vpii;
typedef vector<long long> vll;
typedef vector<vll> vlll;
typedef vector<st> vs;

const int           mod = 1e9 + 7;
#define infi        inf++;assert(inf<mod)
#define pb          push_back
#define mp          make_pair
#define fori(i,a,b) for(int i = (a); i <= (b); i++)
#define ford(i,a,b) for(int i = (a); i >= (b); i--)
#define test        int t; cin >> t; while(t--)
#define debug(x)    cout << '>' << #x << ':' << x << "\n";
#define endl        '\n'
#define off         ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define ip(x)       int x;cin>>x;
#define ip1(x,y)     int x,y;cin>>x>>y;
#define pp          cout<<
#define nl          <<endl
#define sort(v)     sort(v.begin(),v.end())
#define lmax(a,b)   a>b?a:b
#define lmin(a,b)   a<b?a:b
#define mem(array,val,m,n)      memset(array, val, sizeof(array[0][0]) * m * n);

int main() {

	off;
	ll ans = 0;
	ip(n);
	vi v[n];
	string arr[n + 1];
	for (int i = 0; i < n; i++)
		cin>>arr[i];

	for (int i = 0; i < n; i++)
	{
		for (int j = i + 1; j < n; j++)
		{
			if (arr[i][j] == '1')
			{
				v[i].pb(j);
				v[j].pb(i);
			}
		}
	}
	for (int i = 0; i < n; i++)
	{
		for (int j = i + 1; j < n; j++)
		{
			if (arr[i][j] == '0')
			{
				for (int k = 0; k < (int)v[i].size(); k++)
				{
					if (arr[v[i][k]][j] == '1')
					{
						ans += 2;
						break;
					}
				}
			}
		}
	}
	cout << ans << endl;
	return 0;

}
