"""This file contains auxiliary function that we use throughout the respy tutorial."""

import matplotlib.pyplot as plt
import pandas as pd


def plot_choice_shares(df):
    fig, ax = plt.subplots()

    df.groupby("Period").Choice.value_counts(normalize=True).unstack().plot.bar(
        stacked=True, ax=ax
    )

    plt.xticks(rotation="horizontal")

    plt.legend(loc="lower center", bbox_to_anchor=(0.5, -0.275), ncol=2)

    plt.show()
    plt.close()

def plot_choice_prob_and_exp_level(df, friday=False):

    fig, axs = plt.subplots(1, 2, figsize=(14, 5))
        
    (
        df.groupby("Period")
        .Choice.value_counts(normalize=True)
        .unstack()
        .plot.bar(ax=axs[0], color = colors, stacked=True, rot=0, title="Choice Probabilities")
    )

    (
        df.groupby("Period")
        .Experience_Fishing.value_counts(normalize=True)
        .unstack()
        .plot.bar(
            ax=axs[1],
            stacked=True,
            rot=0,
            title="Share of Experience Level per Period",
            cmap="Blues",
        )
    )
    
    
    axs[0].legend(
       label , loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=2
    )
    axs[1].legend(loc="right", bbox_to_anchor=(1.3, 0.5), ncol=1, title="Experience")

    plt.show()
    
    
def plot_choice_prob(df):
    
    fig, ax = plt.subplots()

    df.groupby("Period").Choice.value_counts(normalize=True).unstack().plot.bar(
        stacked=True, ax=ax
    )

    plt.xticks(rotation="horizontal")

    plt.legend(loc="lower center", bbox_to_anchor=(0.5, -0.275), ncol=2)

    plt.show()
    plt.close()