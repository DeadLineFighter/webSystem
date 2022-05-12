from http import server
from requests import options
from db import db
import dash
import pandas as pd
import plotly.express as px
import pymongo
import os
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from plotlyFunction import *
from dash_ser import app


##Style##

NAVBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 8,
    "bottom": 0,
    "width": "10rem",
    "padding": "1rem 1rem",
    "background-color": "Orange",
}

CONTENT_STYLE = {
    "top":0,
    "margin-top":'2rem',
    "margin-left": "18rem",
    "margin-right": "2rem",
    "width": "48rem",
}

##Components##

def nav_bar():
    """
    Creates Navigation bar
    """
    navbar = html.Div(
    [
        html.H4("UK Data Dashboard", className="display-10",style={'textAlign':'center'}),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Crime", href="/crime",active="exact", external_link=True),
                dbc.NavLink("POI", href="/poi", active="exact", external_link=True),
                dbc.NavLink("School", href="/school", active="exact", external_link=True),
                dbc.NavLink("Property", href="/property", active="exact", external_link=True)
            ],
            pills=True,
            vertical=True
        ),
    ],
    style=NAVBAR_STYLE,
    )  
    return navbar

#graph 1
crime_month1 = crime_month_line("LS1")

#graph 2
crime_month2 = crime_month_line("LS2")

#graph 3
poi1 = POI_type("LS2")


##bodylayout##
def bodylayout1(value):

    x = html.Div(children=[
    # All elements from the top of the page
    html.Div([
        html.Div([
            dcc.Graph(
                id='graph1',
                figure=crime_month_line(value)
            ),  
        ], className='six columns'),
        html.Div([
            dcc.Graph(
                id='graph2',
                figure=POI_type(value)
            ),  
        ], className='six columns'),
    ], className='row')
])

    return x

    
