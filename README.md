# Sistema PDV com Descontos Progressivos

**Autora:** Maria Cecilia

## O que o código faz
O sistema consiste em um Ponto de Venda (PDV) para cálculo automático de descontos progressivos em transações comerciais. Ele calcula abatimentos cumulativos com base na idade do comprador e no valor acumulado da compra, mantendo um histórico das operações da sessão e apresentando o balanço financeiro consolidado ao término das operações.

## Como ele faz
1. **Entrada e Validação:** Solicita o valor da transação e a idade do cliente. Caso o usuário insira tipos incompatíveis ou valores negativos, o sistema emite um aviso e reinicia a captura via `continue`.
2. **Desconto de Idade:** Para clientes com 65 anos ou mais, aplica um desconto de 20% sobre o valor inicial da compra.
3. **Desconto por Valor:** Avalia o valor remanescente do passo anterior. Se exceder R$ 100,00, aplica uma redução adicional de 10% sobre essa quantia já reduzida.
4. **Histórico e Encerramento:** O loop é interrompido ao informar `0` no valor da compra. Cada transação válida é gravada em uma lista usando `.append()`. Por fim, o relatório consolida a quantidade total de vendas, a receita bruta, o total concedido em descontos e a receita líquida.

## Como rodar
Para executar a aplicação, navegue até a pasta `nivel_1` e execute o comando:

```bash
python pdv.py
