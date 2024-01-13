from algosdk import account, mnemonic
from typing import Dict, Any
from algosdk.v2client import algod

class AlgorandAccountManager:
    def __init__(self):
        # Initialize any necessary parameters or dependencies here.
        pass

    def create_account(self):
        """
        Generate a new Algorand account securely for production use.

        Returns:
            private_key (str): The private key of the new account.
            address (str): The public address associated with the private key.
            mnemonic_phrase (str): The mnemonic phrase for the private key.
        """
        private_key, address = account.generate_account()
        mnemonic_phrase = mnemonic.from_private_key(private_key)

        return private_key, address, mnemonic_phrase

    def get_account_info(algod_address: str, algod_token: str, account_address: str) -> Dict[str, Any]:
        """
        Get the account information, including balance, from the Algorand blockchain.

        Args:
            algod_address (str): The Algorand API endpoint.
            algod_token (str): The API key for authentication.
            account_address (str): The public address of the account.

        Returns:
            account_info (Dict[str, Any]): The account information.
        """
        algod_client = algod.AlgodClient(algod_token, algod_address)

        try:
            account_info = algod_client.account_info(account_address)
            balance = account_info.get("amount")
            print(f"Account Balance for {account_address}: {balance} microAlgos")
            return account_info
        except Exception as e:
            print(f"Error getting account information: {e}")
            return None
