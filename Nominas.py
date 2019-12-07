#Nominas trabajadores
#Autor: Oscar Carranza
#Referencias:LFT
#UMA=84.49  #valor del UMA en el 2019
UMA=80.6  #valor del UMA en el 2018


def baseGravable():
	print()
	salarioMensual=float(input("Ingrese su salario Mensual  "))
	
	bonos=str(input("Tienes bonos? Ingrese \'S\' para sí o  \'N\' para no  "))
	if (bonos=='S'):
		bonosP=float(input("Ingrese cantidad recibida en bonos  "))
	else:
		bonosP=0
	
	horasExtra=str(input("Trabajo horas extras? Ingrese \'S\' para sí o  \'N\' para no  "))
	if (horasExtra=='S'):
		n=int(input("Ingrese la cantidad de horas extras trabajadas  "))
		jornada=int(input("Ingrese 1 si su jornada es diurna, 2 si su jornada es nocturna o 3 si su jornada es mixta  "))
		if(jornada==1):
			horas=8
		else:
			if(jornada==2):
				horas=7
			else:
				if(jornada==3):
					horas=7.5
				else:
					horas=0
					print("Error. Se tomaran en cuenta 0 horas extra ")
		
		if((horas !=0) & (n>0)):
			bandera=True #bandera para saber si se trabajaroin horas extras
			if (n<9):
				#las 8 primeras horas se pagan al doble
				salarioHora= (salarioMensual/30)/n
				hE=2*salarioHora*n
				hE_1=hE/2  #El 50% no exenta
				if ((5*UMA)<hE_1):
					hE_2=hE_1-(5*UMA)
				else:
					hE_2=0 #exenta
				montoHE1=hE_1+hE_2
				montoHE2=0
			if (n>=9):
				m=n-8
				n=8
				#las 8 primeras horas se pagan al doble
				salarioHora= (salarioMensual/30)/n
				hE=2*salarioHora*n
				hE_1=hE/2  #El 50% no exenta
				if ((5*UMA)<hE_1):
					hE_2=hE_1-(5*UMA)
				else:
					hE_2=0 #exenta
				montoHE1=hE_1+hE_2
				#De la 9 en adelante horas extra no exentan
				#De la 9 en adelante horas extra se pagan al triple
				montoHE2=3*salarioHora*m
		
		totalHorasExtras=montoHE1+montoHE2
		totalHorasExtras_paraPercepciones=hE+montoHE2
	else:
		totalHorasExtras=0
		bandera=False
	

	base=(salarioMensual/2)+bonosP+totalHorasExtras

	percepciones=0
	if (bandera):
		#Se trabajaron horas extras
		percepciones=(salarioMensual/2)+bonosP+totalHorasExtras_paraPercepciones
	else:
		percepciones=(salarioMensual/2)+bonosP

	return base, percepciones, salarioMensual
#FIN DE LA FUNCIÓN


def cuotaIMSS(salarioMensual):
	salarioDiario=salarioMensual/30
	aguinaldo=15*salarioDiario/365  #Se consideran 15 días
	anos=int(input("Ingrese el numero de años que ha laborado para la empresa  "))

	if(anos==0):
		diasvacaciones=0
	else:
		if(anos==1):
			diasvacaciones=6
		else:
			if(anos==2):
				diasvacaciones=8
			else:
				if(anos==3):
					diasvacaciones=10
				else:
					if(anos==4):
						diasvacaciones=12
					else:
						if((anos==5) | (anos==6) | (anos==7) | (anos==8) | (anos==9) ):
							diasvacaciones=14
						else:
							if((anos==10) | (anos==11) | (anos==12) | (anos==13) | (anos==14) ):
								diasvacaciones=16
							#Y ahi le sigo...

	primaVacacional=anos*salarioDiario*(0.25)/365

	subtotal= salarioDiario+aguinaldo+primaVacacional
	SBCquincenal=subtotal*15

	#Cuotas:
	prestEspecie=SBCquincenal*0.00375
	prestDinero=SBCquincenal*0.0025
	invalidez=SBCquincenal*0.00625
	cesantia=SBCquincenal*0.01125
	if((SBCquincenal-(3*UMA*15))>0):
		cuotaAdicional=(SBCquincenal-(3*UMA*15))*(0.004)
	else:
		cuotaAdicional=0

	IMSS=prestEspecie+prestDinero+invalidez+cesantia+cuotaAdicional
	return IMSS
#FIN DE LA FUNCIÓN


def ISR(base):
	#Calculo del impuesto quincenal del Art 113 LISR
	if(base>0 and base<=244.8):
		cuotaFija=0
		porcentaje=0.0192
		limInf=0
	else:
		if(base>244.8 and base<=2077.5):
			cuotaFija=4.65
			porcentaje=0.064
			limInf=244.81
		else:
			if(base>2077.5 and base<=3651):
				cuotaFija=121.95
				porcentaje=0.1088
				limInf=2077.51
			else:
				if(base>3651 and base<=4244.1):
					cuotaFija=293.25
					porcentaje=0.16
					limInf=3651.1
				else:
					if(base>4244.1 and base<=5081.4):
						cuotaFija=388.05
						porcentaje=0.1792
						limInf=4244.11
					else:
						if(base>5081.4 and base<=10248.45):
							cuotaFija=538.2
							porcentaje=0.2136
							limInf=5081.41
						else:
							if(base>10248.45 and base<=16153.05):
								cuotaFija=1641.75
								porcentaje=0.2352
								limInf=10248.46
							else:
								cuotaFija=3030.6
								porcentaje=0.3
								limInf=16153.06

	excedenteLimInf=base-limInf
	impuestoMarginal=excedenteLimInf*porcentaje
	ISR_parte1=impuestoMarginal+cuotaFija


	#Subsidio para el empleo (quincenal)
	if(base>0 and base<=872.85):
		sub=200.85
	else:
		if(base>872.85 and base<=1713.6):
			sub=200.7
		else:
			if(base>1713.6 and base<=1745.7):
				sub=193.8
			else:
				if(base>1745.7 and base<=2193.75):
					sub=188.7
				else:
					if(base>2193.75 and base<=2327.55):
						sub=174.75
					else:
						if(base>2327.55 and base<=2632.65):
							sub=160.35
						else:
							if(base>2632.65 and base<=3071.4):
								sub=145.35
							else:
								if(base>3071.4 and base<=3510.15):
									sub=125.1
								else:
									if(base>3510.15 and base<=3642.6):
										sub=107.4
									else:
										sub=0

	ISR_aRetener=ISR_parte1-sub
	return ISR_aRetener




#Main:
print()
print("Programa desarrollado para el calculo del neto a pagar a un trabajador a la quincena")
print("Desarrollado por Oscar Carranza")
print("**********NOMINA**********" +'\n')

(base, percepciones, salarioMensual) =baseGravable()
print("Percepciones: " + str(percepciones))

Imss=cuotaIMSS(salarioMensual)
Isr=ISR(base)

deducciones=Imss+Isr
print("Deducciones: " + str(deducciones))

print()
print("Pago quincenal al trabajador: " +str(percepciones-deducciones))