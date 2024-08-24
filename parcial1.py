#MARIA FERNANDA QUINILLA RAGUESX 
#2100157
#PARCIAL 1

# Definición de las reglas del sistema experto
def recomendar_pelicula(preferencias):
    # Base de conocimientos
    if preferencias['género'] == 'acción' and preferencias['duración'] == 'corta' and preferencias['estilo'] == 'intensa':
        return "John Wick"
    elif preferencias['género'] == 'drama' and preferencias['duración'] == 'larga' and preferencias['estilo'] == 'emocional':
        return "The Shawshank Redemption"
    elif preferencias['género'] == 'comedia' and preferencias['duración'] == 'corta' and preferencias['estilo'] == 'ligera':
        return "Superbad"
    elif preferencias['género'] == 'aventura' and preferencias['duración'] == 'larga' and preferencias['estilo'] == 'épica':
        return "The Lord of the Rings"
    else:
        return "No se encontró una recomendación basada en tus preferencias."

# Solicitar las preferencias del usuario
def obtener_preferencias_usuario():
    print("Bienvenido al sistema experto, en donde te  recomendamos películas.")
    género = input("¿Qué género prefieres? (acción, drama, comedia, aventura): ").lower()
    duración = input("¿Prefieres películas cortas o largas?: ").lower()
    estilo = input("¿Qué estilo prefieres? (intensa, emocional, ligera, épica): ").lower()

    return {'género': género, 'duración': duración, 'estilo': estilo}

# Función principal
def sistema_experto_recomendador():
    preferencias = obtener_preferencias_usuario()
    recomendación = recomendar_pelicula(preferencias)
    print(f"Recomendación: {recomendación}")

# Ejecutar el sistema experto
sistema_experto_recomendador()
