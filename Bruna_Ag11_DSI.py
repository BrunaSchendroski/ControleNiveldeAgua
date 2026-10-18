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