#layout1
layout1 = html.Div([
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
                                        "BL0", "BL1", "BL2", "BL3", "BL4", "BL5", "BL6", "BL7", "BL8", "BL9", "M1", "M12", "M13", "M17", "M18", "M19", "M20", "M21", "M22", "M23", "M24", "M25", "M26", "M27", "M28", "M29", "M30", "M31", "M32", "M33", "M34", "M35", "M38", "M41", "M43", "M44", "M45", "M46", "M5", "M7", "M8", "OL1", "OL10", "OL11", "OL12", "OL15", "OL16", "OL2", "OL3", "OL4", "OL5", "OL6", "OL7", "OL8", "OL9", "SK1", "SK14", "SK15", "SK16", "SK2", "SK4", "SK5", "SK6", "SK7", "SK8", "WA13", "WA14", "WA15", "WA3", "WN1", "WN2", "WN3", "WN4", "WN6", "WN7", "B1", "B10", "B11", "B12", "B13", "B14", "B15", "B16", "B17", "B18", "B19", "B2", "B20", "B21", "B22", "B23", "B24", "B25", "B26", "B27", "B28", "B29", "B3", "B30", "B31", "B32", "B33", "B34", "B35", "B36", "B37", "B38", "B39", "B4", "B40", "B41", "B42", "B43", "B44", "B45", "B46", "B47", "B48", "B49", "B5", "B50", "B51", "B52", "B53", "B54", "B55", "B56", "B57", "B58", "B59", "B6", "B60", "B61", "B62", "B63", "B64", "B65", "B66", "B67", "B68", "B69", "B7", "B70", "B71", "B72", "B73", "B74", "B75", "B76", "B77", "B78", "B79", "B8", "B80", "B81", "B82", "B83", "B84", "B85", "B86", "B87", "B88", "B89", "B9", "B90", "B91", "B92", "BS1", "BS10", "BS11", "BS12", "BS13", "BS14", "BS15", "BS16", "BS17", "BS18", "BS19", "BS2", "BS20", "BS21", "BS22", "BS23", "BS24", "BS25", "BS26", "BS27", "BS28", "BS29", "BS3", "BS30", "BS31", "BS32", "BS33", "BS34", "BS35", "BS36", "BS37", "BS38", "BS39", "BS4", "BS40", "BS41", "BS42", "BS43", "BS44", "BS45", "BS46", "BS47", "BS48", "BS49", "BS5", "BS6", "BS7", "BS8", "BS9", "BS98", "BS99", "CB1", "CB2", "CB3", "CB4", "CB5", "BR1", "BR2", "BR3", "BR4", "BR5", "BR6", "BR7", "BR8", "CR0", "CR2", "CR3", "CR4", "CR44", "CR5", "CR6", "CR7", "CR8", "CR9", "CR90", "DA1", "DA14", "DA15", "DA16", "DA17", "DA18", "DA5", "DA6", "DA7", "DA8", "E1", "E10", "E11", "E12", "E13", "E14", "E15", "E16", "E17", "E18", "E1W", "E2", "E20", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E98", "EC1A", "EC1M", "EC1N", "EC1P", "EC1R", "EC1V", "EC1Y", "EC2A", "EC2M", "EC2N", "EC2P", "EC2R", "EC2V", "EC2Y", "EC3A", "EC3M", "EC3N", "EC3P", "EC3R", "EC3V", "EC4A", "EC4M", "EC4N", "EC4P", "EC4R", "EC4V", "EC4Y", "EN1", "EN2", "EN3", "EN4", "EN5", "EN6", "EN7", "EN8", "EN9", "HA0", "HA1", "HA2", "HA3", "HA4", "HA5", "HA6", "HA7", "HA8", "HA9", "IG1", "IG11", "IG2", "IG3", "IG4", "IG5", "IG6", "IG7", "IG8", "IG9", "KT1", "KT17", "KT18", "KT19", "KT2", "KT22", "KT3", "KT4", "KT5", "KT6", "KT7", "KT8", "KT9", "N1", "N10", "N11", "N12", "N13", "N14", "N15", "N16", "N17", "N18", "N19", "N1C", "N1P", "N2", "N20", "N21", "N22", "N3", "N4", "N5", "N6", "N7", "N8", "N81", "N9", "NW1", "NW10", "NW11", "NW1W", "NW2", "NW26", "NW3", "NW4", "NW5", "NW6", "NW7", "NW8", "NW9", "RM1", "RM10", "RM11", "RM12", "RM13", "RM14", "RM15", "RM2", "RM3", "RM4", "RM5", "RM6", "RM7", "RM8", "RM9", "SE1", "SE10", "SE11", "SE12", "SE13", "SE14", "SE15", "SE16", "SE17", "SE18", "SE19", "SE1P", "SE2", "SE20", "SE21", "SE22", "SE23", "SE24", "SE25", "SE26", "SE27", "SE28", "SE3", "SE4", "SE5", "SE6", "SE7", "SE8", "SE9", "SM1", "SM2", "SM3", "SM4", "SM5", "SM6", "SM7", "SW10", "SW11", "SW12", "SW13", "SW14", "SW15", "SW16", "SW17", "SW18", "SW19", "SW1A", "SW1E", "SW1H", "SW1P", "SW1V", "SW1W", "SW1X", "SW1Y", "SW2", "SW20", "SW3", "SW4", "SW5", "SW6", "SW7", "SW8", "SW9", "SW95", "TN14", "TN16", "TW1", "TW10", "TW11", "TW12", "TW13", "TW14", "TW15", "TW19", "TW2", "TW3", "TW4", "TW5", "TW6", "TW7", "TW8", "TW9", "UB1", "UB10", "UB11", "UB18", "UB2", "UB3", "UB4", "UB5", "UB6", "UB7", "UB8", "UB9", "W10", "W11", "W12", "W13", "W14", "W1A", "W1B", "W1C", "W1D", "W1F", "W1G", "W1H", "W1J", "W1K", "W1S", "W1T", "W1U", "W1W", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "WC1A", "WC1B", "WC1E", "WC1H", "WC1N", "WC1R", "WC1V", "WC1X", "WC2A", "WC2B", "WC2E", "WC2H", "WC2N", "WC2R", "WD23", "WD3", "WD6", "BR6", "BR8", "CT1", "CT10", "CT11", "CT12", "CT13", "CT14", "CT15", "CT16", "CT17", "CT18", "CT19", "CT2", "CT20", "CT21", "CT3", "CT4", "CT5", "CT6", "CT7", "CT8", "CT9", "DA1", "DA10", "DA11", "DA12", "DA13", "DA2", "DA3", "DA4", "DA9", "ME1", "ME10", "ME11", "ME12", "ME13", "ME14", "ME15", "ME16", "ME17", "ME18", "ME19", "ME2", "ME20", "ME3", "ME4", "ME5", "ME6", "ME7", "ME8", "ME9", "TN1", "TN10", "TN11", "TN12", "TN13", "TN14", "TN15", "TN16", "TN17", "TN18", "TN2", "TN23", "TN24", "TN25", "TN26", "TN27", "TN28", "TN29", "TN3", "TN30", "TN4", "TN8", "TN9", "BD1", "BD10", "BD11", "BD3", "BD4", "LS1", "LS10", "LS11", "LS12", "LS13", "LS14", "LS15", "LS16", "LS17", "LS18", "LS19", "LS2", "LS20", "LS21", "LS22", "LS23", "LS24", "LS25", "LS26", "LS27", "LS28", "LS29", "LS3", "LS4", "LS5", "LS6", "LS7", "LS8", "LS88", "LS9", "LS98", "LS99", "WF10", "WF12", "WF17", "WF2", "WF3", "L1", "L10", "L11", "L12", "L13", "L14", "L15", "L16", "L17", "L18", "L19", "L2", "L20", "L24", "L25", "L26", "L27", "L28", "L3", "L30", "L36", "L4", "L41", "L43", "L5", "L6", "L67", "L68", "L69", "L7", "L70", "L71", "L73", "L74", "L75", "L8", "L9", "OX1", "OX10", "OX11", "OX12", "OX13", "OX14", "OX15", "OX16", "OX17", "OX18", "OX2", "OX20", "OX25", "OX26", "OX27", "OX28", "OX29", "OX3", "OX33", "OX39", "OX4", "OX44", "OX49", "OX5", "OX6", "OX7", "OX8", "OX9", "RG1", "RG10", "RG18", "RG19", "RG2", "RG26", "RG27", "RG3", "RG30", "RG31", "RG4", "RG5", "RG6", "RG7", "SL0", "SL1", "SL2", "SL3", "SL4", "SL6", "SL95", "SO1", "SO14", "SO15", "SO16", "SO17", "SO18", "SO19", "SO2", "SO3", "SO4", "SO45", "SO9"
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
                            html.H4('Crime_month'),
                            #create tabs
                            dbc.Tabs(
                                [
                                    dbc.Tab(label='graph1',tab_id='graph1'),
                                    # dbc.Tab(label='graph2',tab_id='graph2')
                                ],
                                id="tabs",
                                active_tab='graph1',
                                ),
                            html.Div(id="content1",className="p-4")
                            ]
                        ),
                    ],
                    width=12
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


