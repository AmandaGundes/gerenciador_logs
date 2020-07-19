class log():
    def __init__(self, descricao, origem, data_registro, level, usuario, tipo, eventos, detalhes):
        self.__descricao = descricao
        self.__origem = origem
        self.__data_registro = data_registro
        self.__level = level
        self.__usuario = usuario
        self.__tipo = tipo
        self.__eventos = eventos
        self.__detalhes = detalhes

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def origem(self):
        return self.__origem

    @origem.setter
    def origem(self, origem):
        self.__origem = origem

    @property
    def data_registro(self):
        return self.__data_registro

    @data_registro.setter
    def data_registro(self, data_registro):
        self.__data_registro = data_registro

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level):
        self.__level = level

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def eventos(self):
        return self.__eventos

    @eventos.setter
    def eventos(self, eventos):
        self.__eventos = eventos

    @property
    def detalhes(self):
        return self.__detalhes

    @detalhes.setter
    def detalhes(self, detalhes):
        self.__detalhes = detalhes
