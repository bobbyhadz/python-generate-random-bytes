# Generate random bytes of length N in Python

import os


# ✅ create random bytestring that is 8 bytes long

random_bytes = os.urandom(8)
print(random_bytes)  # 👉️ b'\xd8\xa7\\\xe4~\xa2y\xe3'
print(len(random_bytes))  # 👉️ 8

# ------------------------------------------

# ✅ create random bytestring that is 16 bytes long

random_bytes = os.urandom(16)

# 👇️ b'\xeb\xba^\x81\xe1\x00\xb9\x0c\x99\x1e\xe9\x86\x86\x0bl]'
print(random_bytes)
print(len(random_bytes))  # 👉️ 16