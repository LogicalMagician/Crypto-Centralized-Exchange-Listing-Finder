This script is designed to monitor Ethereum addresses for incoming ETH deposits and check the transaction history of the depositor's ETH wallets for any contract deployments. The script can be used to identify new ERC20 tokens that are being listed on centralized cryptocurrency exchanges before they are officially announced, giving the user an edge over others who are waiting for the announcement.

Requirements
To run this script, you will need:

Python 3.6 or higher
An Etherscan API key
Setup
To set up the script, follow these steps:

Clone the repository to your local machine.
Install the required Python packages by running the following command:
Copy code
pip install -r requirements.txt
Add the Ethereum addresses you want to monitor to a text file called "eth_addresses.txt". Each address should be added on a new line.
Add your Etherscan API key to the "API_KEY" variable in the script.
Run the script using the following command:
Copy code
python monitor_eth_addresses.py
The script will monitor the ETH addresses in the "eth_addresses.txt" file and save any new ERC20 tokens that are identified to a new text file called "new_tokens.txt".

Why is this useful?
Many centralized cryptocurrency exchanges offer a listing service where the owner of a specific cryptocurrency pays them to get their asset listed. This process can be expensive and time-consuming, and it is often kept secret until the listing is officially announced. By monitoring Ethereum addresses for incoming ETH deposits and checking the transaction history of the depositor's ETH wallets for any contract deployments, the script can identify new ERC20 tokens that are likely being listed on centralized exchanges before they are officially announced. This can give the user an edge over others who are waiting for the announcement and allow them to potentially profit from buying the token before it is listed on a major exchange.

You need to add your list of wallet addresses which you will have collected where listing payments are made into.
