import pandas as pd
import tti.indicators as tti

eth_df = pd.read_csv("file path")


# ------------------ On Balance Volume Index ------------------
OBV_df = eth_df[["Open Time","Close","Volume"]]
OBV_df.index = pd.to_datetime(OBV_df["Open Time"],format="%Y-%m-%d %H:%M:%S")
OBV_Ind = tti.OnBalanceVolume(input_data=OBV_df)
#OBV_Ind.getTiGraph().show()


# ------------------ Relative Strenght Index ------------------
RSI_df = eth_df
RSI_df.index = pd.to_datetime(RSI_df["Open Time"],format="%Y-%m-%d %H:%M:%S")
RSI_Ind = tti.RelativeStrengthIndex(input_data=RSI_df)
#RSI_Ind.getTiGraph().show()
simulation_data, simulation_statistics, simulation_graph = RSI_Ind.getTiSimulation(
    close_values=RSI_df[['close']], max_exposure=None,
    short_exposure_factor=1.5)
simulation_data.to_csv("file path")


