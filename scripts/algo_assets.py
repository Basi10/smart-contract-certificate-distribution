from algosdk import account, mnemonic
from algosdk.v2client import algod
from algosdk import transaction

class AlgoAssetManager:
    def __init__(self, algod_client: algod.AlgodClient):
        self.algod_client = algod_client

    def create_asset(self, private_key: str, address: str, url: str):
        sp = self.algod_client.suggested_params()
        txn = transaction.AssetConfigTxn(
            sender=address,
            sp=sp,
            default_frozen=False,
            unit_name="CERT",
            asset_name="Certification",
            manager=address,
            reserve=address,
            freeze=address,
            clawback=address,
            url=url,
            total=1,
            decimals=0,
        )
        stxn = txn.sign(private_key)
        txid = self.algod_client.send_transaction(stxn)
        print(f"Sent asset create transaction with txid: {txid}")
        results = transaction.wait_for_confirmation(self.algod_client, txid, 4)
        print(f"Result confirmed in round: {results['confirmed-round']}")
        created_asset = results["asset-index"]
        print(f"Asset ID created: {created_asset}")
        return created_asset

    def transfer_asset(self, private_key: str, sender: str, receiver: str, created_asset: int):
        sp = self.algod_client.suggested_params()
        xfer_txn = transaction.AssetTransferTxn(
            sender=sender,
            sp=sp,
            receiver=receiver,
            amt=1,
            index=created_asset,
        )
        signed_xfer_txn = xfer_txn.sign(private_key)
        txid = self.algod_client.send_transaction(signed_xfer_txn)
        print(f"Sent transfer transaction with txid: {txid}")
        results = transaction.wait_for_confirmation(self.algod_client, txid, 4)
        print(f"Result confirmed in round: {results['confirmed-round']}")
        return txid

    def receive_asset(self, acct2: account.Account, created_asset: int):
        sp = self.algod_client.suggested_params()
        optin_txn = transaction.AssetOptInTxn(
            sender=acct2.address, sp=sp, index=created_asset
        )
        signed_optin_txn = optin_txn.sign(acct2.private_key)
        txid = self.algod_client.send_transaction(signed_optin_txn)
        print(f"Sent opt in transaction with txid: {txid}")
        results = transaction.wait_for_confirmation(self.algod_client, txid, 4)
        print(f"Result confirmed in round: {results['confirmed-round']}")
        return txid

    def get_asset_info(self, asset_id: int):
        asset_info = self.algod_client.asset_info(asset_id)
        print(asset_info)
        return asset_info