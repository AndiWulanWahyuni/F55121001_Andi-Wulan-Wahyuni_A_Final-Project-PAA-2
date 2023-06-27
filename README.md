# F55121001_Andi-Wulan-Wahyuni_A_Final-Project-PAA-2

Nama  : Andi Wulan Wahyuni
NIM   : F55121001
Kelas : A

Final Project Perancangan Dan Analisis Algoritma 2
1. Analisis algoritma Bubble Sort dan Insertion Sort untuk mengevaluasi :
   a. Worst case
     - Bubble Sort : Worst case terjadi ketika array dalam keadaan terbalik secara terurut. Kompleksitas waktu adalah O(n^2), di mana n adalah jumlah elemen dalam
       array.
     - Insertion Sort : Worst case terjadi ketika array dalam keadaan terbalik secara terurut. Kompleksitas waktu adalah O(n^2), di mana n adalah jumlah elemen dalam
       array.
   b. Best case
      - Bubble Sort : Best case terjadi ketika array sudah dalam keadaan terurut secara terbalik. Kompleksitas waktu adalah O(n), di mana n adalah jumlah elemen dalam
        array. Namun, karena ada iterasi tambahan untuk memeriksa apakah ada pertukaran dalam setiap langkah, secara umum kompleksitas waktu tetap O(n^2).
      - Insertion Sort : Best case terjadi ketika array sudah dalam keadaan terurut. Kompleksitas waktu adalah O(n), di mana n adalah jumlah elemen dalam array.
        Setiap elemen hanya perlu dibandingkan dengan elemen-elemen sebelumnya hingga elemen yang lebih kecil ditemukan.
   c. Average case
      - Bubble Sort : Rata-rata kasus terjadi ketika array dalam keadaan acak. Kompleksitas waktu adalah O(n^2), di mana n adalah jumlah elemen dalam array. Dalam
        rata-rata kasus, Bubble Sort akan melakukan sejumlah iterasi yang sama seperti dalam worst case, tetapi dengan beberapa pertukaran yang lebih sedikit.
      - Insertion Sort : Rata-rata kasus terjadi ketika array dalam keadaan acak. Kompleksitas waktu adalah O(n^2), di mana n adalah jumlah elemen dalam array. Dalam
        rata-rata kasus, Insertion Sort juga akan melakukan sejumlah iterasi yang sama seperti dalam worst case, tetapi dengan beberapa pergeseran yang lebih sedikit.
3. Analisis algoritma TSP dan Dijkstra untuk mengevaluasi :
   a. Worst case
      - TSP : Worst case dalam algoritma TSP adalah O(n!) di mana n adalah jumlah simpul dalam grafik. Pada kasus ini, TSP akan mencoba semua kemungkinan permutasi
        untuk menemukan jalur terpendek, yang meningkat secara faktorial seiring bertambahnya jumlah simpul.
      - Dijkstra : Worst case dalam algoritma Dijkstra adalah O((V+E) log V) di mana V adalah jumlah simpul dan E adalah jumlah tepi dalam grafik. Pada kasus ini,
        Dijkstra akan menjelajahi semua simpul dan tepi dalam grafik untuk mencari jalur terpendek.
   b. Best case
      - TSP : Best case dalam algoritma TSP adalah O(n^2) di mana n adalah jumlah simpul dalam grafik. Namun, karena TSP adalah permasalahan NP-sulit, tidak ada
        pendekatan best-case yang dapat mencapai kompleksitas waktu yang lebih rendah secara umum.
      - Dijkstra : Best case dalam algoritma Dijkstra adalah O(V+E) di mana V adalah jumlah simpul dan E adalah jumlah tepi dalam grafik. Pada kasus ini, Dijkstra
        akan menemukan jalur terpendek dengan jumlah simpul dan tepi minimum yang diperlukan.
   c. Average case
      - TSP : Rata-rata kasus dalam algoritma TSP sangat sulit untuk dihitung karena melibatkan banyak faktor seperti struktur grafik, jarak, dan urutan simpul yang
        dijelajahi. Rata-rata kasus dapat bervariasi tergantung pada karakteristik grafik dan metode pendekatan yang digunakan.
      - Dijkstra : Rata-rata kasus dalam algoritma Dijkstra adalah O((V+E) log V) di mana V adalah jumlah simpul dan E adalah jumlah tepi dalam grafik. Dalam
        rata-rata kasus, Dijkstra akan mengunjungi sejumlah simpul dan tepi yang proporsional dengan ukuran grafik.
