users = {
"admin": "1234",
"user1": "abcd",
"user2": "pass"
}
username = input("Masukkan username: ")
password = input("Masukkan password: ")

if username in users:
    if users[username] == password:
        print("Login berhasil")
    else:
        print("Password salah")
else:
    print("Username tidak ditemukan")