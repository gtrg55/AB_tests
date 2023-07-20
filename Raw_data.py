import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta


plt.ylabel('Переходы на сайт ')
plt.xlabel('Время')


x = np.linspace(0, 1, 200)

Values = beta.pdf(x,180,20)
Values2 = beta.pdf(x,60,20)

plt.plot(x,Values,label="группа A")
plt.plot(x,Values2,label="группа Б")
plt.legend()
plt.show()