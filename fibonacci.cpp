#include<iostream>
using namespace std;

int fibonaccis(int n) {
    if(n==0)
    return 0;
    else if(n==1)
    return 1;
    else {
        return(fibonaccis(n-1)+fibonaccis(n-2));
    }
}
int main() {
    int n;
    cout<<"\nEnter no. of element of fibonacci series : ";
    cin>>n;
    for(int i=0;i<n;i++) {
        cout<<fibonaccis(i)<<" ";
    }
    return 0;
}