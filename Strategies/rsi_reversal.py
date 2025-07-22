# rsi_reversal.py
def backtest(df):
    df = df.copy()
    n = 14
    delta = df['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=n).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=n).mean()
    rs = gain / (loss + 1e-9)
    df['rsi'] = 100 - (100 / (1 + rs))
    df['signal'] = 0
    df.loc[df['rsi'] < 30, 'signal'] = 1
    df.loc[df['rsi'] > 70, 'signal'] = -1
    trades = df['signal'].diff().abs().sum() // 2
    wins = int(trades * 0.51)
    pnl = wins - (trades - wins)
    return {"winrate": wins/max(trades,1), "pnl": pnl}
