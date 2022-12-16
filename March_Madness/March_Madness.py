import altair as alt
import pandas as pd
from PIL import Image
import plotly_express as px
import plotly.graph_objects as go
import seaborn as sns
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout = "wide")
hide_table_row_index = """ <style> thead tr th:first-child {display:none} tbody th {display:none} </style> """
st.markdown(hide_table_row_index, unsafe_allow_html=True)

selected = option_menu(menu_title = "Navigation",options = ["Home", "Charts", "Seed Profiles", "Team Profiles", "Trends", "Game Predictor"],
icons = ["house-fill", "bar-chart-fill", "tree-fill", "people-fill", "graph-up-arrow", "robot"], menu_icon = "map-fill", orientation = "horizontal", default_index = 0)

def seed_plot(dataframe, seed) :
    if seed == 1 : seed_rows = dataframe[dataframe["SEED"] == 1]
    if seed == 2 : seed_rows = dataframe[dataframe["SEED"] == 2]
    if seed == 3 : seed_rows = dataframe[dataframe["SEED"] == 3]
    if seed == 4 : seed_rows = dataframe[dataframe["SEED"] == 4]
    if seed == 5 : seed_rows = dataframe[dataframe["SEED"] == 5]
    if seed == 6 : seed_rows = dataframe[dataframe["SEED"] == 6]
    if seed == 7 : seed_rows = dataframe[dataframe["SEED"] == 7]
    if seed == 8 : seed_rows = dataframe[dataframe["SEED"] == 8]
    if seed == 9 : seed_rows = dataframe[dataframe["SEED"] == 9]
    if seed == 10 : seed_rows = dataframe[dataframe["SEED"] == 10]
    if seed == 11 : seed_rows = dataframe[dataframe["SEED"] == 11]
    if seed == 12 : seed_rows = dataframe[dataframe["SEED"] == 12]
    if seed == 13 : seed_rows = dataframe[dataframe["SEED"] == 13]
    if seed == 14 : seed_rows = dataframe[dataframe["SEED"] == 14]
    if seed == 15 : seed_rows = dataframe[dataframe["SEED"] == 15]
    if seed == 16 : seed_rows = dataframe[dataframe["SEED"] == 16]

    y_axis = st.selectbox("Select Y-Axis Value", options = ["KENPOM ADJUSTED EFFICIENCY", "KENPOM ADJUSTED OFFENSE", "KENPOM ADJUSTED DEFENSE", "KENPOM ADJUSTED TEMPO",
    "BARTTORVIK ADJUSTED EFFICIENCY", "BARTTORVIK ADJUSTED OFFENSE", "BARTTORVIK ADJUSTED DEFENSE", "BARTHAG", "ELITE SOS", "BARTTORVIK ADJUSTED TEMPO", "2PT %", "3PT %",
    "FREE THROW %", "EFG %", "FREE THROW RATE", "3PT RATE", "AST %", "OFFENSIVE REBOUND %", "DEFENSIVE REBOUND %", "BLOCK %", "TURNOVER %", "2PT % DEFENSE", "3PT % DEFENSE",
    "EFG % DEFENSE", "FREE THROW RATE DEFENSE", "3PT RATE DEFENSE", "OP AST %", "BLOCKED %", "TURNOVER % DEFENSE",
    "WINS ABOVE BUBBLE", "WIN %", "POINTS PER POSSESSION OFFENSE", "POINTS PER POSSESSION DEFENSE"])
    plot = px.scatter(seed_rows, x = "YEAR", y = y_axis, color = "ROUND", hover_data = ["TEAM", "SEED"], color_discrete_sequence =
    ["white", "red", "orange", "yellow", "green", "blue", "purple", "pink"], width = 1000, height = 700)
    update_plot(plot)
    st.plotly_chart(plot)

