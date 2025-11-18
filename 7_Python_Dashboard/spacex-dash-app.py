# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()
print(spacex_df.head())

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown',
                                             options=[
                                                 {'label': 'All Sites', 'value': 'ALL'},
                                                 {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                                 {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'},
                                                 {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                                 {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'}],
                                                 value='ALL',
                                                 placeholder="Select a Launch Site here",
                                                 searchable=True),
                                html.Br(),
                                dcc.Graph(id='success-pie-chart'),
                                html.Br(),
                                html.P("Payload range (Kg):"),
                                dcc.RangeSlider(id='payload-slider',
                                                min=0, max=10000, step=1000,
                                                marks={0: '0', 2500: '2500', 5000: '5000', 7500: '7500', 10000: '10000'},
                                                value=[min_payload, max_payload]),
                                dcc.Graph(id='success-payload-scatter-chart')])



                                # # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                #html.Div(dcc.Graph(id='success-pie-chart')),
                                #html.Br(),
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    if entered_site == 'ALL':
        # Count total successful launches per site
        success_counts = spacex_df[spacex_df['class'] == 1]['Launch Site'].value_counts().reset_index()
        success_counts.columns = ['Launch Site', 'Successes']
        fig = px.pie(success_counts, names='Launch Site', values='Successes',
                     title='Total Successful Launches by Site')
        return fig
    else:
        # Filter for selected site
        site_df = spacex_df[spacex_df['Launch Site'] == entered_site]
        # Count success and failure
        outcome_counts = site_df['class'].value_counts().reset_index()
        outcome_counts.columns = ['Outcome', 'Count']
        outcome_counts['Outcome'] = outcome_counts['Outcome'].map({1: 'Success', 0: 'Failure'})
        fig = px.pie(outcome_counts, names='Outcome', values='Count',
                     title=f'Success vs Failure for {entered_site}')
        return fig
                                # html.P("Payload range (Kg):"),
                                # # TASK 3: Add a slider to select payload range
                                # #dcc.RangeSlider(id='payload-slider',...)
# TASK 3: Add a Range Slider to Select Payload
html.P("Payload range (Kg):"),
dcc.RangeSlider(id='payload-slider',
                min=0,
                max=10000,
                step=1000,
                marks={0: '0', 2500: '2500', 5000: '5000', 7500: '7500', 10000: '10000'},
                value=[min_payload, max_payload])
                                # # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                # html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                # ])
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site-dropdown', component_property='value'),
     Input(component_id='payload-slider', component_property='value')]
)
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range
    # Filter by payload range
    filtered_df = spacex_df[(spacex_df['Payload Mass (kg)'] >= low) &
                            (spacex_df['Payload Mass (kg)'] <= high)]
    
    if entered_site == 'ALL':
        # Scatter plot for all sites
        fig = px.scatter(filtered_df, x='Payload Mass (kg)', y='class',
                         color='Booster Version Category',
                         title='Success vs Payload for All Sites')
    else:
        # Filter by selected site
        site_df = filtered_df[filtered_df['Launch Site'] == entered_site]
        fig = px.scatter(site_df, x='Payload Mass (kg)', y='class',
                         color='Booster Version Category',
                         title=f'Success vs Payload for {entered_site}')
    return fig

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
