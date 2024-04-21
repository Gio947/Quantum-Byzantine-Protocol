import importlib
import start # first execution

for _ in range(28): # other 49 executions
    importlib.reload(start)