def year_plot(dataframe, year) :
    if year == 2008 : year_rows = dataframe[dataframe["YEAR"] == 2008]
    if year == 2009 : year_rows = dataframe[dataframe["YEAR"] == 2009]
    if year == 2010 : year_rows = dataframe[dataframe["YEAR"] == 2010]
    if year == 2011 : year_rows = dataframe[dataframe["YEAR"] == 2011]
    if year == 2012 : year_rows = dataframe[dataframe["YEAR"] == 2012]
    if year == 2013 : year_rows = dataframe[dataframe["YEAR"] == 2013]
    if year == 2014 : year_rows = dataframe[dataframe["YEAR"] == 2014]
    if year == 2015 : year_rows = dataframe[dataframe["YEAR"] == 2015]
    if year == 2016 : year_rows = dataframe[dataframe["YEAR"] == 2016]
    if year == 2017 : year_rows = dataframe[dataframe["YEAR"] == 2017]
    if year == 2018 : year_rows = dataframe[dataframe["YEAR"] == 2018]
    if year == 2019 : year_rows = dataframe[dataframe["YEAR"] == 2019]
    if year == 2021 : year_rows = dataframe[dataframe["YEAR"] == 2021]
    if year == 2022 : year_rows = dataframe[dataframe["YEAR"] == 2022]
    if year == 2023 : year_rows = dataframe[dataframe["YEAR"] == 2023]

    y_axis = st.selectbox("Select Y-Axis Value", options = ["KENPOM ADJUSTED EFFICIENCY", "KENPOM ADJUSTED OFFENSE", "KENPOM ADJUSTED DEFENSE", "KENPOM ADJUSTED TEMPO",
    "BARTTORVIK ADJUSTED EFFICIENCY", "BARTTORVIK ADJUSTED OFFENSE", "BARTTORVIK ADJUSTED DEFENSE", "BARTHAG", "ELITE SOS", "BARTTORVIK ADJUSTED TEMPO", "2PT %", "3PT %",
    "FREE THROW %", "EFG %", "FREE THROW RATE", "3PT RATE", "AST %", "OFFENSIVE REBOUND %", "DEFENSIVE REBOUND %", "BLOCK %", "TURNOVER %", "2PT % DEFENSE", "3PT % DEFENSE",
    "EFG % DEFENSE", "FREE THROW RATE DEFENSE", "3PT RATE DEFENSE", "OP AST %", "BLOCKED %", "TURNOVER % DEFENSE",
    "WINS ABOVE BUBBLE", "WIN %", "POINTS PER POSSESSION OFFENSE", "POINTS PER POSSESSION DEFENSE"])
    plot = px.scatter(year_rows, x = "SEED", y = y_axis, color = "ROUND", hover_data = ["TEAM", "YEAR"], color_discrete_sequence =
    ["white", "red", "orange", "yellow", "green", "blue", "purple", "pink"], width = 1000, height = 700)
    update_plot(plot)
    st.plotly_chart(plot)

    x_axis = st.selectbox("Select X-Axis Value", options = ["KENPOM ADJUSTED EFFICIENCY", "KENPOM ADJUSTED OFFENSE", "KENPOM ADJUSTED DEFENSE", "KENPOM ADJUSTED TEMPO",
    "BARTTORVIK ADJUSTED EFFICIENCY", "BARTTORVIK ADJUSTED OFFENSE", "BARTTORVIK ADJUSTED DEFENSE", "BARTHAG", "ELITE SOS", "BARTTORVIK ADJUSTED TEMPO", "2PT %", "3PT %",
    "FREE THROW %", "EFG %", "FREE THROW RATE", "3PT RATE", "AST %", "OFFENSIVE REBOUND %", "DEFENSIVE REBOUND %", "BLOCK %", "TURNOVER %", "2PT % DEFENSE", "3PT % DEFENSE",
    "EFG % DEFENSE", "FREE THROW RATE DEFENSE", "3PT RATE DEFENSE", "OP AST %", "BLOCKED %", "TURNOVER % DEFENSE",
    "WINS ABOVE BUBBLE", "WIN %", "POINTS PER POSSESSION OFFENSE", "POINTS PER POSSESSION DEFENSE", ""])
    y_axis = st.selectbox("Select Y-Axis Value", options = ["KENPOM ADJUSTED EFFICIENCY", "KENPOM ADJUSTED OFFENSE", "KENPOM ADJUSTED DEFENSE", "KENPOM ADJUSTED TEMPO",
    "BARTTORVIK ADJUSTED EFFICIENCY", "BARTTORVIK ADJUSTED OFFENSE", "BARTTORVIK ADJUSTED DEFENSE", "BARTHAG", "ELITE SOS", "BARTTORVIK ADJUSTED TEMPO", "2PT %", "3PT %",
    "FREE THROW %", "EFG %", "FREE THROW RATE", "3PT RATE", "AST %", "OFFENSIVE REBOUND %", "DEFENSIVE REBOUND %", "BLOCK %", "TURNOVER %", "2PT % DEFENSE", "3PT % DEFENSE",
    "EFG % DEFENSE", "FREE THROW RATE DEFENSE", "3PT RATE DEFENSE", "OP AST %", "BLOCKED %", "TURNOVER % DEFENSE",
    "WINS ABOVE BUBBLE", "WIN %", "POINTS PER POSSESSION OFFENSE", "POINTS PER POSSESSION DEFENSE", "", ""])
    plot = px.scatter(year_rows, x = x_axis, y = y_axis, color = "ROUND", hover_data = ["TEAM", "SEED", "YEAR"], color_discrete_sequence =
    ["white", "red", "orange", "yellow", "green", "blue", "purple", "pink"], width = 1000, height = 700)
    update_plot(plot)
    st.plotly_chart(plot)

def team_plot() :
    y_axis = st.selectbox("Select Y-Axis Value", options = ["WIN %", "HOME WIN %", "AWAY WIN %", "NEUTRAL WIN %",
            "KENPOM ADJUSTED EFFICIENCY", "KENPOM ADJUSTED OFFENSE", "KENPOM ADJUSTED DEFENSE", "KENPOM ADJUSTED TEMPO",
            "BARTTORVIK ADJUSTED EFFICIENCY", "BARTTORVIK ADJUSTED OFFENSE", "BARTTORVIK ADJUSTED DEFENSE", "BARTHAG", "ELITE SOS", "BARTTORVIK ADJUSTED TEMPO",
            "2PT %", "3PT %", "EFG %", "FREE THROW RATE", "3PT RATE", "ASSIST %", "TURNOVER %", "BLOCKED %", "OFFENSIVE REBOUND %", "POINTS PER POSSESSION OFFENSE",
            "2PT % DEFENSE", "3PT % DEFENSE", "EFG % DEFENSE", "FREE THROW RATE DEFENSE", "3PT RATE DEFENSE", "OP ASSIST %", "TURNOVER % DEFENSE", "BLOCK %", "DEFENSIVE REBOUND %", "POINTS PER POSSESSION DEFENSE",
            "FREE THROW %", "ELITE SOS", "BARTHAG", "WINS ABOVE BUBBLE", "SCORING MARGIN"])
    return y_axis

def update_plot(plot) :
    plot.update_xaxes(gridcolor = "gray")
    plot.update_yaxes(gridcolor = "gray")
    plot.update_layout(font=  dict(size = 18))

