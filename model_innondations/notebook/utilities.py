# -*- coding: utf-8 -*-
import pandas as pd
import os

DATASET_FOLDER = "../../datasets/"


def gen_worldbank_countries():
    # Écrit un csv avec les pays et les codes associés des pays qui nous intéresses

    df_des = dataframe_flood()

    df = pd.DataFrame(df_des.groupby("Country")[["Country", "ISO"]].head(1))
    df.rename(columns={"Country": "name", "ISO": "code"}, inplace=True)
    df.to_csv(f"{DATASET_FOLDER}worldbank_countries.csv", index=False)


def dataframe_flood():
    # Renvoit une dataframe avec les désastres de type flood

    try:
        df = pd.read_excel(
            f"{DATASET_FOLDER}emdat_public_2020_09_12_query_uid-tAnKEX.xlsx",
            index_col=0,
        )
    except FileNotFoundError:
        print(
            f"Le fichier 'edmat_public_2020_09_12_query_uid-tAnKEX.xlsx'\
        n'est pas dans le dossier {DATASET_FOLDER}"
        )

    # Mise en forme de la dataframe (les premières lignes ne nous intéressent pas)
    df.columns = list(df.iloc[5])
    df = df.iloc[6:]

    # On ne prends que les désatres de type inondations
    df = df[df["Disaster Type"] == "Flood"]

    return df


def gen_dataset():
    """Créer les deux fichier : historique_precipitation_clean.csv et projection_precipitation_clean.csv
    """

    def abreviation2nombre(abr):
        lst_abr = [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ]
        return lst_abr.index(abr) + 1

    dir_precipitation = DATASET_FOLDER + "precipitation/"

    df_hist = pd.DataFrame()
    df_pred = pd.DataFrame()

    for i, entry in enumerate(os.scandir(dir_precipitation)):

        print(f"\r{i+1}/899", end="")

        if ".csv" in entry.name:

            df = pd.read_csv(dir_precipitation + entry.name, sep=r", ", engine="python")

            if "historical" in entry.name:
                # S'il y a un problème de vigule on nettoit le dataframe
                if df.Country.all() in [
                    "The",
                    "State of",
                    "United Republic of",
                    "Democratic People’s Republic of",
                ]:
                    df.reset_index(inplace=True)

                    # On récuppère le nom réel
                    df["new_Country"] = df[["Statistics", "Country"]].apply(
                        lambda x: x[0] + ", " + x[1], axis=1
                    )
                    df.drop("Country", axis=1, inplace=True)
                    df.rename(
                        columns={
                            "index": "Rainfall - (MM)",
                            "Rainfall - (MM)": "Year",
                            "Year": "Statistics",
                            "Statistics": "tmp",
                            "new_Country": "Country",
                        },
                        inplace=True,
                    )
                    df.drop("tmp", axis=1, inplace=True)
                df_hist = df_hist.append(df)

            else:
                # S'il y a un problème de vigule on nettoit le dataframe
                if df.Country.all() in ["State of", "United Republic of"]:
                    df.reset_index(inplace=True)

                    # On récuppère le nom réel
                    df["new_Country"] = df[["Statistics", "Country"]].apply(
                        lambda x: x[0] + ", " + x[1], axis=1
                    )
                    df.drop("Country", axis=1, inplace=True)

                    df.rename(
                        columns={
                            "index": "Monthly Precipitation - (MM)",
                            "Monthly Precipitation - (MM)": "Year",
                            "Year": "Model",
                            "Model": "Statistics",
                            "Statistics": "tmp",
                            "new_Country": "Country",
                        },
                        inplace=True,
                    )
                    df.drop("tmp", axis=1, inplace=True)
                df_pred = df_pred.append(df)

    # On créé une variable pour pouvoir faire le tri sur les mois
    df_pred["Month"] = (
        df_pred["Statistics"].str[:4].apply(lambda x: abreviation2nombre(x.strip()))
    )

    df_pred.sort_values(["Country", "Year", "Model", "Month"], inplace=True)

    # On rajoute la variable 'Region'
    add_region(df_pred)

    df_pred.to_csv(f"{DATASET_FOLDER}projection_precipitation_clean.csv", index=False)

    # On créé une variable pour pouvoir faire le tri sur les mois
    df_hist["Month"] = (
        df_hist["Statistics"].str[:4].apply(lambda x: abreviation2nombre(x.strip()))
    )

    # On rajoute la variable 'Region'
    add_region(df_hist)

    df_hist.sort_values(["Country", "Year", "Month"], inplace=True)
    df_hist.to_csv(f"{DATASET_FOLDER}historical_precipitation_clean.csv", index=False)


def add_region(df):
    """Rajoute une variable 'Region' dans une dataframe qui contient une variable 'Country' """
    try:
        df_region = pd.read_csv(f"{DATASET_FOLDER}country_region.csv", index_col=0)
    except FileNotFoundError:
        df_des = dataframe_flood()
        df_region = df_des.groupby("Country")[["Country", "Region"]].head(1)

        # On créer une dataframe qu'on utilisera comme un dict
        df_region = df_region.set_index("Country", drop=True)["Region"]

        # On sauvgarde la dataframe
        df_region.to_csv(f"{DATASET_FOLDER}country_region.csv")

    country_region = df_region.to_dict()["Region"]

    try:
        df["Region"] = df.Country.apply(lambda x: country_region[x])
    except KeyError:
        print("La dataframe n'a pas de variable 'Country'")
