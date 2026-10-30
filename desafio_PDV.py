"""
Desafio Nível 1: PDV com Descontos Progressivos
Desenvolvido por: Maria Cecilia
"""

def main():
    compras = []
    
    print("=== SISTEMA PDV - DESCONTOS PROGRESSIVOS ===")
    print("Digite 0 no valor da compra para encerrar e exibir o resumo.\n")
    
    while True:
        try:
            valor_original = float(input("Digite o valor da compra (R$): "))
        except ValueError:
            print("Entrada inválida. Digite um número decimal válido.\n")
            continue
            
        if valor_original == 0:
            break
            
        try:
            idade = int(input("Digite a idade do cliente: "))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro para a idade.\n")
            continue
            
        if valor_original < 0 or idade < 0:
            print("Aviso: Valor e idade não podem ser negativos. Tente novamente.\n")
            continue
            
        valor_com_desconto_idade = valor_original * 0.80 if idade >= 65 else valor_original
        
        valor_final = valor_com_desconto_idade * 0.90 if valor_com_desconto_idade > 100 else valor_com_desconto_idade
        
        desconto_total = valor_original - valor_final
        
        print(f"Valor final: R$ {valor_final:.2f}\n")
        
        compras.append({
            "bruto": valor_original,
            "liquido": valor_final,
            "desconto": desconto_total
        })
        
    print("\n" + "=" * 40)
    print("           RESUMO DO DIA")
    print("=" * 40)
    
    if not compras:
        print("Nenhuma compra foi registrada.")
    else:
        total_bruto = sum(c["bruto"] for c in compras)
        total_descontos = sum(c["desconto"] for c in compras)
        total_final = sum(c["liquido"] for c in compras)
        
        print(f"Quantidade de compras: {len(compras)}")
        print(f"Total bruto: R$ {total_bruto:.2f}")
        print(f"Total de descontos: R$ {total_descontos:.2f}")
        print(f"Total final: R$ {total_final:.2f}")
        
    print("=" * 40)

if __name__ == "__main__":
    main()
