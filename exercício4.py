"""
1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior
"""
numero1: int = int(input("Informe o primeiro número: "))
numero2: int = int(input("Informe o segundo número: "))


if numero1 > numero2:
    print(f"0 número {numero1} eh maior que {numero2}")
elif numero1 == numero2:
    print(f"0s números {numero1} e {numero2} são inguais.")
else:
    print(f"0 número {numero2} é maior que {numero1}")