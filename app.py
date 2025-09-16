import os
import sys


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, render_template, request, redirect, url_for, session

from model.atributos import Atributos
from model.classe import Classe
from model.raca import Raca

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

RACAS = ["Elfo", "Anão", "Humano"]
CLASSES = ["Guerreiro", "Mago", "Ladrão"]
ATRIBUTOS = ["forca", "destreza", "constituicao", "inteligencia", "sabedoria", "carisma"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        session['nome'] = request.form['nome']
        session['idade'] = int(request.form['idade'])
        session['raca'] = request.form['raca']
        session['classe'] = request.form['classe']
        session['estilo'] = request.form['estilo']

        a = Atributos()
        
        if session['estilo'] == 'classico':
            a.gerar_classico()
            session['atributos_gerados'] = a.AtributosRandom
            return redirect(url_for('resultado'))
        
        elif session['estilo'] in ['aventureiro', 'heroico']:
            if session['estilo'] == 'aventureiro':
                valores = a.gerar_aventureiro()
            else: 
                valores = a.gerar_heroico()
            
           
            session['valores_gerados'] = valores
           
            return redirect(url_for('index'))
    
    
    valores = session.pop('valores_gerados', None)
    
    return render_template('index.html',
                           racas=RACAS,
                           classes=CLASSES,
                           atributos=ATRIBUTOS,
                           valores=valores)

@app.route('/distribuir', methods=['POST'])
def distribuir():
    
    valores_originais = session.get('valores_gerados', [])
    distribuicao = {}
    
    
    for atributo in ATRIBUTOS:
        valor = request.form.get(atributo)
        if valor and valor.isdigit():
            distribuicao[atributo] = int(valor)
    
    a = Atributos()
    a.distribuir_valores(valores_originais, distribuicao)
    session['atributos_gerados'] = a.AtributosRandom
    
    return redirect(url_for('resultado'))

@app.route('/resultado')
def resultado():
    nome = session.get('nome')
    idade = session.get('idade')
    raca_escolhida = session.get('raca')
    classe_escolhida = session.get('classe')
    atributos_gerados = session.get('atributos_gerados')

    if not nome or not atributos_gerados:
        return redirect(url_for('index'))

    r = Raca()
    r.escolhaRaca(raca_escolhida)
    r.atributosRaca(idade)

    c = Classe()
    c.escolhaClasse(classe_escolhida)
    
    a = Atributos()
    a.AtributosRandom = atributos_gerados

    atributos_formatados = []
    for nome_attr, valor in a.AtributosRandom.items():
        desc = a.descricao(nome_attr, valor)
        atributos_formatados.append({'nome': nome_attr, 'valor': valor, 'descricao': desc})

    return render_template('resultado.html', 
                           nome=nome, 
                           idade=idade, 
                           raca=r, 
                           classe=c, 
                           atributos=atributos_formatados)

if __name__ == '__main__':
    app.run(debug=True)