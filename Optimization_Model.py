import numpy as np
import tensorflow as tf
import os

#%%
## These are parameters we should control to get max profit
smma_slow_length = tf.Variable(300, name = "smma_slow_length")
smma_fast_length = tf.Variable(100, name = "smma_fast_length")
smma_fastest_length = tf.Variable(50, name = "smma_fastest_length")

donchain_period = tf.Variable(20, name = "donchain_period")
volatility_period = tf.Variable(100, name = "volatility_period")

tdi_rsi = tf.Variable(11, name = "tdi_rsi")
band_length = tf.Variable(31, name = "band_length")
fast_ma_on_rsi = tf.Variable(1, name = "fast_ma_on_rsi")
slow_ma_on_rsi = tf.variable(9, name = "slow_ma_on_rsi")

volume_ma_length = tf.Variable(40, name = "volume_ma_length")

tema_period = tf.Variable(55, name = "tema_period")
ema_period = tf.Variable(60, name = "tema_period")
candle_size_factor = tf.Variable(1.1, name = "candle_size_factor")

short_alma_length = tf.Variable(5, name = "short_alma_length")
long_alma_length = tf.Variable(21, name = "long_alma_length")
fast_sigma = tf.Variable(4, name = "fast_sigma")
fast_offset = tf.Variable(0.75, name = "fast_offset")
trend_offset = tf.Variable(0.75, name = "trend_offset")
trend_sigma = tf.Variable(4, name = "trend_sigma")
signal_offset = tf.Variable(0.85, name = "signal_offset")
signal_sigma = tf.Variable(0.85, name = "signal_sigma")

#%%
##Now, we should represent the function using tensorflow


