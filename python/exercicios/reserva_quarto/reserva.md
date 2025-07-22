# 🏖️Sistema de Reservas de Pousada

## 📝Descrição

Este projeto tem como objetivo automatizar o sistema de reservas de uma pousada.  
Através de uma função simples, o sistema verifica automaticamente se as reservas solicitadas pelos clientes podem ser confirmadas ou se devem ser recusadas por falta de disponibilidade dos quartos.

## ⚙️Funcionamento

A função recebe:

- **Uma lista de quartos disponíveis**
- **Uma lista de quartos solicitados nas reservas**

A função compara as listas e retorna:

- **Reservas confirmadas** (quando o quarto solicitado está disponível e ainda não foi reservado)
- **Reservas recusadas** (quando o quarto solicitado não está disponível ou já foi reservado)

## Exemplo de Entrada e Saída

| **Quartos Disponíveis** | **Reservas Solicitadas** | **Saída Esperada**                                                 |
| ----------------------- | ------------------------ | ------------------------------------------------------------------ |
| 101 102 103 104         | 102 105 101 103          | Reservas confirmadas: 102 101 103 <br> Reservas recusadas: 105     |
| 201 202 203 204 205     | 205 202 208 201 203      | Reservas confirmadas: 205 202 201 203 <br> Reservas recusadas: 208 |
| 10 20 30 40 50          | 25 30 10 40 50 60        | Reservas confirmadas: 30 10 40 50 <br> Reservas recusadas: 25 60   |

## Como Usar

Você pode implementar a função no Python da seguinte forma:

```python
def processar_reservas(quartos_disponiveis, reservas_solicitadas):
    reservas_confirmadas = []
    reservas_recusadas = []

    for quarto in reservas_solicitadas:
        if quarto in quartos_disponiveis:
            reservas_confirmadas.append(quarto)
            quartos_disponiveis.remove(quarto)  # Remove da lista para evitar reserva duplicada
        else:
            reservas_recusadas.append(quarto)

    print("Reservas confirmadas:", ' '.join(map(str, reservas_confirmadas)))
    print("Reservas recusadas:", ' '.join(map(str, reservas_recusadas)))
```
