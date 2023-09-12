# Instruções para Executar o Dockerfile com Jupyter Notebook

Este README fornece um guia passo a passo sobre como construir uma imagem Docker a partir do Dockerfile e executar um contêiner com Jupyter Notebook. Isso permitirá que você acesse o Jupyter Notebook em sua máquina local.

## Passo 1: Build da Imagem Docker

Certifique-se de que o Docker esteja instalado em sua máquina. Se não estiver, você pode obtê-lo em [https://www.docker.com/get-started](https://www.docker.com/get-started).

1. Navegue até o diretório onde o seu Dockerfile está localizado.

2. Abra um terminal e execute o seguinte comando para construir a imagem Docker:

```bash
docker build -t desafio_final_tsp .
```

## Passo 2: Execução do Contêiner

Após ter construído a imagem com o nome `desafio_final_tsp`, você pode executar um contêiner a partir dessa imagem para iniciar o Jupyter Notebook. Certifique-se de que você já tenha concluído o Passo 1 (Build da Imagem Docker) antes de prosseguir.

3. Para executar o contêiner, utilize o seguinte comando:

```bash
docker run -d --name jupyterserver -p 8888:8888 desafio_final_tsp
```

- O `-d` executa o contêiner em segundo plano.
- `--name jupyterserver` atribui um nome ao contêiner (neste caso, "jupyterserver").
- `-p 8888:8888` mapeia a porta do host 8888 para a porta do contêiner 8888.
- `desafio_final_tsp` é o nome da imagem Docker que você construiu no Passo 1.

## Passo 3: Acessar o Jupyter Notebook

4. Para acessar o Jupyter Notebook, você precisará obter o token de acesso gerado. Você pode fazer isso exibindo os logs do contêiner com o seguinte comando:

```bash
docker container logs jupyterserver
```


5. Os logs mostrarão uma URL semelhante à seguinte:
```bash
http://127.0.0.1:8888/?token=c8719e2f1c4361b2a8c899e8c10793f7e4bf293726b655b7
```


## Download do HTML Interativo

Baixe o HTML interativo gerado pelo codigo em sua propria maquina para poder acessá-lo.