##layout2
layout2 = html.Div(
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
                                        "BL0", "BL1", "BL2", "BL3", "BL4", "BL5", "BL6", "BL7", "BL8", "BL9", "M1", "M12", "M13", "M17", "M18", "M19", "M20", "M21", "M22", "M23", "M24", "M25", "M26", "M27", "M28", "M29", "M30", "M31", "M32", "M33", "M34", "M35", "M38", "M41", "M43", "M44", "M45", "M46", "M5", "M7", "M8", "OL1", "OL10", "OL11", "OL12", "OL15", "OL16", "OL2", "OL3", "OL4", "OL5", "OL6", "OL7", "OL8", "OL9", "SK1", "SK14", "SK15", "SK16", "SK2", "SK4", "SK5", "SK6", "SK7", "SK8", "WA13", "WA14", "WA15", "WA3", "WN1", "WN2", "WN3", "WN4", "WN6", "WN7", "B1", "B10", "B11", "B12", "B13", "B14", "B15", "B16", "B17", "B18", "B19", "B2", "B20", "B21", "B22", "B23", "B24", "B25", "B26", "B27", "B28", "B29", "B3", "B30", "B31", "B32", "B33", "B34", "B35", "B36", "B37", "B38", "B39", "B4", "B40", "B41", "B42", "B43", "B44", "B45", "B46", "B47", "B48", "B49", "B5", "B50", "B51", "B52", "B53", "B54", "B55", "B56", "B57", "B58", "B59", "B6", "B60", "B61", "B62", "B63", "B64", "B65", "B66", "B67", "B68", "B69", "B7", "B70", "B71", "B72", "B73", "B74", "B75", "B76", "B77", "B78", "B79", "B8", "B80", "B81", "B82", "B83", "B84", "B85", "B86", "B87", "B88", "B89", "B9", "B90", "B91", "B92", "BS1", "BS10", "BS11", "BS12", "BS13", "BS14", "BS15", "BS16", "BS17", "BS18", "BS19", "BS2", "BS20", "BS21", "BS22", "BS23", "BS24", "BS25", "BS26", "BS27", "BS28", "BS29", "BS3", "BS30", "BS31", "BS32", "BS33", "BS34", "BS35", "BS36", "BS37", "BS38", "BS39", "BS4", "BS40", "BS41", "BS42", "BS43", "BS44", "BS45", "BS46", "BS47", "BS48", "BS49", "BS5", "BS6", "BS7", "BS8", "BS9", "BS98", "BS99", "CB1", "CB2", "CB3", "CB4", "CB5", "BR1", "BR2", "BR3", "BR4", "BR5", "BR6", "BR7", "BR8", "CR0", "CR2", "CR3", "CR4", "CR44", "CR5", "CR6", "CR7", "CR8", "CR9", "CR90", "DA1", "DA14", "DA15", "DA16", "DA17", "DA18", "DA5", "DA6", "DA7", "DA8", "E1", "E10", "E11", "E12", "E13", "E14", "E15", "E16", "E17", "E18", "E1W", "E2", "E20", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E98", "EC1A", "EC1M", "EC1N", "EC1P", "EC1R", "EC1V", "EC1Y", "EC2A", "EC2M", "EC2N", "EC2P", "EC2R", "EC2V", "EC2Y", "EC3A", "EC3M", "EC3N", "EC3P", "EC3R", "EC3V", "EC4A", "EC4M", "EC4N", "EC4P", "EC4R", "EC4V", "EC4Y", "EN1", "EN2", "EN3", "EN4", "EN5", "EN6", "EN7", "EN8", "EN9", "HA0", "HA1", "HA2", "HA3", "HA4", "HA5", "HA6", "HA7", "HA8", "HA9", "IG1", "IG11", "IG2", "IG3", "IG4", "IG5", "IG6", "IG7", "IG8", "IG9", "KT1", "KT17", "KT18", "KT19", "KT2", "KT22", "KT3", "KT4", "KT5", "KT6", "KT7", "KT8", "KT9", "N1", "N10", "N11", "N12", "N13", "N14", "N15", "N16", "N17", "N18", "N19", "N1C", "N1P", "N2", "N20", "N21", "N22", "N3", "N4", "N5", "N6", "N7", "N8", "N81", "N9", "NW1", "NW10", "NW11", "NW1W", "NW2", "NW26", "NW3", "NW4", "NW5", "NW6", "NW7", "NW8", "NW9", "RM1", "RM10", "RM11", "RM12", "RM13", "RM14", "RM15", "RM2", "RM3", "RM4", "RM5", "RM6", "RM7", "RM8", "RM9", "SE1", "SE10", "SE11", "SE12", "SE13", "SE14", "SE15", "SE16", "SE17", "SE18", "SE19", "SE1P", "SE2", "SE20", "SE21", "SE22", "SE23", "SE24", "SE25", "SE26", "SE27", "SE28", "SE3", "SE4", "SE5", "SE6", "SE7", "SE8", "SE9", "SM1", "SM2", "SM3", "SM4", "SM5", "SM6", "SM7", "SW10", "SW11", "SW12", "SW13", "SW14", "SW15", "SW16", "SW17", "SW18", "SW19", "SW1A", "SW1E", "SW1H", "SW1P", "SW1V", "SW1W", "SW1X", "SW1Y", "SW2", "SW20", "SW3", "SW4", "SW5", "SW6", "SW7", "SW8", "SW9", "SW95", "TN14", "TN16", "TW1", "TW10", "TW11", "TW12", "TW13", "TW14", "TW15", "TW19", "TW2", "TW3", "TW4", "TW5", "TW6", "TW7", "TW8", "TW9", "UB1", "UB10", "UB11", "UB18", "UB2", "UB3", "UB4", "UB5", "UB6", "UB7", "UB8", "UB9", "W10", "W11", "W12", "W13", "W14", "W1A", "W1B", "W1C", "W1D", "W1F", "W1G", "W1H", "W1J", "W1K", "W1S", "W1T", "W1U", "W1W", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "WC1A", "WC1B", "WC1E", "WC1H", "WC1N", "WC1R", "WC1V", "WC1X", "WC2A", "WC2B", "WC2E", "WC2H", "WC2N", "WC2R", "WD23", "WD3", "WD6", "BR6", "BR8", "CT1", "CT10", "CT11", "CT12", "CT13", "CT14", "CT15", "CT16", "CT17", "CT18", "CT19", "CT2", "CT20", "CT21", "CT3", "CT4", "CT5", "CT6", "CT7", "CT8", "CT9", "DA1", "DA10", "DA11", "DA12", "DA13", "DA2", "DA3", "DA4", "DA9", "ME1", "ME10", "ME11", "ME12", "ME13", "ME14", "ME15", "ME16", "ME17", "ME18", "ME19", "ME2", "ME20", "ME3", "ME4", "ME5", "ME6", "ME7", "ME8", "ME9", "TN1", "TN10", "TN11", "TN12", "TN13", "TN14", "TN15", "TN16", "TN17", "TN18", "TN2", "TN23", "TN24", "TN25", "TN26", "TN27", "TN28", "TN29", "TN3", "TN30", "TN4", "TN8", "TN9", "BD1", "BD10", "BD11", "BD3", "BD4", "LS1", "LS10", "LS11", "LS12", "LS13", "LS14", "LS15", "LS16", "LS17", "LS18", "LS19", "LS2", "LS20", "LS21", "LS22", "LS23", "LS24", "LS25", "LS26", "LS27", "LS28", "LS29", "LS3", "LS4", "LS5", "LS6", "LS7", "LS8", "LS88", "LS9", "LS98", "LS99", "WF10", "WF12", "WF17", "WF2", "WF3", "L1", "L10", "L11", "L12", "L13", "L14", "L15", "L16", "L17", "L18", "L19", "L2", "L20", "L24", "L25", "L26", "L27", "L28", "L3", "L30", "L36", "L4", "L41", "L43", "L5", "L6", "L67", "L68", "L69", "L7", "L70", "L71", "L73", "L74", "L75", "L8", "L9", "OX1", "OX10", "OX11", "OX12", "OX13", "OX14", "OX15", "OX16", "OX17", "OX18", "OX2", "OX20", "OX25", "OX26", "OX27", "OX28", "OX29", "OX3", "OX33", "OX39", "OX4", "OX44", "OX49", "OX5", "OX6", "OX7", "OX8", "OX9", "RG1", "RG10", "RG18", "RG19", "RG2", "RG26", "RG27", "RG3", "RG30", "RG31", "RG4", "RG5", "RG6", "RG7", "SL0", "SL1", "SL2", "SL3", "SL4", "SL6", "SL95", "SO1", "SO14", "SO15", "SO16", "SO17", "SO18", "SO19", "SO2", "SO3", "SO4", "SO45", "SO9"
                                        ]
        ]
                                ),
                                html.Div(id='selected-dropdown')
                            ],
                            width=6
                        ),
                        dbc.Col(
                            [
                                html.H4('(Some filter /Slide)'),
                                html.Hr(),
                                dcc.RadioItems(
                                    id='poi-buttons',
                                    options = [
                                        {'label':'{}'.format(i), 'value': i} for i in [
                                        'School ', 'Hotel ', 'Bus stop ','....'
                                        ]
                                    ]
                                ),
                                html.Div(id='selected-button')
                            ],
                        ),
                        dbc.Col(
                    [
                        html.Div(
                            [
                            html.H4('POI_type'),
                            dbc.Tabs(
                                [
                                    dbc.Tab(label='graph3',tab_id='graph3')  
                                ],
                                id="tabs",
                                active_tab='graph3',
                                ),
                            html.Div(id="tab-content",className="p-4")
                            ]
                        ),
                    ],width=9)
                    ]
                ),
            ]
        )
    ])

