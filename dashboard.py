import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import urllib.parse
from flask import Flask
from requests import options
from model.plotlyFunction import *
import dash_bootstrap_components as dbc

def dashboard(server):
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u',
        'crossorigin': 'anonymous'
    }]

    app = dash.Dash(
        __name__,
        server=server,
        routes_pathname_prefix='/dash/',
        # external_stylesheets = [dbc.themes.CYBORG]
        external_stylesheets = external_stylesheets
    )
    app.title = 'UK Dashboard'

    ###############################LAYOUT###############################

    ##Style##

    NAVBAR_STYLE = {
        "position": "fixed",
        "top": 0,
        "left": 8,
        "bottom": 0,
        "width": "15rem",
        "padding": "1rem 2rem",
        "background-color": "#474A76",
        "font-size": "20pt",
        "color": "#E0E0E0"
    }

    CONTENT_STYLE = {
        "top":0,
        "margin-top":'2rem',
        "margin-left": "18rem",
        "margin-right": "2rem",
        "width": "auto",
        "font-size": "15pt"
    }

    ##Components##

    def nav_bar():
        """
        Creates Navigation bar
        """
        navbar = html.Div(
        [
            html.H4("UK Data Dashboard", className="display-10",style={'textAlign':'center','font-size':'20pt'}),
            html.Hr(),
            dbc.Nav(
                [
                    dbc.NavLink("Crime\n", href="/dash/crime",active="exact", external_link=True),
                    dbc.NavLink("Google POI\n", href="/dash/poi", active="exact", external_link=True),
                    dbc.NavLink("School\n", href="/dash/school", active="exact", external_link=True),
                    dbc.NavLink("Property\n", href="/dash/property", active="exact", external_link=True)
                ],
                pills=True,
                vertical=True
            ),
        ],
        style=NAVBAR_STYLE,
        )  
        return navbar


    ##bodylayout##
    def maplayout(p): #map
        x1 = html.Div(children=[
        html.Div([
            html.Div([
                dcc.Graph(
                    id='map_graph',
                    figure=plotMap(p)
                
                ),  
            ], className='nine columns'),
        ], className='row')
    ])

        return x1
    def bodylayout1(p): #crime

        x1 = html.Div(children=[
        # All elements from the top of the page
        html.Div([
            # html.Div([
            #     dcc.Graph(
            #         id='map_graph',
            #         figure=plotMap(p)
                
            #     ),  
            # ], className='six columns'),
            html.Div([
                dcc.Graph(
                    id='crime_graph',
                    
                ),  
            ], className='twelve columns'),
            html.Div([
                dcc.Graph(
                    id='crime_graph2',
                
                ),  
            ], className='twelve columns'),
        ], className='row')
    ])

        return x1

    def bodylayout2(p): #poi

        x2 = html.Div(children=[
        # All elements from the top of the page
        html.Div([
            # html.Div([
            #     dcc.Graph(
            #         id='map_graph',
            #         figure=plotMap(p)
                
            #     ),  
            # ], className='five columns'),
            html.Div([
                dcc.Graph(
                    id='poi_graph',
                    
                ),  
            ], className='six columns'),
            html.Div([
                dcc.Graph(
                    id='poi_graph2',
                    
                ),  
            ], className='six columns'),
            html.Div([
                dcc.Graph(
                    id='poi_graph3',
                    
                ),  
            ], className='twelve columns'),
        ], className='row')
    ])

        return x2

    def bodylayout3(p): #school

        x3 = html.Div(children=[
        # All elements from the top of the page
        html.Div([
            html.Div([
                dcc.Graph(
                    id='school_graph',
                    
                ),  
            ], className='six columns'),
            html.Div([
                dcc.Graph(
                    id='school_graph2',
                    
                ),  
            ], className='six columns'),
            html.Div([
                dcc.Graph(
                    id='school_graph3',
                    
                ),  
            ], className='twelve columns'),
        ], className='row')
    ])

        return x3

    def bodylayout4(p): #property

        x4 = html.Div(children=[
        # All elements from the top of the page
        html.Div([
            html.Div([
                dcc.Graph(
                    id='pro_graph',
                    
                ),  
            ], className='six columns'),
            html.Div([
                dcc.Graph(
                    id='pro_graph2',
                    
                ),  
            ], className='six columns'),
            html.Div([
                dcc.Graph(
                    id='pro_graph3',
                    
                ),  
            ], className='twelve columns'),
        ], className='row')
    ])

        return x4 


    x = []
    #layout crime
    def layout1(x): 
        y = html.Div([
        html.H2("Crime"),
        html.Hr(),
        dbc.Container([
            dbc.Row(
                [
                            dbc.Col(
                                [
                                    html.H4('Postcode'),
                                    html.Hr(),
                                    dcc.Dropdown(
                                        id='page2-dropdown',
                                        options=[
                                            {'label': '{}'.format(i), 'value': i} for i in [
                                            x[0],x[1],x[2],x[3],x[4]
                                            ]
            ]
                                    ),
                                    html.Div(id='selected-dropdown')
                                ],
                                width=6
                            ),
                    dbc.Col(
                        [
                            html.Div(
                                [
                                html.Div(id="map",className="p-4")
                                ]
                            ),
                        ],
                        width="auto"
                    ),
                    dbc.Col(
                        [
                            html.Div(
                                [
                                html.H4('Crime'),
                                html.Div(id="content1",className="p-4")
                                ]
                            ),
                        ],
                        width="auto"
                    ),
                    dbc.Col(
                        [
                            
                            html.P('Click on graph to display the detail', id='graph-text')
                        ],
                        width=12
                    )               
                    
                ],
            ), 
        ]),
    ])

        return y

    ##layout poi
    def layout2(x):
        
        y = html.Div(
        [
            html.H2('POI'),
            html.Hr(),
            dbc.Container(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.H4('Postcode'),
                                    html.Hr(),
                                    dcc.Dropdown(
                                        id='page2-dropdown',
                                        options=[
                                            {'label': '{}'.format(i), 'value': i} for i in [
                                            x[0],x[1],x[2],x[3],x[4]
                                            ]
            ]
                                    ),
                                    html.Div(id='selected-dropdown')
                                ],
                                width=6
                            ),
                            dbc.Col(
                        [
                            html.Div(
                                [
                                html.Div(id="map",className="p-4")
                                ]
                            ),
                        ],
                        width="auto"
                    ),
                            dbc.Col(
                        [
                            html.Div(
                                [
                                html.Div(id="content2",className="p-4")
                                ]
                            ),
                        ],width="auto"),
                    dbc.Col(
                        [
                            
                            html.P('Click on graph to display the detail', id='graph-text')
                        ],
                        width=12
                    )    
                        ]
                    ),
                ]
            )
        ])

        return y

    ##layout school
    def layout3(x):
        y = html.Div(
        [
            html.H2('School'),
            html.Hr(),
            dbc.Container(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.H4('Postcode'),
                                    html.Hr(),
                                    dcc.Dropdown(
                                        id='page2-dropdown',
                                        options=[
                                            {'label': '{}'.format(i), 'value': i} for i in [
                                            x[0],x[1],x[2],x[3],x[4]
                                            ]
            ]
                                    ),
                                    html.Div(id='selected-dropdown')
                                ],
                                width=6
                            ),
                            dbc.Col(
                        [
                            html.Div(
                                [
                                html.Div(id="map",className="p-4")
                                ]
                            ),
                        ],
                        width="auto"
                    ),                            
                            dbc.Col(
                        [
                            html.Div(
                                [
                                html.Div(id="content3",className="p-4")
                                ]
                            ),
                        ],width="auto"),
                    dbc.Col(
                        [
                            
                            html.P('Click on graph to display the detail', id='graph-text')
                        ],
                        width=12
                    )    
                        ]
                    ),
                ]
            )
        ])

        return y

    ##layout property
    def layout4(x):
        
        y = html.Div(
        [
            html.H2('Property'),
            html.Hr(),
            dbc.Container(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.H4('Postcode'),
                                    html.Hr(),
                                    dcc.Dropdown(
                                        id='page2-dropdown',
                                        options=[
                                            {'label': '{}'.format(i), 'value': i} for i in [
                                            x[0],x[1],x[2],x[3],x[4]
                                            ]
            ]
                                    ),
                                    html.Div(id='selected-dropdown')
                                ],
                                width=6
                            ),
                            dbc.Col(
                        [
                            html.Div(
                                [
                                html.Div(id="map",className="p-4")
                                ]
                            ),
                        ],
                        width="auto"
                    ),                            
                            dbc.Col(
                        [
                            html.Div(
                                [
                                html.Div(id="content4",className="p-4")
                                ]
                            ),
                        ],width="auto"),
                    dbc.Col(
                        [
                            
                            html.P('Click on graph to display the detail', id='graph-text')
                        ],
                        width=12
                    )    
                        ]
                    ),
                ]
            )
        ])

        return y
    ###############################CALLBACK###############################

    ###crime
    #1
    @app.callback(Output('crime_graph','figure'),
                    [Input('page2-dropdown','value')])
    def fig_content(postcode):
        return crime_month_line(pd.DataFrame(countMonthCrime(postcode)))
    #2
    @app.callback(Output('crime_graph2','figure'),
                    [Input('page2-dropdown','value')])
    def fig_content(postcode):
        return criTyp_line(pd.DataFrame(countCrimeType(postcode)))

    ###poi
    #1
    @app.callback(Output('poi_graph','figure'),
                    [Input('page2-dropdown','value')])
    def fig_content(postcode):
        return POI_type(pd.DataFrame(countPoiType(postcode)))
    #2
    @app.callback(Output('poi_graph2','figure'),
                    [Input('page2-dropdown','value')])
    def fig_content(postcode):
        return poiRat_bar(pd.DataFrame(poiRatingAvg(postcode)))
    #3
    @app.callback(Output('poi_graph3','figure'),
                    [Input('page2-dropdown','value')])
    def fig_content(postcode):
        return higRat_sca(pd.DataFrame(highScoreRatingType(postcode)))

    ###school
    #1
    @app.callback(Output('school_graph','figure'),
                    [Input('page2-dropdown','value')])
    def fig_content(postcode):
        return schGen_pie(pd.DataFrame(schoolGender(postcode)))
    #2
    @app.callback(Output('school_graph2','figure'),
                    [Input('page2-dropdown','value')])
    def fig_content(postcode):
        return schPha_bar(pd.DataFrame(schoolPhase(postcode)))
    #3
    @app.callback(Output('school_graph3','figure'),
                    [Input('page2-dropdown','value')])
    def fig_content(postcode):
        return schRat_bar(pd.DataFrame(schoolRating(postcode)))

    ###property
    #1
    @app.callback(Output('pro_graph','figure'),
                    [Input('page2-dropdown','value')])
    def fig_content(postcode):
        return avgPri_pieBar(pd.DataFrame(rightmoveAvgPrice(postcode)))

    #2
    @app.callback(Output('pro_graph2','figure'),
                    [Input('page2-dropdown','value')])
    def fig_content(postcode):
        return chaPie(pd.DataFrame(rightmoveChannel(postcode)))
    #3
    @app.callback(Output('pro_graph3','figure'),
                    [Input('page2-dropdown','value')])
    def fig_content(postcode):
        return pro_line(pd.DataFrame(rightmoveProperty(postcode)))

    ####map####
    @app.callback(Output('map', 'children'),
                [Input('page2-dropdown', 'value')])
    def tab_content(value):
        return maplayout(value)

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




    ###############################SERVER###############################

    app.layout = html.Div([
        dcc.Location(id='url', refresh=False), 
        nav_bar(),
        html.Div(id='page-content',style=CONTENT_STYLE) 
    ])

    @app.callback(Output('page-content', 'children'), 
                [Input('url', 'href')]) 
    def display_page(pathname):
        if (pathname):
            param = urllib.parse.urlparse(pathname)
            param_dict = urllib.parse.parse_qs(param.query)
            if 'postcode' in param_dict.keys():
                for i in range(len(param_dict['postcode'])):
                    x.append(param_dict['postcode'][i])  
            if pathname == 'http://127.0.0.1:5000/dash/crime':
                return layout1(x)
            elif pathname == 'http://127.0.0.1:5000/dash/poi':
                return layout2(x)
            elif pathname == 'http://127.0.0.1:5000/dash/school':
                return layout3(x)
            elif pathname == 'http://127.0.0.1:5000/dash/property':
                return layout4(x)
    return app
if __name__ == '__main__':
    server = Flask(__name__)
    dash_server = dashboard(server)
    server.run(debug=False)
