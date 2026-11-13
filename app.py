servidores = [
    {
        "hostname": "AIX-PRD-01",
        "ambiente": "Producao",
        "softwares": [
            {"nome": "DB2", "versao": "11.5"},
            {"nome": "WebSphere", "versao": "9.0"}
        ]
    },
    {
        "hostname": "AIX-HML-01",
        "ambiente": "Homologacao",
        "softwares": [
            {"nome": "Java", "versao": "8"},
            {"nome": "Python", "versao": "3.11"}
        ]
    }
]

for servidor in servidores:
    print(f"Servidor: {servidor['hostname']}")
    print(f"Ambiente: {servidor['ambiente']}")

    for software in servidor["softwares"]:
        print(f"  - {software['nome']}: {software['versao']}")

    print("-" * 30)
