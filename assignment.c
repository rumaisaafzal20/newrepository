#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

int array[1000];
void* SumOfArray (void *argument);

int main()
{
  void* sum[10];
  int total=0;
  int i;

  for (i=0 ; i<1000 ; i++)
  {
	array[i]=i;
  }

  pthread_t thread[10];

  pthread_create(&thread[0],NULL,SumOfArray,(void*)0);

  pthread_create(&thread[1],NULL,SumOfArray,(void*)100);

  pthread_create(&thread[2],NULL,SumOfArray,(void*)200);

  pthread_create(&thread[3],NULL,SumOfArray,(void*)300);

  pthread_create(&thread[4],NULL,SumOfArray,(void*)400);

  pthread_create(&thread[5],NULL,SumOfArray,(void*)500);

  pthread_create(&thread[6],NULL,SumOfArray,(void*)600);

  pthread_create(&thread[7],NULL,SumOfArray,(void*)700);

  pthread_create(&thread[8],NULL,SumOfArray,(void*)800);

  pthread_create(&thread[9],NULL,SumOfArray,(void*)900);
 
  int j;
  for (j=0 ; j<10 ; j++)
  {	
	pthread_join (thread[j],&sum[j]);
  }

  int k;
  for (k=0 ; k<10 ; k++)
  {
	total=total+(int)sum[k];
  }


  printf("TOTAL SUM IS = %d ",total);
 
  return 0;
}

void* SumOfArray (void * argument)
{
  int sum=0;
  int size=(int)argument;

  int i;
  for (i=size ; i<size+100 ; i++)
	sum=sum+array[i];

  return (void*)sum;
}


