# %%

# import
import random
from my_module.my_classes import Enemy, AnnoyingEnemy

# use external classes
# enemy = Enemy(10)
enemy = AnnoyingEnemy(10, 0.5)
for iTurn in range(3):
    hit = random.randint(2, 5)
    print(f"blow force: {hit}")
    enemy.take_damage(hit)
    print(f"enemy health: {enemy.health}")


# %%
# juniper compliant implementation (reload module)

# import
import random
import my_module.my_classes as mymodule

# force reload (jupyter kernel problem)
import importlib
importlib.reload(mymodule)

# use external class
enemy = mymodule.Enemy(10)
enemy.take_damage(2)
print(f"enemy health: {enemy.health}")