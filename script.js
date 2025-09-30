const data = [
  {
    id: 101,
    nama_produk: "Laptop Gaming X500",
    harga: 15000000,
    stok: 12,
  },
  {
    id: 102,
    nama_produk: "Mouse Wireless Logitech",
    harga: 350000,
    stok: 45,
  },
  {
    id: 103,
    nama_produk: "Monitor LED 24 Inci",
    harga: 1800000,
    stok: 20,
  },
];

for (let i = 0; i < data.length; i++) {
  console.log(data[i].id + data[i].nama_produk);
}
