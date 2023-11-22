import matplotlib.pyplot as plt
import janela
import PySimpleGUI as sg
import plot
import firebase_utils


enable_table = False
firebase_utils.initialize_firebase_app()
db = firebase_utils.get_firestore_client()
firebase_utils.initialize_firebase_app_auth()
auth=firebase_utils.get_firestore_client_auth()
storage=firebase_utils.get_firestore_client_storage()


cpf_ids = "NONE"
data = 0
# loop interface ----------------------------------------------------------------

janela0, janela1, janela2, janela3, janela4 = janela.login(), None, None, None, None

while True:

    window,event,values = sg.read_all_windows()
    if window == janela0:

        if event == sg.WINDOW_CLOSED:
            break


        if event == 'Cancelar':
            break


        elif event == 'Login' or (event == '-PASSWORD-' and values['-PASSWORD-'] == '\r'):




            email = values['-USERNAME-']
            password = values['-PASSWORD-']
            try:
                auth.sign_in_with_email_and_password(email, password)

                nome_colecao = "colecao"
                nome_documento = "Users"
                subcolecao = "Accounts"
                subcolecao_ref = db.collection(nome_colecao).document(nome_documento).collection(subcolecao)
                docs = subcolecao_ref.get()
                data_user = {}

                for doc in docs:
                    data_user[doc.id] = doc.to_dict()
                    print(data_user)

                for key, value in data_user.items():
                    if value['email'] == email:
                        tipo = value['tipo']
                        print(tipo)
                        break
                if tipo == "medico":

                    doc_ref = db.collection('colecao').document('Test')
                    cpf_ids = []
                    collections_ref = doc_ref.collections()

                    for collection_ref in collections_ref:
                        cpf_ids.append(collection_ref.id)

                    nome_colecao = "colecao"
                    nome_documento = "Test"
                    subcolecao = cpf_ids[0]
                    id_documento = "exames"
                    nome_subcolecao = "data"

                    subcolecao_ref = db.collection(nome_colecao).document(nome_documento).collection(
                        subcolecao).document(id_documento).collection(nome_subcolecao)

                    docs = subcolecao_ref.get()
                    data_id = {}

                    for doc in docs:
                        data_id[doc.id] = doc.to_dict()

                    print(data_id)
                    print(cpf_ids)
                    print(cpf_ids[0])

                    janela0.hide()
                    janela1 = janela.Tabela(data_id, cpf_ids, cpf_ids[0])
                elif tipo == "paciente":
                    janela0.hide()
                    janela3 = janela.Tabela(data)
                elif tipo == "enfermeira":
                    janela0.hide()
                    janela4 = janela.cadastro()

            except:
                sg.popup('Login Invalide!')




    if window == janela1:
        if event == sg.WINDOW_CLOSED:
            break

        elif event == '-CPF2-':
            try:

                new_cpf = values['-CPF2-']
                nome_colecao = "colecao"
                nome_documento = "Test"
                subcolecao = new_cpf
                id_documento = "exames"
                nome_subcolecao = "data"


                subcolecao_ref = db.collection(nome_colecao).document(nome_documento).collection(
                    subcolecao).document(id_documento).collection(nome_subcolecao)


                docs = subcolecao_ref.get()
                data_id5 = {}

                for doc in docs:
                    data_id5[doc.id] = doc.to_dict()


                type = [(data_id5[key]['data'], data_id5[key]['nome'], data_id5[key]['dado']) for key in data_id5]

                type = sorted(type, key=lambda x: x[0])
                window['-TABLE-'].Update(values=type)
                janela.set_type(type)
            except:
                sg.popup('Project without data !')


        if event == 'Deslogar':
            janela1.hide()
            janela0.un_hide()

        elif event == '-TABLE-':

            if not values['-TABLE-']:
                continue

            selected_row_index = values['-TABLE-'][0]
            print(selected_row_index)
            var = janela.get_type()
            selected_row = var[selected_row_index]
            data = selected_row[0]
            nome = selected_row[1]
            exame = selected_row[2]
            print(exame)
            exame = [float(val) for val in exame.split(';') if val]  # Converte e ignora valores vazios
            print(exame)

            # Criar uma lista de índices para os valores (pode ser o tempo, por exemplo)
            indices = list(range(len(exame)))
            print(indices)




            enable_table = True

        elif event == '-ACD-':
            if enable_table == False:
                sg.popup('Exame não selecionado!')
            else:

                try:
                    janela1.hide()


                    if janela2 == None:
                        janela2 = janela.plot_exame()
                    else:
                        janela2.un_hide()

                    graph = janela2['canvas']
                    canvas = plot.draw_figure(janela2['canvas'].TKCanvas, plot.plot_time_fig(exame, 0.002))
                except:
                    sg.popup('Dado corrompido! ')


    if window == janela2:

        if event == sg.WINDOW_CLOSED:
            break

        elif event == 'Retornar':
            plt.clf()
            canvas.get_tk_widget().destroy()
            janela2.hide()
            janela1.un_hide()
            janela1.refresh()

    if window == janela3:

        if event == sg.WINDOW_CLOSED:
            break


    if window == janela4:

        if event == sg.WINDOW_CLOSED:
            break

        if event == "Iniciar Exame":

            cpf = values['-CPF-']
            # Converta o conteúdo de string para bytes
            cpf_txt = cpf.encode('utf-8')
            storage.child("cpf.txt").put(cpf_txt)

        if event == "Deslogar":
            janela4.hide()
            janela0.un_hide()
