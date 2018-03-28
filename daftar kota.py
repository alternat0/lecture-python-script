daftar_kota={'jkt': 'Jakarta','mnd': 'manado','gto': 'gorontalo','mam': 'mamuju','mks': 'makassar','pal': 'palu','kdi': 'kendari','amb': 'ambon','jap': 'jayapura','mnk': 'manokwari','bgl': 'bengkulu','bna': 'banda aceh','jmb': 'jambi'}
b=1
while b==1:
    a=input('Masukkan Nama Kota : ')
    print(daftar_kota.get(a))
    b=int(input("Ulang 1.ya 2.no :"))
