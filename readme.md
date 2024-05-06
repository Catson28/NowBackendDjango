#   passos da criacao do projecto django(backend)

1. **Criar um Ambiente Virtual**
   Vamos criar um ambiente virtual chamado "env" na pasta onde queremos criar o projeto Django:

   ```bash
   mkdir jabackend
   cd jabackend
   python3 -m venv env
   ```

2. **Ativar o Ambiente Virtual**
   Ative o ambiente virtual para começar a usar suas configurações isoladas:

   ```bash
   source env/bin/activate
   ```

3. **Instalar o Django**
   Agora que estamos dentro do ambiente virtual, podemos instalar o Django:

   ```bash
   pip install django
   ```

4. **Criar o Projeto Django**
   Com o Django instalado, crie um novo projeto chamado "jabackend":

   ```bash
   django-admin startproject core .
   ```

5. **Executar o Servidor de Desenvolvimento**
   Navegue até o diretório do projeto e execute o servidor de desenvolvimento para verificar se tudo está funcionando corretamente:

   ```bash
   cd jabackend
   python manage.py runserver
   ```

   Isso iniciará o servidor de desenvolvimento do Django. Abra um navegador e acesse `http://127.0.0.1:8000/` para ver a página inicial do projeto.

O ambiente virtual precisa ser ativado sempre que você quiser trabalhar no projeto Django. Para desativá-lo, basta digitar `deactivate` no terminal.