# ¡Hola Mundo! - Semana 1 <br/> Introducción a la Ciencia de la Computación

Queremos darte la bienvenida a este curso del lenguaje del programación Python.

Estas guías te acompañaran durante tu viaje, serán el material de apoyo que tendrás siempre a la mano, un complemento de las clases para ayudarte a recordar lo que irás aprendiendo, mantén siempre en mente que no tienes que realizar o leer la guía en un solo día, tomate tú tiempo.

En esta primera guía nos dedicaremos a a descargar y configurar (en muchos lados en vez de configurar verás la palabra *setear*) nuestro entorno de trabajo.


Pero antes hablemos un poco de los **sistemas operativos (OS).**

---

# Sistemas Operativos
Un sistema operativo es la base sobre la cuál instalamos los programas/aplicaciones y su trabajo es de servir de intermediario entre el *hardware* y las aplicaciones que usamos.

Vamos a verlo como los planos de un edificio.

El *Hardware* es como un edificio sin acabados, tiene las conexiones de luz, agua, tienes el piso pero en concreto puro, no hay llaves de agua, no hay interruptores, tampoco luces,  etc, es decir, no es habitable. 

 El *OS* es el mismo edificio pero con todos los acabados, tiene sus pisos, sus interruptores, sus luces etc. ¡Pero está vacío!
 ¿Para hacerlo habitable que podría faltar?
 
Necesita un amoblado que le de funcionaldiad y propósito al edificio, en nuestro caso aquí entran las *aplicaciones*.


Existen tres sistemas operativos dominantes en el mundo, y estos poseen detalles que pueden modificar la forma en que tendemos a programar, *casi nunca radicalmente*, pero hay detalles de los que debemos estar pendientes y que aprenderemos poco a poco.

Estos son:

 - Windows
 - MasOS
 - Y Linux


## Windows
Este sistema no necesita presentación, domina el mercado mundial de computadores personales, y si te gusta el gaming estas prácticamente obligado a tener Windows en tu computadora.

Ya que este **SO** está dirigido a un público general, no deja muy a la mano las herramientas de programación y su flexibilidad es poca, aunque su soporte es grande y la mayoría de las instalaciones están automatizadas.

## MacOs
El sistema operativo por excelencia de las computadoras de Apple, está inspirado en una familia de SO que se denominan **Unix**, una de la caracteristicas de la que hablaremos más adelante es de su poderosa terminal, con la cuál se instalan muchos programas.

Por su arquitectura y diseño el desempeño de las Macs es excelente y da mucha flexibilidad a los programadores.

## Linux
En realidad, Linux es lo que se denomina un *Kernel*, por lo cuál es en realidad una familia de SO (inspirados en Unix), está familia destaca por ser gratuita (casi siempre) y altamente personalizable. En el pasado se consideraba que solo los programadores más avanzados podía usar un SO Linux (¡y no sin razón!), pero hoy en día con distribuciones como Ubuntu, Pop_Os o Manjaro, entre muchos otros, usar un SO Linux está sencillo como usar Windows o MacOs.

Además, casi todos ya tienen preinstalado Python además de la terminal tan característica de estos sistemas.

