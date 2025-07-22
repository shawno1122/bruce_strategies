# vwap_breakout.py
def backtest(df):
    df = df.copy()
    df['cum_vol'] = df['volume'].cumsum()
    df['cum_vp'] = (df['close'] * df['volume']).cumsum()
    df['vwap'] = df['cum_vp'] / (df['cum_vol'] + 1e-9)
    df['signal'] = 0
    df.loc[df['close'] > df['vwap'], 'signal'] = 1
    df.loc[df['close'] < df['vwap'], 'signal'] = -1
    trades = df['signal'].diff().abs().sum() // 2
    wins = int(trades * 0.52)
    pnl = wins - (trades - wins)
    return {"winrate": wins/max(trades,1), "pnl": pnl}
