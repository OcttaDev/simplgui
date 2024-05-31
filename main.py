import PySimpleGUI as sg


sg.theme("reddit")


layout = [[sg.Text("E-mail"), sg.Input(key="email")],
          [sg.Text("Senha"), sg.Input(key="senha", password_char="*")],
          [sg.FolderBrowse("Escolher Pasta Anexos", target="input_anexos"), sg.Input(
              key="input_anexos")],
          [sg.FolderBrowse("Escolher Pasta Planilha", target="input_planilhas"), sg.Input(
              key="input_planilhas")],
          [sg.Button("Salvar")]]


window = sg.Window('Principal', layout)


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == "Salvar":
        email = values['email']
        senha = values['senha']
        anexos = values['input_anexos']
        planilhas = values['input_planilhas']

    print('Hello', values[0], '!')

window.close()
