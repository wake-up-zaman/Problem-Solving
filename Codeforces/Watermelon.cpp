#include<bits/stdc++.h>
using namespace std;

int main(){
    int num;
    int sum;
    cin>>num;
    sum=num/2;
    if(num != 2 && num%2 == 0){     
        cout<<"YES";  
    }
    else{
        cout<<"NO";
    }
    return 0;
}