# ATENÇÃO

**PRÉVIA**: ainda não foi atualizado para 2022/2.


# Introdução

Neste trabalho, vamos juntar todas as camadas que implementamos até agora e depois testar o funcionamento em uma rede física real!


# Por que o grupo é de até 8 pessoas?

Para vocês terem a liberdade de testar várias implementações diferentes de P1, P2, P3 e P4, afinal esse trabalho consiste em juntar as diversas camadas.

As implementações não precisam estar perfeitas para funcionarem em conjunto:

 * Teoricamente, uma implementação de TCP passando até o teste do Passo 3 é suficiente para estabelecer uma conexão, trocar dados e comprovar o funcionamento. Uma implementação de TCP passando até o teste do Passo 4 deve funcionar quase perfeitamente, pois a nossa camada física é bastante confiável e tem probabilidade baixíssima de perder ou corromper pacotes.

 * Uma implementação de IP passando até o teste do Passo 3 deve funcionar bem se você não alterar as tabelas de encaminhamento fornecidas (se alterar, o Passo 4 é importante para evitar loops de roteamento). Você só vai precisar do Passo 5 do IP se quiser testar o mtr ou traceroute.

No entanto, a implementação de vocês pode ter erros que, por azar, não foram exercitados pelos testes automatizados. Portanto, dica valiosa: testem todas as combinações possíveis de implementações dos seus integrantes, até funcionar.


# Por que a Zybo Z7-20 e não um PC?

Nós configuramos a Zybo Z7-20 para disponibilizar 8 interfaces seriais em cada placa. Assim, conseguimos montar redes usando uma camada física simples e fácil de entender.

![](fig/portas.jpg)


# Configuração sugerida


![](fig/diagrama.svg)


# Orientações gerais

Como o ambiente é compartilhado, algumas **orientações gerais muito importantes**:

 * Antes de começar a trabalhar, observe se não há ninguém usando aquela placa naquele momento (use o comando `w`). Se tiver alguém usando, tente olhar as placas da outra mesa.

 * Se você usa `tmux` ou `screen`, não deixe nenhuma sessão detachada ao terminar de usar a placa, para deixar claro que aquela placa está livre.

 * Crie um diretório para o seu grupo trabalhar.

 * Não bisbilhote o diretório dos outros grupos.


# Instruções

Copie para o diretório do seu grupo, em cada placa, os arquivos:

 * [tcputils.py](https://github.com/thotypous/redes-t2-grader/blob/main/tcputils.py)
 * [iputils.py](https://github.com/thotypous/redes-t3-grader/blob/main/iputils.py)
 * [camadafisica.py](camadafisica.py)
 * Os arquivos `tcp.py`, `ip.py` e `slip.py` que vocês implementaram no P2, P3 e P4.

Copie também o executável principal que você vai executar em cada placa, respectivamente:

 * [placa1.py](placa1.py)
 * [placa2.py](placa2.py)
 * [placa3.py](placa3.py)

Execute o executável principal em cada placa.

Na placa 1, você vai ter que executar, em outros terminais (sem matar o Python!), alguns comandos que o executável principal vai indicar. Obs.: é normal aparecer uma vez a mensagem `BlockingIOError: [Errno 11] Resource temporarily unavailable` depois de executar o `slattach`.

Teste se o servidor de eco está funcionando: conecte-se a ele a partir da placa 1 executando:
```
nc 192.168.200.4 7000
```

Se tiver problemas, pode ser útil fazer algumas simulações locais (veja os arquivos `exemplo_integracao.py` que foram fornecidos ao longo dos trabalhos anteriores), pois é mais fácil depurar localmente do que nas placas.

Uma vez com o servidor de eco funcionando, edite o arquivo `placa3.py` e tente inserir sua implementação de camada de aplicação do P1 (servidor de IRC).
