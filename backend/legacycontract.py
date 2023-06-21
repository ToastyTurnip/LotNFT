import smartpy as sp

FA2 = sp.io.import_template("fa2_lib.py")

class LotNFT(
    FA2.Fa2Nft,
    FA2.Admin,
    FA2.BurnNft,
    FA2.MintNft,
    FA2.ChangeMetadata,
    FA2.WithdrawMutez
):
    def __init__(self, admin, metadata, token_metadata = {}, ledger = {}, policy = None, metadata_base = None):
        FA2.Fa2Nft.__init__(self, metadata, token_metadata = token_metadata, ledger = ledger, policy = policy, metadata_base = metadata_base)
        FA2.Admin.__init__(self, admin)

@sp.add_test(name='sampletest')
def test():
    sc = sp.test_scenario()
    admin = sp.address("tz1NPvQ8agyyP87cm54ja5zyNs3Lw2prv5FU")

    sc.h1("LotNFT")
    nft = LotNFT(admin=admin, metadata = sp.utils.metadata_of_url("http://example.com"))
    sc += nft
    
sp.add_compilation_target(
    "LotNFT Deployment",
    LotNFT(
        admin = sp.address("tz1NPvQ8agyyP87cm54ja5zyNs3Lw2prv5FU"),
        metadata = sp.utils.metadata_of_url("https://example.com")
    )
)