# TODO Найдите количество книг, которое можно разместить на дискете
disketa=1.44
GG=1024
disketa_v_KB=disketa*GG
disketa_v_BA=disketa_v_KB*GG
kNIGA_STR=100
kNIGA_STROK=kNIGA_STR*50
kNIGA_SIMVOL=kNIGA_STROK*25
kNIGA_RAZMER=kNIGA_SIMVOL*4
BLACK_BABOL=disketa_v_BA/kNIGA_RAZMER
NE_NY_VSE=round(BLACK_BABOL)
print("Количество книг, помещающихся на дискету:", NE_NY_VSE)
