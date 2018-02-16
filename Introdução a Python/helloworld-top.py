#!/usr/bin/env python

# aqui importamos os módulos utilizados -- sys é um bem importante!
import sys

# Todo o código da função main()
def main():
    print ('Hello there', sys.argv[1])
    # Os argumentos da linha de comando estão em sys.argv[1], sys.argv[2] ...
    # sys.argv[0] é o nome do script, pode ser ignorado

# Como SEMPRE chamar a função main
if __name__ == '__main__':
    main()