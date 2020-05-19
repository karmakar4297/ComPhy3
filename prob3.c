#include <stdio.h>
#include <math.h>
#include <gsl/gsl_errno.h>
#include <gsl/gsl_fft_complex.h>
#define pi 3.1415926535
#define REAL(z,i) ((z)[2*(i)])
#define IMAG(z,i) ((z)[2*(i)+1])
int n=128;
double func(float);
double gunc(float); 

int main (void)
{
	int i;
	double xmin=-20,xmax=20,dx,fft[n],karr[n],trfft[n],in[2*n],out[2*n];
	FILE *fp;

	dx=(xmax-xmin)/(double)(n-1);

	for(i=0;i<n;i++)	
	{
		REAL(in,i) = func(xmin+dx*i); 
		IMAG(in,i) = 0.0;
		REAL(out,i) = func(xmin+dx*i); 
		IMAG(out,i) = 0.0;
	}

	gsl_fft_complex_radix2_forward(out, 1, n); 

	for (i=0;i<n/2;i++)
	{   
		karr[i]=2.0*pi*i/((double)n*dx);
		fft[i]=dx/sqrt(2.0*pi)*(cos(karr[i]*xmin)*REAL(out,i)-sin(karr[i]*xmin)*IMAG(out,i));
	}
	
	for (i=n/2;i<n;i++)
	{    
		karr[i]=2.0*pi*(i-n)/(n*dx);
		fft[i]=dx/sqrt(2.0*pi)*(cos(karr[i]*xmin)*REAL(out,i)-sin(karr[i]*xmin)*IMAG(out,i));
	}



	fp=fopen("prob3out.txt","w");

	for(i=0;i<n;i++)
	{
		trfft[i]=gunc(karr[i]);
	}
	for(i=n/2;i<n;i++)
		fprintf(fp,"%f, %f, %f\n", karr[i],fft[i],trfft[i]);
	for (i=0;i<n/2;i++)
		fprintf(fp,"%f, %f, %f\n", karr[i],fft[i],trfft[i]);
		
	fclose(fp);

return 0;
}

double func(float x)
{ 
	if(x==0.0)
		return 1.0;
	else
		return sin(x)/x;
}

double gunc(float x) 
{ 
	if (x<=1&&x>=-1)
		return sqrt(pi/2.0);
	else
		return 0.0;
}

