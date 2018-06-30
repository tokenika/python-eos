class WalletContextManager:
    def __init__(self, wallet_eos_client, wallet_password):
        self.wallet_eos_client = wallet_eos_client
        self.wallet_pasword = wallet_password

    def __enter__(self):
        self.wallet_eos_client.wallet_unlock(self.wallet_pasword)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.wallet_eos_client.wallet_lock()