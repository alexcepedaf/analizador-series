import math
from functools import reduce

def calculate_gcd(numbers):
    """Calcula el MCD de una lista de números enteros"""
    if not numbers or not isinstance(numbers, list):
        return 0
    return reduce(math.gcd, numbers)
    
def calculate_mean_std(numbers):
    """Calcula (media, desviación_estándar) de una lista de números"""
    if not numbers or not isinstance(numbers, list):
        return 0.0, 0.0
    
    n = len(numbers)
    mean = sum(numbers) / n
    
    if n == 1:
        return round(mean, 2), 0.0
    
    variance = sum((x - mean) ** 2 for x in numbers) / n
    std_dev = math.sqrt(variance)
    return round(mean, 2), round(std_dev, 2)

def is_prime(n):
    """Verifica si un número es primo"""
    if not isinstance(n, int) or n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes(numbers):
    """Retorna lista de números primos encontrados"""
    if not numbers or not isinstance(numbers, list):
        return []
    return [n for n in numbers if is_prime(n)]