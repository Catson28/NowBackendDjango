#   Repositorio do Backend(api)

Aqui estão os links relevantes para o projeto:

- Repositório do Frontend: [GitHub](https://github.com/Catson28/NowFrontendReact)
- Repositório do Backend: [GitHub](https://github.com/Catson28/NowBackendDjango)
- Repositório do Build (Executável) do Frontend: [GitHub](https://github.com/Catson28/BuildedNowFrontendReact)
- Domínio Free do Executável: [JASoftware](https://jasoftware.netlify.app)
- API do Projeto: [PythonAnywhere](https://jasoftware.pythonanywhere.com/)

Estes links fornecem acesso aos diferentes aspectos do projeto, incluindo o código-fonte, o executável do frontend, o domínio onde o frontend pode ser visualizado em qualquer dispositivo e a API para integração com outros sistemas.

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

##   Codigo para baixar sempre actualizacoes

```bash
git pull origin main
```

Para instalar as dependências listadas em um arquivo `requirements.txt`, você pode usar o comando `pip install -r requirements.txt`. Aqui está como você faria isso:

1. Certifique-se de estar dentro do ambiente virtual onde deseja instalar as dependências.

2. No terminal, navegue até o diretório onde está localizado o arquivo `requirements.txt`.

3. Execute o comando a seguir para instalar as dependências listadas no arquivo:
   
   ```bash
   pip install -r requirements.txt
   ```

#  _

Para ativar o ambiente virtual no Windows, siga estes passos:

1. **Abra o Prompt de Comando**:
   - Pressione `Win + R`, digite `cmd` e pressione `Enter`.

2. **Navegue até o Diretório do Projeto**:
   - Use o comando `cd` para ir até o diretório onde o ambiente virtual foi criado. Por exemplo:
     ```shell
     cd caminho\para\seu\projeto
     ```

3. **Ative o Ambiente Virtual**:
   - No diretório do projeto, ative o ambiente virtual usando o seguinte comando:
     ```shell
     env\Scripts\activate
     ```

Após executar esse comando, você verá o nome do ambiente virtual no prompt de comando, indicando que o ambiente está ativado.

Se precisar de ajuda adicional ou encontrar algum erro, por favor, me avise!