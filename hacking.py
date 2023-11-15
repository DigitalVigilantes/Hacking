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


def gerar_email():
    nomes = ['maria', 'joao', 'ana', 'pedro', 'julia', 'carlos', 'lucas', 'isabela', 'mateus']
    sobrenomes = ['silva', 'santos', 'oliveira', 'souza', 'rodrigues', 'pereira', 'almeida']
    provedores = ['gmail.com', 'outlook.com', 'yahoo.com', 'protonmail.com', 'hotmail.com']
    nome = random.choice(nomes)
    sobrenome = random.choice(sobrenomes)
    provedor = random.choice(provedores)
    return f'{nome}{sobrenome}@{provedor}'

def gerar_telefone_fixo():
    return f'({random.randint(10, 99)}) {random.randint(2000, 9999)}-{random.randint(1000, 9999)}'

def gerar_celular():
    return f'({random.randint(10, 99)}) 9{random.randint(4000, 9999)}-{random.randint(1000, 9999)}'

def verificar_dados_gerados():
    print("Gerando informações...\n")
    certidao = gerar_certidao()
    pis_pasep = gerar_pis_pasep()
    cep, endereco, bairro, cidade, estado = gerar_cep(), *gerar_endereco()
    rg = gerar_rg()
    email = gerar_email()
    telefone_fixo = gerar_telefone_fixo()
    celular = gerar_celular()


    print("\nInformações Geradas:")
    print("Certidão Gerada:", certidao)
    print("PIS/PASEP Gerado:", pis_pasep)
    print("CEP:", cep)
    print("Endereço:", endereco)
    print("Bairro:", bairro)
    print("Cidade:", cidade)
    print("Estado:", estado)
    print("RG:", rg)
    print("E-Mail:", email)
    print("Telefone Fixo:", telefone_fixo)
    print("Celular:", celular)

verificar_dados_gerados()
