#include <stdio.h>
#include "calculadora.h"

int soma(CLIENT *c, int x, int y){
	operandos o;
	int *resultado;
	o.x = x;
	o.y = y;
	resultado = soma_1(&o, c);
	if(resultado == NULL){
		printf("problemas ao chamar operacao remota\n");
		exit(1);
	}

	return (*resultado);
}

int subtracao(CLIENT *c, int x, int y){
	operandos o;
	int *resultado;
	o.x = x;
	o.y = y;
	resultado = subtracao_1(&o, c);
	if(resultado == NULL){
		printf("problema ao chamar a funcao remota \n");
		exit(1);
	}

	return (*resultado);
}

int main(int argc, char *argv[]){
	CLIENT *c = clnt_create(argv[1], SOMA_SUB_PROG, SOMA_SUB_VERSION, "udp");
	int x, y;
	if(argc != 4){
		fprintf(stderr, "USO: %s endereco <numero1> <numero2>\n", argv[0]);
		exit(1);
	}
	if(c == (CLIENT *)NULL){
		clnt_pcreateerror(argv[1]);
	}
	x = atoi(argv[2]);
	y = atoi(argv[3]);
	printf("%d + %d = %d \n", x, y, soma(c, x, y));
	printf("%d - %d = %d \n", x, y, subtracao(c, x, y));
	return(0);
}
