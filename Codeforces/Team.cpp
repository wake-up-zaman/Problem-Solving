#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n,p,v,t;
    int sum;
    int count=0;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>p>>v>>t;
        sum=p+v+t;
        if(sum>=2){
        count++;
    }
    }
    cout<<count;
    
    return 0;
}