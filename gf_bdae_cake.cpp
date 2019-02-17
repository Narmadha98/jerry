#include<iostream>
using namespace std;
int main()
{
int n,m;
cin>>n>>m;
char a[n][m],b[n][m],c[n][m];
for(int i=0;i<n;i++){
    for(int j=0;j<m;j++){
        if ((i+j)%2==0){
                a[i][j]='R';
                b[i][j]='G';
        }
        else{
            a[i][j]='G';
            b[i][j]='R';
        }
           cin>>c[i][j];
        }
    }
    int c1=0,c2=0;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++){
                if(c[i][j]=='R' && a[i][j]=='G')
                    c1=c1+5;
                if(c[i][j]=='G' && a[i][j]=='R')
                    c1=c1+3;
                if(c[i][j]=='R' && b[i][j]=='G')
                    c2=c2+5;
                if(c[i][j]=='G' && b[i][j]=='R')
                    c2=c2+3;

        }
    }
    if(c1<c2)
        cout<<c1;
    else
        cout<<c2;
}
