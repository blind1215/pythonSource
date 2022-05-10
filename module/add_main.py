#%%
import add

print(add.add(5, 6))

print(add.safe_add(50, "60"))


# %%
from add import add, safe_add

print(add(5, 6))
print(safe_add(50, "60"))
