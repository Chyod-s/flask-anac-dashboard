""" Módulo com as rotas da aplicação para a análise de voos. """
from flask import render_template, request
from flask_login import login_required
from sqlalchemy import and_
import pandas as pd
import plotly.express as px
from app.repositories import Voos


def analise_controller(app):
    """ Registra as rotas da aplicação. """
    def gerar_grafico(voos, title):
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
                             title=title,
                             color='mes',
                             color_continuous_scale=['#FFB380', '#FF7020'])
                fig.update_layout(
                    legend=dict(x=0.5, y=-0.2, xanchor='center', yanchor='top'),
                    width=600,
                    height=400,
                    autosize=True)

            else:
                fig = px.bar(df, x='mes', y='rpk', title=title, color='mes', color_continuous_scale='Oranges')
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
            graph_html = gerar_grafico(voos, "Análise de voos")

        if request.method == 'POST':
            mercado = request.form.get('mercado', None)
            ano = request.form.get('ano', None)
            mes = request.form.get('mes', None)

            ano = int(ano) if ano and ano.isdigit() else None
            mes = int(mes) if mes and mes.isdigit() else None

            if mercado or ano or mes:
                voos = Voos.query.filter(
                    and_(
                        Voos.mercado == mercado,
                        Voos.ano == ano,
                        Voos.mes == mes,
                        Voos.rpk.isnot(None),
                        Voos.rpk != 0
                    )
                ).all()
                graph_html = gerar_grafico(voos, f"Análise de voos - {mercado} - {mes}/{ano}")

        return render_template('analise.html', graph_html=graph_html)
