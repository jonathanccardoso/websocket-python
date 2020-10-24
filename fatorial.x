#define NUMERO_PROGRAMA 1234
#define VERSAO_PROGRAMA 2

struct operando{
	int x;
};

program FATORIAL_PROG{
	version FATORIAL_VERSION{
		int SOMA(operando) = 1;
	} = VERSAO_PROGRAMA;
} = NUMERO_PROGRAMA;
