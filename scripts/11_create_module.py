# %%

# import
from my_module.my_classes import Vehicle

# use external class
car = Vehicle("Flash", 12)
car.print()


# %%
# juniper compliant implementation (reload module)

# import
import my_module.my_classes as mymodule

# force reload (jupyter kernel problem)
import importlib
importlib.reload(mymodule)

# use external class
car = mymodule.Vehicle("Flash", 12)
car.print()