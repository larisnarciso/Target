# Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

import os
import json

def carregandoDados(arquivo):
  with open(arquivo, 'r') as file: dados = json.load(file)
  return dados

def calculoFaturamento(dados):
  faturamentoDiario = [item['valor'] for item in dados]

  menorValor = min(faturamentoDiario)
  maiorValor = max(faturamentoDiario)

  diasFaturamento = [item['valor'] for item in dados if item ['valor'] > 0]
  media = sum(diasFaturamento) / len(diasFaturamento)
  diasAM = sum(1 for item in dados if item['valor'] > media)

  return menorValor, maiorValor, diasAM

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo = os.path.join(diretorio_atual, 'dados.json')
dadosJSON = carregandoDados(arquivo)

menor, maior, diasAM = calculoFaturamento(dadosJSON)
print('Menor valor de faturamento:', menor)
print('Maior valor de faturamento:', maior)
print('Número de dias com faturamento acima da média:', diasAM)