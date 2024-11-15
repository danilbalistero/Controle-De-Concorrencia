# Sistema de Gerenciamento de Clientes
Este projeto é um sistema de gerenciamento de clientes desenvolvido como atividade prática para a disciplina de Gerenciamento da Transação em Banco de Dados e Otimização de Consultas e Segurança. 
O sistema realiza operações de listagem e atualização de clientes, com suporte a transações e tratamento de erros em cenários de concorrência.

## 📋 Funcionalidades

1. **Listagem de Clientes**: Exibe todos os clientes cadastrados no banco de dados.  
2. **Atualização de Clientes**: Permite atualizar o nome e o limite de um cliente.  
3. **Tratamento de Concorrência**: 
   - Verifica se os dados do cliente foram alterados por outro processo antes de confirmar a atualização.
   - Gerencia situações de bloqueio no banco de dados com mensagens amigáveis.  
4. **Transações**: Utiliza transações para garantir a consistência dos dados:
   - *Commit* em alterações confirmadas.
   - *Rollback* em caso de erro ou cancelamento.
