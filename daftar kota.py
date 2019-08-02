daftar_kota =
    {
        'jkt': 'Jakarta',
        'mnd': 'manado',
        'gto': 'gorontalo',
        'mam': 'mamuju',
        'mks': 'makassar',
        'pal': 'palu',
        'kdi': 'kendari',
        'amb': 'ambon',
        'jap': 'jayapura',
        'mnk': 'manokwari',
        'bgl': 'bengkulu',
        'bna': 'banda aceh',
        'jmb': 'jambi'
    }
b = 1
while b == 2:
    a = input('Masukkan Singkatan Kota: ')
    print('Nama Kota: ' + daftar_kota.get(a))
    b = int(input("Ulang? 1 - Ya, 2 - Tidak :"))
