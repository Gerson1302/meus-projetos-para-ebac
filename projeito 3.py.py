import pandas as pd  # Importar a biblioteca Pandas
import dash
from dash import dcc, html
import plotly.express as px

# Ler o arquivo CSV
df = pd.read_csv('C:\\Users\\Gerson\\PycharmProjects\\pythonProject\\ecommerce_estatistica 2.csv')

# Inicializar o app Dash
app = dash.Dash(__name__)

# Layout da aplicação
app.layout = html.Div(children=[
    html.H1(children='Dashboard de Análise de E-commerce'),

    html.Div(children=[
        dcc.Graph(
            id='histograma',
            figure=px.histogram(df, x='Desconto', title='Distribuição de Desconto')
        ),
        dcc.Graph(
            id='dispersao',
            figure=px.scatter(df, x='Qtd_Vendidos_Cod', y='Preço_MinMax', title='Dispersão de Vendas')
        ),
        dcc.Graph(
            id='mapa_calor',
            figure=px.imshow(df.select_dtypes(include=['float64', 'int64']).corr(), title='Mapa de Calor de Correlação')
        ),
        dcc.Graph(
            id='grafico_barras',
            figure=px.bar(df, x='Marca_Freq', y='Qtd_Vendidos_Cod', title='Quantidade Vendida por Marca')
        ),
        dcc.Graph(
            id='grafico_pizza',
            figure=px.pie(df, names='Material_Freq', title='Distribuição por Material')
        ),
        dcc.Graph(
            id='densidade',
            figure=px.density_heatmap(df, x='Preço_MinMax', y='Qtd_Vendidos_Cod', title='Densidade de Preço e Vendas')
        ),
        dcc.Graph(
            id='regressao',
            figure=px.scatter(df, x='N_Avaliações_MinMax', y='Preço_MinMax', title='Gráfico de Regressão')
        )
    ], style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-around'})
])

# Rodar a aplicação
if __name__ == '__main__':
    app.run_server(debug=True)




