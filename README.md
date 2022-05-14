# graficoCotacoes
Sistema para guardar e apresentar cotaçoes de Euro, Dolar e Iene

### Para instalação dos requisitos
Assumindo que a maquina já possui o python3 e o pip instalados:
```bash
    pip install -r requirements.txt
```

### Para rodar o projeto
```bash
    python manage.py runserver
```
Este comando deixará acessível o projeto via browser no endereço `http://127.0.0.1:8000/`

### Para carregar dados anuais de valores via API Vatcomply:
Este comando customizado vai realizar o load de todos os dias do ano escolhido (até o dia vigente para o caso do ano vigente) no banco de dados
```bash
    python manage.py charge_since_year --year <ano_escolhido>
```