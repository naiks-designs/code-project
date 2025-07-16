#include<stdio.h>
#include<string.h>
int main() {
char str1[50],str2[50];
int i=0,same=0,len1=0, len2=0;
printf("enter the first string:");
gets(str1);
printf("enter the second string:");
gets(str2);
len1=strlen(str1);
len2=strlen(str2);
if(len1==len2)
{
while(i<len1)
{
if(str1[i]==str2[i])
	i++;
else break;
}
}
if(i==len1)
{	same=1;
	printf("two string are equal\n");
	}
	if(len1!=len2)
	
		printf(" strings are not equal\n");
	if(same==0);
	{
if(str1[i] > str2[i])  
printf(" string 1 is greater than string two\n");
else  if (str1[i] < str2[i])
printf(" string 1 is smaller than string two\n");
	}
	return 0;
}