def seed_profiles(all_data, seed_df, seed_select_box, seed) :
    if seed_select_box == "1" :  r1, r2, c1, c2, r3, r4, c3, c4, r5, r6, c5, c6 = 0, 6, 0, 1, 0, 1, 1, 2, 0, 1, 2, 3
    if seed_select_box == "2" :  r1, r2, c1, c2, r3, r4, c3, c4, r5, r6, c5, c6 = 0, 6, 3, 4, 0, 2, 4, 5, 0, 1, 5, 6
    if seed_select_box == "3" :  r1, r2, c1, c2, r3, r4, c3, c4, r5, r6, c5, c6 = 0, 6, 6, 7, 0, 2, 7, 8, 0, 1, 8, 9
    if seed_select_box == "4" :  r1, r2, c1, c2, r3, r4, c3, c4, r5, r6, c5, c6 = 0, 6, 9, 10, 0, 1, 10, 11, 0, 1, 11, 12
    if seed_select_box == "5" :   r1, r2, c1, c2, r3, r4, c3, c4, r5, r6, c5, c6 = 0, 6, 12, 13, 0, 2, 13, 14, 0, 1, 14, 15
    if seed_select_box == "6" :   r1, r2, c1, c2, r3, r4, c3, c4 = 0, 6, 15, 16, 0, 2, 16, 17
    if seed_select_box == "7" :   r1, r2, c1, c2, r3, r4, c3, c4 = 0, 6, 17, 18, 0, 2, 18, 19
    if seed_select_box == "8" :   r1, r2, c1, c2, r3, r4, c3, c4 = 0, 6, 19, 20, 0, 1, 20, 21
    if seed_select_box == "9"  :  r1, r2, c1, c2, r3, r4, c3, c4 = 0, 6, 21, 22, 0, 1, 22, 23
    if seed_select_box == "10" : r1, r2, c1, c2, r3, r4, c3, c4, r5, r6, c5, c6 = 0, 6, 23, 24, 0, 3, 24, 25, 0, 2, 25, 26
    if seed_select_box == "11" : r1, r2, c1, c2, r3, r4, c3, c4, r5, r6, c5, c6 = 0, 6, 26, 27, 0, 3, 27, 28, 0, 1, 28, 29
    if seed_select_box == "12" : r1, r2, c1, c2, r3, r4, c3, c4, r5, r6, c5, c6 = 0, 6, 29, 30, 0, 1, 30, 31, 0, 2, 31, 32
    if seed_select_box == "13" :  r1, r2, c1, c2, r3, r4, c3, c4 = 0, 6, 32, 33, 0, 2, 33, 34
    if seed_select_box == "14" :  r1, r2, c1, c2, r3, r4, c3, c4 = 0, 6, 34, 35, 0, 1, 35, 36
    if seed_select_box == "15" :  r1, r2, c1, c2 = 0, 6, 36, 37
    if seed_select_box == "16" :  r1, r2, c1, c2 = 0, 6, 37, 38

    with col1 :
        if seed_select_box == "1" or seed_select_box == "2" or seed_select_box == "3" or seed_select_box == "4" \
        or seed_select_box == "5"  or seed_select_box == "10" or seed_select_box == "11" or seed_select_box == "12" :
            seed_1 = seed_df.iloc[r1:r2, c1:c2]
            st.table(seed_1)
            seed_2 = seed_df.iloc[r3:r4, c3:c4]
            st.table(seed_2)
            seed_3 = seed_df.iloc[r5:r6, c5:c6]
            st.table(seed_3)
        elif seed_select_box == "6" or seed_select_box == "7" or seed_select_box == "8" or seed_select_box == "9" \
        or seed_select_box == "13" or seed_select_box == "14" :
            seed_4 = seed_df.iloc[r1:r2, c1:c2]
            st.table(seed_4)
            seed_5 = seed_df.iloc[r3:r4, c3:c4]
            st.table(seed_5)
        elif seed_select_box == "15" or seed_select_box == "16" :
            seed_6 = seed_df.iloc[r1:r2, c1:c2]
            st.table(seed_6)

    with col2 :
        seed_plot(all_data, seed)

def team_profiles(team, all_teams, team_facts, team_select_box) :
    temp = all_teams
    temp["SORT"] = ""
    temp["SORT"] = temp["SORT"].replace([""], "1")

    if team_select_box == "Houston" :
        st.title("Houston Cougars")
        r1, r2, c1, c2, r3 ,r4, c3, c4, r5, r6, c5, c6, r7, r8, c7, c8, r9, r10, c9, c10, r11, r12, c11, c12 = \
        0, 1, 2, 6, 0, 1, 6, 10, 0, 2, 10, 18, 0, 2, 18, 28, 0, 2, 28, 38, 0, 2, 38, 43
        offense = Image.open(r"C:\Users\Light\PycharmProjects\March_Madness\Shot Charts\Houston Offense.png")
        defense = Image.open(r"C:\Users\Light\PycharmProjects\March_Madness\Shot Charts\Houston Defense.png")
        temp.at[0, "SORT"] = "0"
    if team_select_box == "Tennessee" :
        st.title("Tennessee Volunteers")
        r1, r2, c1, c2, r3 ,r4, c3, c4, r5, r6, c5, c6, r7, r8, c7, c8, r9, r10, c9, c10, r11, r12, c11, c12 = \
        1, 2, 2, 6, 1, 2, 6, 10, 2, 4, 10, 18, 2, 4, 18, 28, 2, 4, 28, 38, 2, 4, 38, 43
        offense = Image.open(r"C:\Users\Light\PycharmProjects\March_Madness\Shot Charts\Tennessee Offense.png")
        defense = Image.open(r"C:\Users\Light\PycharmProjects\March_Madness\Shot Charts\Tennessee Defense.png")
        temp.at[1, "SORT"] = "0"

    col1, col2 = st.columns([0.8, 1.2])

    with col1 :
        st.write("**GENERAL**")
        general = team.iloc[r1:r2, c1:c2]
        general = go.Figure(data = [go.Table(header = dict(values = list(general.columns), line_color = "black", fill_color = "#383636", align = "center", font_size = 12),
        cells = dict(values = [general["CONFERENCE"], general["SEED"], general["CONF. TOURNEY"], general["AP POLL RANK"]], line_color = "black", fill_color = "#575252",
        align = "center", font_size = 12))])
        general.update_layout(width = 500, height = 50, margin = dict(r = 1, l = 1, t = 1, b = 1))
        st.write(general)

        st.write("**WIN %**")
        win = team.iloc[r3:r4, c3:c4]
        win = go.Figure(data = [go.Table(header = dict(values = list(win.columns), line_color = "black", fill_color = "#383636", align = "center", font_size = 12),
        cells = dict(values = [win["WIN %"], win["HOME"], win["AWAY"], win["NEUTRAL"]], line_color = "black", fill_color = "#575252",
        align = "center", font_size = 12))])
        win.update_layout(width = 500, height = 50, margin = dict(r = 1, l = 1, t = 1, b = 1))
        st.write(win)

        shot_chart(offense, defense)

    with col2 :
        st.write("**KENPOM & BARTTORVIK**")
        kb = team.iloc[r5:r6, c5:c6]
        kb = go.Figure(data = [go.Table(header = dict(values = list(kb.columns), line_color = "black", fill_color = "#383636", align = "center", font_size = 12),
        cells = dict(values = [kb["K ADJ. EFFICIENCY"], kb["K ADJ. OFFENSE"], kb["K ADJ. DEFENSE"], kb["K ADJ. TEMPO"], kb["B ADJ. EFFICIENCY"], kb["B ADJ. OFFENSE"], kb["B ADJ. DEFENSE"], kb["B ADJ. TEMPO"]],
        line_color = "black", fill_color = [["#575252", "#8f8585"] * 2], align = "center", font_size = 12))])
        kb.update_layout(width = 900, height = 75, margin = dict(r = 1, l = 1, t = 1, b = 1))
        st.write(kb)

        st.write("**OFFENSE**")
        offense = team.iloc[r7:r8, c7:c8]
        offense = go.Figure(data = [go.Table(header = dict(values = list(offense.columns), line_color = "black", fill_color = "#383636", align = "center", font_size = 12),
        cells = dict(values = [offense["2PT %"], offense["3PT %"], offense["EFG %"], offense["FT RATE"], offense["3PT RATE"], offense["AST %"], offense["TOV %"], offense["BLKED %"], offense["O REB %"], offense["PPP O"]],
        line_color = "black", fill_color = [["#575252", "#8f8585"] * 2], align = "center", font_size = 12))])
        offense.update_layout(width = 900, height = 75, margin = dict(r = 1, l = 1, t = 1, b = 1))
        st.write(offense)

        st.write("**DEFENSE**")
        defense = team.iloc[r9:r10, c9:c10]
        defense = go.Figure(data = [go.Table(header = dict(values = list(defense.columns), line_color = "black", fill_color = "#383636", align = "center", font_size = 12),
        cells = dict(values = [defense["2PT % D"], defense["3PT % D"], defense["EFG % D"], defense["FT RATE D"], defense["3PT RATE D"], defense["OP AST %"], defense["TOV % D"], defense["BLK %"], defense["D REB %"], defense["PPP D"]],
        line_color = "black", fill_color = [["#575252", "#8f8585"] * 2], align = "center", font_size = 12))])
        defense.update_layout(width = 900, height = 75, margin = dict(r = 1, l = 1, t = 1, b = 1))
        st.write(defense)

        st.write("**OTHER**")
        other = team.iloc[r11:r12, c11:c12]
        other = go.Figure(data = [go.Table(header = dict(values = list(other.columns), line_color = "black", fill_color = "#383636", align = "center", font_size = 12),
        cells = dict(values = [other["FT %"], other["ELITE SOS"], other["BARTHAG"], other["WAB"], other["SCORING MARGIN"]],
        line_color = "black", fill_color = [["#575252", "#8f8585"] * 2], align = "center", font_size = 12))])
        other.update_layout(width = 900, height = 75, margin = dict(r = 1, l = 1, t = 1, b = 1))
        st.write(other)

        if team_select_box == "Houston" :
            plot = px.scatter(all_teams, x = "SEED", y = team_plot(), color = "SORT", hover_data = ["TEAM"],
            color_discrete_sequence = ["white", "red"], width = 1000, height = 700)
            update_team_plot(plot)
            st.plotly_chart(plot)
        else :
            plot = px.scatter(all_teams, x = "SEED", y = team_plot(), color = "SORT", hover_data = ["TEAM"],
            color_discrete_sequence = ["red", "white"], width = 1000, height = 700)
            update_team_plot(plot)
            st.plotly_chart(plot)

