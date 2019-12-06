Projeto Demandai

Comandos basicos

*Instalar dependencias 

    pip install -r requirements.txt
    pip install django-crispy-forms
*Criar migrates

    python manage.py makemigrations

*Criar tabelas no banco de dados

    python manage.py migrate
    
*Seed database
    
    python manage.py seed demandai_administrador --number=50
    
*Resetar database 

    python manage.py flush 
    
*Criar Super Usuário

    python manage.py createsuperuser
    
*Atualizar arquivo requirements

    pip freeze > requirements.txt
    
*Start Projeto 

    python manage.py runserver
    
                    ou
    
    python manage.py runserver 192.168.0.101:8001
    
*SQL
    UPDATE `demandai_administrador_demand` SET  `action_id`=FLOOR(RAND() * 50 +1)
