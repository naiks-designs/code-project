#include<stdio.h>
#include<math.h>
int main(){
float a,b,c,r1,r2,d,imag,real;
printf("enter values for a,b,c");
scanf("%f %f %f",&a,&b,&c);
d=b*b-4*a*c;
if(d == 0)
{
	printf("\nroots are real and equal\n");
	r1=-b/(2*a);
	r2=-b/(2*a);
	printf("\nroot 1=%f and root 2=%f",r1,r2);
}
 else if(d>0)
{

	printf("\nroots are real and distinct\n");
	r1=(-b+sqrt(d))/(2*a);
	r2=(-b-sqrt(d))/(2*a);
	printf("\nroot 1=%f",r1);
	printf("\nroot 2=%f",r2);
}


else 
	
{




real=-b/(2*a);
imag =sqrt(-d)/(2*a);
printf(" root 1=%f+i%f and root 2=%f-i%f\n",real,imag,real,imag);
}
return 0;
}
