from .. import read_input
from ..fuel import total_fuel

print(sum(map(total_fuel, read_input())))