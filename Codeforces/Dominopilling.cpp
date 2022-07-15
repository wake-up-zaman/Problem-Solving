#include<iostream>
using namespace std;

int main(){
    int n,m;
    int sum=0;
    int np=0;
    cin>>m>>n;
    if(n>=m){
        sum=m*n;
        np=sum/2;
        
        cout<<np;
        }
    
    return 0;
}