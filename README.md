# LED -  Bancos de Dados na Prática

### Setup do Ambiente

- De preferência que tenha o python >3.12 instalado.
- Configuração do Docker para rodar as instâncias do Redis e Postgres localmente.

Recomenda-se criar um ambiente virtual, `vitualenv` para essa prática, pois a instalação dos pacotes será referente a esse ambiente e não global.

```bash
python -m venv venv
```

#### Criando os containers

Vá para a pasta específica em que você quer realizar os testes (`/sql` ou `/nosql`) e rode o comando para subir os containers necessários.

```bash
docker compose up
```