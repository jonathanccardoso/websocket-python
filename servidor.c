#include <stdio.h>
#include "calculadora.h"

int* soma_1_svc(operandos *a, struct svc_req *r){
	static int resultado;
	printf("Recebi requisicao de soma %d %d\n", a->x, a->y);
	resultado = a->x + a->y;
	return (&resultado);
}


int* subtracao_1_svc(operandos *a, struct svc_req *r){
	static int resultado;
	printf("Recebi requisicao de subtracao %d %d \n", a->x, a->y);
	resultado = a->x - a->y;
	return (&resultado);
}
