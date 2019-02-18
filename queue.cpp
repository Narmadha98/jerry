#include<iostream>
using namespace std;
void swap1(int *x,int *y){
    int temp=*x;
    *x=*y;
    *y=temp;
}
void sortb(int a[],int n){
    for(int i=0;i<n-1;i++){
        for(int j=0;j<n-i-1;j++){
            if(a[j]>a[j+1])
                swap1(&a[j],&a[j+1]);
        }
    }
}
int main(){
     int n,sum=0,c=0;
     cin>>n;
     int a[n];
     for(int i=0;i<n;i++)
        cin>>a[i];
     sortb(a,n);
    for(int i=0;i<n;i++)
    {   sum=0;
        for(int j=0;j<i;j++)
            sum+=a[j];
        if(sum<=a[i])
            c+=1;
    }
    cout<<c;
}
