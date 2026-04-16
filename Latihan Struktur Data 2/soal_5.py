transaksi = []
transaksi.append("Beli pulsa")
transaksi.append("Bayar listrik")
transaksi.append("Top up e-wallet")

print("Riwayat transaksi:", transaksi)

# batalkan transaksi terakhir
dibatalkan = transaksi.pop()

print("Transaksi dibatalkan:", dibatalkan)
print("Sisa transaksi:", transaksi)