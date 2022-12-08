import pandas as pd
from PIL import Image
import plotly_express as px
import plotly.graph_objects as go
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout = "wide")

hide_table_row_index = """ <style> thead tr th:first-child {display:none} tbody th {display:none} </style> """
st.markdown(hide_table_row_index, unsafe_allow_html=True)

# Navigation Bar
selected = option_menu(
    menu_title = "Navigation",
    options = ["Home", "Seed Profiles", "Team Profiles", "Trends", "Game Predictor"],
    icons = ["house-fill", "tree-fill", "people-fill", "graph-up-arrow", "robot"],
    menu_icon = "map-fill",
    orientation = "horizontal",
    default_index = 0,
    )

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
    update_seed_plot(plot)
    st.plotly_chart(plot)

def team_plot() :
    y_axis = st.selectbox("Select Y-Axis Value", options = ["WIN %", "HOME WIN %", "AWAY WIN %", "NEUTRAL WIN %",
            "KENPOM ADJUSTED EFFICIENCY", "KENPOM ADJUSTED OFFENSE", "KENPOM ADJUSTED DEFENSE", "KENPOM ADJUSTED TEMPO",
            "BARTTORVIK ADJUSTED EFFICIENCY", "BARTTORVIK ADJUSTED OFFENSE", "BARTTORVIK ADJUSTED DEFENSE", "BARTHAG", "ELITE SOS", "BARTTORVIK ADJUSTED TEMPO",
            "2PT %", "3PT %", "EFG %", "FREE THROW RATE", "3PT RATE", "ASSIST %", "TURNOVER %", "BLOCKED %", "OFFENSIVE REBOUND %", "POINTS PER POSSESSION OFFENSE",
            "2PT % DEFENSE", "3PT % DEFENSE", "EFG % DEFENSE", "FREE THROW RATE DEFENSE", "3PT RATE DEFENSE", "OP ASSIST %", "TURNOVER % DEFENSE", "BLOCK %", "DEFENSIVE REBOUND %", "POINTS PER POSSESSION DEFENSE",
            "FREE THROW %", "ELITE SOS", "BARTHAG", "WINS ABOVE BUBBLE", "SCORING MARGIN"])
    return y_axis

def update_seed_plot(plot) :
    plot.update_xaxes(gridcolor = "gray")
    plot.update_yaxes(gridcolor = "gray")
    plot.update_layout(font=  dict(size = 18))

def update_team_plot(plot) :
    update_seed_plot(plot)
    plot.update_layout(xaxis = dict(dtick = 1), showlegend = False)

def shot_chart(offense, defense) :
    st.subheader("**Shot Charts**")
    offense = offense.resize((500, 500))
    st.image(offense)
    defense = defense.resize((500, 500))
    st.image(defense)

# Home Page ============================================================================================================
if selected == "Home" :
    st.title(f" {selected}")

