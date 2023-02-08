from debug import *
from math import pow



def test_hello(capsys):
	hello()
	stdout, stderr = capsys.readouterr()
	assert stdout == "Hello World!\n"


def test_hola(capsys):
	hola()
	stdout, stderr = capsys.readouterr()
	assert stdout == "Hola mundo!\n"

def test_monty_python(capsys):
	monty_python()
	stdout, stderr = capsys.readouterr()
	assert stdout == "'Are you suggesting coconuts migrate?'\n"


def test_suma():
	assert suma(234, 769) == 1003


def test_otra_suma():
	assert otra_suma(2, 40) == 42


def test_sum2():
	assert sum2(57, 49) ==  106


def test_multiplicacion():
	assert multiplicacion(23, 71) == 1633


def test_division():
	assert division(7, 1.5) == 4.666666666666667


def test_otra_division():
	assert otra_division(7, 4) == 1


def test_elevado_al_cubo():
	assert elevado_al_cubo(4.5) == pow(4.5, 3)


def elevado_al_cuadrado():
	assert elevado_al_cuadrado(9) == 81