##layout3
layout3 = html.Div(
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
                                        "BL0", "BL1", "BL2", "BL3", "BL4", "BL5", "BL6", "BL7", "BL8", "BL9", "M1", "M12", "M13", "M17", "M18", "M19", "M20", "M21", "M22", "M23", "M24", "M25", "M26", "M27", "M28", "M29", "M30", "M31", "M32", "M33", "M34", "M35", "M38", "M41", "M43", "M44", "M45", "M46", "M5", "M7", "M8", "OL1", "OL10", "OL11", "OL12", "OL15", "OL16", "OL2", "OL3", "OL4", "OL5", "OL6", "OL7", "OL8", "OL9", "SK1", "SK14", "SK15", "SK16", "SK2", "SK4", "SK5", "SK6", "SK7", "SK8", "WA13", "WA14", "WA15", "WA3", "WN1", "WN2", "WN3", "WN4", "WN6", "WN7", "B1", "B10", "B11", "B12", "B13", "B14", "B15", "B16", "B17", "B18", "B19", "B2", "B20", "B21", "B22", "B23", "B24", "B25", "B26", "B27", "B28", "B29", "B3", "B30", "B31", "B32", "B33", "B34", "B35", "B36", "B37", "B38", "B39", "B4", "B40", "B41", "B42", "B43", "B44", "B45", "B46", "B47", "B48", "B49", "B5", "B50", "B51", "B52", "B53", "B54", "B55", "B56", "B57", "B58", "B59", "B6", "B60", "B61", "B62", "B63", "B64", "B65", "B66", "B67", "B68", "B69", "B7", "B70", "B71", "B72", "B73", "B74", "B75", "B76", "B77", "B78", "B79", "B8", "B80", "B81", "B82", "B83", "B84", "B85", "B86", "B87", "B88", "B89", "B9", "B90", "B91", "B92", "BS1", "BS10", "BS11", "BS12", "BS13", "BS14", "BS15", "BS16", "BS17", "BS18", "BS19", "BS2", "BS20", "BS21", "BS22", "BS23", "BS24", "BS25", "BS26", "BS27", "BS28", "BS29", "BS3", "BS30", "BS31", "BS32", "BS33", "BS34", "BS35", "BS36", "BS37", "BS38", "BS39", "BS4", "BS40", "BS41", "BS42", "BS43", "BS44", "BS45", "BS46", "BS47", "BS48", "BS49", "BS5", "BS6", "BS7", "BS8", "BS9", "BS98", "BS99", "CB1", "CB2", "CB3", "CB4", "CB5", "BR1", "BR2", "BR3", "BR4", "BR5", "BR6", "BR7", "BR8", "CR0", "CR2", "CR3", "CR4", "CR44", "CR5", "CR6", "CR7", "CR8", "CR9", "CR90", "DA1", "DA14", "DA15", "DA16", "DA17", "DA18", "DA5", "DA6", "DA7", "DA8", "E1", "E10", "E11", "E12", "E13", "E14", "E15", "E16", "E17", "E18", "E1W", "E2", "E20", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E98", "EC1A", "EC1M", "EC1N", "EC1P", "EC1R", "EC1V", "EC1Y", "EC2A", "EC2M", "EC2N", "EC2P", "EC2R", "EC2V", "EC2Y", "EC3A", "EC3M", "EC3N", "EC3P", "EC3R", "EC3V", "EC4A", "EC4M", "EC4N", "EC4P", "EC4R", "EC4V", "EC4Y", "EN1", "EN2", "EN3", "EN4", "EN5", "EN6", "EN7", "EN8", "EN9", "HA0", "HA1", "HA2", "HA3", "HA4", "HA5", "HA6", "HA7", "HA8", "HA9", "IG1", "IG11", "IG2", "IG3", "IG4", "IG5", "IG6", "IG7", "IG8", "IG9", "KT1", "KT17", "KT18", "KT19", "KT2", "KT22", "KT3", "KT4", "KT5", "KT6", "KT7", "KT8", "KT9", "N1", "N10", "N11", "N12", "N13", "N14", "N15", "N16", "N17", "N18", "N19", "N1C", "N1P", "N2", "N20", "N21", "N22", "N3", "N4", "N5", "N6", "N7", "N8", "N81", "N9", "NW1", "NW10", "NW11", "NW1W", "NW2", "NW26", "NW3", "NW4", "NW5", "NW6", "NW7", "NW8", "NW9", "RM1", "RM10", "RM11", "RM12", "RM13", "RM14", "RM15", "RM2", "RM3", "RM4", "RM5", "RM6", "RM7", "RM8", "RM9", "SE1", "SE10", "SE11", "SE12", "SE13", "SE14", "SE15", "SE16", "SE17", "SE18", "SE19", "SE1P", "SE2", "SE20", "SE21", "SE22", "SE23", "SE24", "SE25", "SE26", "SE27", "SE28", "SE3", "SE4", "SE5", "SE6", "SE7", "SE8", "SE9", "SM1", "SM2", "SM3", "SM4", "SM5", "SM6", "SM7", "SW10", "SW11", "SW12", "SW13", "SW14", "SW15", "SW16", "SW17", "SW18", "SW19", "SW1A", "SW1E", "SW1H", "SW1P", "SW1V", "SW1W", "SW1X", "SW1Y", "SW2", "SW20", "SW3", "SW4", "SW5", "SW6", "SW7", "SW8", "SW9", "SW95", "TN14", "TN16", "TW1", "TW10", "TW11", "TW12", "TW13", "TW14", "TW15", "TW19", "TW2", "TW3", "TW4", "TW5", "TW6", "TW7", "TW8", "TW9", "UB1", "UB10", "UB11", "UB18", "UB2", "UB3", "UB4", "UB5", "UB6", "UB7", "UB8", "UB9", "W10", "W11", "W12", "W13", "W14", "W1A", "W1B", "W1C", "W1D", "W1F", "W1G", "W1H", "W1J", "W1K", "W1S", "W1T", "W1U", "W1W", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "WC1A", "WC1B", "WC1E", "WC1H", "WC1N", "WC1R", "WC1V", "WC1X", "WC2A", "WC2B", "WC2E", "WC2H", "WC2N", "WC2R", "WD23", "WD3", "WD6", "BR6", "BR8", "CT1", "CT10", "CT11", "CT12", "CT13", "CT14", "CT15", "CT16", "CT17", "CT18", "CT19", "CT2", "CT20", "CT21", "CT3", "CT4", "CT5", "CT6", "CT7", "CT8", "CT9", "DA1", "DA10", "DA11", "DA12", "DA13", "DA2", "DA3", "DA4", "DA9", "ME1", "ME10", "ME11", "ME12", "ME13", "ME14", "ME15", "ME16", "ME17", "ME18", "ME19", "ME2", "ME20", "ME3", "ME4", "ME5", "ME6", "ME7", "ME8", "ME9", "TN1", "TN10", "TN11", "TN12", "TN13", "TN14", "TN15", "TN16", "TN17", "TN18", "TN2", "TN23", "TN24", "TN25", "TN26", "TN27", "TN28", "TN29", "TN3", "TN30", "TN4", "TN8", "TN9", "BD1", "BD10", "BD11", "BD3", "BD4", "LS1", "LS10", "LS11", "LS12", "LS13", "LS14", "LS15", "LS16", "LS17", "LS18", "LS19", "LS2", "LS20", "LS21", "LS22", "LS23", "LS24", "LS25", "LS26", "LS27", "LS28", "LS29", "LS3", "LS4", "LS5", "LS6", "LS7", "LS8", "LS88", "LS9", "LS98", "LS99", "WF10", "WF12", "WF17", "WF2", "WF3", "L1", "L10", "L11", "L12", "L13", "L14", "L15", "L16", "L17", "L18", "L19", "L2", "L20", "L24", "L25", "L26", "L27", "L28", "L3", "L30", "L36", "L4", "L41", "L43", "L5", "L6", "L67", "L68", "L69", "L7", "L70", "L71", "L73", "L74", "L75", "L8", "L9", "OX1", "OX10", "OX11", "OX12", "OX13", "OX14", "OX15", "OX16", "OX17", "OX18", "OX2", "OX20", "OX25", "OX26", "OX27", "OX28", "OX29", "OX3", "OX33", "OX39", "OX4", "OX44", "OX49", "OX5", "OX6", "OX7", "OX8", "OX9", "RG1", "RG10", "RG18", "RG19", "RG2", "RG26", "RG27", "RG3", "RG30", "RG31", "RG4", "RG5", "RG6", "RG7", "SL0", "SL1", "SL2", "SL3", "SL4", "SL6", "SL95", "SO1", "SO14", "SO15", "SO16", "SO17", "SO18", "SO19", "SO2", "SO3", "SO4", "SO45", "SO9"
                                        ]
        ]
                                ),
                                html.Div(id='selected-dropdown')
                            ],
                            width=6
                        ),
                        dbc.Col(
                            [
                                html.H4('(Some filter /Slide)'),
                                html.Hr(),
                                dcc.RadioItems(
                                    id='poi-buttons',
                                    options = [
                                        {'label':'{}'.format(i), 'value': i} for i in [
                                        'School ', 'Hotel ', 'Bus stop ','....'
                                        ]
                                    ]
                                ),
                                html.Div(id='selected-button')
                            ],
                        ),
                        dbc.Col(
                    [
                        html.Div(
                            [
                            html.H4('School'),
                            dbc.Tabs(
                                [
                                    dbc.Tab(label='graph3',tab_id='graph3')  
                                ],
                                id="tabs",
                                active_tab='graph3',
                                ),
                            html.Div(id="tab-content",className="p-4")
                            ]
                        ),
                    ],width=9)
                    ]
                ),
            ]
        )
    ])

