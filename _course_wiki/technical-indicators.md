---
title: "Technical Indicators"
summary: "Engineered market features — moving averages, momentum, volatility — computed with the Ta-Lib library."
related_course:
  - Backtesting
  - LangChain
  - Market Data APIs
  - Pandas
  - Playwright
  - Time Series Decomposition
---

Technical indicators are derived features computed from price series: moving averages that smooth trends, momentum measures over lookback windows, volatility bands, and the classic oscillator family. Module 2 computes them with the Ta-Lib library on top of the cleaned price data, turning raw OHLCV columns into model-ready features.

The module pairs each indicator with the predictive framing question: does this feature help predict future growth over the next week, month, or year? That question — features in, future growth out — is the bridge from this module into the time-series modeling module.

## Taught in

- [Machine Learning Zoomcamp](/course-wiki/machine-learning-zoomcamp/)
  - [Module 3: Machine Learning for Classification](/course-wiki/mlz-module-03/)
    - [Feature importance: Churn rate and risk ratio](/course-wiki/mlz-m03-feature-importance-churn-rate-and-risk-ratio/)
- [Stock Markets Analytics Zoomcamp](/course-wiki/stock-markets-analytics-zoomcamp/)
  - [Module 5: Deployment and Automation](/course-wiki/sma-module-05/)
    - [Deployment and Automation](/course-wiki/sma-m05-deployment-and-automation/)
## Related concepts

- [Pandas](/course-wiki/pandas/)
- [Time Series Decomposition](/course-wiki/time-series-decomposition/)
- [Market Data APIs](/course-wiki/market-data-apis/)
- [Backtesting](/course-wiki/backtesting/)
