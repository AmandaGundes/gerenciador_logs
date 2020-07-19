from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ..forms import LogForm
from ..entidades.log import log
from ..services import log_service

@login_required()
def listar_logs(request):
    logs = log_service.listar_logs()
    return render(request, 'logs/listar_logs.html', {"logs": logs})

@login_required()
def detalhar_log(request, id):
    det_log = log_service.listar_log_id(id)
    return render(request, 'logs/detalhar_log.html', {"det_log": det_log})

@login_required()
def cadastrar_log(request):
    if request.method == 'POST':
        form_log = LogForm(request.POST)
        if form_log.is_valid():
            descricao = form_log.cleaned_data["descricao"]
            origem = form_log.cleaned_data["origem"]
            data_registro = form_log.cleaned_data["data_registro"]
            level = form_log.cleaned_data["level"]
            tipo = form_log.cleaned_data["tipo"]
            eventos = form_log.cleaned_data["eventos"]
            detalhes = form_log.cleaned_data["detalhes"]
            log_nova = log(descricao=descricao, origem=origem, data_registro=data_registro, level=level, usuario=request.user, tipo=tipo, eventos=eventos, detalhes=detalhes)
            log_service.cadastrar_log(log_nova)
            return redirect('listar_logs')
    else:
        form_log = LogForm()
    return render(request, 'logs/form_log.html', {"form_log": form_log})

@login_required()
def editar_log(request, id):
    log_bd = log_service.listar_log_id(id)
    form_log = LogForm(request.POST or None, instance=log_bd)
    if form_log.is_valid():
        descricao = form_log.cleaned_data["descricao"]
        origem = form_log.cleaned_data["origem"]
        data_registro = form_log.cleaned_data["data_registro"]
        level = form_log.cleaned_data["level"]
        tipo = form_log.cleaned_data["tipo"]
        eventos = form_log.cleaned_data["eventos"]
        detalhes = form_log.cleaned_data["detalhes"]
        log_nova = log(descricao=descricao, origem=origem, data_registro=data_registro, level=level, tipo=tipo, eventos=eventos, detalhes=detalhes)
        log_service.editar_log(log_bd, log_nova)
        return redirect('listar_logs')
    return render(request, 'logs/form_log.html', {"form_log": form_log})

@login_required()
def remover_log(request, id):
    log_bd = log_service.listar_log_id(id)
    if request.method == "POST":
        log_service.remover_log(log_bd)
        return redirect('listar_logs')
    return render(request, 'logs/confirma_exclusao.html', {'log': log_bd})