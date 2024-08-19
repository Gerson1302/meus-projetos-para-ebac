# meus-projetos-para-ebac
 tudo que foi feito no curso da ebac 
Passo a Passo para Executar o Script:
1. Criar o Arquivo Script
Abra o terminal no seu sistema.
Crie um arquivo de script com o seguinte comando
nano calculadora2.sh
Cole o seguinte código dentro do arquivo
#!/bin/bash
echo "Escolha uma operação:"
echo "1. Adição"
echo "2. Subtração"
echo "3. Multiplicação"
echo "4. Divisão"
read operacao
echo "Digite o primeiro número:"
read num1
echo "Digite o segundo número:"
read num2

case $operacao in
    1) resultado=$((num1 + num2));;
    2) resultado=$((num1 - num2));;
    3) resultado=$((num1 * num2));;
    4) resultado=$((num1 / num2));;
    *) echo "Operação inválida"; exit 1;;
esac

echo "O resultado é: $resultado"
Salve o arquivo e feche o editor (no nano, aperte CTRL+O para salvar e CTRL+X para sair).
Tornar o Arquivo Executável
No terminal, execute o comando abaixo para dar permissão de execução ao arquivo:
chmod +x calculadora.sh
 Executar o Script
Agora, execute o script digitando o seguinte comando
./calculadora2.sh
Interagir com o Script
Após executar o script, ele pedirá para que você escolha uma operação:
Escolha uma operação:
1. Adição
2. Subtração
3. Multiplicação
4. Divisão
Digite o número correspondente à operação desejada (por exemplo, 1 para adição) e pressione Enter.
Depois, ele pedirá os dois números que deseja operar
Digite o primeiro número:
Digite o primeiro número e pressione Enter.
Digite o segundo número:
Digite o segundo número e pressione Enter
Ver o Resultado
O script calculará e exibirá o resultado da operação
O resultado é: X

Aqui está o passo a passo para executar o código bash que você forneceu. Esse código é um script simples para realizar operações matemáticas básicas, como adição, subtração, multiplicação e divisão.

Passo a Passo para Executar o Script:
1. Criar o Arquivo Script
Abra o terminal no seu sistema.
Crie um arquivo de script com o seguinte comando:
bash
Copiar código
nano calculadora.sh
Cole o seguinte código dentro do arquivo:
bash
Copiar código
#!/bin/bash
echo "Escolha uma operação:"
echo "1. Adição"
echo "2. Subtração"
echo "3. Multiplicação"
echo "4. Divisão"
read operacao
echo "Digite o primeiro número:"
read num1
echo "Digite o segundo número:"
read num2

case $operacao in
    1) resultado=$((num1 + num2));;
    2) resultado=$((num1 - num2));;
    3) resultado=$((num1 * num2));;
    4) resultado=$((num1 / num2));;
    *) echo "Operação inválida"; exit 1;;
esac

echo "O resultado é: $resultado"
Salve o arquivo e feche o editor (no nano, aperte CTRL+O para salvar e CTRL+X para sair).
2. Tornar o Arquivo Executável
No terminal, execute o comando abaixo para dar permissão de execução ao arquivo:
bash
Copiar código
chmod +x calculadora.sh
3. Executar o Script
Agora, execute o script digitando o seguinte comando:
bash
Copiar código
./calculadora.sh
4. Interagir com o Script
Após executar o script, ele pedirá para que você escolha uma operação:
bash
Copiar código
Escolha uma operação:
1. Adição
2. Subtração
3. Multiplicação
4. Divisão
Digite o número correspondente à operação desejada (por exemplo, 1 para adição) e pressione Enter.
Depois, ele pedirá os dois números que deseja operar:
bash
Copiar código
Digite o primeiro número:
Digite o primeiro número e pressione Enter.
bash
Copiar código
Digite o segundo número:
Digite o segundo número e pressione Enter.
5. Ver o Resultado
O script calculará e exibirá o resultado da operação.
bash
Copiar código
O resultado é: X
Exemplo de Execução:
Escolha a operação:

Digite 1 para adição e pressione Enter.
Insira o primeiro número:

Digite 10 e pressione Enter.
Insira o segundo número:

Digite 5 e pressione Enter.
O script retornará:
O resultado é: 15
Com isso, você terá executado o script com sucesso!
