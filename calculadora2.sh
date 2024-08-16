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
