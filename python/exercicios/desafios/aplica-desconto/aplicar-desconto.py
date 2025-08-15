descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}


preco = float(input().strip())
cupom = input().strip()

if cupom == "DESCONTO10":
  preco = preco - (preco*0.10)
elif cupom == "DESCONTO20":
  preco = preco - (preco*0.20)

print(f"{preco:.2f}")