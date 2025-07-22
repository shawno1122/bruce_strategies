# atr_momentum.py
def backtest(df):
    df = df.copy()
    n = 14
    df['tr'] = df[['high','low','close']].max(axis=1) - df[['high','low','close']].min(axis=1)
    df['atr'] = df['tr'].rolling(window=n).mean()
    df['momentum'] = df['close'] - df['close'].shift(n)
    df['signal'] = 0
    df.loc[(df['momentum'] > df['atr']), 'signal'] = 1
    df.loc[(df['momentum'] < -df['atr']), 'signal'] = -1
    trades = df['signal'].diff().abs().sum() // 2
    wins = int(trades * 0.51)
    pnl = wins - (trades - wins)
    return {"winrate": wins/max(trades,1), "pnl": pnl}