# KuCoin Trading Portfolio Viewer

This project is a Python-based application designed to retrieve and display your current trading portfolio from KuCoin. It leverages the power of AI to provide insights and manage your trading account efficiently. The backend is powered by the Gemini_LLM_Backend, which enhances the application's capabilities with advanced AI functionalities.

## Features

- **AI-Powered Insights**: The application uses AI to analyze your trading portfolio, providing valuable insights and recommendations.
- **Real-Time Data**: Fetches real-time data from KuCoin to ensure you have the most up-to-date information.
- **Secure Access**: Utilizes environment variables to securely manage your API credentials.

## How It Works

1. **Environment Setup**: The application uses a `.env` file to store your KuCoin API credentials securely. Make sure to create this file and add your `API_KEY`, `API_SECRET`, and `PASSPHRASE`.

2. **Dependencies**: The project requires Python packages listed in `requirements.txt`, including `python-dotenv` for environment variable management, `kucoin-python` for interacting with the KuCoin API, and `pandas` for data manipulation.

3. **Portfolio Retrieval**: The `getCurrentPortfolio.py` script connects to KuCoin using your API credentials and retrieves your trading account portfolio. It filters the data to show only relevant information about your trading account balances.

4. **AI Integration**: The backend, powered by Gemini_LLM_Backend, processes the portfolio data to provide AI-driven insights and recommendations, helping you make informed trading decisions.

## Getting Started

1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/yourusername/kucoin-trading-portfolio-viewer.git
   cd kucoin-trading-portfolio-viewer
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the root directory and add your KuCoin API credentials:
   ```
   API_KEY=your_api_key
   API_SECRET=your_api_secret
   PASSPHRASE=your_passphrase
   ```

4. **Run the Application**:
   ```bash
   python main.py
   ```