##layout4
layout4 = html.Div(
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
                                        "BL0", "BL1", "BL2", "BL3", "BL4", "BL5", "BL6", "BL7", "BL8", "BL9", "M1", "M12", "M13", "M17", "M18", "M19", "M20", "M21", "M22", "M23", "M24", "M25", "M26", "M27", "M28", "M29", "M30", "M31", "M32", "M33", "M34", "M35", "M38", "M41", "M43", "M44", "M45", "M46", "M5", "M7", "M8", "OL1", "OL10", "OL11", "OL12", "OL15", "OL16", "OL2", "OL3", "OL4", "OL5", "OL6", "OL7", "OL8", "OL9", "SK1", "SK14", "SK15", "SK16", "SK2", "SK4", "SK5", "SK6", "SK7", "SK8", "WA13", "WA14", "WA15", "WA3", "WN1", "WN2", "WN3", "WN4", "WN6", "WN7", "B1", "B10", "B11", "B12", "B13", "B14", "B15", "B16", "B17", "B18", "B19", "B2", "B20", "B21", "B22", "B23", "B24", "B25", "B26", "B27", "B28", "B29", "B3", "B30", "B31", "B32", "B33", "B34", "B35", "B36", "B37", "B38", "B39", "B4", "B40", "B41", "B42", "B43", "B44", "B45", "B46", "B47", "B48", "B49", "B5", "B50", "B51", "B52", "B53", "B54", "B55", "B56", "B57", "B58", "B59", "B6", "B60", "B61", "B62", "B63", "B64", "B65", "B66", "B67", "B68", "B69", "B7", "B70", "B71", "B72", "B73", "B74", "B75", "B76", "B77", "B78", "B79", "B8", "B80", "B81", "B82", "B83", "B84", "B85", "B86", "B87", "B88", "B89", "B9", "B90", "B91", "B92", "BS1", "BS10", "BS11", "BS12", "BS13", "BS14", "BS15", "BS16", "BS17", "BS18", "BS19", "BS2", "BS20", "BS21", "BS22", "BS23", "BS24", "BS25", "BS26", "BS27", "BS28", "BS29", "BS3", "BS30", "BS31", "BS32", "BS33", "BS34", "BS35", "BS36", "BS37", "BS38", "BS39", "BS4", "BS40", "BS41", "BS42", "BS43", "BS44", "BS45", "BS46", "BS47", "BS48", "BS49", "BS5", "BS6", "BS7", "BS8", "BS9", "BS98", "BS99", "CB1", "CB2", "CB3", "CB4", "CB5", "BR1", "BR2", "BR3", "BR4", "BR5", "BR6", "BR7", "BR8", "CR0", "CR2", "CR3", "CR4", "CR44", "CR5", "CR6", "CR7", "CR8", "CR9", "CR90", "DA1", "DA14", "DA15", "DA16", "DA17", "DA18", "DA5", "DA6", "DA7", "DA8", "E1", "E10", "E11", "E12", "E13", "E14", "E15", "E16", "E17", "E18", "E1W", "E2", "E20", "E3", "E4", "E5", "E6", "E7", "E8", "E9", "E98", "EC1A", "EC1M", "EC1N", "EC1P", "EC1R", "EC1V", "EC1Y", "EC2A", "EC2M", "EC2N", "EC2P", "EC2R", "EC2V", "EC2Y", "EC3A", "EC3M", "EC3N", "EC3P", "EC3R", "EC3V", "EC4A", "EC4M", "EC4N", "EC4P", "EC4R", "EC4V", "EC4Y", "EN1", "EN2", "EN3", "EN4", "EN5", "EN6", "EN7", "EN8", "EN9", "HA0", "HA1", "HA2", "HA3", "HA4", "HA5", "HA6", "HA7", "HA8", "HA9", "IG1", "IG11", "IG2", "IG3", "IG4", "IG5", "IG6", "IG7", "IG8", "IG9", "KT1", "KT17", "KT18", "KT19", "KT2", "KT22", "KT3", "KT4", "KT5", "KT6", "KT7", "KT8", "KT9", "N1", "N10", "N11", "N12", "N13", "N14", "N15", "N16", "N17", "N18", "N19", "N1C", "N1P", "N2", "N20", "N21", "N22", "N3", "N4", "N5", "N6", "N7", "N8", "N81", "N9", "NW1", "NW10", "NW11", "NW1W", "NW2", "NW26", "NW3", "NW4", "NW5", "NW6", "NW7", "NW8", "NW9", "RM1", "RM10", "RM11", "RM12", "RM13", "RM14", "RM15", "RM2", "RM3", "RM4", "RM5", "RM6", "RM7", "RM8", "RM9", "SE1", "SE10", "SE11", "SE12", "SE13", "SE14", "SE15", "SE16", "SE17", "SE18", "SE19", "SE1P", "SE2", "SE20", "SE21", "SE22", "SE23", "SE24", "SE25", "SE26", "SE27", "SE28", "SE3", "SE4", "SE5", "SE6", "SE7", "SE8", "SE9", "SM1", "SM2", "SM3", "SM4", "SM5", "SM6", "SM7", "SW10", "SW11", "SW12", "SW13", "SW14", "SW15", "SW16", "SW17", "SW18", "SW19", "SW1A", "SW1E", "SW1H", "SW1P", "SW1V", "SW1W", "SW1X", "SW1Y", "SW2", "SW20", "SW3", "SW4", "SW5", "SW6", "SW7", "SW8", "SW9", "SW95", "TN14", "TN16", "TW1", "TW10", "TW11", "TW12", "TW13", "TW14", "TW15", "TW19", "TW2", "TW3", "TW4", "TW5", "TW6", "TW7", "TW8", "TW9", "UB1", "UB10", "UB11", "UB18", "UB2", "UB3", "UB4", "UB5", "UB6", "UB7", "UB8", "UB9", "W10", "W11", "W12", "W13", "W14", "W1A", "W1B", "W1C", "W1D", "W1F", "W1G", "W1H", "W1J", "W1K", "W1S", "W1T", "W1U", "W1W", "W2", "W3", "W4", "W5", "W6", "W7", "W8", "W9", "WC1A", "WC1B", "WC1E", "WC1H", "WC1N", "WC1R", "WC1V", "WC1X", "WC2A", "WC2B", "WC2E", "WC2H", "WC2N", "WC2R", "WD23", "WD3", "WD6", "BR6", "BR8", "CT1", "CT10", "CT11", "CT12", "CT13", "CT14", "CT15", "CT16", "CT17", "CT18", "CT19", "CT2", "CT20", "CT21", "CT3", "CT4", "CT5", "CT6", "CT7", "CT8", "CT9", "DA1", "DA10", "DA11", "DA12", "DA13", "DA2", "DA3", "DA4", "DA9", "ME1", "ME10", "ME11", "ME12", "ME13", "ME14", "ME15", "ME16", "ME17", "ME18", "ME19", "ME2", "ME20", "ME3", "ME4", "ME5", "ME6", "ME7", "ME8", "ME9", "TN1", "TN10", "TN11", "TN12", "TN13", "TN14", "TN15", "TN16", "TN17", "TN18", "TN2", "TN23", "TN24", "TN25", "TN26", "TN27", "TN28", "TN29", "TN3", "TN30", "TN4", "TN8", "TN9", "BD1", "BD10", "BD11", "BD3", "BD4", "LS1", "LS10", "LS11", "LS12", "LS13", "LS14", "LS15", "LS16", "LS17", "LS18", "LS19", "LS2", "LS20", "LS21", "LS22", "LS23", "LS24", "LS25", "LS26", "LS27", "LS28", "LS29", "LS3", "LS4", "LS5", "LS6", "LS7", "LS8", "LS88", "LS9", "LS98", "LS99", "WF10", "WF12", "WF17", "WF2", "WF3", "L1", "L10", "L11", "L12", "L13", "L14", "L15", "L16", "L17", "L18", "L19", "L2", "L20", "L24", "L25", "L26", "L27", "L28", "L3", "L30", "L36", "L4", "L41", "L43", "L5", "L6", "L67", "L68", "L69", "L7", "L70", "L71", "L73", "L74", "L75", "L8", "L9", "OX1", "OX10", "OX11", "OX12", "OX13", "OX14", "OX15", "OX16", "OX17", "OX18", "OX2", "OX20", "OX25", "OX26", "OX27", "OX28", "OX29", "OX3", "OX33", "OX39", "OX4", "OX44", "OX49", "OX5", "OX6", "OX7", "OX8", "OX9", "RG1", "RG10", "RG18", "RG19", "RG2", "RG26", "RG27", "RG3", "RG30", "RG31", "RG4", "RG5", "RG6", "RG7", "SL0", "SL1", "SL2", "SL3", "SL4", "SL6", "SL95", "SO1", "SO14", "SO15", "SO16", "SO17", "SO18", "SO19", "SO2", "SO3", "SO4", "SO45", "SO9"
                                        ]
        ]
                                ),
                                html.Div(id='selected-dropdown')
                            ],
                            width=6
                        ),
                        dbc.Col(
                            [
                                html.H4('(Some filter /Slide)'),
                                html.Hr(),
                                dcc.RadioItems(
                                    id='poi-buttons',
                                    options = [
                                        {'label':'{}'.format(i), 'value': i} for i in [
                                        'School ', 'Hotel ', 'Bus stop ','....'
                                        ]
                                    ]
                                ),
                                html.Div(id='selected-button')
                            ],
                        ),
                        dbc.Col(
                    [
                        html.Div(
                            [
                            html.H4('Property'),
                            dbc.Tabs(
                                [
                                    dbc.Tab(label='graph3',tab_id='graph3')  
                                ],
                                id="tabs",
                                active_tab='graph3',
                                ),
                            html.Div(id="tab-content",className="p-4")
                            ]
                        ),
                    ],width=9)
                    ]
                ),
            ]
        )
    ])