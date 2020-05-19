#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <fftw3.h>
#define pi 3.1415926535
int n=512;
float func(double);
float gunc(double); 




int main()
{ 
	int i;
	float xmin=-100,xmax=100,dx,fft[n],karr[n],trfft[n];
	fftw_complex in[n], out[n];
	fftw_plan plan;
	plan=fftw_plan_dft_1d(n,in,out,FFTW_FORWARD,FFTW_ESTIMATE);
	
	dx=(xmax-xmin)/(float)(n-1);

	for (i=0;i<n;i++)
	{
		if(i<n/2)
			karr[i]=pi*2.0*(float)i/(float)n/dx;
		else
			karr[i]=pi*2.0*(float)(i-n)/(float)(n)/dx;
		in[i][0]=func(xmin+dx*(float)i);
		in[i][1]=0.0; 
	}

	FILE*fp;
	fp = fopen("prob4out.txt","w");
	fftw_execute(plan); 

	for(i=0;i<n;i++) 
	{ 
		fft[i]=dx*sqrt(1.0/(2.0*pi))*(cos(xmin*karr[i])*out[i][0]-sin(xmin*karr[i])*out[i][1]);
		trfft[i]=gunc(karr[i]);
	}
	for (i=n/2;i<n;i++)
		fprintf(fp,"%f, %f, %f\n", karr[i],fft[i],trfft[i]);
		
	for (i=0;i<n/2;i++)
		fprintf(fp,"%f, %f, %f\n", karr[i],fft[i],trfft[i]);
		
	fclose(fp);
	fftw_destroy_plan(plan);
	return 0;
}

float func(double x) 
{
	return exp(-x*x);
}

float gunc(double x)
{ 
	return exp(-x*x/4.0)/sqrt(2.0);
}	
