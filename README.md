# uffer-backend

## como roda?
tá precário perdão
- instala o postgres
- instala o django
- instala as bibliotecas:
- 
  ```pip install djangorestframework```
  
  ```pip install psycopg[binary]```
- dentro do pgadmin cria um usuário pro app (uffer-app)
  - salva a senha e tal
- cria um banco de dados chamado uffer
- pega a porta do banco de dados
- dentro do /settings.py troca o DATABASES atual pelo que configurou no postgres.
  - um exemplo ai:
    

    DATABASES = {
    
        'default': {
    
            'ENGINE': 'django.db.backends.postgresql',
    
            'NAME': 'uffer',
    
            'USER': 'uffer-app',
    
            'PASSWORD': 'bancodedados',
    
            'HOST': 'localhost',
    
            'PORT': '5432',
    
        }
    
    }

- agora é só fazer as migrations e rodar o servidor, a partir da pasta que tem o /manage.py:
  
    ```python manage.py makemigrations```
  
    ```python manage.py migrate```
  
    ```python manage.py runserver```

- isso aí em cima roda localmente na máquina. pra rodar na rede local, copia o IP da sua rede e cola no ALLOWED_HOSTS no /settings.py e coloca o IP e a porta (pode ser a 8000 que é a que ele abre por padrão) desejada no comando
  ```python manage.py runserver seu_ip:porta```

## endpoints

### Usuario
- usuarios/
- usuarios/<int:pk>/
  
contém
  - nome (CharField)
  - email (CharField)
  - created (DateTime)

### Motorista
- motoristas/
- motoristas/<int:pk>/
  
contém
  - cnh (Big Integer)
  - usuario_id (FK para Usuario)

### Veículo
- veiculos/
- veiculos/<int:pk>
  
contém
  - placa (CharField)
  - cor (CharField)
  - modelo (CharField)
  - ano (Integer)
  - marca (CharField)
  - motorista_id (FK para Motorista)

### Local
- locais/
- locais/<int:pk>/
  
contém
  - coordenadas (CharField)
  
### Favorito
- favoritos/
- favoritos/<int:pk>/
  
contém
  - nome (CharField)
  - local_id (FK para Local)
  - usuario_id (FK para Usuario)

### Local Padrão
- locais_padrao/
- locais_padrao/<int:pk>/
  
contém
  - nome (CharField)
  - local_id (FK para Local)

### Trajeto
- trajetos/
- trajetos/<int:pk>/
  
contém
  - origem (FK para Local)
  - destino (FK para Local)

### Parada
- paradas/
- paradas/<int:pk>/
  
contém
  - posicao (small Int)
  - trajeto (FK para Trajeto)
  - local (FK para Local)

### Carona
- caronas/
- caronas/<int:pk>/
  
contém
  - data_hora_chegada (datetime)
  - data_hora_saida (datetime)
  - assentos_disponiveis (Int)
  - em_aberto (Boolean)
  - retorno (Boolean)
  - apenas_solicitacao (Boolean)
  - detalhes_adicionais (TextField)
  - motorista_id (FK para Motorista)
  - trajeto_id (FK para Trajeto)

### Relação de passageiro de carona
- passageiros/
- passageiros/<int:pk>/
  
contém
  - carona (FK para Carona)
  - usuario (FK para Usuario)

### Solicitação de carona pelo usuário
- solicitacoes_carona/
- solicitacoes_carona/<int:pk>/
  
contém
  - passa_por (FK para Trajeto)
  - data_hora_chegada (datatime)
  - quantidade_passageiros (Int)
  - em_aberto (Boolean)
