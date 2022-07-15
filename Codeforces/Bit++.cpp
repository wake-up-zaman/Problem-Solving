#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    int x=0;
    cin>>n;
    string k;
    //char a[1]={'+'};
    for(int i=0;i<n;i++){
        cin>>k;
        if(k[1]=='+'){
            x++;

        }
        else{
            x--;
        }
    }
    cout<<x;
    return 0;


}