# Seed Profiles Page ===================================================================================================
if selected == "Seed Profiles" :
    st.title(f" {selected}")

    col1, col2 = st.columns([0.8, 1.2])

    with col1 :
        seed_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
        seed_select_box = st.selectbox("Select Seed", options = seed_options)

    df = pd.read_csv("All Data.csv")
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
                      axis = "columns", inplace = True)

    if seed_select_box == "1" :
        with col1 :
            seed_1 = seed_df.iloc[0:6, 0:1]
            st.table(seed_1)
            seed_2 = seed_df.iloc[0:1, 1:2]
            st.table(seed_2)
            seed_3 = seed_df.iloc[0:1, 2:3]
            st.table(seed_3)

        with col2 :
            seed_plot(df, 1)

    if seed_select_box == "2" :
        with col1:
            seed_1 = seed_df.iloc[0:6, 3:4]
            st.table(seed_1)
            seed_2 = seed_df.iloc[0:2, 4:5]
            st.table(seed_2)
            seed_3 = seed_df.iloc[0:1, 5:6]
            st.table(seed_3)

        with col2:
            seed_plot(df, 2)

    if seed_select_box == "3" :
        with col1:
            seed_1 = seed_df.iloc[0:6, 6:7]
            st.table(seed_1)
            seed_2 = seed_df.iloc[0:2, 7:8]
            st.table(seed_2)
            seed_3 = seed_df.iloc[0:1, 8:9]
            st.table(seed_3)

        with col2:
            seed_plot(df, 3)

    if seed_select_box == "4" :
        with col1:
            seed_1 = seed_df.iloc[0:6, 9:10]
            st.table(seed_1)
            seed_2 = seed_df.iloc[0:1, 10:11]
            st.table(seed_2)
            seed_3 = seed_df.iloc[0:1, 11:12]
            st.table(seed_3)

        with col2:
            seed_plot(df, 4)

    if seed_select_box == "5" :
        with col1:
            seed_1 = seed_df.iloc[0:6, 12:13]
            st.table(seed_1)
            seed_2 = seed_df.iloc[0:2, 13:14]
            st.table(seed_2)
            seed_3 = seed_df.iloc[0:1, 14:15]
            st.table(seed_3)

        with col2:
            seed_plot(df, 5)

    if seed_select_box == "6" :
        with col1:
            seed_1 = seed_df.iloc[0:6, 15:16]
            st.table(seed_1)
            seed_2 = seed_df.iloc[0:2, 16:17]
            st.table(seed_2)

        with col2:
            seed_plot(df, 6)

    if seed_select_box == "7" :
        with col1:
            seed_1 = seed_df.iloc[0:6, 17:18]
            st.table(seed_1)
            seed_2 = seed_df.iloc[0:2, 18:19]
            st.table(seed_2)

        with col2:
            seed_plot(df, 7)

    if seed_select_box == "8" :
        with col1:
            seed_1 = seed_df.iloc[0:6, 19:20]
            st.table(seed_1)
            seed_2 = seed_df.iloc[0:1, 20:21]
            st.table(seed_2)

        with col2:
            seed_plot(df, 8)

    if seed_select_box == "9" :
        with col1:
            seed_1 = seed_df.iloc[0:6, 21:22]
            st.table(seed_1)
            seed_2 = seed_df.iloc[0:1, 22:23]
            st.table(seed_2)

        with col2:
            seed_plot(df, 9)

    if seed_select_box == "10" :
        with col1:
            seed_1 = seed_df.iloc[0:6, 23:24]
            st.table(seed_1)
            seed_2 = seed_df.iloc[0:3, 24:25]
            st.table(seed_2)
            seed_3 = seed_df.iloc[0:2, 25:26]
            st.table(seed_3)

        with col2:
            seed_plot(df, 10)

    if seed_select_box == "11" :
        with col1:
            seed_1 = seed_df.iloc[0:6, 26:27]
            st.table(seed_1)
            seed_2 = seed_df.iloc[0:3, 27:28]
            st.table(seed_2)
            seed_3 = seed_df.iloc[0:1, 28:29]
            st.table(seed_3)

        with col2:
            seed_plot(df, 11)

    if seed_select_box == "12" :
        with col1:
            seed_1 = seed_df.iloc[0:6, 29:30]
            st.table(seed_1)
            seed_2 = seed_df.iloc[0:1, 30:31]
            st.table(seed_2)
            seed_3 = seed_df.iloc[0:2, 31:32]
            st.table(seed_3)

        with col2:
            seed_plot(df, 12)

    if seed_select_box == "13" :
        with col1:
            seed_1 = seed_df.iloc[0:6, 32:33]
            st.table(seed_1)
            seed_2 = seed_df.iloc[0:2, 33:34]
            st.table(seed_2)

        with col2:
            seed_plot(df, 13)

    if seed_select_box == "14" :
        with col1:
            seed_1 = seed_df.iloc[0:6, 34:35]
            st.table(seed_1)
            seed_2 = seed_df.iloc[0:1, 35:36]
            st.table(seed_2)

        with col2:
            seed_plot(df, 14)

    if seed_select_box == "15" :
        with col1:
            seed_1 = seed_df.iloc[0:6, 36:37]
            st.table(seed_1)

        with col2:
            seed_plot(df, 15)

    if seed_select_box == "16" :
        with col1:
            seed_1 = seed_df.iloc[0:6, 37:38]
            st.table(seed_1)

        with col2:
            seed_plot(df, 16)

