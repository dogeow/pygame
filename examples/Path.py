"""路径"""
from pathlib import Path

path = Path(__file__).resolve().parent

path_str = str(path)

result = path_str + '/images/ball.png'

print(result)
