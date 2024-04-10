def verificarCamposJson(datos_json, campos):
    # Verificar si se proporcionaron datos JSON
    if datos_json is None:
        return False, "No se proporcionaron datos JSON"

    # Verificar si todos los campos están presentes en el JSON
    for campo in campos:
        if campo not in datos_json:
            return False, f"El campo '{campo}' no está presente en los datos JSON"
    
    # Si todos los campos están presentes, retornar True
    return True, None