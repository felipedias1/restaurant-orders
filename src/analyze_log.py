# import pandas as pd
import csv
from collections import Counter
import operator


# def analyze_log(path_to_file):
# try:
# data = pd.read_csv(path_to_file, header=None)
# data.columns = ["nome", "pedido", "dia"]
# maria = data[data.nome == "maria"].value_counts(["pedido"]).idxmax()[0]
# arnaldo = data[
# (data.nome == "arnaldo") & (data.pedido == "hamburguer")
#  ].value_counts(["pedido"]).max()
#  joao_pedidos = set(data["pedido"].unique()) - (
#   set(data.pedido.loc[data.nome == "joao"].unique()))
#  joao_dias = set(data["dia"].unique()) - (
#  set(data.dia.loc[data.nome == "joao"].unique()))
#  with open('data/mkt_campaign.txt', 'w') as file:
#  file.write(f'{maria}\n{arnaldo}\n{joao_pedidos}\n{joao_dias}')
#  except FileNotFoundError:
#  if not path_to_file.endswith(".csv"):
#  raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
#  raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

def analyze_log(path_to_file):
    try:
        with open(path_to_file) as file:
            header = ["nome", "pedido", "dia"]
            orders = csv.DictReader(file, fieldnames=header)
            data = [line for line in orders]
            maria = maria_dish(data)
            arnaldo = analdo_dish(data)
            joao_pedidos = joao_orders(data)
            joao_dias = joao_days(data)
        with open('data/mkt_campaign.txt', 'w') as file:
            file.write(f'{maria}\n{arnaldo}\n{joao_pedidos}\n{joao_dias}')
    except FileNotFoundError:
        if not path_to_file.endswith(".csv"):
            raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def maria_dish(data):
    customer_orders = []
    for order in data:
        if order["nome"] == "maria":
            customer_orders.append(order["pedido"])
    new_dict = Counter(customer_orders)
    most_ordered = max(new_dict.items(), key=operator.itemgetter(1))[0]
    return most_ordered


def analdo_dish(data):
    customer_orders = []
    for order in data:
        if order["nome"] == "arnaldo":
            customer_orders.append(order["pedido"])
    new_dict = Counter(customer_orders)
    return new_dict["hamburguer"]


def joao_orders(data):
    menu = set(item["pedido"] for item in data)
    customer_orders = []
    for order in data:
        if order["nome"] == "joao":
            customer_orders.append(order["pedido"])
    new_dict = set(customer_orders)
    return menu - new_dict


def joao_days(data):
    menu = set(item["dia"] for item in data)
    customer_days = []
    for order in data:
        if order["nome"] == "joao":
            customer_days.append(order["dia"])
    new_dict = set(customer_days)
    return menu - new_dict
