import PySimpleGUI as sg
import requests
types = []


def get_type():

    return type


def set_type(new_type):
    global type
    type.clear()
    type = new_type

def login():
    # Definir o layout da janela
    sg.theme('DarkRed1')
    # Defina as cores para os elementos do tema


    layout = [
        [sg.Text('Usuario:', size=(6,1)), sg.Input(key='-USERNAME-', size=(25,1))],
        [sg.Text('Senha:', size=(6,1)), sg.Input(key='-PASSWORD-', password_char='*', size=(25,1))],
        [sg.Button('Login', size=(21,1))]
    ]

    return sg.Window('login window', layout, finalize=True, resizable=True, element_justification='r')


def cadastro():
    # Definir o layout da janela
    sg.theme('DarkRed1')
    # Defina as cores para os elementos do tema
    image_url = 'https://firebasestorage.googleapis.com/v0/b/iot2023-8c540.appspot.com/o/eletrodos.png?alt=media'

    response = requests.get(image_url)

    if response.status_code == 200:
        image_bytes = response.content


    layout = [
        [sg.Image(data=image_bytes)],
        [sg.Text('CPF do Paciente:', size=(20,1)), sg.Input(key='-CPF-', size=(25,1))],
        [sg.Button('Iniciar Exame', size=(21,1))],
        [sg.Button('Deslogar', size=(21, 1))],

    ]

    return sg.Window('login window', layout, finalize=True, resizable=True, element_justification='r')


def Tabela(data_id, cpf_ids, cpf):
    global type

    sg.theme('DarkRed1')

    headings = ['data', 'nome' , 'dado']
    type = [(data_id[key]['data'], data_id[key]['nome'], data_id[key]['dado'] ) for key in data_id]
    print(type)
    type = sorted(type, key=lambda x: x[0])
    layout = [
        [sg.T("CPF:", size=(10, 1), visible=True, key="-CPF1-"), sg.Combo(cpf_ids, key="-CPF2-", enable_events=True, size=(21, 5), visible=True, default_value=cpf)],
        [sg.Table(values=type, headings=headings, max_col_width=25, auto_size_columns=False, justification='right', vertical_scroll_only=False, enable_events=True, key='-TABLE-', row_height=35)],
        [sg.Button('Analisar Exame', key="-ACD-"), sg.Button('Deslogar')],
    ]
    return sg.Window('Analyze', layout, finalize=True, resizable=True )


def plot_exame():
    sg.theme('DarkRed1')

    button_size = (36,6)
    layout = [

        [sg.Canvas(size=(700,500), background_color='grey', key='canvas')],
        [sg.Button('Retornar')],

    ]
    return sg.Window('graph window', layout, finalize=True, resizable=True, element_justification='c')