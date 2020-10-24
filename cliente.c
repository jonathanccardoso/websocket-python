#include <stdio.h>
#include "fatorial.h"

int fatorial(CLIENT *c, int x) {
	operandos o;
	int *resultado;
	o.x = x;
	resultado = fatorial_1(&o, c);

	if(resultado == NULL){
		printf("problemas ao chamar operacao remota\n");
		exit(1);
	}

	return (*resultado);
}

int main(int argc, char *argv[]) {
	CLIENT *c = clnt_create(argv[1], FATORIAL_PROG, "udp");
	int x;
	if (argc != 4) {
		fprintf(stderr, "USO: %s endereco <numero1> <numero2>\n", argv[0]);
		exit(1);
	}
	if (c == (CLIENT *)NULL) {
		clnt_pcreateerror(argv[1]);
	}

	x = atoi(argv[2]);
	printf("%d! = %d \n", x, fatorial(c, x));
	return(0);
}
