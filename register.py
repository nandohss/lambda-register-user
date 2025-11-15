import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

def registrar_usuario(data):
    user_id = data['userId']  # ✅ Usa o mesmo ID fixo do Cognito
    email = data['email']
    name = data['name']
    apelido = data['apelido']

    # ✅ Verifica se já existe
    existing = table.get_item(
        Key={'userId': user_id}
    )

    if 'Item' in existing:
        return {
            'userId': user_id,
            'message': 'Usuário já registrado'
        }

    # ✅ Se não existir, insere com isHoster = False
    table.put_item(
        Item={
            'userId': user_id,
            'email': email,
            'name': name,
            'apelido': apelido,
            'isHoster': False  # ← novo campo
        }
    )

    return {
        'userId': user_id,
        'message': 'Usuário registrado com sucesso'
    }