---
![enter image description here](https://www.python.org/static/img/python-logo.png)
# Python v3 
Te hablamos de los *SO* porque estos van a definir como vas a instalar Python (entre otros detalles a futuro), ya que en cada sistemas es  distinto.

Primero que nada debes dirigirte a esta dirección: https://www.python.org/downloads/

Y seguir los pasos segun tu sistema operativo.

 - En Windows basta con bajar el instalador y ejecutarlo como cualquier otro programa que puedes descargar. Es posible que te pida que ejecutes como administrador.
 
 - MacOs aveces viene con Python preisntalado, asi que primero:
	 - Abre una terminal (En el Finder, abre la carpeta /Aplicaciones/Utilidades y, a continuación, haz doble clic en Terminal).
	 - Dentro de la terminal escribe: `python3 --version` (minúscula todo el comando)
	 - Si aparece algo como: `Python 3.xx.xx` (las **x** son números que pueden variar) significa que ya tienes el software .
	 - Si no aprece nada o aparece `Python 2.xx.xx`, deberás bajar la aplicación desde la página oficial e instalarla.
	 - 	 Cuando termien la instalación ingresa otra vez: `python3 --version` para asegurarte de que todo esté bien.

	 
 - En  Linux debes arbir una terminal con `Ctrl + t` y escribir `python3 --version`, y si aparece `Python 3.xx.xx`(las **x** son números que pueden variar) significa que ya tienes el software .
	 - De no aparecer el mensaje ingresa en la terminal: `sudo apt update`
	 -  Una vez terminado ingresa: `sudo apt install python3`
	 - Cuando termien la instalación ingresa otra vez: `python3 --version` para asegurarte de que todo esté bien.



### Paso extra para usuarios de Windows

Si lo sé, es un poco fastidioso que tengas un paso extra, pero como dijimos más arriba, Windows no está pensado en programadores.

 - En el buscador escribe "PowerShell", este emula (imita) las terminales Unix de MacOs/Linux (puede aparecer como Windows PowerShell).
 - Si no lo tienes dirigete aquí y sigue los pasos: https://learn.microsoft.com/es-es/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.3#winget

> **CUALQUIER PROBLEMA RECUERDEN CONSULTAR CON EL PROFESOR**

## Usemos Python

**Nota:** De ahora en más, cuando hablemos de "Terminal", los ususarios de Windows deben abrir el (Windows)PowerShell.

Abre una terminal e ingresa: `py` si eres usuario Windows o `python3` si eres usuario Unix.

Deberias tener un mensaje aprecido a este:

    Python 3.11.1 (main, Jan  6 2023, 00:00:00) 
    [GCC 12.2.1 20221121 (Red Hat 12.2.1-4)] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 
¿Ves esas tres flechas? 
`>>>`

Eso es un **prompt**, especificamente un prompt de Python, y simplemente indica que:

 1. Estás es un espacio vitual de Python, es decir, todo lo que escribas de ahí en más debe ser bajo las reglas de este lenguaje (ya las iremos viendo poco a poco).
 2. Está esperando algun tipo de comando de parte del usuario (es decir, espera a que tú le des una instrucción).

Ahora escribe en el promt: `print("hello world")` y presiona Enter.
Deberias verlo asi:

    >>> print("hello world")
    hello world



No parece muy útil ¿verdad?

Que tal ahora:

    >>> 472 * 195
¿Cuál fue el resultado?

Mejor, pero tampoco particularmente útil, es más fácil usar la calculadora de tu celular.

En la realidad, casi nunca usamos el entorno de Python de esta manera, pero nos sirve para hacer pequeños juegos que nos ayudan a concoer mejor este lenguaje, pero para programar de verdad necesitaremos editores de código.

-----
# Editores de Código

En realidad, son como los block de notas de Windows, y es que de hecho, podemos escribir código de cualquier lenguaje con block de notas, basta con cambiar la terminacion del archivo de .txt a .py (en el caso de python, en un lenguaje como JavaScript debe termianr en .js y en C# en .cs) para que se pueda ejecutar.

Sin embargo un editor moderno como VSCode y Sublime nos va a facilitar el trabajo al momento de escribir y debuggear nuestro código.

En general ambos son muy buenos y modernos, particularmente preferimos VSCode por ser más moldeable y tiene muchas extensiones que aumentan su funcionaldiad, pero eso viene con el coste de hacer este software más pesado.
Si tu computadora es muy vieja o está muy lenta te recomendamos que uses Sublime.

Finalmente no hay nada de malo con que experimentes con ambos editores y decidas cuál es mejor para ti.

Aquí te dejamos una conversación entre Lex Fridman y Guido Van Rossum (el creador de Python) sobre editores de código para Python: https://www.youtube.com/watch?v=G5mtQhWNezQ&ab_channel=LexClips

## VSCode

Este es un editor creado por Microsoft, increiblement popular y ligero. Su nombre es *Visual Studio Code* pero se abrevia como *VSCode* normalmente.
No lo llames Visual Studio, ese es un IDE, un editor altamente especializado, tambien de Microsoft, pero dedicado a un número particular de herramientas y puedes generar confusión.

VScode
![enter image description here](https://code.visualstudio.com/assets/docs/getstarted/tips-and-tricks/getstarted_page.png)

Para instalar, primero ve a https://code.visualstudio.com/

Descarga la app, y la instalas como instalaste Python si estas en Windows o  en Mac.

En Linux, las versiones más reciente tienden a funcionar tal cual Mac y Windows, pero puede ser que no dependiendo de tu distro. En dado caso descargas la app y en la carpeta de descargas con click derecho le das a *abirir en terminal/open in terminal* y ejecutas

```
sudo apt install code_1.xx.xx.deb
```
**Nota:** escribe el comando hasta la letra "c" de modo que quede coomo: `sudo apt install c` y presiona la tecla `tab`  de este modo se autcompleta el nombre del archivo.

 ### Configurando VSCode
Primero abre el VSCode y a la izquierda verás unos cuanto iconos, busca el que dice *extensiones/extensions* y te dará una barra de busqueda.

En esa barra escribe *python*, verás una extension del mismo nombre, abajo tendrá como una *estrella o lazo azul* que dice Microsoft y le das a instalar.

![enter image description here](https://www.mytecbits.com/wp-content/uploads/Visual-Studio-Code-For-Python-01-776x401.jpg)

Esta lo que hará será el indicarnos errores de código.

Luego busca e instala "indent-rainbow" y "Path Intellisense" para ayudas extras.

---

Ahora vamos a *Archivos/Files*-> *Preferencias/Preferences* -> *Configuración/Settings*.

En el buscador ingresa: "word wrap".  Y en la primera opción que aparece "Editor: Word Wrap" la colocas en "on".

![enter image description here](https://www.kindacode.com/wp-content/uploads/2020/10/Screen-Shot-2020-10-11-at-16.58.57.jpg)

Ahora ingesa "bracket pair colorization" en el buscador, y en la opción del mismo nombre asegurate que esté marcada.

Con esto estamos listos con VSCode.

## Sublime Text

Es quizas el otro gran editor de los que hay en el mercado, un poco menos potente que VSCode pero por lo mismo más rápido y ligero.

![enter image description here](https://www.sublimetext.com/screenshots/3.0/linux@2x.png)

Primero ve a su página oficial: https://www.sublimetext.com/

Descarga la app, y la instalas como instalaste Python si estas en Windows o  en Mac. 

En Linux debrás hacer varios pasos:

 1. Abrir una terminal.
 2. Ingresar `wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/sublimehq-archive.gpg > /dev/null`.
 3. Luego ingresas `echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list`.
 4. Después: `sudo apt update`
 5. Finalmente: `sudo apt install sublime-text` 

**Nota:** pregunta en la clase el significado de cada comando.

### Configurando Sublime Text
Abre Sublime Text y presiona en *Ver/View* y busca la casilla "Word Wrap" casi al final y asegurate que esté seleccionada.

Ahora en *Tools/Herramientas* -> *Command Palette/Paleta de Comandos*, haces click en la opcion en ingresas "python" y aparecerá  *"set sintax: Python"*, elige la opción.

¡Todo listo!

---

# !La Terminal!

Las Terminales Unix o Shell Unix son herraminetas poderosas que permite que tú, el usuario, pueda comunicarse de una manera muy directa con la computadora haciendo uso de pocos recursos de procesador y realizando las acciones rápidamente.

Las terminales tienen su propio Scripting (su propio lenguaje de programación) que se llama **bash**, aunque no lo vamos a aprender, si debemos concoer algunos comandos que nos van a ayudar un montón.

 1. Crea una carpeta en cualquier lado de tu escritorio, ponle el nombre que quieras, pero este *no debe contener espacios*.

 2. Entra en la carpeta y ya adentro abre una Terminal.
 
 3. Vamos a crear una nueva carpeta que se llame "esta_es_una_carpeta", pero la crearemos con la terminal usando el comando **mkdir**. `mkdir esta_es_una_carpeta` y presionas "enter".
	 3.1. **mkdir** viene de make directory (crear/hacer directorio) 
	 
 4. Deberias ver la carpeta nueva creada, para verla en la terminal usa el comando **ls**.
	 4.1. **ls** proviene de listing (listado)
	
 5. Vamos a crear un archivo de texto con el comando **touch**. Ingresa `touch mi_texto.txt`. Ahora usa el comando **ls**, ¿lo ves?.
 
 6. Ahora vamor a ir dentro de "esta_es_una_carpeta", usando el comando **cd**, en Unix ingresa `cd /esta_es_una_carpeta` en Windows  `cd \esta_es_una_carpeta`.
		 6. 1  **cd** viene de change directory (cambiar directorio)
		6. 2 En Windows las direcciones de los directorios o carpetas se indican con " \ " mientras que en Unix se hace con  " / ".
 7. Vamos a crear un archivo nuevo usando **touch**, `touch hello.py`. ¡¡¡Has creado tu primer archivo de Python!!!!
 8. Vamos a subir un niverl, usando `cd ..` **OJO**, no uses `cd`, asi sin los dos "." (puntos), ya que esto te llevará a la raíz de todo tu sistema. Si eso pasa, puedes abrir una nueva terminal donde quedamos.
 9. Vamos a eliminar el archivo "mi_texto.txt" usando el comando **rm**. Dejaré que deduscas lo que debes hacer.
	 9.1. **rm** es por remove (remover) 

 10. En este punto tu terminal debe verse algo desastrosa, vamos a limpiarla con el comando **clear**, así eliminamos toda esa info de la pantalla.
	 10.1 **clear** significa limpiar. 
 11. Para terminar puedes abrir todo el contenido usando VSCode con el comando `code .` (incluye el punto) o con Sublime usando `subl .` (también con el punto).

Las terminales Unix tienen muchisimos más comando y se pueden crear comandos propios para casi todo, pero de momento con los que tenemos más que suficiente.

 - **mkdir**
 - **ls**
 - **cd**
 - **touch**
 - **rm**
 - **clear**
 - **code/subl  .**

##### (En esta seccion puedes ver un poco de historia de las primreas terminales de computadora que existieron: https://www.youtube.com/watch?v=47NRaBVxgVM&t=11623s&ab_channel=freeCodeCamp.org)

---
 
![enter image description here](https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/180px-Python.svg.png)

# Volvamos a Python 
Como dijimos antes, Python es lo que se conoce como un lenguaje de programación, vamos a ver como funciona esto.

Las computadoras solo entienden un lenguaje, el binario, es decir, **1s** y **0s**, que vienen representados por cargas eléctricas en el hardware.

Cada peqeño detalle en tu computadora esta representado por una enorme cantidad de suceciones de ceros y unos, y si vamos a un nivel más arriba te daras cuenta que cada letra, color y forma está definido por números, por combinaciones de numeros para ser exactos.

Cada **0** o **1** se conoce como **bit** , un bit por si solo no nos sirve para representar información, por lo que la unidad mínima de información en computación se conoce como **BITE**.

Un BITE es un conjunto de 8 bits, y las letras, las imagenes, los sonidos y toda la información que puede recibir y procesar cualquier dispositivo electrónico maneja conjuntos de *n* cantidad de BITES.

Ahora un programa puede tener desde miles, a millones de BITES facilmente, piensa que una app que tenga un **GIGA BITE** exacto de informacion tendra **1.073.741.824 (mil millones / un millardo) de bytes**. 
¿Imaginas a alguien escribiendo manualmente cada uno de esos digitos?

Aunque la codificación directa en *0s* y *1s* se hizo con las primeras computadoras, en la medida que creció la complejidad de las mismas se inventó un nuevo lenguaje para reducir el trabajo, 
<br/> *** aquí viene una palabra clave **ABSTRACCIÓN**  ***

   

    En el mundo de la programación, podemos pensar en la abstracción como
    la condenzación o el empaqutamiento de muchos procesos que  se dirigen 
    a un fin determinado en un solo comando o instrucción.

<br/> este fue el **lenguaje máquina/assembler**, que permitió resumir todas esas secuencias númericas en comando mas pequeños, es decir, se crea una abstracción de las instrucciones y se ve (porque aun se usa) algo asi:

![enter image description here](https://miro.medium.com/max/640/1*kovZALFR8IG4Trvz3y4Fsw.webp)

Aunque es una gran mejora con respecto a series de ceros y unos, aún asi sigue siendo bastante complejo.

Finalmente llegaron los lenguajes de programación como tal, siendo quizas el más importante en la historia moderna el **Lenguaje C**. Entendamos en este caso para la idea de lenguaje, el hecho de que usamos palabras humanas (en inglés en el 99.99% de los casos) para dar instruccciones a la computadora.
Mira un ejemplo de **Lenguaje** C:
```c
    #include <stdio.h>
    
    int main()
    {
	    float number;
	    
	    printf("Give a number \n");
	    scanf("%f", &number);
	    printf("The value of number is: %.2f \n", number);
	    
	    return 0;
    }
    /*
    float = flotar/flotante
    print = imprimir
    scan = scanear
    f = resumen de la palabra function
    main = principal/central
    */
```
¡Ves! cada vez el lenguaje se vuelve más comprensible, cada instrucción resumen un montón de cosas que sería increiblemente largo y complejo de escribir en ensamblador y más aún en binario.

Python lleva la abstacción del código aún más lejos, vamos a verlo

  ```python
    print("Give a number ")
    number = int(input())
    print("The value of number is " + number)
```
Viste cuanto se redujo el código en Python, esto es parte de su belleza y elegancia, al reducir considerablemente el código y tener instrucciones muy precisas y claras.

## Hagamos un *Hello World!*

Por tradicón, el *Hello World!* es el primer programa que realizas cuando aprender un nuevo lenguaje, herramienta o framework. Su popularidad se debe a ser la primera frase de prueba que aparece en el libro "*El Lenguaje de Programación C" / "The C Programming Language*" de 1978 escrito por  Brian Kernighan y Dennis Ritchie, aunque nadie conoce el origen exacto de esta frase.

Vamos a usar la terminal, abrela en el escritorio y crea una carpeta (comando **mkdir**) y llamémosla "Hello_Word" (no uses caracteres especiales ni espacios).  Entra en la carpeta (comando **cd**/Hello_World ) ahora vamos a crear un archivo Python (comando **touch**) y llamemos al archivo  "hello_world.py", asegúrate que este ahí el archivo (usa el comando **ls**). Finalmente abrelo con el editor (**code .** o **subl .**).

Para crear este programa necesitamos uná función que viene por defecto en Python que se llama "*print*" y se escribe `print()` dentro de python.

 1. Escribe *Hello World!* entre los paréntesis.
 2. Corre el programa usando la terminal de la siguiente manera:
	 2 1	Si estas en Windows o Mac `py hello_world.py`
	 2.2 Linux `python3 hello_world.py `	
 
 Seguro te apareció algo así:
 ```python

    Traceback (most recent call last):
	    File "/home/FranSabt/Dev/sierra-vita-front/src/a.py", line 1, in <module>
	    print(hello_world)
          ^^^^^^^^^^^
    NameError: name 'hello_world' is not defined

```
¡Felicidades!  Tienes tu primer **BUG**

*Bug* es el termino que usamos para para referirnos  a errores de progrmación. ¿Por qué? Averigualo aquí: https://www.youtube.com/watch?v=5sNuPYJpSCI

Verás, para que imprima ese mensaje en la consola/terminal teníamos que rodear el mensaje entre comillas, simples o dobles, cualquiera de las dos maneras funciona.
```python
    print("Hello World!")
    print('Hello World!')
    
"""
En lo particular alentamos a los alumnos a usar la doble comillla, 
esto es porque en ciertos lenguajes de tipado fuerte como C++, C#, 
Java entre otros, la doble comilla indica un 
"string o cadena de caracteres"  y las comilla simple un dato tipo 
'char o caracter unico/aislado'.
"""
   ```
¡Verdad que ahora si!

Hagamos algo distinto

Realiza una suma, para esto usa el operador de suma `+`:
```python
    print("15 + 36")
   ```
Seguro obtuviste:
```bash
    1536
   ```       
Seguro te andas rascando la cabeza pensando que esto no tiene sentido.
Verás, todo es culpa de las comillas. Cuando las comillas rodean los carecteres los transforman en un tipo de dato que se llama `String` o *Cadena de Texto* o *Cadena de Caracteres* en español, para que operencomo numeros deben estar sin las comillas.
```python
    print(15 + 36)
   ```     
---
#### Si ya llegaste hasta aquí es un buen momento para un descanso.
---
# Control de Versiones



¿Has visto a alguien haciendo una Tesis?

Siempre hay como 10 archivos que se llaman "Tesis Final"
![enter image description here](https://pbs.twimg.com/media/Bx1ZBdHCUAAqPpr.jpg)

Y los programadores tuvieron este problema por mucho tiempo hasta que Linus Torval (padre del Linux Kernel) creo Git.

Git lo que hace es tomar como una foto de los cambios que vas realizando, y puedes tener distintas versiones en un mismo archivo sin que afecte el rendimiento del programa o la organización. 

Es un poco abstracto mentalmente hablando pero será más facil de entender con la práctica.

## Instalando Git 

Para Windows ve a esta dirección: https://git-scm.com/download/win
Y baja la versión de 64-bits.

Para Linux y MacOs primero abre una terminal e ingresa:
```bash
    git --version
```
Si obtienes:
````bash
    git version 2.39.1 (puede ser este número o superior)
````
Ya está intalado en tú máquina.

Si no:

Linux:
```bash
    sudo apt update
```
luego:
```bash
    sudo apt install git
```

En el caso de MacOs se puede complicar un poco , pide ayuda a tu profesor, pero si te sientes en confianza ve a esta página y sigue las instrucciones: https://www.atlassian.com/git/tutorials/install-git


### Para todos!!!
No olviden checar su version de Git con:

  ```bash
    git --version
```


---
## Configurando Git
Vamos a configurarlo rápidamente con estos comandos.
Vamos a añadir tu usuario y tu email:
```bash
git config --global user.name  "ActionCoders"
git config --global user.email "acoders@ac.com"
```

Ahora copia el siguiente:
`````bash
git config --global init.defaultBranch main
`````
El anterior es apra evitar conflictos con github.

Vamos a darle algo de color a git:

```bash
git config --global color.ui auto
```
Y para terminar:
```bash
git config --global pull.rebase false
```

Vamos a chequear tu usuario y tu email:
```bash
git config --get user.name
git config --get user.email
```

### !MacOs Alerta!
Usen un paso extra:
```bash
echo .DS_Store >> ~/.gitignore_global
git config --global core.excludesfile ~/.gitignore_global
```
Esto evitara que se guarden y suban unos archivos de seguiento que solo sirven en y para MacOs.


 

## GitHub

Si Git es la herramienta con la que haces videos, GitHub sería el Tiktok a donde los subes.

Es una especie de red social y almacén de proyectos, la idea no es subir programas completos, sino los scripts de los proyectos. Darle vida y movimiento a tu GitHub es de suma importancia, los desarrolladores profesionales son medidos en buena medida por sus aportes dentro de esta comunidad.

Primero que nada ve a https://github.com/ y abre una cuenta con el mismo correo que asociaste a Git.

Ahora vamos a asociar la cuenta de GitHub a Git.

En GitHub, busca el icono a la derecha, has click, y ve a *Settings*, ahora a la izquierda busca *SSH  and GPG keys* y has click, ahora has click en *New SSH Key*.

Aquí va la clave que vamos a crear:
![enter image description here](https://syntaxbytetutorials.com/wp-content/uploads/2019/07/githubssh-1024x530.png)



Vamos a crear una clave **ssh**, es una clave criptográfica que usa algoritmos complejos para proteger tu cuenta y tus archivos. Abre una terminal e ingresa:
```bash
ssh-keygen -t ed25519 -C <youremail>
```
Ahora usa este comando:
```bash
cat ~/.ssh/id_ed25519.pub
```
Deberia salir algo (reemplazamos una clave real por puras 'A' pero para ti serán como un montón de letras aleatorias seguido de tu correo):
```bash
ssh-aa55555 AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/AAAAAAAA 
actioncoders@actioncoders.com

```
   Vamos a probar la conexión:
   Ingresa:
   ```bash
ssh -T git@github.com
```

Deberías obtener:

```bash
> The authenticity of host 'github.com (IP ADDRESS)' can't be established.
> RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
> Are you sure you want to continue connecting (yes/no)?
```
Responde *yes* y debería decir ahora:
```bash
> Hi (Tú nombre se usuario)! You've successfully authenticated, but GitHub does not
> provide shell access.
```

Si te da un mensaje de error, descansa media hora y repite los pasos, si aún así persiste el problema contacta con tu profesor.


# Usemos Git

Primero que nada ve a tu GitHub, crea un nuevo repositorio, ve al ícono de tu perfil, *Your repositories*, y presiona en *New*. Siguiendo la tradición, vamos a llamarlo *Hello_World*.

Ahora Vamos a copiar la clave **ssh** de ese repo asi:
![enter image description here](https://cdn.statically.io/gh/TheOdinProject/curriculum/b54d14c5dcee1c6fac61aee02fca7e9ef7ba1510/foundations/git_basics/project_practicing_git_basics/imgs/02.png)

Crea una carpeta para nuestros proyectos. Lamamla como desees, y dentro de esa carpeta abre una terminal y vamos a usar el comando *git clone*.
```bash
git clone {aquí copias la clave ssh de GitHub}
```
Ahora crea un archivo *Hello_World.txt* (con la consola)

Vamos a ver cuál es el estado con el comando
```bash
git commit status"
```

![enter image description here](https://cdn.statically.io/gh/TheOdinProject/curriculum/b54d14c5dcee1c6fac61aee02fca7e9ef7ba1510/foundations/git_basics/project_practicing_git_basics/imgs/07.png)


Está en rojo porque no hemos iniciado el seguimiento del archivo, para eso debemos usar el comando:
```bash
git add .
```
Esto añade el archivo al seguimiento de Git.
Ahora usa el comando para darle una descripción:
```bash
git commit -m "{aquí debes escribir un mensaje pequeño}"
```

Si usas `git status` una vez más debería estar en verde.

Ahora subelo a GitHub con:
```bash
git push
```
¡¡¡Mira tú GitHub y ve que hay en el repo!!!
Estó será suficiente por ahora, demomento no debemos bajar ni configurar más nada pero puedes consultar esta guía tantas veces necesites.

## Vamos con Python
Antes que nada, crea una carpeta donde vamos a guardar todo el material de aquí en adelante.

Ve ha esta direción: https://github.com/FranSabt/PyEs_1

Y aariba a la derecha hay un botón que dice **Fork**, haz click ahí.
Esto va a generar un *Pull Request*, aceptalo  y tendŕa ti propia copia del repositorio.
![enter image description here](https://codeyourfuture.github.io/syllabus-london/others/assets/making-a-pull-request/fork-button.png)

Ahora ve a botón *< Code >* y copia la dirección **ssh**.

En la carpeta que creaste abre una terminal y escribe:
```bash
git clone {inserta aquí la derección ssh}
```
Verás que ahora tienes una carpeta con unos Script descargados.

Falta una última instalacion. Python por lo general viene con un módulo que se llama **pip** (python installing packaged), puedes verificarlo con el comando:

```bash
pip --version
```
De no tenerlo consulta al profesor.

Primero usa el comando (este solo lo vamos a usar una vez en todo el curso)
```bash
pip install virtualenv
```



En la carpeta donde se descargo el repositorio de GitHub usa el siguiente comando:
```bash
python -m venv env #Windows
#or
python3 -m venv env #Linux MacOS
```
Esto creará lo que se llama un *entorno virtual*, permitirá que nos libremos de problemas de versiones y compatibilidad. Viste que ahora hay una carpeta que se llama **env** (diminutivo de enviorement/entorno).

Debemos activar el entorno usando:


 ```bash
venv\Scripts\activate #Windows
#or
source venv/bin/activate #Linux MacOs 
```

Y el paso final:

```bash
pip install -r requirements.txt
```

Ahora todo esta listo para comenzar.


## Los ejercicios

Abre la carpeta **PyEs_1** con VSCode o Sublime.

Vamos a la carpeta ejecicios primero. Entra dentro de esa carpeta con la terminal, y usa el siguiente comando:

```bash
pytest
```
Verás que se ejecutaron varios tests, pasó uno y fallaron 14. El primer ejecicio dice asi:

```python
# Usa la funcion 'print()' para imprimir "Hello World!"
def hello():

	#Escribe la solución arriba de esta línea
	return
```

Acuerdate que la función **print( )**  sirve para motrar informacion en la terminal, en este caso debemos imprimir "Hello World!". Ahora, resulta que las computadoras no son muy listas, si imprimes "hello world!" o "Helllo World" no vas a pasar el test. Debes fijaste exatamente en que espera cada uno.


Ahora, la información de todos los test puede ser abrumadora, pero hay un truco para hacerlo más simple. Ves que la funcion se llama  *def **hello** ()*, pues los test se llaman como el nombre de la función (la parte en negrita) con **test_** delante del nombre.

Por lo que el test de la función *hello* se llama **test_hello**, usa el nombre con el siguiente comando.

    pytest -k test_hello
Ahora solo corrió el test de la función hello.
Por tanto si despues tenemos la funcion **suma**, debemos llamas a su test **test_suma** y usamos el comando: *pytest -k {nombre_del_test}*

El area de Error en color rojo indica la respuesta que se espera.

Sigue con los ejercicios y apoyate en tus compañeros.

## Las operaciones matemáticas

 - La suma y la resta se hacen con los signos `+ y -`. 
 - La multiplicación    `*`. 
 - La división `/`. 
 - División redondeada hacia abajo `//`, por    ejemplo 7 entre 2 da 3.5 normalmente, pero con este operador solo    dará 3 ya que fue redondeado. 
 - El residuo `%`, es el sobrante que    queda al ir dividiendo por números enteros, volviendo al ejemplo de 7    entre 2, queda un sobrante de valor 1 que no puede ser operado sin    número reales.
Hay otros detalles sobre las operaciones que aprenderemos más adelante.

Finalmente, cada vez que hagas un pequeño progreso usa estos comandos.

    git add . #para cuardar un snap de tu progreso
Despues:

    git commit -m "{un pequeño comentario aquí}"
Finalmente:

    git push
Para que quede grabado en tu GitHub
