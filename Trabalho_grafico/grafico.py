import matplotlib.pyplot as plt

vendas = [100, 150, 1500, 2000, 120]
vendedores = ['João', 'Julia', 'Ana', 'José', 'Maria']
meta = 130

vendedores_atingiram_meta = []

for i in range(len(vendas)):
    if vendas[i] >= meta:
        print(f"O vendedor {vendedores[i]} atingiu a meta e vendeu {vendas[i]} no mes")
        vendedores_atingiram_meta.append(vendedores[i])

if not vendedores_atingiram_meta:
    print("Nenhum vendedor atingiu a meta. A loja não ganhará bônus.")


plt.bar(vendedores, vendas)


plt.title('Gráfico de vendas')
plt.xlabel('Nome dos Vendedores')
plt.ylabel('Valores de Vendas')


plt.show()


