import requests

# Replace with your own Etherscan API key
API_KEY = "your_api_key_here"

# Read the list of ETH addresses to monitor from a text file
with open("eth_addresses.txt", "r") as f:
    eth_addresses = f.read().splitlines()

for address in eth_addresses:
    # Call the Etherscan API to get the list of incoming ETH transactions for this address
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&sort=desc&apikey={API_KEY}"
    response = requests.get(url)
    tx_list = response.json()["result"]

    for tx in tx_list:
        # Call the Etherscan API to get the transaction details
        tx_url = f"https://api.etherscan.io/api?module=proxy&action=eth_getTransactionByHash&txhash={tx['hash']}&apikey={API_KEY}"
        tx_response = requests.get(tx_url)
        tx_data = tx_response.json()["result"]

        # Check if the transaction is a contract deployment
        if tx_data["input"] != "0x":
            contract_url = f"https://api.etherscan.io/api?module=contract&action=getsourcecode&address={tx_data['to']}&apikey={API_KEY}"
            contract_response = requests.get(contract_url)
            contract_data = contract_response.json()["result"]

            if contract_data:
                # Get the name of the ERC20 token associated with the contract address
                contract_name = contract_data[0]["ContractName"]
                contract_address = tx_data["to"]
                contract_deployer = tx_data["from"]
                fee_address = address

                # Save the relevant information to a text file
                with open("new_tokens.txt", "a") as f:
                    f.write(f"{contract_name},{contract_address},{contract_deployer},{fee_address}\n")
