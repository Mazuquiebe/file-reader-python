class CNABReader:

    def __init__(self, cnab_file=None) -> None:
        self.cnab_file = cnab_file
        self.transaction_types = [
            {
                'id': '1', 'description': 'Débito', 'nature': 'entrada', 'signal': '+' 
            },
            {
                'id': '2', 'description': 'Boleto', 'nature': 'saída', 'signal': '-' 
            },
            {
                'id': '3', 'description': 'Financiamento', 'nature': 'saída', 'signal': '-' 
            },
            {
                'id': '4', 'description': 'Crédito', 'nature': 'entrada', 'signal': '+' 
            },
            {
                'id': '5', 'description': 'Recebimento Emprestimo', 'nature': 'entrada', 'signal': '+' 
            },
            {
                'id': '6', 'description': 'Vendas', 'nature': 'entrada', 'signal': '+' 
            },
            {
                'id': '7', 'description': 'Recebimento TED', 'nature': 'entrada', 'signal': '+' 
            },
            {
                'id': '8', 'description': 'Recebimento DOC', 'nature': 'entrada', 'signal': '+' 
            },
            {
                'id': '9', 'description': 'Aluguel', 'nature': 'saída', 'signal': '-' 
            },
        ]


    def filter_type_transaction(self, type_id):
        for t in self.transaction_types:
            if t['id'] == type_id: return t['description']


    def get_cnab_data(self, cnab_file=None):

        if cnab_file: self.cnab_file = cnab_file

        with open(self.cnab_file, "r", encoding="utf-8") as file:

            cnab_data_list = []
            
            for line in file:
  
                year    = line[1:5]
                month   = line[5:7]
                day     = line[7:9]
                hour    = line[42:44]
                minute  = line[44:46]
                seconds = line[46:48]
  
                date = f"{year}-{month}-{day} {hour}:{minute}:{seconds}"
  
                data = {
                    "type": self.filter_type_transaction(line[:1]),
                    "date": date,
                    "value": int(line[9:19])/ 100,
                    "cpf": line[19:30],
                    "card": line[30:42],
                    "owner": line[48:62],
                    "store": line[62:81],
                }
  
                cnab_data_list.append(data)

            return cnab_data_list


