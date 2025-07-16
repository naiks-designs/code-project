#include<stdio.h>
int main()
{
	int a[100],n,i,j,temp;
	printf(" enter the size of array");
	scanf("%d",&n);
	printf(" enter the array elements");
	for (i=0;i<n;i++)
	scanf("%d",&a[i]);
	for(j=0;j<n;j++)
	{
		for(i=0;i<n-i-j;i++)
		{
			if (a[i] > a[i+1]);
			{
			
			temp=a[i];
			a[i]=a[i+1];
			a[i+1]=temp;
			
		}
	}
}
printf(" sorted list in ascending oder\n");
for(i=0;i<n;i++)
printf("%d\t",a[i]);
return 0;
}
