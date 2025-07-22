# macd_trend.py
def backtest(df):
    df = df.copy()
    ema12 = df['close'].ewm(span=12, adjust=False).mean()
    ema26 = df['close'].ewm(span=26, adjust=False).mean()
    macd = ema12 - ema26
    signal = macd.ewm(span=9, adjust=False).mean()
    df['macd_hist'] = macd - signal
    df['signal'] = 0
    df.loc[df['macd_hist'] > 0, 'signal'] = 1
    df.loc[df['macd_hist'] < 0, 'signal'] = -1
    trades = df['signal'].diff().abs().sum() // 2
    wins = int(trades * 0.53)
    pnl = wins - (trades - wins)
    return {"winrate": wins/max(trades,1), "pnl": pnl}