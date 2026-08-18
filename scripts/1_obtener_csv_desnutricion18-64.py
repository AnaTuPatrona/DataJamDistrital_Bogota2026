import pandas as pd
url_csv = "https://datosabiertos.bogota.gov.co/dataset/a1e1ef90-10c0-436f-a290-d1f7c1cf2242/resource/bbe9e920-c564-40f2-a307-5ae1ff087168/download/osb_saludmental-vintrafamiliar.csv"
df = pd.read_csv(url_csv, delimiter=';', encoding='UTF-8-SIG', decimal=',')
df.to_csv('data/osb_saludmental-vintrafamiliar.csv', index=False)