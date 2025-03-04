""" Módulo com as rotas da aplicação para a análise de voos. """
from flask import render_template, request
from flask_login import login_required
import pandas as pd
import plotly.express as px
from app.repositories import Voos

def analise_controller(app):
    """ Registra as rotas da aplicação. """
    def gerar_grafico(voos):
        """Função auxiliar para gerar o gráfico a partir dos voos."""
        if voos:
            df = pd.DataFrame(
                [(v.ano,v.mes,v.mercado,v.rpk) for v in voos],
                columns=['ano', 'mes', 'mercado', 'rpk'])

            if request.method == 'GET':
                df = df.groupby('mes', as_index=False)['rpk'].sum()
                fig = px.bar(df,
                             x='mes',
                             y='rpk',
                             title='RPK por Mês',
                             color='mes',
                             color_continuous_scale=['#FFB380', '#FF7020'])
                fig.update_layout(
                    legend=dict(x=0.5, y=-0.2, xanchor='center', yanchor='top'),
                    width=600,
                    height=400,
                    autosize=True)

            else:
                fig = px.bar(df, x='mes', y='rpk', title='RPK por Mês', color='mes', color_continuous_scale='Oranges')
                fig.update_layout(
                    legend=dict(x=0.5, y=-0.2, xanchor='center', yanchor='top'),
                    width=600,
                    height=400,
                    autosize=True)
            return fig.to_html(full_html=False)

        else:
            return '<p>Nenhum voo encontrado.</p>'

    @app.route('/analise', methods=['GET', 'POST'])
    @login_required
    def analise():
        graph_html = ''

        if request.method == 'GET':
            voos = Voos.query.all()
            graph_html = gerar_grafico(voos)

        if request.method == 'POST':
            mercado = request.form.get('mercado', None)
            ano = request.form.get('ano', None)
            mes = request.form.get('mes', None)

            if mercado or ano or mes:
                voos = Voos.query.filter_by(mercado=mercado, ano=ano, mes=mes).all()
                graph_html = gerar_grafico(voos)

        return render_template('analise.html', graph_html=graph_html)
