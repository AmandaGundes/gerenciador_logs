from ..models import Log

def cadastrar_log(log):
    Log.objects.create(descricao=log.descricao, origem=log.origem, data_registro=log.data_registro, level=log.level, usuario=log.usuario, tipo=log.tipo, eventos=log.eventos, detalhes=log.detalhes)

def listar_logs():
    return Log.objects.all()

def listar_log_id(id):
    return Log.objects.get(id=id)

def editar_log(log_bd, log_nova):
    log_bd.descricao = log_nova.descricao
    log_bd.origem = log_nova.origem
    log_bd.data_registro = log_nova.data_registro
    log_bd.level = log_nova.level
    log_bd.tipo = log_nova.tipo
    log_bd.eventos = log_nova.eventos
    log_bd.detalhes = log_nova.detalhes
    log_bd.save(force_update=True)

def remover_log(log_bd):
    log_bd.delete()