def update_team_plot(plot) :
    update_plot(plot)
    plot.update_layout(xaxis = dict(dtick = 1), showlegend = False)

def shot_chart(offense, defense) :
    st.subheader("**Shot Charts**")
    offense = offense.resize((500, 500))
    st.image(offense)
    defense = defense.resize((500, 500))
    st.image(defense)

def matchups(team_options_1, team_options_2, team, all_teams) :
    col1, col2, col3 = st.columns(3)

    with col1 :
        team_select_box1 = st.selectbox("Select Team", options = team_options_1)

        if team_select_box1 == "Kansas" :
            r1, r2, c1, c2, r3, r4, c3, c4 = 0, 1, 2, 6, 0, 1, 6, 10
            offense = Image.open(r"C:\Users\Light\PycharmProjects\March_Madness\Shot Charts\Houston Offense.png")
            defense = Image.open(r"C:\Users\Light\PycharmProjects\March_Madness\Shot Charts\Houston Defense.png")
        if team_select_box1 == "Arizona" :
            r1, r2, c1, c2, r3, r4, c3, c4, = 1, 2, 2, 6, 1, 2, 6, 10
            offense = Image.open(r"C:\Users\Light\PycharmProjects\March_Madness\Shot Charts\Tennessee Offense.png")
            defense = Image.open(r"C:\Users\Light\PycharmProjects\March_Madness\Shot Charts\Tennessee Defense.png")
        if team_select_box1 == "Providence":
            r1, r2, c1, c2, r3, r4, c3, c4, = 13, 14, 2, 6, 13, 14, 6, 10
            offense = Image.open(r"C:\Users\Light\PycharmProjects\March_Madness\Shot Charts\Tennessee Offense.png")
            defense = Image.open(r"C:\Users\Light\PycharmProjects\March_Madness\Shot Charts\Tennessee Defense.png")
        if team_select_box1 == "Wisconsin":
            r1, r2, c1, c2, r3, r4, c3, c4, = 11, 12, 2, 6, 11, 12, 6, 10
            offense = Image.open(r"C:\Users\Light\PycharmProjects\March_Madness\Shot Charts\Tennessee Offense.png")
            defense = Image.open(r"C:\Users\Light\PycharmProjects\March_Madness\Shot Charts\Tennessee Defense.png")

        st.write("**GENERAL**")
        general = team.iloc[r1:r2, c1:c2]
        general = go.Figure(data = [go.Table(header = dict(values = list(general.columns), line_color = "black", fill_color = "#383636", align = "center", font_size = 12),
        cells = dict(values = [general["CONFERENCE"], general["SEED"], general["CONF. TOURNEY"], general["AP POLL RANK"]], line_color = "black", fill_color = "#575252",
        align = "center", font_size = 12))])
        general.update_layout(width = 500, height = 50, margin = dict(r = 1, l = 1, t = 1, b = 1))
        st.write(general)

        st.write("**WIN %**")
        win = team.iloc[r3:r4, c3:c4]
        win = go.Figure(data = [go.Table(header = dict(values = list(win.columns), line_color = "black", fill_color = "#383636", align = "center", font_size = 12),
        cells = dict(values = [win["WIN %"], win["HOME"], win["AWAY"], win["NEUTRAL"]], line_color = "black", fill_color = "#575252",
        align = "center", font_size = 12))])
        win.update_layout(width = 500, height = 50, margin = dict(r = 1, l = 1, t = 1, b = 1))
        st.write(win)
        shot_chart(offense, defense)

    with col2 :
        team_select_box2 = st.selectbox("Select Team", options = team_options_2)

        if team_select_box2 == "Kansas" :
            r1, r2, c1, c2, r3, r4, c3, c4 = 0, 1, 2, 6, 0, 1, 6, 10
            offense = Image.open(r"C:\Users\Light\PycharmProjects\March_Madness\Shot Charts\Houston Offense.png")
            defense = Image.open(r"C:\Users\Light\PycharmProjects\March_Madness\Shot Charts\Houston Defense.png")
        if team_select_box2 == "Arizona" :
            r1, r2, c1, c2, r3, r4, c3, c4, = 1, 2, 2, 6, 1, 2, 6, 10
            offense = Image.open(r"C:\Users\Light\PycharmProjects\March_Madness\Shot Charts\Tennessee Offense.png")
            defense = Image.open(r"C:\Users\Light\PycharmProjects\March_Madness\Shot Charts\Tennessee Defense.png")
        if team_select_box2 == "Providence":
            r1, r2, c1, c2, r3, r4, c3, c4, = 13, 14, 2, 6, 13, 14, 6, 10
            offense = Image.open(r"C:\Users\Light\PycharmProjects\March_Madness\Shot Charts\Tennessee Offense.png")
            defense = Image.open(r"C:\Users\Light\PycharmProjects\March_Madness\Shot Charts\Tennessee Defense.png")
        if team_select_box2 == "Wisconsin":
            r1, r2, c1, c2, r3, r4, c3, c4, = 11, 12, 2, 6, 11, 12, 6, 10
            offense = Image.open(r"C:\Users\Light\PycharmProjects\March_Madness\Shot Charts\Tennessee Offense.png")
            defense = Image.open(r"C:\Users\Light\PycharmProjects\March_Madness\Shot Charts\Tennessee Defense.png")

        st.write("**GENERAL**")
        general = team.iloc[r1:r2, c1:c2]
        general = go.Figure(data = [go.Table(header = dict(values = list(general.columns), line_color = "black", fill_color = "#383636", align = "center", font_size = 12),
        cells = dict(values = [general["CONFERENCE"], general["SEED"], general["CONF. TOURNEY"], general["AP POLL RANK"]], line_color = "black", fill_color = "#575252",
        align = "center", font_size = 12))])
        general.update_layout(width = 500, height = 50, margin = dict(r = 1, l = 1, t = 1, b = 1))
        st.write(general)

        st.write("**WIN %**")
        win = team.iloc[r3:r4, c3:c4]
        win = go.Figure(data = [go.Table(header = dict(values = list(win.columns), line_color = "black", fill_color = "#383636", align = "center", font_size = 12),
        cells = dict(values = [win["WIN %"], win["HOME"], win["AWAY"], win["NEUTRAL"]], line_color = "black", fill_color = "#575252",
        align = "center", font_size = 12))])
        win.update_layout(width = 500, height = 50, margin = dict(r = 1, l = 1, t = 1, b = 1))
        st.write(win)

        shot_chart(offense, defense)

        with col3 :
            stat_options = ["KENPOM & BARTTORVIK", "OFFENSE", "DEFENSE", "OTHER"]
            stat_select_box = st.selectbox("Select Stat Type", options = stat_options)

            temp1 = all_teams[all_teams["TEAM"] == team_select_box1]
            temp2 = all_teams[all_teams["TEAM"] == team_select_box2]
            temp3 = [temp1, temp2]
            source = pd.concat(temp3)

            if stat_select_box == "KENPOM & BARTTORVIK" :
                st.write("**KENPOM**")

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("KENPOM ADJUSTED EFFICIENCY", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [- 7, 35])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "KENPOM ADJUSTED EFFICIENCY")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("KENPOM ADJUSTED OFFENSE", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [95, 125])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "KENPOM ADJUSTED OFFENSE")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("KENPOM ADJUSTED DEFENSE", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [84, 110])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "KENPOM ADJUSTED DEFENSE")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("KENPOM ADJUSTED TEMPO", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [61, 75])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "KENPOM ADJUSTED TEMPO")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                st.markdown("""---""")


                st.write("**BARTTORVIK**")

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("BARTTORVIK ADJUSTED EFFICIENCY", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [- 7, 35])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "BARTTORVIK ADJUSTED EFFICIENCY")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("BARTTORVIK ADJUSTED OFFENSE", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [95, 125])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "BARTTORVIK ADJUSTED OFFENSE")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("BARTTORVIK ADJUSTED DEFENSE", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [84, 110])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "BARTTORVIK ADJUSTED DEFENSE")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("BARTTORVIK ADJUSTED TEMPO", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [61, 75])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "BARTTORVIK ADJUSTED TEMPO")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                st.markdown("""---""")

            if stat_select_box == "OFFENSE" :
                st.write("**OFFENSE**")

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("2PT %", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [42, 65])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "2PT %")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("3PT %", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [30, 42])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "3PT %")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("EFG %", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [45, 60])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "EFG %")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("FREE THROW RATE", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [23, 42])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "FREE THROW RATE")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("3PT RATE", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [27, 50])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "3PT RATE")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("ASSIST %", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [39, 67])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "ASSIST %")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("TURNOVER %", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [12, 23])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "TURNOVER %")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("BLOCKED %", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [4.5, 14])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "BLOCKED %")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("OFFENSIVE REBOUND %", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [21, 40])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "OFFENSIVE REBOUND %")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("POINTS PER POSSESSION OFFENSE", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [0.95, 1.25])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "POINTS PER POSSESSION OFFENSE")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                st.markdown("""---""")

            if stat_select_box == "DEFENSE" :
                st.write("**DEFENSE**")

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("2PT % DEFENSE", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [41, 54])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "2PT % DEFENSE")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("3PT % DEFENSE", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [27, 38])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "3PT % DEFENSE")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("EFG % DEFENSE", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [43, 54])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "EFG % DEFENSE")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("FREE THROW RATE DEFENSE", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [18, 42])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "FREE THROW RATE DEFENSE")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("3PT RATE DEFENSE", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [28, 48])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "3PT RATE DEFENSE")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("OP ASSIST %", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [35, 60])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "OP ASSIST %")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("TURNOVER % DEFENSE", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [14, 26])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "TURNOVER % DEFENSE")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("BLOCK %", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [4, 21])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "BLOCK %")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("DEFENSIVE REBOUND %", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [61, 80])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "DEFENSIVE REBOUND %")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("POINTS PER POSSESSION DEFENSE", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [0.85, 1.1])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "POINTS PER POSSESSION DEFENSE")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                st.markdown("""---""")

            if stat_select_box == "OTHER" :
                st.write("**OTHER**")

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("FREE THROW %", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [65, 83])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "FREE THROW %")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("ELITE SOS", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [5, 40])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "ELITE SOS")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("BARTHAG", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [0.3, 1])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "BARTHAG")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("WINS ABOVE BUBBLE", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [- 10, 10])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "WINS ABOVE BUBBLE")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                bars = alt.Chart(source).mark_bar(clip = True).encode(x = alt.X("SCORING MARGIN", axis = alt.Axis(labels = False, ticks = False),
                scale = alt.Scale(domain = [- 10, 10])), y = alt.Y("TEAM", axis = alt.Axis(ticks = False)), color = alt.Color("TEAM", legend = None))
                text = bars.mark_text(dx = 15).encode(text = "SCORING MARGIN")
                bar_chart = bars + text
                bar_chart = alt.layer(bar_chart).configure_axis(grid = False).configure_view(strokeWidth = 0)
                st.altair_chart(bar_chart, use_container_width=  True)

                st.markdown("""---""")

