# Tarefa -> Implementação

from flask import Blueprint, request, jsonify
from src.controller.colaborador_controller import bp_colaborador
from src.model import db
from src.model.reembolso_model import Reembolso

bp_reembolso  = Blueprint('reembolso', __name__, url_prefix='/reembolso')
# Rota de visualizacao de todos os reembolsos -> GET
@bp_reembolso.route('/todos-reembolsos', methods=['GET'])
def visualizar_todos_os_reembolsos():
    num_prestacoes = request.args.get('num_prestacao', type=int)
    query = db.select(Reembolso)
    
    if num_prestacoes:
        query = query.filter(Reembolso.num_prestacoes == num_prestacoes)
    reembolsos = db.session.execute(
        db.select(Reembolso)
    ).scalars().all()

    reembolsos = [reembolso.all_data() for reembolso in reembolsos]
    return jsonify(reembolsos), 200
    
# Solicitação de reembolsos - > POST    

@bp_reembolso.route('/solicitar-reembolsos', methods=['POST'])
def solicitar_reembolsos():

    dados_requisicao = request.get_json()
    print("Dados recebidos:", dados_requisicao)
    reembolsos = [
        Reembolso(**dados) for dados in dados_requisicao
    ]
    db.session.bulk_save_objects(reembolsos)
    db.session.commit()
    return jsonify({'mensagem': "Reembolsos salvos com sucesso"}), 201
    
# Para enviar multiplos dados para o BD, utilize: db.session.bulk_save_Objects(lista[[instancias]])