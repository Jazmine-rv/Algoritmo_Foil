import math

# Datos de ejemplo
datos = [ 
    {"edad": 22, "departamento": "IT", "nivel_educativo": "terciario", "en_formacion": True}, 
    {"edad": 24, "departamento": "IT", "nivel_educativo": "universitario", "en_formacion": True}, 
    {"edad": 21, "departamento": "RRHH", "nivel_educativo": "terciario", "en_formacion": True}, 
    {"edad": 35, "departamento": "IT", "nivel_educativo": "universitario", "en_formacion": False}, 
    {"edad": 40, "departamento": "Finanzas", "nivel_educativo": "maestría", "en_formacion": False}, 
    {"edad": 29, "departamento": "RRHH", "nivel_educativo": "universitario", "en_formacion": False}, 
    {"edad": 23, "departamento": "IT", "nivel_educativo": "terciario", "en_formacion": True}, 
    {"edad": 38, "departamento": "Finanzas", "nivel_educativo": "universitario", "en_formacion": False} 
] 

# Valores antes de aplicar la condición
P = sum(1 for d in datos if d["en_formacion"])  # positivos antes
N = sum(1 for d in datos if not d["en_formacion"])  # negativos antes

# Aplicar condición: edad ≤ 23
filtrados = [d for d in datos if d["edad"] <= 23]
p = sum(1 for d in filtrados if d["en_formacion"])  # positivos después
n = sum(1 for d in filtrados if not d["en_formacion"])  # negativos después

# Función log2 segura
def log2_safe(x): 
    return math.log2(x) if x > 0 else float('-inf') 

# Cálculo FOIL Gain
foil_gain = p * (log2_safe(p / (p + n)) - log2_safe(P / (P + N)))

# Mostrar resultados
print("Condición: edad ≤ 23")
print(f"P (positivos antes) = {P}")
print(f"N (negativos antes) = {N}")
print(f"p (positivos después) = {p}")
print(f"n (negativos después) = {n}")
print(f"p / (p + n) = {p / (p + n):.3f}")
print(f"P / (P + N) = {P / (P + N):.3f}")
print(f"log2(p / (p + n)) = {log2_safe(p / (p + n)):.3f}")
print(f"log2(P / (P + N)) = {log2_safe(P / (P + N)):.3f}")
print(f"FOIL Gain = {foil_gain:.3f}")
