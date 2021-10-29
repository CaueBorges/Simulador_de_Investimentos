while  True :
    print ( "-----------------------------------" )
    print ( "Seja bem-vindo (a) ao MyBank" )
    print ( "SIMULADOR DE INVESTIMENTO" )
    print ( "-----------------------------------" )
    print ( "Titulos disponiveis:" )
    print ( "1 - Tesouro Prefixado 2024" )
    print ( "2 - Tesouro Prefixado 2026" )

    cliente  =  str ( input ( "Qual titulo você gostaria de fazer uma simulação ?:" ))
    investir  =  float ( input ( "Qual o valor você quer investir ?:" ))
    mês  =  float ( input ( "Se você for investir todo o mês, qual o valor ?:" ))

    if  cliente  ==  '1' :
        total  = (mês * 32 ) + investir 
        bruto  =  total  + ( total * 0.1656236 )
        IR = bruto * 0.023415
        ValorIR = bruto - IR
        b3  = bruto * 0.003
        valorliquido  =  ValorIR  -  b3
        aportes = 32

    else :
        total  = ( mês  *  50 ) +  investir 
        bruto  =  total  + ( total * 0.2799 )
        IR = bruto * 0.03402
        ValorIR = bruto - IR
        b3 = bruto * 0.0045
        valorliquido  =  ValorIR  -  b3
        aportes = 50


    print ( "-----------------------------------" )       
    print ( "RESULTADO DA SIMULAÇÃO" )
    print ( "-----------------------------------" )
    print ( "Valor inicial investido: {}" .format( investir ))
    print ( "Aportes de {} por {} meses" .format( mês , aportes ))
    print ( "Valor investido total de {}" .format( total ))
    print ( "-----------------------------------" )  
    print ( "Valor Bruto: {}" .format( bruto ))
    print ( "IR: {}" .format( IR ))
    print ( "Taxa da B3: {}" .format( b3 ))
    print ( "Valor Liquido: {}" .format( valorliquido ))
    print ( "-----------------------------------" )
    opcao  =  str ( input ( "Deseja realizar outra simulação? s / n:" ))
    if  opcao  ==  'n' :
        break
print ( "Progrma Encerrado" )