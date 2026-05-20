
from ex_026 import *
from rich import inspect, print

func1 = Horista(nome="João", horas_trab=200, valor_hora=15)
func1.calcular_sal()
func1.analisar_sal()
#inspect(func1)

func2 = Mensalista(nome="José", sal_bruto=4000)
func2.calcular_sal()
func2.analisar_sal()
