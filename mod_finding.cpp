#include <iostream>
#include <map>
using namespace std;
map<int,int> arr;
int main(){
    int a,b,n;
    cin >> a >> b >> n;
    int s;
    arr[1]=a%n;
    for (int i=2;i<=b;i=i*2){
        arr[i]=(arr[i/2]*arr[i/2])%n;
        s=i;
    }
    int k=b;
    int mod=1;
    for (int i=s;i>=1;i=i/2){
        if (k/i==1){
            mod*=arr[i];
            k=k%i;
        }
    }
    cout << mod%n << endl;

}