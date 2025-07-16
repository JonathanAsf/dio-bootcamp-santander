def salvar_carro(marca,modelo,ano,placa):
    #salvar carro no banco de dados
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

#Formas de atribuir argumentos a esta função (A saída é a mesma):
    
salvar_carro("Fiat","Palio",1999,"ABC-1234") #Passando dessa forma pode haver inserção errada de dados caso insira o argumento na ordem errada ou o argumento mude de posição na função
 
salvar_carro(marca="Fiat",modelo="Palio", ano=1999,placa="ABC-1234") #Caso o argumento mude de nome, um erro acontece. Exemplo: de:modelo para:modelos

salvar_carro(**{"marca": "Fiat","modelo": "Palio", "ano":"1999","placa":"ABC-1234"}) #Faz uma associação parecida com um dicionário
