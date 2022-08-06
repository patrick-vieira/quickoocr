# Quick OCR

## Objetivo transcrever texto de fotos rapidamente usando copy and paste.



### Criando o primeiro app
    docker-compose -f docker-compose.yaml run --rm app sh -c "python manage.py startapp reader"

#### executando a primeira migração / criação do banco de dados.
    docker-compose -f docker-compose.yaml run --rm app sh -c "python manage.py migrate"