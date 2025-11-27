from flask import request

def data_validation():
    """Validação de dados do corpo de requisição

    Returns:
        data: dado validado
        None: dado invalido
    """
    try:
        data = request.get_json()
        if data is None:
            return None
    except Exception as e:
        return None
    return data