#define NUMERO_PROGRAMA 123
#define VERSAO_PROGRAMA 1

struct operandos{
	int x;
	int y;
};

program SOMA_SUB_PROG{
	version SOMA_SUB_VERSION{
		int SOMA(operandos) = 1;
		int SUBTRACAO(operandos) = 2;
	} = VERSAO_PROGRAMA;
} = NUMERO_PROGRAMA;
