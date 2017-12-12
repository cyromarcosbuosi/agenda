


def pacienteValidator(paciente):
    if str(paciente).__len__() <= 2:
        return False

def  dataValidator(data):
    if data is None:
        return False

def horaInitValidator(hora_init):
    if hora_init is None:
        return False

def horaFinValidator(hora_fin,hora_init):
    if int(hora_fin < hora_init):
        return False

def procedimentoValidator(procedimento):
    #Imagino que um procedimento deva ter ao menos duas palavras
    if str(procedimento).__len__()<= 10:
        return False