#include <iostream>

using namespace std;

int existeInvOuOpp(int T[])
{
    int i, j;
    for(i=0;i<10;i++)
    {
        for(j=1;j<10;j++)
        {
            if(T[i]!= T[j])
            {
                if((T[i]+T[j])== 0 || (T[i]*T[j])==1)
                {
                    cout<<"True"<<endl;
                }else
                {
                    cout<<"False"<<endl;
                }
            }
        }
    }
}

int main()
{
    int i, t[100];
    cout<<"Entrez les nombre que contiendra le tablau: "<<endl;
    for(i=0;i<10;i++)
    {
        cin>>t[i];
    }
    cout<<endl;
    existeInvOuOpp(t);
    return 0;
}
