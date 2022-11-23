import matplotlib.pyplot as plt 
import random as r

def sjf(number_process):
    list_name_process = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T"]
    id_process = list_name_process[0:number_process]

    #tempo de processos aleatórios
    process_time = [r.randint(1,20) for i in range(number_process)]

    list_dict = []
    for i in range(number_process):
        dict = {"name process":id_process[i],"time process": process_time[i]}
        list_dict.append(dict)

    #revertendo a lista de dicts
    list_dict = sorted(list_dict, key=lambda k : k['time process'])

    id_process = []
    time_process = []
    for i in list_dict:
        id_process.append(i["name process"])
        time_process.append(i["time process"])

    index_time_run = 0 #index de controle de processo que roda atualmente
    time_run = 0 # controlador de tempo de processos
    list_run = [] # lista auxiliar de tempo de processos 
    list_wait_run = [] # lista auxiliar de tempo de espera

    for i in range(number_process):
        #zerando as listas auxiliares
        list_run.append(0)
        list_wait_run.append(0)

    plt.style.use('ggplot')
    plt.ion()

    while index_time_run < number_process:
        if time_run < time_process[index_time_run]: # verificando se o tempo de processo ainda é igual ou menor que na lista original
            list_run[index_time_run] = list_run[index_time_run] + 1 # incrementando o tempo na lista auxiliar de tempo de processos
            #incrementando as outras pocições de espera na lista auxiliar de espera
            for i in range(index_time_run +1 ,len(list_wait_run)): 
                list_wait_run[i] = list_wait_run[i] + 1
            time_run = time_run + 1
        else:
            time_run = 0
            index_time_run = index_time_run + 1
        x = id_process
        y1 = list_wait_run
        y2 = list_run
  
        plt.bar(x,y1, color='r')
        plt.bar(x,y2,bottom=y1, color='b')
        plt.ylabel("tempo de processo em segundos")
        plt.xlabel("id do processo")
        plt.title("processo X tempo de processamento SJF")

        plt.pause(1)
  

    plt.ioff()

          