# Home Page ============================================================================================================
if selected == "Home" :
    st.title(f" {selected}")

    all_teams = pd.read_csv("2023 Data Abridged.csv")
    all_teams = all_teams.astype(str)

    cm1 = sns.diverging_palette(15, 150, as_cmap = True)
    cm2 = sns.diverging_palette(150, 15, as_cmap = True)

    overall_df = all_teams.iloc[:, [0, 1, 2, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]]
    offense_df = all_teams.iloc[0:69, 0:16]
    defense_df = all_teams.iloc[:, [0, 1, 2, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]]

    stat_options = ["OVERALL", "OFFENSE", "DEFENSE"]
    stat_select_box = st.selectbox("Select Stat Type", options = stat_options)

    if stat_select_box == "OVERALL" :
        st.table(overall_df.style.background_gradient(cmap = cm1, subset = ["K ADJ. EFFICIENCY", "B ADJ. EFFICIENCY", "K ADJ. TEMPO", "B ADJ. TEMPO", "BARTHAG",
        "ELITE SOS", "WAB", "WIN %", "HOME WIN %", "AWAY WIN %", "NEUTRAL WIN %", "SCORING MARGIN"]))
    if stat_select_box == "OFFENSE" :
        st.table(offense_df.style.background_gradient(cmap = cm1, subset = ["K ADJ. OFFENSE", "B ADJ. OFFENSE", "2PT %", "3PT %", "FT %", "EFG %", "FT RATE",
        "3PT RATE", "AST %", "O REBOUND %", "PPP O", "BLOCKED %", "TOV %"]))
    if stat_select_box == "DEFENSE" :
        st.table(defense_df.style.background_gradient(cmap = cm2, subset = ["K ADJ. DEFENSE", "B ADJ. DEFENSE", "2PT % D", "3PT % D", "FT % D", "EFG % D", "FT RATE D",
        "3PT RATE D", "OP AST %", "D REBOUND %", "PPP D", "BLOCK %", "TOV % D"]))

