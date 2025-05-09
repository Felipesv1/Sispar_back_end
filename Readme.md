# Documentação do Projeto

## Como realizar o clone do repositório
1. Certifique-se de ter o Git instalado em sua máquina.
2. Execute o seguinte comando no terminal para clonar o repositório:
    ```bash
    git clone <URL_DO_REPOSITORIO>
    ```
    Substitua `<URL_DO_REPOSITORIO>` pela URL do repositório do projeto.

## Como baixar as dependências
1. Navegue até o diretório do projeto clonado:
    ```bash
    cd <NOME_DO_DIRETORIO>
    ```
    Substitua `<NOME_DO_DIRETORIO>` pelo nome do diretório do projeto.
2. Instale as dependências do projeto utilizando o gerenciador de pacotes apropriado. Por exemplo, se o projeto utiliza Node.js e npm:
    ```bash
    npm install
    ```
    Ou, se utiliza Yarn:
    ```bash
    yarn install
    ```

## Como executar o projeto
1. Após instalar as dependências, execute o seguinte comando para iniciar o projeto:
    ```bash
    npm start
    ```
    Ou, se estiver utilizando Yarn:
    ```bash
    yarn start
    ```
2. O projeto será iniciado e estará disponível no navegador no endereço padrão, como `http://localhost:3000`, a menos que especificado de outra forma.
## Novas Rotas do Projeto

- **Rota de cadastro de colaborador (`/colaboradores/cadastrar`)**: Permite o cadastro de novos colaboradores no sistema.
- **Rota de solicitação de reembolso (`/reembolsos/solicitar-reembolsos`)**: Permite que os usuários solicitem reembolsos.
- **Rota para visualizar todos os colaboradores (`/todos-colaboradores`)**: Permite listar todos os colaboradores cadastrados no sistema.
- **Rota para visualizar todos os reembolsos (`/reembolsos`)**: Permite listar todos os reembolsos registrados no sistema.
## Rotas importantes do projeto


- **Rota de autenticação (`/login`)**: Permite que os usuários façam login no sistema.
- **Rota de cadastro (`/cadastrar`)**: Permite que novos usuários se cadastrem no sistema.

Certifique-se de verificar o código-fonte ou a documentação adicional para mais informações sobre rotas e funcionalidades específicas.
