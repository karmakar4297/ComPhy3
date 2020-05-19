#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <fftw3.h>
#define pi 3.1415926535
int n=128;
float func(float);
float gunc(float); 




int main()
{ 
	int i;
	float xmin=-20,xmax=20,dx,fft[n],karr[n],trfft[n];
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
	fp = fopen("prob2out.txt","w");
	fftw_execute(plan); 

	for(i=0;i<n;i++) 
	{ 
		fft[i]=dx*sqrt(1.0/(2.0*pi))*(cos(-xmin*karr[i])*out[i][0]-sin(-xmin*karr[i])*out[i][1]);
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
float func(float x)
{ 
	if(x==0.0)
		return 1.0;
	else
		return sin(x)/x;
}

float gunc(float x) 
{ 
	if (x<=1&&x>=-1)
		return sqrt(pi/2.0);
	else
		return 0.0;
}
	
