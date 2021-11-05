from app import app

from flask import render_template, request, flash, redirect, url_for

from producer.models.Usuario import Usuario


@app.route('/usuario/inserir', methods=['GET', 'POST'], endpoint='usuario.inserir')
def inserir():
    if request.method == 'GET':
        return render_template('usuario/inserir.html')

    else:
        usuario = Usuario(
            nome=request.form.get('nome', ''),
            idade=request.form.get('idade', '')
        )

        if not usuario.nome or len(usuario.nome) > 40:
            flash("Campo 'nome' é obrigatório e deve ter no máximo 40 caracteres.")

        elif not usuario.idade or not usuario.idade.isdigit() or int(usuario.idade) < 0:
            flash("Campo 'idade' é obrigatório e deve ser numérico.")

        elif not usuario.client_process_message('localhost', 'usuario.inserir'):
            flash('Erro ao inserir usuário.')

        else:
            flash('Usuário criado com sucesso.')
            return redirect(url_for('usuario.listar'))

        return redirect(url_for('usuario.inserir'))


@app.route('/usuario/deletar', methods=['GET'], endpoint='usuario.deletar')
def deletar():
    usuario = Usuario(
        id_usuario=request.values.get('id_usuario', ''),
    )

    if not usuario.id_usuario or not usuario.id_usuario.isdigit() or int(usuario.id_usuario) < 0:
        flash("Campo 'id_usuario' é obrigatório e deve ser numérico.")

    elif not usuario.client_process_message('localhost', 'usuario.deletar'):
        flash('Erro ao excluir usuário.')

    else:
        flash('Usuário excluído com sucesso.')

    return redirect(url_for('usuario.listar'))


@app.route('/', methods=['GET'], endpoint='usuario.listar')
def listar():
    usuario = Usuario()
    success, usuarios = usuario.client_process_message('localhost', 'usuario.listar')

    if not usuarios:
        flash('Erro ao listar usuários.')

    return render_template('index.html', usuarios=usuarios)


@app.route('/usuario/visualizar', methods=['GET'], endpoint='usuario.visualizar')
def visualizar():
    usuario = Usuario(
        id_usuario=request.values.get('id_usuario', ''),
    )

    if not usuario.id_usuario or not usuario.id_usuario.isdigit() or int(usuario.id_usuario) < 0:
        flash("Campo 'id_usuario' é obrigatório e deve ser numérico.")

    else:
        success, usuario = usuario.client_process_message('localhost', 'usuario.visualizar')

        if not usuario:
            flash('Erro ao selecionar usuário.')

        else:
            return render_template('usuario/editar.html', usuario=usuario[0])

    return redirect(url_for('usuario.listar'))


@app.route('/usuario/editar', methods=['GET', 'POST'], endpoint='usuario.editar')
def editar():
    if request.method == 'GET':
        return visualizar()

    else:
        usuario = Usuario(
            id_usuario=request.values.get('id_usuario', ''),
            nome=request.form.get('nome', ''),
            idade=request.form.get('idade', '')
        )

        if not usuario.id_usuario or not usuario.id_usuario.isdigit() or int(usuario.id_usuario) < 0:
            flash("Campo 'id_usuario' é obrigatório e deve ser numérico.")

        elif not usuario.nome or len(usuario.nome) > 40:
            flash("Campo 'nome' é obrigatório e deve ter no máximo 40 caracteres.")

        elif not usuario.idade or not usuario.idade.isdigit() or int(usuario.idade) < 0:
            flash("Campo 'idade' é obrigatório e deve ser numérico.")

        elif not usuario.client_process_message('localhost', 'usuario.editar'):
            flash('Erro ao alterar usuário.')

        else:
            flash('Usuário alterado com sucesso.')
            return render_template('usuario/editar.html', usuario=request.form)

        return redirect(url_for('usuario.listar'))
