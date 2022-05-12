from dash import dcc, html
from dash.dependencies import Input, Output
from layouts import *
from dash_ser import app

# @app.callback(
#     Output("tab-content", "children"),
#     Input("tabs", "active_tab"),
# )
# def render_tab_content(active_tab):
#     if active_tab is not None:
#         if active_tab == "graph1":
#             return dcc.Graph(figure=crime_month1, id='graph')
#         elif active_tab == "graph2":
#             return dcc.Graph(figure=crime_month2, id='graph')
#         elif active_tab == "graph3":
#             return dcc.Graph(figure=poi1, id='graph')
#     return "No tab selected"

####Crime####
@app.callback(Output('content1', 'children'),
              [Input('page2-dropdown', 'value')])
def tab_content(value):
     if value is not None:
        return bodylayout1(value)
     return "No postcode selected"

#####POI#####
@app.callback(Output('content2', 'children'),
              [Input('page2-dropdown', 'value')])
def tab_content(value):
     if value is not None:
        return bodylayout2(value)
     return "No postcode selected"

#####School#####
@app.callback(Output('content3', 'children'),
              [Input('page2-dropdown', 'value')])
def tab_content(value):
     if value is not None:
        return bodylayout3(value)
     return "No postcode selected"

#####Property#####
@app.callback(Output('content4', 'children'),
              [Input('page2-dropdown', 'value')])
def tab_content(value):
     if value is not None:
        return bodylayout4(value)
     return "No postcode selected"


####graph_click####
@app.callback(
    Output("graph-text","children"),
    Input("graph","clickData"),
)
def graph_click(clickData):
    if 'pointIndex' in clickData['points'][0]:
        return html.P(f"Date: {clickData['points'][0]['x']}\nNumber of crime cases: {clickData['points'][0]['y']}")
    elif 'binNumber' in clickData['points'][0]:
        return html.P(f"Date: {clickData['points'][0]['x']}\nCount: {clickData['points'][0]['y']}")

@app.callback(
    Output("selected-button","children"),
    Input("poi-buttons","value")
)
def button_choice(value):
    return 'You have selected "{}"'.format(value)

@app.callback(
    Output("selected-dropdown","children"),
    Input("page2-dropdown","value")
)
def dropdown_choice(value):
    return 'You have selected "{}"'.format(value)
