#Login simulation using sha256
from hashlib import sha256

#O usuário irá inserir sua senha e iremos codifica-la para podermos armazenala
first_password = input("Digite sua senha: ").strip()
hash_first_password = sha256(first_password.encode()).digest()

#Uma vez armazenada a senha, iremos demandar ao usuário de confirmar sua senha
second_password = input("Confirme sua senha: ").strip()
hash_second_password = sha256(second_password.encode()).digest()

if hash_first_password == hash_second_password:
  print("Login realizado com sucesso!")
else:
  print("Senha incorreta")
