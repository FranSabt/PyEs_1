from ejercicios import *
import random

def test_hello(capsys):
    hello()
    stdout, stderr = capsys.readouterr()
    assert stdout == "Hello World!\n"

def test_saludo(capsys):
    saludo()
    stdout, stderr = capsys.readouterr()
    saludos = ["Hello\n", "Buenas\n", "Buen Día\n", "Aloha\n", "holis\n", "holiwiss\n", "hablame\n"]
    assert stdout in saludos


def test_string(capsys):
    string()
    stdout, stderr = capsys.readouterr()
    assert len(stdout) >= 20

def test_string2(capsys):
    string2()
    stdout, stderr = capsys.readouterr()
    assert len(stdout) >= 20 and len(stdout) < 30




def test_suma():
    assert suma(55, 44) == 99
    a = random.randint(0,100)
    b = random.randint(0,100)
    assert suma(a, b) == a + b
    a = random.randint(-100,100)
    b = random.randint(-100,100)
    assert suma(a, b) == a + b


def test_suma_negativa():
    assert suma_negativa(55, 44) == -99
    a = random.randint(0,100)
    b = random.randint(0,100)
    assert suma_negativa(a, b) == (a + b) * -1
    a = random.randint(-100,100)
    b = random.randint(-100,100)
    assert suma_negativa(a, b) == (a + b) * -1


def test_resta():
    assert resta(55, 44) == 11
    a = random.randint(0,100)
    b = random.randint(0,100)
    assert resta(a, b) == a - b
    a = random.randint(-100,100)
    b = random.randint(-100,100)
    assert resta(a, b) == a - b

def test_resta_invertida():
    assert resta_invertida(55, 44) == -11
    a = random.randint(0,100)
    b = random.randint(0,100)
    assert resta_invertida(a, b) == b - a
    a = random.randint(-100,100)
    b = random.randint(-100,100)
    assert resta_invertida(a, b) == b - a

def test_multiplicacion():
    assert multiplicacion(7, 5) == 35 
    a = random.randint(0,100)
    b = random.randint(0,100)
    assert multiplicacion(a, b) == a * b
    a = random.randint(-100,100)
    b = random.randint(-100,100)
    assert multiplicacion(a, b) == a * b


def test_division():
    assert division(125, 5) == 25 
    a = random.randint(0,100)
    b = random.randint(0,100)
    assert division(a, b) == a / b
    a = random.randint(-100,100)
    b = random.randint(-100,100)
    assert division(a, b) == a / b

def test_division_entera():
    assert division_entera(125, 5) == 25 
    a = random.randint(0,100)
    b = random.randint(0,100)
    assert division_entera(a, b) == a // b
    a = random.randint(-100,100)
    b = random.randint(-100,100)
    assert division_entera(a, b) == a // b

def test_modulo():
    assert modulo(125, 5) == 0
    a = random.randint(1,100)
    b = random.randint(1,100)
    assert modulo(a, b) == a % b
    a = random.randint(-100,100)
    b = random.randint(-100,100)
    assert modulo(a, b) == a % b

def test_potencia():
    assert potencia(5) == 25 
    a = random.randint(1,100)
    assert potencia(a) == a * a
    a = random.randint(1,100)
    assert potencia(a) == a * a

def test_de_negativo_a_positivo():
    assert de_negativo_a_positivo(-5) == 5 
    a = random.randint(1, 100)
    a = a * -1
    assert de_negativo_a_positivo(a) == -1 * a
    a = random.randint(1,100)
    assert de_negativo_a_positivo(a) == -1 * a

def test_de_positivo_a_negativo():
    assert de_positivo_a_negativo(5) == -5 
    a = random.randint(1, 100)
    assert de_positivo_a_negativo(a) == -1 * a
    a = random.randint(1,100)
    assert de_positivo_a_negativo(a) == -1 * a


