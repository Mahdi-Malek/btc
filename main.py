import pandas as pd
import tti.indicators as tti

eth_df = pd.read_csv("Your Path")
eth_df.index = pd.to_datetime(eth_df["Open Time"],format="%Y-%m-%d %H:%M:%S")

# ------------------ On Balance Volume Index ------------------
OBV_Ind = tti.OnBalanceVolume(input_data=eth_df)
#OBV_Ind.getTiGraph().show()
simulation_data, simulation_statistics, simulation_graph = OBV_Ind.getTiSimulation(
    close_values=eth_df[['close']], max_exposure=None,
    short_exposure_factor=1.5)
#print('\nSimulation Data:\n', simulation_data)
simulation_data.to_csv("Your Path")

# ------------------ Relative Strenght Index ------------------
RSI_Ind = tti.RelativeStrengthIndex(input_data=eth_df)
#RSI_Ind.getTiGraph().show()
simulation_data, simulation_statistics, simulation_graph = RSI_Ind.getTiSimulation(
    close_values=eth_df[['close']], max_exposure=None,
    short_exposure_factor=1.5)
#print('\nSimulation Data:\n', simulation_data)
simulation_data.to_csv("Your Path")

# ------------------ Bollinger Bands Index ------------------
BBI_Ind = tti.BollingerBands(input_data=eth_df)
#BBI_Ind.getTiGraph().show()
simulation_data, simulation_statistics, simulation_graph = BBI_Ind.getTiSimulation(
    close_values=eth_df[['close']], max_exposure=None,
    short_exposure_factor=1.5)
#print('\nSimulation Data:\n', simulation_data)
simulation_data.to_csv("Your Path")

# ------------------ Moving Average Convergence Divergence ------------------
MACD_Ind = tti.MovingAverageConvergenceDivergence(input_data=eth_df)
#MACD_Ind.getTiGraph().show()
simulation_data, simulation_statistics, simulation_graph = MACD_Ind.getTiSimulation(
    close_values=eth_df[['close']], max_exposure=None,
    short_exposure_factor=1.5)#print('\nSimulation Data:\n', simulation_data)
#print('\nSimulation Data:\n', simulation_data)
simulation_data.to_csv("Your Path")

# ------------------ Time Series Forecast Index ------------------
TSF_Ind = tti.TimeSeriesForecast(input_data=eth_df)
#TSF_Ind.getTiGraph().show()
simulation_data, simulation_statistics, simulation_graph = TSF_Ind.getTiSimulation(
    close_values=eth_df[['close']], max_exposure=None,
    short_exposure_factor=1.5)
#print('\nSimulation Data:\n', simulation_data)
simulation_data.to_csv("Your Path")

# ------------------ Relative Volatility Index ------------------
RVI_Ind = tti.RelativeVolatilityIndex(input_data=eth_df)
#TSF_Ind.getTiGraph().show()
simulation_data, simulation_statistics, simulation_graph = RVI_Ind.getTiSimulation(
    close_values=eth_df[['close']], max_exposure=None,
    short_exposure_factor=1.5)
#print('\nSimulation Data:\n', simulation_data)
simulation_data.to_csv("Your Path")

# ------------------ Fibonacci Retracement Index ------------------
Fib_Ind = tti.FibonacciRetracement(input_data=eth_df)
#TSF_Ind.getTiGraph().show()
simulation_data, simulation_statistics, simulation_graph = Fib_Ind.getTiSimulation(
    close_values=eth_df[['close']], max_exposure=None,
    short_exposure_factor=1.5)
#print('\nSimulation Data:\n', simulation_data)
simulation_data.to_csv("Your Path")