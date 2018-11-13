#Função que calcula quantos dias no mês o cara 12/36 vaitrabalhar no mes.
def calc_transporte_12_36( data, valor ):
	dia = int(data.split('/')[0])
	mes = int(data.split('/')[1])
	ano = int(data.split('/')[2])
	if mes == 12:
		proximo_mes = 1
		proximo_ano = ano+1
	dias_no_mes = date(proximo_ano, proximo_mes, 1) - date(ano, mes, dia)
	qtd_dias = 0
	while dias_no_mes.days > 0:
	  #print(dias_no_mes)
	  dias_no_mes = dias_no_mes - hora_trabalhada - hora_folgada
	  qtd_dias+=1
	print("Dias trabalhados: ", qtd_dias)
	print("Valor do vale: R$%.2f" % (qtd_dias*valor*2))
	
calc_transporte_12_36('01/12/2018', 4.10)