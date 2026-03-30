import os
import mne
import numpy as np
import pandas as pd
from pathlib import Path

pasta_entrada = Path("/content/drive/MyDrive/IC2026/dados_transe")
pasta_saida = Path("/content/drive/MyDrive/IC2026/dados_transe_limpos")

pasta_saida.mkdir(parents=True, exist_ok=True)

#Definição de parâmetros:
epoch_size = 1.28
low_freq = 0.5
high_freq = 48
up_tresh = 100

def processar_e_salvar_edf(arquivo_edf, pasta_saida):
  #Carrega o arquivo em formato .edf
  raw = mne.io.read_raw_edf(arquivo_edf, preload=True)
  
  #Nome dos canais para remoção
  canais_remover = ['VEOG', 'HEOG', 'M1', 'M2', 'EKG', 'EMG', 'Cb1', 'Cb2',
                    'Fz', 'F11', 'F12', 'FT11', 'FT12']
  
  #Remove os canais desejados caso algum deles esteja presente no EEG
  raw.drop_channels([ch for ch in canais_remover if ch in raw.ch_names])
  
  #Aplica os filtros para obter sinais 0.5 <= f <= 48.0
  raw.filter(low_freq, high_freq)
  
  #Cria eventos artificias a cada 1,28 segundos conforme o tempo do sinal
  eventos = mne.make_fixed_length_events(raw, duration = epoch_size)
  
  epochs = mne.Epochs(raw,
                      events = eventos,
                      tmin = 0,
                      tmax = epoch_size,
                      baseline = None,
                      preload = True)
  total_epochs = len(epochs)
    
  #Ultrapassando 100mV, a época é marcada como ruim
  reject_criteria = dict(eeg = up_tresh * 1e-6)
  epochs.drop_bad(reject = reject_criteria)
  
  #Calcula quantas épocas foram removidas
  remaining_epochs = len(epochs)
  removed_epochs = total_epochs - remaining_epochs
  print(removed_epochs)
  epochs = epochs[:100]
  print(f"  Salvando {len(epochs)} épocas")

for arquivo_edf in pasta_entrada.glob("*.edf"):
    print(f"\n Processando: {arquivo_edf.name}")
    processar_e_salvar_edf(arquivo_edf, pasta_saida)

print("\n Todos os arquivos foram processados")
