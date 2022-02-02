## Linus

Desenvolvido em 1991 por Linux Torvalds na Finlândia quando terminava 
sua graduação em ciência da computação, e não satisfeito com o os sistemas 
operacionais da época que eram PAGOS (MAC, UNIX, ...) ou puramente acadêmico 
(Minix)

  - https://en.wikipedia.org/wiki/Linux
  - https://en.wikipedia.org/wiki/Linus_Torvalds
  - https://pt.wikipedia.org/wiki/MINIX

Resolveu criar um sistema operacional do zero, baseado em UNIX e seguindo o livro 
de um de seus professores: Andrew S. Tanenbaum, que era a base do minix porém liberado
apenas para complementar o livro.

  - https://en.wikipedia.org/wiki/Andrew_S._Tanenbaum
  - livro: https://www.amazon.com/Operating-Systems-Design-Implementation-3rd/dp/0131429388
  - https://images-na.ssl-images-amazon.com/images/I/61rSUrfS5HL._SX384_BO1,204,203,200_.jpg
  
> UNIX? Define a arquitetura do sistema operacional, as APIS e estrutura do kernel

> Fato: Unix + Linus = Linux!

## Primeira versão

Aos 21 anos, Linus terminou a primeira versão do OS e publicou em uma lista de mensagens (não 
tinha forum/ e-mail/ ... na época, essas listas eram o começo) a seguinte mensagem:

>Hello everybody out there using minix -
>
>I'm doing a (free) operating system (just a hobby, won't be big and professional like gnu) for 386(486) AT clones. This has been brewing since april, and is starting to get ready. I'd like any feedback on things people like/dislike in minix, as my OS resembles it somewhat (same physical layout of the file-system (due to practical reasons) among other things).
>
>I've currently ported bash(1.08) and gcc(1.40), and things seem to work. This implies that I'll get something practical within a few months, and I'd like to know what features most people would want. Any suggestions are welcome, but I won't promise I'll implement them :-)
>
>Linus (torvalds@kruuna.helsinki.fi)
>
>PS. Yes - it's free of any minix code, and it has a multi-threaded fs. It is NOT portable (uses 386 task switching etc), and it probably never will support anything other than AT-harddisks, as that's all I have :-(.
> 
> — Linus Torvalds

- https://en.wikipedia.org/wiki/History_of_Linux

## GNU

Um dos fatores que deu força para o sistema operacional recém lançado foi que ele foi
desenvolvido utilizando ferramentas de outro projeto importante o GNU,
que estava ganhando força na mesma época e fornecia uma série
de programas gratuitos para a comunidade, ele também introduziu o conceito de "Software Livre"
e licença open source. Conduzido por Richard Stallman no MIT.

- https://en.wikipedia.org/wiki/GNU_Project
- https://pt.wikipedia.org/wiki/Richard_Matthew_Stallman

O Linux como conhecemos hoje em dia é também conhecido como Linux/GNU, pois faz uso
extensivo dos dois projetos (compiladores, editores de texto, ...). Inclusive, a versão
0.99 o linux já foi publicado utilizando a licença GNU GPL.

## GPL

A licença GNU GPL (GNU General Public License) possui os seguintes princípios:

1. A liberdade de executar o programa, para qualquer propósito (liberdade nº 0)
1. A liberdade de estudar como o programa funciona e adaptá-lo às suas necessidades (liberdade nº 1). O acesso ao código-fonte é um pré-requisito para esta liberdade.
1. **A liberdade de redistribuir cópias de modo que você possa ajudar ao seu próximo (liberdade nº 2).**
1. **A liberdade de aperfeiçoar o programa e liberar os seus aperfeiçoamentos, de modo que toda a comunidade beneficie deles (liberdade nº 3). O acesso ao código-fonte é um pré-requisito para esta liberdade.**

- https://pt.wikipedia.org/wiki/GNU_General_Public_License

> Não podemos confundir software livre com software gratuito (como o google por exemplo).

## Mascote - Tux

Em 1996 Linux anuncia o novo mascote para o Linux, um pinguim! Torvalds faz muitos mergulhos
como hoobie, e diz ele que foi mordido por um pinguim na visita a um aquário. 

- https://duckduckgo.com/?q=linux+mascote&t=canonical&iax=images&ia=images&iai=http%3A%2F%2F4.bp.blogspot.com%2F-c8uUx6EnHv8%2FVo7_P8mUt4I%2FAAAAAAAACEw%2FeKA-7sjxGak%2Fs400%2FTux%252Bmascote%252Bdo%252Blinux.png

## Distribuições 

No começo os softwares não eram distribuídos junto com o Linux, o desenvolvedor tinha que 
instalar e compilar tudo o que queria utilizar, e a coisas eram dispersas. Foi ai que 
surgiu a ideia de distribuir um pacote com o kernel do linux + alguns programas + configurações
básicas. A distribuição mais antiga e ainda em 'uso' é o SlackWare.

- https://www.cyberciti.biz/tips/wp-content/uploads/2007/06/44218-linuxdistrotimeline-7.2.png
- http://www.slackware.com/

## Ubuntu

Ubuntu foi criado em 2004 pelo empresário sul africano Mark Shuttleworth com o foco de
disponibilizar uma distribuição para todos os usuários (desktop + server) e não apenas com
foco empresarial como as demais distribuições.

- https://en.wikipedia.org/wiki/Mark_Shuttleworth
- https://en.wikipedia.org/wiki/Ubuntu

O Ubuntu é baseado em outra distribuição, o Debian, que teve sua origem muito antes em 1993.
Os pacotes `.deb` foram criados por essa distro.

## distro hopping

Achar uma distribuição que te agrade é muito difícil, o distro hopping é o ato de ficar
mudando de distribuição toda hora, instalando tudo novamente e então, mudando de distro
novamente.

- https://www.quora.com/What-is-distro-hopping-as-regards-Linux

## linux != Distro != Ambiente de desktop

O linux em si é apenas o kernel, o core do sistema operacional, porém hoje me dia poucas
pessoas utilizam apenas o bash no desktop. Muitas vezes o Linux é associado apenas a interface
gráfica, que alias tem para todos os gostos!

- https://pt.wikipedia.org/wiki/Ambiente_de_desktop
- (padrão atual do ubuntu) https://www.gnome.org/
- https://kde.org/
- https://ubuntubudgie.org/
- (pantheon) https://elementary.io/
- https://en.wikipedia.org/wiki/LXDE
- https://linuxmint.com/

## Linux atualmente

- https://www.youtube.com/watch?v=yVpbFMhOAwE
- https://www.youtube.com/watch?v=SOXeXauRAm0&list=PLbzoR-pLrL6rsb1bc3En9zaEor9S0gyIp
- https://www.youtube.com/watch?v=rSjgVeNQrN0&list=PLbzoR-pLrL6rsb1bc3En9zaEor9S0gyIp&index=2

## git?

Até 2005 o linux utilizava um sistema privado de gerenciamento de versão privado, Linus tirou uma semana de férias e nasceu o git!
