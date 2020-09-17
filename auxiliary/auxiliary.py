"""This file contains auxiliary function that we use throughout the respy tutorial."""

import matplotlib.pyplot as plt
import pandas as pd


def plot_fishing_grounds(df):
    fig, ax = plt.subplots(1, 2, figsize=(14, 5))

    for i, observable in enumerate(["rich", "poor"]):
        df.query("Fishing_Grounds == @observable").groupby(
            "Period").Choice.value_counts(
            normalize=True,
        ).unstack().plot.bar(width=0.4, stacked=True, rot=0, legend=False, ax=ax[i])
        ax[i].set_title("Fishing grounds: " + observable, pad=10)
        ax[i].xaxis.label.set_visible(False)

    plt.legend(loc="lower center", bbox_to_anchor=(-0.15, -0.3), ncol=2)
    plt.suptitle("Robinson's choices by period", y=1.05)

    plt.show()


def plot_choice_shares(df, friday=False):
    if friday:
        color = ["C0", "C2", "C1"]
        choices = 3
    else:
        color = ["C0", "C1"]
        choices = 2

    fig, ax = plt.subplots()

    df.groupby("Period").Choice.value_counts(normalize=True).unstack().plot.bar(
        stacked=True, ax=ax, color=color
    )

    plt.xticks(rotation="horizontal")

    plt.legend(loc="lower center", bbox_to_anchor=(0.5, -0.275), ncol=choices)

    plt.show()
    plt.close()


def plot_choice_prob_and_exp_level(df, friday=False):

    fig, axs = plt.subplots(1, 2, figsize=(14, 5))
        
    (
        df.groupby("Period")
        .Choice.value_counts(normalize=True)
        .unstack()
        .plot.bar(ax=axs[0], stacked=True, rot=0, title="Choice Probabilities")
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
    
    
    axs[0].legend(loc="lower center", bbox_to_anchor=(0.5, -0.4), ncol=2
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