# Team Profiles Page ===================================================================================================
if selected == "Team Profiles" :
    st.title(f" {selected}")

    team_options = ["Houston", "Tennessee", "Texas", "Gonzaga", "Arizona", "Purdue", "UCLA", "Indiana", "Connecticut", "West Virginia", "Illinois", "Kentucky", "Duke",
                    "Creighton", "Virginia", "Saint Mary's"]
    team_select_box = st.selectbox("Select Team", options = team_options)

    team = pd.read_csv("Team Profile Data.csv")
    team = team.astype(str)

    all_teams = pd.read_csv("2023 Data.csv")
    team_facts = pd.read_csv("Team Facts.csv")

    if team_select_box == "Houston" :
        st.title("Houston Cougars")

        temp = all_teams
        temp["SORT"] = ""
        col1, col2 = st.columns([0.8, 1.2])

        with col1 :
            st.write("**GENERAL**")
            general = team.iloc[0:1, 2:6]
            general = go.Figure(data = [go.Table(header = dict(values = list(general.columns), line_color = "black", fill_color = "#383636", align = "center", font_size = 12),
            cells = dict(values = [general["CONFERENCE"], general["SEED"], general["CONF. TOURNEY"], general["AP POLL RANK"]], line_color = "black", fill_color = "#575252",
            align = "center", font_size = 12))])
            general.update_layout(width = 500, height = 50, margin = dict(r = 1, l = 1, t = 1, b = 1))
            st.write(general)

            st.write("**WIN %**")
            win = team.iloc[0:1, 6:10]
            win = go.Figure(data = [go.Table(header = dict(values = list(win.columns), line_color = "black", fill_color = "#383636", align = "center", font_size = 12),
            cells = dict(values = [win["WIN %"], win["HOME"], win["AWAY"], win["NEUTRAL"]], line_color = "black", fill_color = "#575252",
            align = "center", font_size = 12))])
            win.update_layout(width = 500, height = 50, margin = dict(r = 1, l = 1, t = 1, b = 1))
            st.write(win)

            offense = Image.open(r"C:\Users\Light\PycharmProjects\March_Madness\Shot Charts\Houston Offense.png")
            defense = Image.open(r"C:\Users\Light\PycharmProjects\March_Madness\Shot Charts\Houston Defense.png")
            shot_chart(offense, defense)

        with col2 :
            st.write("**KENPOM & BARTTORVIK**")
            kb = team.iloc[0:2, 10:18]
            kb = go.Figure(data = [go.Table(header = dict(values = list(kb.columns), line_color = "black", fill_color = "#383636", align = "center", font_size = 12),
            cells = dict(values = [kb["K ADJ. EFFICIENCY"], kb["K ADJ. OFFENSE"], kb["K ADJ. DEFENSE"], kb["K ADJ. TEMPO"], kb["B ADJ. EFFICIENCY"], kb["B ADJ. OFFENSE"], kb["B ADJ. DEFENSE"], kb["B ADJ. TEMPO"]],
            line_color = "black", fill_color = [["#575252", "#8f8585"] * 2], align = "center", font_size = 12))])
            kb.update_layout(width = 1050, height = 75, margin = dict(r = 1, l = 1, t = 1, b = 1))
            st.write(kb)

            st.write("**OFFENSE**")
            offense = team.iloc[0:2, 18:28]
            offense = go.Figure(data = [go.Table(header = dict(values = list(offense.columns), line_color = "black", fill_color = "#383636", align = "center", font_size = 12),
            cells = dict(values = [offense["2PT %"], offense["3PT %"], offense["EFG %"], offense["FT RATE"], offense["3PT RATE"], offense["AST %"], offense["TOV %"], offense["BLKED %"], offense["O REB %"], offense["PPP O"]],
            line_color = "black", fill_color = [["#575252", "#8f8585"] * 2], align = "center", font_size = 12))])
            offense.update_layout(width = 1050, height = 75, margin = dict(r = 1, l = 1, t = 1, b = 1))
            st.write(offense)

            st.write("**DEFENSE**")
            defense = team.iloc[0:2, 28:38]
            defense = go.Figure(data = [go.Table(header = dict(values = list(defense.columns), line_color = "black", fill_color = "#383636", align = "center", font_size = 12),
            cells = dict(values = [defense["2PT % D"], defense["3PT % D"], defense["EFG % D"], defense["FT RATE D"], defense["3PT RATE D"], defense["OP AST %"], defense["TOV % D"], defense["BLK %"], defense["D REB %"], defense["PPP D"]],
            line_color = "black", fill_color = [["#575252", "#8f8585"] * 2], align = "center", font_size = 12))])
            defense.update_layout(width = 1050, height = 75, margin = dict(r = 1, l = 1, t = 1, b = 1))
            st.write(defense)

            st.write("**OTHER**")
            other = team.iloc[0:2, 38:43]
            other = go.Figure(data = [go.Table(header = dict(values = list(other.columns), line_color = "black", fill_color = "#383636", align = "center", font_size = 12),
            cells = dict(values = [other["FT %"], other["ELITE SOS"], other["BARTHAG"], other["WAB"], other["SCORING MARGIN"]],
            line_color = "black", fill_color = [["#575252", "#8f8585"] * 2], align = "center", font_size = 12))])
            other.update_layout(width = 1050, height = 75, margin = dict(r = 1, l = 1, t = 1, b = 1))
            st.write(other)

            temp["SORT"] = temp["SORT"].replace([""], "1")
            temp.at[0, "SORT"] = "0"
            plot = px.scatter(all_teams, x = "SEED", y = team_plot(), color = "SORT", hover_data = ["TEAM"],
            color_discrete_sequence = ["white", "red"], width = 1000, height = 700)
            update_team_plot(plot)
            st.plotly_chart(plot)

# Trends Page ==========================================================================================================
if selected == "Trends" :
    st.title(f" {selected}")

# Game Predictor Page ==================================================================================================
if selected == "Game Predictor" :
    st.title(f" {selected}")
    # https: // evolytics.com / blog / march - madness - tableau - dashboard - enhances - machine - learning - model /

