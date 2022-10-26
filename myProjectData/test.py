import streamlit as st
import pandas as pd
# import seaborn as sbn
import numpy as nump
# import matplotlib.pyplot as plt
st.write("data analyst on programmation loanguages")
repos = pd.read_csv('repos.csv')
prs = pd.read_csv('prs.csv')
repos_df = pd.DataFrame(repos)
prs_df = pd.DataFrame(prs)
prs_df = prs_df.rename(columns={'name': 'language'})

langages_df = pd.merge(repos_df, prs_df, how="right", on=["language", "language"])

langages_df

langages_df.info()

mo = langages_df['num_repos'].rolling(300).mean()

langages_list = langages_df[langages_df['num_repos'] > mo];
langages_list

Lg = langages_list[langages_list['year'] > 2019];Lg

lg_prog_df = Lg[Lg['count'] >= 100000];
# sbn.relplot(x="num_repos",y="count",data=lg_prog_df,height=7)

st.line_chart(lg_prog_df)


# sbn.relplot(x='language', y='count', data=lg_prog_df, kind='line')
st.vega_lite_chart(lg_prog_df, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'a', 'type': 'quantitative'},
        'y': {'field': 'b', 'type': 'quantitative'},
        'size': {'field': 'c', 'type': 'quantitative'},
        'color': {'field': 'c', 'type': 'quantitative'},
    },
})
