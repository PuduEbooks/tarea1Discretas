#include <stdio.h>

 void kioskito(int X, int coins[], int k)
{
	int j = k;
	int c = 0;
	do
	{
		if (X - coins[j-1] >= 0){
			c++;
			X = X-coins[j-1];
		}
		else // Se dejan de entregar monedas del mismo valor, se dice cuantas se entregaron
			// Y se resetea el contador
		{
			printf("%d moneda%s de %d peso%s\n", c,
				 c==1 ? "" : "s", coins[j-1], coins[j-1]==1 ? "" : "s");
			if(!X) break; //Si X es 0, terminar
			c = 0;
			j--;
		}
	} while(true);
	return;
}

int main()
{	
	int k;
	printf("Ingrese número de monedas: ");
	scanf("%d", &k);
	int coins[k];
	coins[0] = 1;
	int i;
	for(i = 1; i<k; i++)
	{
		printf("Ingrese valor de moneda numero %d: ", i+1);
		scanf("%d", &coins[i]);
	}
	int X;
	printf("Ingrese el valor del vuelto\n");
	scanf("%d", &X);
	printf("Para dar el vuelto se usan\n");
	kioskito(X, coins, k);
}