# Projeto Python Inventory Report! :bar_chart:
Projeto desenvolvido por mim durante o curso de Desenvolvimento Web na Trybe. Divulgado aqui como portfólio de aprendizado.

<details>
<summary><strong>Objetivos do projeto:</strong></summary>
 
  * Desenvolver um gerador de relatórios. Deve receber arquivos contendo informações sobre um estoque e produzir um relatório abrangente com base nesses dados.
  * Verificar se sou capaz de:
    * Aplicar conceitos de Programação Orientada a Objetos em Python.
    * Implementar leitura e escrita de arquivos CSV e JSON em Python.
</details>
<details>
<summary><strong> Requisitos do projeto:</strong></summary>

  *  Eliminar o(s) bug(s) da função `show_deepest_file`.
  *  Eliminar o(s) bug(s) da função `find_file_by_name`.
  *  Criar testes para a função `show_preview`.
  *  Criar testes para a função `show_details`.
  *  Criar testes para a função `show_disk_usage`.
  *  Criar testes para a função `find_duplicate_files`.
</details>
  
## Rodando o projeto localmente

Para rodar o projeto em sua máquina, abra seu terminal, crie um diretório no local de sua preferência com o comando `mkdir` e acesse o diretório criado com o comando `cd`:

```bash
mkdir meu-diretorio &&
cd meu-diretorio
```

Clone o projeto com o comando `git clone`:

```bash
git clone git@github.com:marcosadrianoti/tb-python-inventory-report.git
```

Acesse o diretório do projeto com o comando `cd`:

```bash
cd tb-python-inventory-report
```

crie o ambiente virtual:
```bash
python3 -m venv .venv
```

Ative o ambiente virtual:
```bash
source .venv/bin/activate
```

Instale as dependências no ambiente virtual:
```bash
python3 -m pip install -r dev-requirements.txt
```
Configure o auto-complete da aplicação com o comando `pro-filer --install-completion` e reinicie o terminal.

Execute o comando pro-filer seguido de --help para obter orientação como usar a aplicação:
```bash
pro-filer --help
```
Execute os testes com:
```bash
python3 -m pytest
```
