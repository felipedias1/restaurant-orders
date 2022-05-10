import pandas as pd


def analyze_log(path_to_file):
    try:
        data = pd.read_csv(path_to_file, header=None)
        data.columns = ["nome", "pedido", "dia"]
        maria = data[data.nome == "maria"].value_counts(["pedido"]).idxmax()[0]
        arnaldo = data[
            (data.nome == "arnaldo") & (data.pedido == "hamburguer")
        ].value_counts(["pedido"]).max()
        joao_pedidos = set(data["pedido"].unique())- (
            set(data.pedido.loc[data.nome == "joao"].unique()))
        joao_dias = set(data["dia"].unique()) - (
            set(data.dia.loc[data.nome == "joao"].unique()))
        with open('data/mkt_campaign.txt', 'w') as file:
            file.write(f'{maria}\n{arnaldo}\n{joao_pedidos}\n{joao_dias}')
    except FileNotFoundError:
        if not path_to_file.endswith(".csv"):
            raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
