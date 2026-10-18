# Controle de Níveis de Água

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Colorama](https://img.shields.io/badge/Biblioteca-Colorama-6C63FF?style=for-the-badge)](https://pypi.org/project/colorama/)
[![Status](https://img.shields.io/badge/Status-Concluído-2E8B57?style=for-the-badge)](#sobre-o-projeto)

## Sobre o projeto

Programa em Python que simula o monitoramento do nível de água de um reservatório. Cada nível recebe uma mensagem de alerta com uma cor específica, usando a biblioteca Colorama.

## Níveis do reservatório

| Nível | Situação | Cor |
|---|---|---|
| 1 | Muito baixo (crítico) | Vermelho |
| 2 | Baixo | Amarelo |
| 3 | Médio | Verde |
| 4 | Alto | Ciano |
| 5 | Muito alto (alerta) | Azul |

## Código-fonte

```python
from colorama import Fore, Style, init

init()

niveis = [
    {"nivel": 1, "situacao": "Muito baixo (crítico)", "cor": Fore.RED},
    {"nivel": 2, "situacao": "Baixo", "cor": Fore.YELLOW},
    {"nivel": 3, "situacao": "Médio", "cor": Fore.GREEN},
    {"nivel": 4, "situacao": "Alto", "cor": Fore.CYAN},
    {"nivel": 5, "situacao": "Muito alto (alerta)", "cor": Fore.BLUE},
]


def definir_cor(nivel):
    """Retorna a cor correspondente ao nível informado."""
    for item in niveis:
        if item["nivel"] == nivel:
            return item["cor"]
    return Fore.WHITE


def exibir_situacao(item):
    cor = definir_cor(item["nivel"])
    mensagem = f"Nível {item['nivel']}: {item['situacao']}"
    print(f"{cor}{mensagem}{Style.RESET_ALL}")


def main():
    print("CONTROLE DE NÍVEIS DE ÁGUA")
    print("=" * 28)

    nivel_atual = 3
    for item in niveis:
        exibir_situacao(item)

    print("=" * 28)
    situacao_atual = next(item for item in niveis if item["nivel"] == nivel_atual)
    print("Situação atual do reservatório:")
    exibir_situacao(situacao_atual)
    print(Style.RESET_ALL, end="")


if __name__ == "__main__":
    main()
```

## Como executar

1. Instale o Python 3.
2. Instale a dependência com `pip install -r requirements.txt`.
3. Execute `python Bruna_Ag11_DSI.py`.

## Tecnologias utilizadas

- Python
- Biblioteca Colorama
- Listas e funções

## Autora

Bruna Schendroski Rocha

Atividade da Agenda 11 — Desenvolvimento de Sistemas I (DS_I).
