import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-darkgrid')  # Estilo bonito

# Dados
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

# Modelo


y_pred = y

# Gráfico
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='dodgerblue', s=70, alpha=0.7, label='Dados observados')
plt.plot(x, y_pred, color='firebrick', linewidth=2.5, label='Linha de Regressão')
plt.title('Regressão Linear Simples', fontsize=16)
plt.xlabel('X', fontsize=14)
plt.ylabel('Y', fontsize=14)
plt.legend(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()