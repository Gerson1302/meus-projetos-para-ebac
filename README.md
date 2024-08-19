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
