# Monografias API

API desenvolvida com Django REST Framework. Esta aplicação oferece endpoints RESTful com documentação integrada via Swagger e ReDoc.

## Instalação

Clone o repositório:

```bash
git clone https://github.com/moraismariana/sd-api.git
cd sd-api
```

Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # no Windows use `venv\Scripts\activate`
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Aplique as migrações:

```bash
python manage.py migrate
```

Crie um superusuário (opcional, mas útil para acessar o admin):

```bash
python manage.py createsuperuser
```

Execute o servidor:

```bash
python manage.py runserver
```

## Acessando a API

A API estará disponível em:

```
http://127.0.0.1:8000/monografias/
```

## Documentação da API

- **Swagger UI**: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- **ReDoc**: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)
