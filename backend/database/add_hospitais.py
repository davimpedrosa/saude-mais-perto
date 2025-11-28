import sqlite3

con = sqlite3.connect("hospitais.db")
cur = con.cursor()

hospitais = [ 
("Hospital Agamenon Magalhães",
 "Estr. do Arraial, 2723 – Casa Amarela, Recife", "Casa Amarela",
 -8.017608, -34.923355, "(81) 3182-4000",
 "clinico geral, cardiologia, cirurgia geral, uti, emergencia",
 "hospital"),

("Hospital Barão de Lucena",
 "Av. Caxangá, 3860 – Iputinga, Recife", "Iputinga",
 -8.039311, -34.944573, "(81) 3183-1000",
 "clinico geral, pediatria, ginecologia, obstetricia, cirurgia geral",
 "hospital"),

("Hospital Correia Picanço",
 "Av. Recife, 810 – Madalena, Recife", "Madalena",
 -8.061812, -34.909492, "(81) 3184-8100",
 "infectologia, clinico geral, emergencia",
 "hospital"),

("Hospital da Restauração",
 "Av. Gov. Agamenon Magalhães – Derby, Recife", "Derby",
 -8.054260, -34.894230, "(81) 3184-1000",
 "trauma, neurocirurgia, ortopedia, uti, emergencia, cirurgia geral",
 "hospital"),

("Hospital Geral de Areias",
 "R. do Cupim, 90 – Areias, Recife", "Areias",
 -8.090210, -34.939350, "(81) 3355-2000",
 "clinico geral, obstetricia, pediatria",
 "hospital"),

("Hospital Getúlio Vargas",
 "Av. Gen. San Martin, 1941 – Cordeiro, Recife", "Cordeiro",
 -8.065090, -34.927410, "(81) 3184-1600",
 "cirurgia geral, ortopedia, emergencia, clinico geral, uti",
 "hospital"),

("Hospital Metropolitano Oeste – Pelópidas Silveira",
 "BR-408 – Curado, Recife", "Curado",
 -8.080782, -34.997809, "(81) 3183-3000",
 "neurocirurgia, avc, emergencia, uti",
 "hospital"),

("Hospital Otávio de Freitas",
 "BR-232, km 4 – Sancho, Recife", "Sancho",
 -8.071710, -34.951670, "(81) 3181-5555",
 "clinico geral, cirurgia geral, obstetricia, oftalmologia, urologia, emergencia",
 "hospital"),

("Hospital Professor Agamenon Magalhães",
 "Estr. do Arraial, 2723 – Casa Amarela, Recife", "Casa Amarela",
 -8.017608, -34.923355, "(81) 3182-4000",
 "clinico geral, cardiologia, cirurgia geral, emergencia",
 "hospital"),

("Hospital São Lucas",
 "R. Estrada dos Remédios – Madalena, Recife", "Madalena",
 -8.061200, -34.912600, "(81) 3216-1255",
 "clinico geral, pediatria, obstetricia",
 "hospital"),

("Hospital Ulysses Pernambucano",
 "Av. Conselheiro Rosa e Silva, 213 – Graças, Recife", "Graças",
 -8.045100, -34.899800, "(81) 3181-1500",
 "psiquiatria, emergencia",
 "hospital"),

("UPA Ibura (Boa Esperança)",
 "Av. Dois Rios, 500 – Ibura, Recife", "Ibura",
 -8.110890, -34.942410, "(81) 3355-0001",
 "emergencia, clinico geral, pediatria",
 "upa"),

("UPA Caxangá",
 "Av. Caxangá, 4820 – Iputinga, Recife", "Iputinga",
 -8.036810, -34.957190, "(81) 3355-0002",
 "emergencia, clinico geral, pediatria",
 "upa"),

("UPA Campo Grande",
 "Av. João de Barros, 415 – Campo Grande, Recife", "Campo Grande",
 -8.040920, -34.885420, "(81) 3355-0003",
 "emergencia, clinico geral",
 "upa"),

("UPA Torreão (Arruda)",
 "Av. Beberibe, 1390 – Arruda, Recife", "Arruda",
 -8.024540, -34.885030, "(81) 3355-0004",
 "emergencia, pediatria, clinico geral",
 "upa"),

("UPA Mustardinha",
 "Rua Pres. Artur Bernardes, 72 – Mustardinha, Recife", "Mustardinha",
 -8.082920, -34.914560, "(81) 3355-0005",
 "emergencia, clinico geral",
 "upa"),

("UPA Doutor José Mariano (Madalena)",
 "Av. Gov. Agamenon Magalhães, 3040 – Madalena, Recife", "Madalena",
 -8.057680, -34.909110, "(81) 3355-0006",
 "emergencia, clinico geral, ortopedia",
 "upa"),

("UPA Nova Descoberta",
 "Rua Nova Descoberta, 2560 – Nova Descoberta, Recife", "Nova Descoberta",
 -8.016600, -34.926780, "(81) 3355-0007",
 "emergencia, clinico geral",
 "upa"),

("UPA Imbiribeira",
 "Rua Jean Emile Favre, 521 – Imbiribeira, Recife", "Imbiribeira",
 -8.117780, -34.909880, "(81) 3355-0008",
 "emergencia, clinico geral, pediatria",
 "upa"),

("Policlínica Lessa de Andrade",
 "Rua Real da Torre, 585 – Madalena, Recife", "Madalena",
 -8.055820, -34.909900, "(81) 3355-0101",
 "clinico geral, cardiologia, ginecologia, pediatria, dermatologia, endocrinologia",
 "policlinica"),

("Policlínica Amaury Coutinho",
 "Rua Gal. Estilac Leal, 195 – Campina do Barreto, Recife", "Campina do Barreto",
 -8.021880, -34.871310, "(81) 3355-0102",
 "clinico geral, pediatria, ginecologia, odontologia",
 "policlinica"),

("Policlínica Salomão Kelner",
 "Rua Sargento Silvino Macedo, 130 – Água Fria, Recife", "Água Fria",
 -8.014950, -34.881460, "(81) 3355-0103",
 "clinico geral, pediatria, ginecologia, cardiologia",
 "policlinica"),

("Policlínica Clementino Fraga",
 "Rua da Paz, 23 – Afogados, Recife", "Afogados",
 -8.085570, -34.917760, "(81) 3355-0104",
 "clinico geral, pediatria, ginecologia, odontologia",
 "policlinica"),

("Policlínica Arnaldo Marques",
 "Avenida Dois Rios, 101 – Ibura, Recife", "Ibura",
 -8.112260, -34.942200, "(81) 3355-0105",
 "clinico geral, ortopedia, ginecologia, pediatria",
 "policlinica"),

("Policlínica Clementino Fraga II",
 "Rua da Paz, 25 – Cohab, Recife", "Cohab",
 -8.128510, -34.949350, "(81) 3355-0106",
 "clinico geral, pediatria, ginecologia",
 "policlinica"),

("Policlínica Agamenon Magalhães",
 "Rua dos Palmares, 525 – Santo Amaro, Recife", "Santo Amaro",
 -8.055100, -34.885900, "(81) 3355-0107",
 "clinico geral, oftalmologia, ginecologia, pediatria",
 "policlinica"),

("Policlínica Barros Lima",
 "Estrada do Arraial, 1771 – Casa Amarela, Recife", "Casa Amarela",
 -8.017100, -34.916900, "(81) 3355-0108",
 "clinico geral, cardiologia, ginecologia, pediatria",
 "policlinica"),

("Policlínica Gouveia de Barros",
 "Rua dos Palmares, 565 – Boa Vista, Recife", "Boa Vista",
 -8.057000, -34.885400, "(81) 3355-0109",
 "clinico geral, pediatria, endocrinologia, ginecologia",
 "policlinica"),

("Policlínica Guilherme Abath",
 "Rua do Cajueiro, 340 – Beberibe, Recife", "Beberibe",
 -8.012220, -34.889300, "(81) 3355-0110",
 "clinico geral, pediatria, ginecologia, odontologia",
 "policlinica"),

("Policlínica Israel Fonseca",
 "Rua Artur Muniz, 257 – Água Fria, Recife", "Água Fria",
 -8.018240, -34.879600, "(81) 3355-0111",
 "clinico geral, pediatria, ginecologia",
 "policlinica"),

("Policlínica Hélio Mendonça",
 "Rua José Nunes da Cunha, 265 – Jordão, Recife", "Jordão",
 -8.136280, -34.944750, "(81) 3355-0112",
 "clinico geral, pediatria, ginecologia",
 "policlinica"),

("Policlínica Oswaldo Lima",
 "Rua João Simplício, 118 – Brasília Teimosa, Recife", "Brasília Teimosa",
 -8.085310, -34.883090, "(81) 3355-0113",
 "clinico geral, pediatria, ginecologia",
 "policlinica"),

("Policlínica Leôncio Miranda",
 "Rua Amaro Coutinho, 495 – Hipódromo, Recife", "Hipódromo",
 -8.038700, -34.887500, "(81) 3355-0114",
 "clinico geral, pediatria, ginecologia",
 "policlinica"),

("Maternidade Bandeira Filho",
 "Rua José de Holanda, 165 – Afogados, Recife", "Afogados",
 -8.086870, -34.914730, "(81) 3355-0201",
 "maternidade, obstetricia, pediatria",
 "centro"),

("Maternidade Barros Lima",
 "Estrada do Arraial, 1700 – Casa Amarela, Recife", "Casa Amarela",
 -8.016920, -34.916580, "(81) 3355-0202",
 "maternidade, obstetricia, pediatria",
 "centro"),

("Centro Especializado em Reabilitação (CER)",
 "Av. Saturnino de Brito, 385 – Ilha Joana Bezerra, Recife", "Ilha Joana Bezerra",
 -8.066200, -34.889900, "(81) 3355-0203",
 "reabilitacao, fisioterapia, terapia ocupacional, fonoaudiologia",
 "centro"),

("CAPS AD Boa Vista",
 "Av. João de Barros, 555 – Boa Vista, Recife", "Boa Vista",
 -8.056800, -34.889220, "(81) 3355-0204",
 "psiquiatria, apoio psicossocial, dependencia quimica",
 "centro"),

("CAPS Casa Forte",
 "Rua da Harmonia, 255 – Casa Forte, Recife", "Casa Forte",
 -8.032800, -34.924200, "(81) 3355-0205",
 "psiquiatria, psicologia, apoio psicossocial",
 "centro"),

("CAPS Jordão",
 "Rua Maria Zacarias, 70 – Jordão, Recife", "Jordão",
 -8.138720, -34.944100, "(81) 3355-0206",
 "psiquiatria, psicologia, apoio psicossocial",
 "centro"),

("Centro Médico Senador José Ermírio de Moraes",
 "Rua Félix de Brito, 100 – Pina, Recife", "Pina",
 -8.093710, -34.881220, "(81) 3355-0207",
 "clinico geral, cardiologia, pediatria, ginecologia",
 "centro"),

("Centro de Saúde Gaspar Regueira",
 "Rua Amélia, 105 – Derby, Recife", "Derby",
 -8.055330, -34.893680, "(81) 3355-0208",
 "clinico geral, vacinacao, pediatria",
 "centro"),

("Centro de Saúde Vila Tamandaré",
 "Rua Major Codeceira, 115 – Afogados, Recife", "Afogados",
 -8.086100, -34.916500, "(81) 3355-0209",
 "clinico geral, vacinacao, pediatria",
 "centro"),

("Centro de Saúde Manguinhos",
 "Rua Padre Carapuceiro, 300 – Pina, Recife", "Pina",
 -8.099880, -34.884100, "(81) 3355-0210",
 "clinico geral, pediatria, ginecologia",
 "centro"),

("Centro de Saúde Dr. José Barbosa",
 "Av. Visconde de Albuquerque, 1020 – Madalena, Recife", "Madalena",
 -8.058550, -34.914260, "(81) 3355-0211",
 "clinico geral, pediatria, ginecologia",
 "centro"),

("CTA/SAE Santo Amaro",
 "Av. Mário Melo, 1000 – Santo Amaro, Recife", "Santo Amaro",
 -8.053620, -34.881330, "(81) 3355-0212",
 "infectologia, testagem, aconselhamento",
 "centro"),

("CEO Recife – Centro de Especialidades Odontológicas",
 "Rua do Apolo, 220 – Recife Antigo, Recife", "Recife Antigo",
 -8.061860, -34.871750, "(81) 3355-0213",
 "odontologia, endodontia, periodontia",
 "centro"),

("CEO Afogados",
 "Rua da Independência, 200 – Afogados, Recife", "Afogados",
 -8.087800, -34.915500, "(81) 3355-0214",
 "odontologia, endodontia, periodontia",
 "centro"),

("CEO Ibura",
 "Rua Dois Rios, 200 – Ibura, Recife", "Ibura",
 -8.112050, -34.942900, "(81) 3355-0215",
 "odontologia, pediatria odontologica",
 "centro"),

("USF Alto do Reservatório",
 "Rua Alto do Reservatório, 120 – Dois Unidos, Recife", "Dois Unidos",
 -8.010930, -34.907720, "(81) 3355-0301",
 "clinico geral, enfermagem, vacinacao, odontologia",
 "usf"),

("USF Linha do Tiro",
 "Rua Linha do Tiro, 350 – Beberibe, Recife", "Linha do Tiro",
 -8.010410, -34.889090, "(81) 3355-0302",
 "clinico geral, enfermagem, vacinacao, pediatria",
 "usf"),

("USF Beberibe",
 "Rua José dos Santos, 95 – Beberibe, Recife", "Beberibe",
 -8.015850, -34.886800, "(81) 3355-0303",
 "clinico geral, enfermagem, vacinacao",
 "usf"),

("USF Morro da Conceição",
 "Rua do Morro, 420 – Morro da Conceição, Recife", "Morro da Conceição",
 -8.013420, -34.903110, "(81) 3355-0304",
 "clinico geral, enfermagem, vacinacao, odontologia",
 "usf"),

("USF Água Fria",
 "Rua Sargento Silvino Macedo, 200 – Água Fria, Recife", "Água Fria",
 -8.014940, -34.880400, "(81) 3355-0305",
 "clinico geral, enfermagem, pediatria",
 "usf"),

("USF Alto da Bela Vista",
 "Rua Bela Vista, 150 – Vasco da Gama, Recife", "Vasco da Gama",
 -8.025280, -34.927100, "(81) 3355-0306",
 "clinico geral, enfermagem, vacinacao",
 "usf"),

("USF Cajueiro",
 "Rua do Cajueiro, 300 – Cajueiro, Recife", "Cajueiro",
 -8.017700, -34.884300, "(81) 3355-0307",
 "clinico geral, enfermagem, vacinacao, odontologia",
 "usf"),

("USF Curado",
 "Rua General Polidoro, 180 – Curado, Recife", "Curado",
 -8.087800, -34.996900, "(81) 3355-0308",
 "clinico geral, enfermagem, pediatria",
 "usf"),

("USF Ibura",
 "Rua Dois Rios, 210 – Ibura, Recife", "Ibura",
 -8.112300, -34.943100, "(81) 3355-0309",
 "clinico geral, enfermagem, vacinacao, odontologia",
 "usf"),

("USF Brasília Teimosa",
 "Rua João Simplício, 130 – Brasília Teimosa, Recife", "Brasília Teimosa",
 -8.085520, -34.883200, "(81) 3355-0310",
 "clinico geral, enfermagem, vacinacao",
 "usf"),

("USF Coqueiral",
 "Rua Sucupira do Norte, 55 – Coqueiral, Recife", "Coqueiral",
 -8.054910, -34.973880, "(81) 3355-0311",
 "clinico geral, enfermagem, pediatria",
 "usf"),

("USF Passarinho",
 "Rua da Esperança, 210 – Passarinho, Recife", "Passarinho",
 -7.990800, -34.922300, "(81) 3355-0312",
 "clinico geral, enfermagem, vacinacao",
 "usf"),

("USF Lagoa Encantada",
 "Rua Lagoa Encantada, 400 – Ibura, Recife", "Ibura",
 -8.124200, -34.940500, "(81) 3355-0313",
 "clinico geral, enfermagem, vacinacao, pediatria",
 "usf"),

("USF Bomba do Hemetério",
 "Rua São Bento, 180 – Bomba do Hemetério, Recife", "Bomba do Hemetério",
 -8.011200, -34.898200, "(81) 3355-0314",
 "clinico geral, enfermagem, odontologia",
 "usf"),

("USF Lagoa do Araçá",
 "Rua Lagoa do Araçá, 55 – Imbiribeira, Recife", "Imbiribeira",
 -8.111000, -34.906700, "(81) 3355-0315",
 "clinico geral, enfermagem, vacinacao",
 "usf"),
]

# Inserindo todos os registros no banco
cur.executemany("""
INSERT INTO hospitais (nome, endereco, bairro, latitude, longitude, telefone, especialidades, tipo)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", hospitais)

con.commit()
con.close()

print("Unidades de saúde adicionadas com sucesso!")


