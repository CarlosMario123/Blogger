import hashlib

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    # Truncar el hash a una longitud máxima de 50 caracteres
    truncated_hash = hashed_password[:49]
    return truncated_hash

def verify_password(stored_password, provided_password):
    return stored_password == hash_password(provided_password)

