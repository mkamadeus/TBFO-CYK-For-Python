# IF2124 - Teori Bahasa Formal dan Otomata
## Compiler Bahasa Python
**Kelompok** : *_Kweatiau Awih Halal_*
* 13518035 - Matthew Kevin Amadeus
* 13518056 - Michael Hans
* 13518128 - Lionnarta Savirandy

### Cara Menggunakan :
Berikut ini adalah list file yang ada beserta penjelasannya:
* `cfg.txt` -> berisi daftar terminal, variables, dan productions grammar
* `cnf.txt` -> berisi productions yang sudah dalam bentuk chomsky normal form, sudah diconvert
* `input.txt` -> tempat untuk memasukkan input untuk dicompile dengan compiler

1. Untuk mendapatkan cnf.txt terbaru, jalankan command pada terminal :
```shell
python CFG2CNF.py cfg.txt
```
2. Tuliskan input yang ingin dicompile pada `input.txt`
3. Jalankan program bisa dengan menggunakan dua cara:
```shell
python main.py <nama_file.txt>
python main.py <default = cnf.txt>
```

#### Selamat mencoba! 