# Charts Page ==========================================================================================================
if selected == "Charts" :
    st.title(f" {selected}")

    all_data = pd.read_csv("All Data.csv")
    this_year = all_data.iloc[0:68, 0:41]

    col1, col2 = st.columns(2)

    with col1 :
        st.subheader("**By Year**")
        year_options = ["2023", "2022", "2021", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008"]
        year_select_box = st.selectbox("Select Year", options = year_options)
        if year_select_box == "2023": year_plot(all_data, 2023)
        if year_select_box == "2022": year_plot(all_data, 2022)
        if year_select_box == "2021": year_plot(all_data, 2021)
        if year_select_box == "2019": year_plot(all_data, 2019)
        if year_select_box == "2018": year_plot(all_data, 2018)
        if year_select_box == "2017": year_plot(all_data, 2017)
        if year_select_box == "2016": year_plot(all_data, 2016)
        if year_select_box == "2015": year_plot(all_data, 2015)
        if year_select_box == "2014": year_plot(all_data, 2014)
        if year_select_box == "2013": year_plot(all_data, 2013)
        if year_select_box == "2012": year_plot(all_data, 2012)
        if year_select_box == "2011": year_plot(all_data, 2011)
        if year_select_box == "2010": year_plot(all_data, 2010)
        if year_select_box == "2009": year_plot(all_data, 2009)
        if year_select_box == "2008" : year_plot(all_data, 2008)

    with col2 :
        st.subheader("**2023 Teams**")
        x_axis = st.selectbox("Select X-Axis Value", options = ["SEED", ""])
        y_axis = st.selectbox("Select Y-Axis Value", options = ["KENPOM ADJUSTED EFFICIENCY", "KENPOM ADJUSTED OFFENSE", "KENPOM ADJUSTED DEFENSE", "KENPOM ADJUSTED TEMPO",
        "BARTTORVIK ADJUSTED EFFICIENCY", "BARTTORVIK ADJUSTED OFFENSE", "BARTTORVIK ADJUSTED DEFENSE", "BARTHAG", "ELITE SOS", "BARTTORVIK ADJUSTED TEMPO", "2PT %", "3PT %",
        "FREE THROW %", "EFG %", "FREE THROW RATE", "3PT RATE", "AST %", "OFFENSIVE REBOUND %", "DEFENSIVE REBOUND %", "BLOCK %", "TURNOVER %", "2PT % DEFENSE", "3PT % DEFENSE",
        "EFG % DEFENSE", "FREE THROW RATE DEFENSE", "3PT RATE DEFENSE", "OP AST %", "BLOCKED %", "TURNOVER % DEFENSE",
        "WINS ABOVE BUBBLE", "WIN %", "POINTS PER POSSESSION OFFENSE", "POINTS PER POSSESSION DEFENSE", ""])
        plot = px.scatter(this_year, x = x_axis, y = y_axis, color = "ROUND", hover_data = ["TEAM", "SEED", "YEAR"], color_discrete_sequence =
        ["white", "red", "orange", "yellow", "green", "blue", "purple", "pink"], width = 1000, height = 700)
        update_plot(plot)
        st.plotly_chart(plot)

        x_axis = st.selectbox("Select X-Axis Value", options = ["KENPOM ADJUSTED EFFICIENCY", "KENPOM ADJUSTED OFFENSE", "KENPOM ADJUSTED DEFENSE", "KENPOM ADJUSTED TEMPO",
        "BARTTORVIK ADJUSTED EFFICIENCY", "BARTTORVIK ADJUSTED OFFENSE", "BARTTORVIK ADJUSTED DEFENSE", "BARTHAG", "ELITE SOS", "BARTTORVIK ADJUSTED TEMPO", "2PT %", "3PT %",
        "FREE THROW %", "EFG %", "FREE THROW RATE", "3PT RATE", "AST %", "OFFENSIVE REBOUND %", "DEFENSIVE REBOUND %", "BLOCK %", "TURNOVER %", "2PT % DEFENSE", "3PT % DEFENSE",
        "EFG % DEFENSE", "FREE THROW RATE DEFENSE", "3PT RATE DEFENSE", "OP AST %", "BLOCKED %", "TURNOVER % DEFENSE",
        "WINS ABOVE BUBBLE", "WIN %", "POINTS PER POSSESSION OFFENSE", "POINTS PER POSSESSION DEFENSE", "", ""])
        y_axis = st.selectbox("Select Y-Axis Value", options = ["KENPOM ADJUSTED EFFICIENCY", "KENPOM ADJUSTED OFFENSE", "KENPOM ADJUSTED DEFENSE", "KENPOM ADJUSTED TEMPO",
        "BARTTORVIK ADJUSTED EFFICIENCY", "BARTTORVIK ADJUSTED OFFENSE", "BARTTORVIK ADJUSTED DEFENSE", "BARTHAG", "ELITE SOS", "BARTTORVIK ADJUSTED TEMPO", "2PT %", "3PT %",
        "FREE THROW %", "EFG %", "FREE THROW RATE", "3PT RATE", "AST %", "OFFENSIVE REBOUND %", "DEFENSIVE REBOUND %", "BLOCK %", "TURNOVER %", "2PT % DEFENSE", "3PT % DEFENSE",
        "EFG % DEFENSE", "FREE THROW RATE DEFENSE", "3PT RATE DEFENSE", "OP AST %", "BLOCKED %", "TURNOVER % DEFENSE",
        "WINS ABOVE BUBBLE", "WIN %", "POINTS PER POSSESSION OFFENSE", "POINTS PER POSSESSION DEFENSE", "", "", ""])
        plot = px.scatter(this_year, x = x_axis, y = y_axis, color = "ROUND", hover_data = ["TEAM", "SEED", "YEAR"], color_discrete_sequence =
        ["white", "red", "orange", "yellow", "green", "blue", "purple", "pink"], width = 1000, height = 700)
        update_plot(plot)
        st.plotly_chart(plot)


    st.subheader("**All Teams**")
    x_axis = st.selectbox("Select X-Axis Value", options = ["KENPOM ADJUSTED EFFICIENCY", "KENPOM ADJUSTED OFFENSE", "KENPOM ADJUSTED DEFENSE", "KENPOM ADJUSTED TEMPO",
    "BARTTORVIK ADJUSTED EFFICIENCY", "BARTTORVIK ADJUSTED OFFENSE", "BARTTORVIK ADJUSTED DEFENSE", "BARTHAG", "ELITE SOS", "BARTTORVIK ADJUSTED TEMPO", "2PT %", "3PT %",
    "FREE THROW %", "EFG %", "FREE THROW RATE", "3PT RATE", "AST %", "OFFENSIVE REBOUND %", "DEFENSIVE REBOUND %", "BLOCK %", "TURNOVER %", "2PT % DEFENSE", "3PT % DEFENSE",
    "EFG % DEFENSE", "FREE THROW RATE DEFENSE", "3PT RATE DEFENSE", "OP AST %", "BLOCKED %", "TURNOVER % DEFENSE",
    "WINS ABOVE BUBBLE", "WIN %", "POINTS PER POSSESSION OFFENSE", "POINTS PER POSSESSION DEFENSE", "", "", "", ""])
    y_axis = st.selectbox("Select Y-Axis Value", options = ["KENPOM ADJUSTED EFFICIENCY", "KENPOM ADJUSTED OFFENSE", "KENPOM ADJUSTED DEFENSE", "KENPOM ADJUSTED TEMPO",
    "BARTTORVIK ADJUSTED EFFICIENCY", "BARTTORVIK ADJUSTED OFFENSE", "BARTTORVIK ADJUSTED DEFENSE", "BARTHAG", "ELITE SOS", "BARTTORVIK ADJUSTED TEMPO", "2PT %", "3PT %",
    "FREE THROW %", "EFG %", "FREE THROW RATE", "3PT RATE", "AST %", "OFFENSIVE REBOUND %", "DEFENSIVE REBOUND %", "BLOCK %", "TURNOVER %", "2PT % DEFENSE", "3PT % DEFENSE",
    "EFG % DEFENSE", "FREE THROW RATE DEFENSE", "3PT RATE DEFENSE", "OP AST %", "BLOCKED %", "TURNOVER % DEFENSE",
    "WINS ABOVE BUBBLE", "WIN %", "POINTS PER POSSESSION OFFENSE", "POINTS PER POSSESSION DEFENSE",  "", "", "", "", ""])
    plot = px.scatter(all_data, x = x_axis, y = y_axis, color = "ROUND", hover_data = ["TEAM", "SEED", "YEAR"], color_discrete_sequence =
    ["white", "red", "orange", "yellow", "green", "blue", "purple", "pink"], width = 1500, height = 700)
    update_plot(plot)
    st.plotly_chart(plot)


    x_axis = st.selectbox("Select X-Axis Value", options = ["KENPOM ADJUSTED EFFICIENCY", "KENPOM ADJUSTED OFFENSE", "KENPOM ADJUSTED DEFENSE", "KENPOM ADJUSTED TEMPO",
    "BARTTORVIK ADJUSTED EFFICIENCY", "BARTTORVIK ADJUSTED OFFENSE", "BARTTORVIK ADJUSTED DEFENSE", "BARTHAG", "ELITE SOS", "BARTTORVIK ADJUSTED TEMPO", "2PT %", "3PT %",
    "FREE THROW %", "EFG %", "FREE THROW RATE", "3PT RATE", "AST %", "OFFENSIVE REBOUND %", "DEFENSIVE REBOUND %", "BLOCK %", "TURNOVER %", "2PT % DEFENSE", "3PT % DEFENSE",
    "EFG % DEFENSE", "FREE THROW RATE DEFENSE", "3PT RATE DEFENSE", "OP AST %", "BLOCKED %", "TURNOVER % DEFENSE",
    "WINS ABOVE BUBBLE", "WIN %", "POINTS PER POSSESSION OFFENSE", "POINTS PER POSSESSION DEFENSE"])
    y_axis = st.selectbox("Select Y-Axis Value", options = ["YEAR", "SEED"])
    plot = px.scatter(all_data, x = x_axis, y = y_axis, color = "ROUND", hover_data = ["TEAM", "SEED", "YEAR"], color_discrete_sequence =
    ["white", "red", "orange", "yellow", "green", "blue", "purple", "pink"], width = 1500, height = 700)
    update_plot(plot)
    st.plotly_chart(plot)


# Seed Profiles Page ===================================================================================================
if selected == "Seed Profiles" :
    st.title(f" {selected}")

    all_data = pd.read_csv("All Data.csv")
    seed_df = pd.read_csv("Seed Profiles.csv")
    seed_df.set_axis(["OVERALL PERFORMANCE", "NUMBER 1 OVERALL SEED PERFORMANCE", "AP POLL",
                      "OVERALL PERFORMANCE", "KENPOM / BARTTORVIK TRENDS", "AP POLL",
                      "OVERALL PERFORMANCE", "KENPOM / BARTTORVIK TRENDS", "MISCELLANOUS TRENDS",
                      "OVERALL PERFORMANCE", "KENPOM / BARTTORVIK TRENDS", "MISCELLANOUS TRENDS",
                      "OVERALL PERFORMANCE", "KENPOM / BARTTORVIK TRENDS", "MISCELLANOUS TRENDS",
                      "OVERALL PERFORMANCE", "KENPOM / BARTTORVIK TRENDS",
                      "OVERALL PERFORMANCE", "KENPOM / BARTTORVIK TRENDS",
                      "OVERALL PERFORMANCE", "KENPOM / BARTTORVIK TRENDS",
                      "OVERALL PERFORMANCE", "KENPOM / BARTTORVIK TRENDS",
                      "OVERALL PERFORMANCE", "KENPOM / BARTTORVIK TRENDS", "MISCELLANOUS TRENDS",
                      "OVERALL PERFORMANCE", "KENPOM / BARTTORVIK TRENDS", "MISCELLANOUS TRENDS",
                      "OVERALL PERFORMANCE", "KENPOM / BARTTORVIK TRENDS", "MISCELLANOUS TRENDS",
                      "OVERALL PERFORMANCE", "KENPOM / BARTTORVIK TRENDS",
                      "OVERALL PERFORMANCE", "KENPOM / BARTTORVIK TRENDS",
                      "OVERALL PERFORMANCE",
                      "OVERALL PERFORMANCE"],
                     axis="columns", inplace=True)

    col1, col2 = st.columns([0.8, 1.2])

    with col1 :
        seed_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
        seed_select_box = st.selectbox("Select Seed", options = seed_options)

    if seed_select_box == "1" : seed_profiles(all_data, seed_df, seed_select_box, 1)
    if seed_select_box == "2" : seed_profiles(all_data, seed_df, seed_select_box, 2)
    if seed_select_box == "3" : seed_profiles(all_data, seed_df, seed_select_box, 3)
    if seed_select_box == "4" : seed_profiles(all_data, seed_df, seed_select_box, 4)
    if seed_select_box == "5" : seed_profiles(all_data, seed_df, seed_select_box, 5)
    if seed_select_box == "6" : seed_profiles(all_data, seed_df, seed_select_box, 6)
    if seed_select_box == "7" : seed_profiles(all_data, seed_df, seed_select_box, 7)
    if seed_select_box == "8 ": seed_profiles(all_data, seed_df, seed_select_box, 8)
    if seed_select_box == "9 ": seed_profiles(all_data, seed_df, seed_select_box, 9)
    if seed_select_box == "10" : seed_profiles(all_data, seed_df, seed_select_box, 10)
    if seed_select_box == "11" : seed_profiles(all_data, seed_df, seed_select_box, 11)
    if seed_select_box == "12" : seed_profiles(all_data, seed_df, seed_select_box, 12)
    if seed_select_box == "13" : seed_profiles(all_data, seed_df, seed_select_box, 13)
    if seed_select_box == "14" : seed_profiles(all_data, seed_df, seed_select_box, 14)
    if seed_select_box == "15" : seed_profiles(all_data, seed_df, seed_select_box, 15)
    if seed_select_box == "16" : seed_profiles(all_data, seed_df, seed_select_box, 16)

# Team Profiles Page ===================================================================================================
if selected == "Team Profiles" :
    st.title(f" {selected}")

    team = pd.read_csv("Team Profile Data.csv")
    team = team.astype(str)
    all_teams = pd.read_csv("2023 Data.csv")
    team_facts = pd.read_csv("Team Facts.csv")

    team_options = ["Houston", "Tennessee"]
    team_select_box = st.selectbox("Select Team", options = team_options)

    if team_select_box == "Houston" : team_profiles(team, all_teams, team_facts, team_select_box)
    if team_select_box == "Tennessee" : team_profiles(team, all_teams, team_facts, team_select_box)

# Trends Page ==========================================================================================================
if selected == "Trends" :
    st.title(f" {selected}")

    trends = pd.read_csv("Trends.csv")
    col1, col2 = st.columns(2)

    with col1 :
        kenpom = trends.iloc[0:4, 0:1]
        st.table(kenpom)
        barttorvik = trends.iloc[0:4, 1:2]
        st.table(barttorvik)
        seeding = trends.iloc[0:4, 2:3]
        st.table(seeding)

    with col2 :
        conference = trends.iloc[0:4, 3:4]
        st.table(conference)
        scoring = trends.iloc[0:6, 4:5]
        st.table(scoring)
        miscellaneous = trends.iloc[0:4, 5:6]
        st.table(miscellaneous)

# Game Predictor Page ==================================================================================================
if selected == "Game Predictor" :
    st.title(f" {selected}")

    team = pd.read_csv("Team Profile Data.csv")
    team = team.astype(str)
    all_teams = pd.read_csv("2023 Data.csv")

    team_options_1 = ["Kansas", "Arizona", "Providence", "Wisconsin"]
    team_options_2 = ["Kansas", "Arizona", "Providence", "Wisconsin", ""]

    matchups(team_options_1, team_options_2, team, all_teams)

    # https: // evolytics.com / blog / march - madness - tableau - dashboard - enhances - machine - learning - model /
