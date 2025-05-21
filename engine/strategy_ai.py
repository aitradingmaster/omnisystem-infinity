def make_decisions(data):
    from engine.analysis import predict, analyze_sentiment
    from engine.indicators import get_rsi, get_sma

    predictions = predict(data)
    decisions = []

    for ticker, price in data.items():
        pred = predictions.get(ticker, 0)
        sentiment = analyze_sentiment(ticker)
        rsi = get_rsi(ticker)
        sma = get_sma(ticker)

        confidence = 0.4 * pred + 0.2 * sentiment + 0.2 * (1 - abs(rsi - 50) / 50) + 0.2 * (1 if price > sma else 0)

        if confidence > 0.75:
            action = "buy"
        elif confidence < 0.4:
            action = "sell"
        else:
            action = "hold"

        decisions.append({
            "ticker": ticker,
            "action": action,
            "confidence": round(confidence, 2),
            "price": price
        })

    return decisions