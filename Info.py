import random
import string

def gerar_certidao():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

def gerar_pis_pasep():
    return ''.join(random.choices(string.digits, k=11))

def gerar_cep():
    return f'{random.randint(10000, 99999)}-{random.randint(100, 999)}'

def gerar_endereco():
    logradouros = ['Rua', 'Avenida', 'Travessa', 'Alameda']
    ruas = ['Renato Braga', 'das Flores', 'São Paulo', 'dos Girassóis', 'José da Silva']
    bairros = ['Vila Santa Isabel', 'Centro', 'Jardim América', 'Bairro Novo', 'Alto da Colina']
    cidades = ['Taubaté', 'São Paulo', 'Rio de Janeiro', 'Porto Alegre', 'Belo Horizonte']
    estados = ['SP', 'RJ', 'MG', 'RS', 'BA']
    return f'{random.choice(logradouros)} {random.choice(ruas)}', random.choice(bairros), \
           random.choice(cidades), random.choice(estados)

def gerar_rg():
    return f'{random.randint(10_000_000, 99_999_999)}-{random.randint(1, 9)}'

def gerar_cartao_credito():
    return f'{random.randint(4000, 6999)} {random.randint(1000, 9999)} {random.randint(1000, 9999)} {random.randint(1000, 9999)}'

def gerar_data_validade():
    return f'{random.randint(1, 12):02d}/{random.randint(2023, 2030)}'

def gerar_cvv():
    return f'{random.randint(100, 999)}'

def gerar_cpf():
    return f'{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}-{random.randint(10, 99)}'

def gerar_data_nascimento():
    return f'{random.randint(1, 28):02d}/{random.randint(1, 12):02d}/{random.randint(1940, 2004)}'

def gerar_sexo():
    return random.choice(['Masculino', 'Feminino'])

def gerar_signo():
    signos = ['Áries', 'Touro', 'Gêmeos', 'Câncer', 'Leão', 'Virgem', 'Libra', 'Escorpião', 'Sagitário', 'Capricórnio', 'Aquário', 'Peixes']
    return random.choice(signos)

def gerar_nome_completo():
    nomes = ['Kevin', 'Gustavo', 'Raul', 'Vanessa', 'Eduarda', 'Jorge', 'Maria', 'Pedro', 'Paulo', 'Ana']
    sobrenomes = ['dos Santos', 'da Silva', 'Mendes', 'Rocha', 'Oliveira', 'Ferreira', 'Almeida', 'Souza']
    return f'{random.choice(nomes)} {random.choice(sobrenomes)}'

def gerar_email(nome_completo):
    nome = nome_completo.lower().replace(' ', '') + str(random.randint(1, 999))
    dominios = ['gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com']
    return f'{nome}@{random.choice(dominios)}'

def gerar_senha():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(random.randint(10, 15)))

def gerar_telefones():
    return f'Telefone: ({random.randint(10, 99)}) {random.randint(2000, 9999)}-{random.randint(1000, 9999)}', \
           f'Celular: ({random.randint(10, 99)}) {random.randint(90000, 99999)}-{random.randint(1000, 9999)}'

def gerar_altura():
    return round(random.uniform(1.50, 2.00), 2)

def gerar_peso():
    return random.randint(50, 100)

def gerar_tipo_sanguineo():
    tipos = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    return random.choice(tipos)

def gerar_cor_favorita():
    cores = ['vermelho', 'azul', 'verde', 'amarelo', 'roxo', 'laranja', 'preto', 'branco']
    return random.choice(cores)

def verificar_dados_gerados():
    while True:
        print("Gerando informações...\n")
        certidao = gerar_certidao()
        pis_pasep = gerar_pis_pasep()
        cep, endereco, bairro, cidade, estado = gerar_cep(), *gerar_endereco()
        rg = gerar_rg()
        cartao_credito = gerar_cartao_credito()
        data_validade = gerar_data_validade()
        cvv = gerar_cvv()
        cpf = gerar_cpf()
        data_nascimento = gerar_data_nascimento()
        sexo = gerar_sexo()
        signo = gerar_signo()
        nome_completo = gerar_nome_completo()
        email = gerar_email(nome_completo)
        senha = gerar_senha()
        altura = gerar_altura()
        peso = gerar_peso()
        tipo_sanguineo = gerar_tipo_sanguineo()
        cor_favorita = gerar_cor_favorita()

        # Verificar se não há dados repetidos
        dados_gerados = [certidao, pis_pasep, cep, endereco, bairro, cidade, estado, rg, cartao_credito, data_validade,
                         cvv, cpf, data_nascimento, sexo, signo, nome_completo, email, senha, altura, peso, tipo_sanguineo, cor_favorita]

        if len(set(dados_gerados)) == len(dados_gerados):
            break
        else:
            print("Foram gerados dados repetidos. Tentando novamente...\n")

    # Exibir as informações
    print("Certidão Gerada:", certidao)
    print("PIS/PASEP Gerado:", pis_pasep)
    print("CEP", cep)
    print("Endereço", endereco)
    print("Bairro", bairro)
    print("Cidade", cidade)
    print("Estado", estado)
    print("RG:", rg)
    print("Cartão de Crédito:")
    print("Número do Cartão", cartao_credito)
    print("Data de Validade", data_validade)
    print("Código Segurança (CVV)", cvv)
    print("Dados Pessoais")
    print("Nome", nome_completo)
    print("CPF", cpf)
    print("Data de Nascimento", data_nascimento)
    print("Sexo", sexo)
    print("Signo", signo)
    print("Filiação")
    print("Mãe Vanessa Eduarda")
    print("Pai Jorge Gustavo dos Santos")
    print("Online")
    print("E-Mail", email)
    print("Senha", senha)
    print("Endereço")
    print("CEP", cep)
    print("Endereço", endereco)
    print("Número", random.randint(1, 999))
    print("Bairro", bairro)
    print("Cidade", cidade)
    print("Estado", estado)
    telefones = gerar_telefones()
    print(telefones[0])
    print(telefones[1])
    print("Características Físicas")
    print("Altura", altura)
    print("Peso", peso)
    print("Tipo Sanguíneo", tipo_sanguineo)
    print("Cor Favorita", cor_favorita)

verificar_dados_gerados()
