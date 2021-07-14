import pandas as pd

# criar uma função com o código como argumento
def bcb(codigo):
  link_bcb = f'https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados?formato=json'
  df = pd.read_json(link_bcb)
  # redefinindo index
  df.index = pd.to_datetime(df['data'])
  df = df['valor']
  return df

cdi = bcb(12)
cdi.head()

# exportar planilha .xlsx
cdi.to_excel('/content/drive/MyDrive/00_Adglow/cdi.xlsx')