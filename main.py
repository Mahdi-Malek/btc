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
OBV_signal = simulation_data['signal']
OBV_signal = pd.Series(OBV_signal)
print (simulation_data.head())

# ------------------ Relative Strenght Index ------------------
RSI_Ind = tti.RelativeStrengthIndex(input_data=eth_df)
#RSI_Ind.getTiGraph().show()
simulation_data, simulation_statistics, simulation_graph = RSI_Ind.getTiSimulation(
    close_values=eth_df[['close']], max_exposure=None,
    short_exposure_factor=1.5)
#print('\nSimulation Data:\n', simulation_data)
simulation_data.to_csv("Your Path")
RSI_signal = simulation_data['signal']
RSI_signal = pd.Series(RSI_signal)
print (simulation_data.head())

# ------------------ Bollinger Bands Index ------------------
BBI_Ind = tti.BollingerBands(input_data=eth_df)
#BBI_Ind.getTiGraph().show()
simulation_data, simulation_statistics, simulation_graph = BBI_Ind.getTiSimulation(
    close_values=eth_df[['close']], max_exposure=None,
    short_exposure_factor=1.5)
#print('\nSimulation Data:\n', simulation_data)
simulation_data.to_csv("Your Path")
BBI_signal = simulation_data['signal']
BBI_signal = pd.Series(BBI_signal)
print (simulation_data.head())

# ------------------ Moving Average Convergence Divergence ------------------
MACD_Ind = tti.MovingAverageConvergenceDivergence(input_data=eth_df)
#MACD_Ind.getTiGraph().show()
simulation_data, simulation_statistics, simulation_graph = MACD_Ind.getTiSimulation(
    close_values=eth_df[['close']], max_exposure=None,
    short_exposure_factor=1.5)#print('\nSimulation Data:\n', simulation_data)
#print('\nSimulation Data:\n', simulation_data)
simulation_data.to_csv("Your Path")
MACD_signal = simulation_data['signal']
MACD_signal = pd.Series(MACD_signal)
print (simulation_data.head())

# ------------------ Time Series Forecast Index ------------------
TSF_Ind = tti.TimeSeriesForecast(input_data=eth_df)
#TSF_Ind.getTiGraph().show()
simulation_data, simulation_statistics, simulation_graph = TSF_Ind.getTiSimulation(
    close_values=eth_df[['close']], max_exposure=None,
    short_exposure_factor=1.5)
#print('\nSimulation Data:\n', simulation_data)
simulation_data.to_csv("Your Path")
TSF_signal = simulation_data['signal']
TSF_signal = pd.Series(TSF_signal)
print (simulation_data.head())

# ------------------ Relative Volatility Index ------------------
RVI_Ind = tti.RelativeVolatilityIndex(input_data=eth_df)
#TSF_Ind.getTiGraph().show()
simulation_data, simulation_statistics, simulation_graph = RVI_Ind.getTiSimulation(
    close_values=eth_df[['close']], max_exposure=None,
    short_exposure_factor=1.5)
#print('\nSimulation Data:\n', simulation_data)
simulation_data.to_csv("Your Path")
RVI_signal = simulation_data['signal']
RVI_signal = pd.Series(RVI_signal)
print (simulation_data.head())

# ------------------ Fibonacci Retracement Index ------------------
Fib_Ind = tti.FibonacciRetracement(input_data=eth_df)
#TSF_Ind.getTiGraph().show()
simulation_data, simulation_statistics, simulation_graph = Fib_Ind.getTiSimulation(
    close_values=eth_df[['close']], max_exposure=None,
    short_exposure_factor=1.5)
#print('\nSimulation Data:\n', simulation_data)
simulation_data.to_csv("Your Path")
Fib_signal = simulation_data['signal']
Fib_signal = pd.Series(Fib_signal)
print (simulation_data.head())

# ------------------ Total Signal output ------------------
df = pd.concat([OBV_signal,RSI_signal,BBI_signal,MACD_signal,TSF_signal,RVI_signal,Fib_signal],axis=1)
df.columns = ['OBV','RSI','BBI','MACD','TSF','RVI','Fib']
df.to_csv("Your Path")