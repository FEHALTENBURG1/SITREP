# Classificador de Risco — SITREP · SDS UnB

Aplicação interativa para classificação de risco em contexto de SITREP, adaptada para publicação no **Streamlit Community Cloud**.

O projeto utiliza um arquivo HTML completo e interativo (`SITREP_CLASS.html`) carregado dentro de um aplicativo Streamlit (`app.py`). Essa estratégia preserva o layout, os estilos e a lógica em JavaScript da aplicação original.

## Estrutura dos arquivos

```text
sitrep_classificador_streamlit/
├── app.py
├── SITREP_CLASS.html
├── requirements.txt
└── README.md
```

## Arquivos principais

### `SITREP_CLASS.html`

Arquivo principal da interface. Contém a estrutura visual, estilos CSS e lógica interativa em JavaScript do classificador.

### `app.py`

Arquivo usado pelo Streamlit para carregar e exibir o HTML interativo.

### `requirements.txt`

Lista mínima de dependências necessárias para publicação.

## Como rodar localmente

1. Instale o Streamlit:

```bash
pip install -r requirements.txt
```

2. Execute o aplicativo:

```bash
streamlit run app.py
```

3. O navegador abrirá automaticamente com a aplicação.

## Como publicar no Streamlit Community Cloud

1. Crie um repositório no GitHub.

2. Envie estes arquivos para o repositório:

```text
app.py
SITREP_CLASS.html
requirements.txt
README.md
```

3. Acesse o Streamlit Community Cloud.

4. Clique em **New app**.

5. Selecione o repositório criado.

6. Em **Main file path**, informe:

```text
app.py
```

7. Clique em **Deploy**.

## Observações importantes

- O arquivo `SITREP_CLASS.html` deve permanecer na mesma pasta do `app.py`.
- Não renomeie o HTML sem alterar também a linha correspondente no `app.py`.
- A aplicação é renderizada dentro de um componente HTML do Streamlit.
- A altura do componente está configurada em `3200`. Caso a tela fique cortada ou com excesso de rolagem, ajuste este trecho no `app.py`:

```python
components.html(
    html_content,
    height=3200,
    scrolling=True,
)
```

## Requisitos

- Python 3.9 ou superior
- Streamlit

## Uso recomendado

Esta aplicação pode ser usada para apoio à sistematização de análise de risco em boletins, relatórios situacionais e processos de triagem de eventos, preservando uma interface simples para usuários sem necessidade de programação.

## Aviso

Esta ferramenta tem finalidade de apoio técnico e educacional. A classificação gerada deve ser interpretada por profissionais responsáveis, considerando o contexto epidemiológico, institucional e operacional.
