#include <stdio.h>
#include "fatorial.h"

int* fatorial_1_svc(operando *a, struct svc_req *r){
	static int resultado;
	printf("Recebi requisicao resolver o fatorial de %d \n", a->x);
	resultado = a->x;
	return (&resultado);
}
