// First Come First Serve Scheduling Algorithm 
#include<stdio.h>
#include<conio.h>
#define max 30
void main()
{
    int i,j,n,bt[max],at[max],wt[max],tat[max],temp[max];
    // i and j are looping variables
    // n is the number of process
    // bt is the burst time
    // at is the arrival time
    // wt is the waiting time
    // tat is the turn around time
    // temp is a temporary variable
    float awt=0,atat=0;
    // awt is the average waiting time
    // atat is the average turn around time

    printf("Enter the number of process: ");
    scanf("%d",&n);
    printf("Enter the burst time of the process: ");
    for(i=0;i<n;i++)
           scanf("%d",&bt[i]);
    printf("Enter the arrival time of the process: ");
    for(i=0;i<n;i++)
           scanf("%d",&at[i]);
    temp[0]=0;
    printf("PROCESS\t BURST TIME\t ARRIVAL TIME\t WAITING TIME\t TURN AROUND TIME\n");
    for(i=0;i<n;i++)
    {
        wt[i]=0;
        tat[i]=0;
        temp[i+1]=temp[i]+bt[i];
        wt[i]=temp[i]-at[i];
        tat[i]=wt[i]+bt[i];
        awt=awt+wt[i]; // this will give us just the sum of all waiting time
        atat=atat+tat[i];
        printf("%d\t\t%d\t\t%d\t\t%d\t\t%d\n",i+1,bt[i],at[i],wt[i],tat[i]);
    }            
awt=awt/n;
atat=atat/n;
printf("Average waiting time: %f\n",awt);
printf("Average turn around time: %f",atat);
getch();
}







