# Code generated by moonworm : https://github.com/bugout-dev/moonworm
# Moonworm version : 0.6.0

import argparse
import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from brownie import Contract, network, project
from brownie.network.contract import ContractContainer
from eth_typing.evm import ChecksumAddress


PROJECT_DIRECTORY = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BUILD_DIRECTORY = os.path.join(PROJECT_DIRECTORY, "build", "contracts")


def boolean_argument_type(raw_value: str) -> bool:
    TRUE_VALUES = ["1", "t", "y", "true", "yes"]
    FALSE_VALUES = ["0", "f", "n", "false", "no"]

    if raw_value.lower() in TRUE_VALUES:
        return True
    elif raw_value.lower() in FALSE_VALUES:
        return False

    raise ValueError(
        f"Invalid boolean argument: {raw_value}. Value must be one of: {','.join(TRUE_VALUES + FALSE_VALUES)}"
    )


def bytes_argument_type(raw_value: str) -> str:
    return raw_value


def get_abi_json(abi_name: str) -> List[Dict[str, Any]]:
    abi_full_path = os.path.join(BUILD_DIRECTORY, f"{abi_name}.json")
    if not os.path.isfile(abi_full_path):
        raise IOError(
            f"File does not exist: {abi_full_path}. Maybe you have to compile the smart contracts?"
        )

    with open(abi_full_path, "r") as ifp:
        build = json.load(ifp)

    abi_json = build.get("abi")
    if abi_json is None:
        raise ValueError(f"Could not find ABI definition in: {abi_full_path}")

    return abi_json


def contract_from_build(abi_name: str) -> ContractContainer:
    # This is workaround because brownie currently doesn't support loading the same project multiple
    # times. This causes problems when using multiple contracts from the same project in the same
    # python project.
    PROJECT = project.main.Project("moonworm", Path(PROJECT_DIRECTORY))

    abi_full_path = os.path.join(BUILD_DIRECTORY, f"{abi_name}.json")
    if not os.path.isfile(abi_full_path):
        raise IOError(
            f"File does not exist: {abi_full_path}. Maybe you have to compile the smart contracts?"
        )

    with open(abi_full_path, "r") as ifp:
        build = json.load(ifp)

    return ContractContainer(PROJECT, build)


class CharactersFacet:
    def __init__(self, contract_address: Optional[ChecksumAddress]):
        self.contract_name = "CharactersFacet"
        self.address = contract_address
        self.contract = None
        self.abi = get_abi_json("CharactersFacet")
        if self.address is not None:
            self.contract: Optional[Contract] = Contract.from_abi(
                self.contract_name, self.address, self.abi
            )

    def deploy(self, transaction_config):
        contract_class = contract_from_build(self.contract_name)
        deployed_contract = contract_class.deploy(transaction_config)
        self.address = deployed_contract.address
        self.contract = deployed_contract
        return deployed_contract.tx

    def assert_contract_is_instantiated(self) -> None:
        if self.contract is None:
            raise Exception("contract has not been instantiated")

    def verify_contract(self):
        self.assert_contract_is_instantiated()
        contract_class = contract_from_build(self.contract_name)
        contract_class.publish_source(self.contract)

    def approve(
        self, operator: ChecksumAddress, token_id: int, transaction_config
    ) -> Any:
        self.assert_contract_is_instantiated()
        return self.contract.approve(operator, token_id, transaction_config)

    def balance_of(
        self,
        account: ChecksumAddress,
        block_number: Optional[Union[str, int]] = "latest",
    ) -> Any:
        self.assert_contract_is_instantiated()
        return self.contract.balanceOf.call(account, block_identifier=block_number)

    def contract_uri(self, block_number: Optional[Union[str, int]] = "latest") -> Any:
        self.assert_contract_is_instantiated()
        return self.contract.contractURI.call(block_identifier=block_number)

    def create_character(self, player: ChecksumAddress, transaction_config) -> Any:
        self.assert_contract_is_instantiated()
        return self.contract.createCharacter(player, transaction_config)

    def get_approved(
        self, token_id: int, block_number: Optional[Union[str, int]] = "latest"
    ) -> Any:
        self.assert_contract_is_instantiated()
        return self.contract.getApproved.call(token_id, block_identifier=block_number)

    def init(
        self,
        admin_terminus_address: ChecksumAddress,
        admin_terminus_pool_id: int,
        character_creation_terminus_pool_id: int,
        contract_name: str,
        contract_symbol: str,
        contract_uri: str,
        transaction_config,
    ) -> Any:
        self.assert_contract_is_instantiated()
        return self.contract.init(
            admin_terminus_address,
            admin_terminus_pool_id,
            character_creation_terminus_pool_id,
            contract_name,
            contract_symbol,
            contract_uri,
            transaction_config,
        )

    def inventory(self, block_number: Optional[Union[str, int]] = "latest") -> Any:
        self.assert_contract_is_instantiated()
        return self.contract.inventory.call(block_identifier=block_number)

    def is_approved_for_all(
        self,
        account: ChecksumAddress,
        operator: ChecksumAddress,
        block_number: Optional[Union[str, int]] = "latest",
    ) -> Any:
        self.assert_contract_is_instantiated()
        return self.contract.isApprovedForAll.call(
            account, operator, block_identifier=block_number
        )

    def is_metadata_valid(
        self, token_id: int, block_number: Optional[Union[str, int]] = "latest"
    ) -> Any:
        self.assert_contract_is_instantiated()
        return self.contract.isMetadataValid.call(
            token_id, block_identifier=block_number
        )

    def name(self, block_number: Optional[Union[str, int]] = "latest") -> Any:
        self.assert_contract_is_instantiated()
        return self.contract.name.call(block_identifier=block_number)

    def owner_of(
        self, token_id: int, block_number: Optional[Union[str, int]] = "latest"
    ) -> Any:
        self.assert_contract_is_instantiated()
        return self.contract.ownerOf.call(token_id, block_identifier=block_number)

    def safe_transfer_from_0x42842e0e(
        self,
        from_: ChecksumAddress,
        to: ChecksumAddress,
        token_id: int,
        transaction_config,
    ) -> Any:
        self.assert_contract_is_instantiated()
        return self.contract.safeTransferFrom(from_, to, token_id, transaction_config)

    def safe_transfer_from_0xb88d4fde(
        self,
        from_: ChecksumAddress,
        to: ChecksumAddress,
        token_id: int,
        data: bytes,
        transaction_config,
    ) -> Any:
        self.assert_contract_is_instantiated()
        return self.contract.safeTransferFrom(
            from_, to, token_id, data, transaction_config
        )

    def set_approval_for_all(
        self, operator: ChecksumAddress, status: bool, transaction_config
    ) -> Any:
        self.assert_contract_is_instantiated()
        return self.contract.setApprovalForAll(operator, status, transaction_config)

    def set_contract_information(
        self,
        contract_name: str,
        contract_symbol: str,
        contract_uri: str,
        transaction_config,
    ) -> Any:
        self.assert_contract_is_instantiated()
        return self.contract.setContractInformation(
            contract_name, contract_symbol, contract_uri, transaction_config
        )

    def set_inventory(
        self, inventory_address: ChecksumAddress, transaction_config
    ) -> Any:
        self.assert_contract_is_instantiated()
        return self.contract.setInventory(inventory_address, transaction_config)

    def set_metadata_validity(
        self, token_id: int, valid: bool, transaction_config
    ) -> Any:
        self.assert_contract_is_instantiated()
        return self.contract.setMetadataValidity(token_id, valid, transaction_config)

    def set_token_uri(
        self,
        token_id: int,
        uri: str,
        is_appropriately_licensed: bool,
        transaction_config,
    ) -> Any:
        self.assert_contract_is_instantiated()
        return self.contract.setTokenUri(
            token_id, uri, is_appropriately_licensed, transaction_config
        )

    def supports_interface(
        self, interface_id: bytes, block_number: Optional[Union[str, int]] = "latest"
    ) -> Any:
        self.assert_contract_is_instantiated()
        return self.contract.supportsInterface.call(
            interface_id, block_identifier=block_number
        )

    def symbol(self, block_number: Optional[Union[str, int]] = "latest") -> Any:
        self.assert_contract_is_instantiated()
        return self.contract.symbol.call(block_identifier=block_number)

    def token_by_index(
        self, index: int, block_number: Optional[Union[str, int]] = "latest"
    ) -> Any:
        self.assert_contract_is_instantiated()
        return self.contract.tokenByIndex.call(index, block_identifier=block_number)

    def token_of_owner_by_index(
        self,
        owner: ChecksumAddress,
        index: int,
        block_number: Optional[Union[str, int]] = "latest",
    ) -> Any:
        self.assert_contract_is_instantiated()
        return self.contract.tokenOfOwnerByIndex.call(
            owner, index, block_identifier=block_number
        )

    def token_uri(
        self, token_id: int, block_number: Optional[Union[str, int]] = "latest"
    ) -> Any:
        self.assert_contract_is_instantiated()
        return self.contract.tokenURI.call(token_id, block_identifier=block_number)

    def total_supply(self, block_number: Optional[Union[str, int]] = "latest") -> Any:
        self.assert_contract_is_instantiated()
        return self.contract.totalSupply.call(block_identifier=block_number)

    def transfer_from(
        self,
        from_: ChecksumAddress,
        to: ChecksumAddress,
        token_id: int,
        transaction_config,
    ) -> Any:
        self.assert_contract_is_instantiated()
        return self.contract.transferFrom(from_, to, token_id, transaction_config)


def get_transaction_config(args: argparse.Namespace) -> Dict[str, Any]:
    signer = network.accounts.load(args.sender, args.password)
    transaction_config: Dict[str, Any] = {"from": signer}
    if args.gas_price is not None:
        transaction_config["gas_price"] = args.gas_price
    if args.max_fee_per_gas is not None:
        transaction_config["max_fee"] = args.max_fee_per_gas
    if args.max_priority_fee_per_gas is not None:
        transaction_config["priority_fee"] = args.max_priority_fee_per_gas
    if args.confirmations is not None:
        transaction_config["required_confs"] = args.confirmations
    if args.nonce is not None:
        transaction_config["nonce"] = args.nonce
    return transaction_config


def add_default_arguments(parser: argparse.ArgumentParser, transact: bool) -> None:
    parser.add_argument(
        "--network", required=True, help="Name of brownie network to connect to"
    )
    parser.add_argument(
        "--address", required=False, help="Address of deployed contract to connect to"
    )
    if not transact:
        parser.add_argument(
            "--block-number",
            required=False,
            type=int,
            help="Call at the given block number, defaults to latest",
        )
        return
    parser.add_argument(
        "--sender", required=True, help="Path to keystore file for transaction sender"
    )
    parser.add_argument(
        "--password",
        required=False,
        help="Password to keystore file (if you do not provide it, you will be prompted for it)",
    )
    parser.add_argument(
        "--gas-price", default=None, help="Gas price at which to submit transaction"
    )
    parser.add_argument(
        "--max-fee-per-gas",
        default=None,
        help="Max fee per gas for EIP1559 transactions",
    )
    parser.add_argument(
        "--max-priority-fee-per-gas",
        default=None,
        help="Max priority fee per gas for EIP1559 transactions",
    )
    parser.add_argument(
        "--confirmations",
        type=int,
        default=None,
        help="Number of confirmations to await before considering a transaction completed",
    )
    parser.add_argument(
        "--nonce", type=int, default=None, help="Nonce for the transaction (optional)"
    )
    parser.add_argument(
        "--value", default=None, help="Value of the transaction in wei(optional)"
    )
    parser.add_argument("--verbose", action="store_true", help="Print verbose output")


def handle_deploy(args: argparse.Namespace) -> None:
    network.connect(args.network)
    transaction_config = get_transaction_config(args)
    contract = CharactersFacet(None)
    result = contract.deploy(transaction_config=transaction_config)
    print(result)
    if args.verbose:
        print(result.info())


def handle_verify_contract(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    result = contract.verify_contract()
    print(result)


def handle_approve(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    transaction_config = get_transaction_config(args)
    result = contract.approve(
        operator=args.operator,
        token_id=args.token_id,
        transaction_config=transaction_config,
    )
    print(result)
    if args.verbose:
        print(result.info())


def handle_balance_of(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    result = contract.balance_of(account=args.account, block_number=args.block_number)
    print(result)


def handle_contract_uri(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    result = contract.contract_uri(block_number=args.block_number)
    print(result)


def handle_create_character(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    transaction_config = get_transaction_config(args)
    result = contract.create_character(
        player=args.player, transaction_config=transaction_config
    )
    print(result)
    if args.verbose:
        print(result.info())


def handle_get_approved(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    result = contract.get_approved(
        token_id=args.token_id, block_number=args.block_number
    )
    print(result)


def handle_init(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    transaction_config = get_transaction_config(args)
    result = contract.init(
        admin_terminus_address=args.admin_terminus_address,
        admin_terminus_pool_id=args.admin_terminus_pool_id,
        character_creation_terminus_pool_id=args.character_creation_terminus_pool_id,
        contract_name=args.contract_name,
        contract_symbol=args.contract_symbol,
        contract_uri=args.contract_uri,
        transaction_config=transaction_config,
    )
    print(result)
    if args.verbose:
        print(result.info())


def handle_inventory(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    result = contract.inventory(block_number=args.block_number)
    print(result)


def handle_is_approved_for_all(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    result = contract.is_approved_for_all(
        account=args.account, operator=args.operator, block_number=args.block_number
    )
    print(result)


def handle_is_metadata_valid(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    result = contract.is_metadata_valid(
        token_id=args.token_id, block_number=args.block_number
    )
    print(result)


def handle_name(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    result = contract.name(block_number=args.block_number)
    print(result)


def handle_owner_of(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    result = contract.owner_of(token_id=args.token_id, block_number=args.block_number)
    print(result)


def handle_safe_transfer_from_0x42842e0e(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    transaction_config = get_transaction_config(args)
    result = contract.safe_transfer_from_0x42842e0e(
        from_=args.from_arg,
        to=args.to,
        token_id=args.token_id,
        transaction_config=transaction_config,
    )
    print(result)
    if args.verbose:
        print(result.info())


def handle_safe_transfer_from_0xb88d4fde(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    transaction_config = get_transaction_config(args)
    result = contract.safe_transfer_from_0xb88d4fde(
        from_=args.from_arg,
        to=args.to,
        token_id=args.token_id,
        data=args.data,
        transaction_config=transaction_config,
    )
    print(result)
    if args.verbose:
        print(result.info())


def handle_set_approval_for_all(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    transaction_config = get_transaction_config(args)
    result = contract.set_approval_for_all(
        operator=args.operator,
        status=args.status,
        transaction_config=transaction_config,
    )
    print(result)
    if args.verbose:
        print(result.info())


def handle_set_contract_information(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    transaction_config = get_transaction_config(args)
    result = contract.set_contract_information(
        contract_name=args.contract_name,
        contract_symbol=args.contract_symbol,
        contract_uri=args.contract_uri,
        transaction_config=transaction_config,
    )
    print(result)
    if args.verbose:
        print(result.info())


def handle_set_inventory(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    transaction_config = get_transaction_config(args)
    result = contract.set_inventory(
        inventory_address=args.inventory_address, transaction_config=transaction_config
    )
    print(result)
    if args.verbose:
        print(result.info())


def handle_set_metadata_validity(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    transaction_config = get_transaction_config(args)
    result = contract.set_metadata_validity(
        token_id=args.token_id, valid=args.valid, transaction_config=transaction_config
    )
    print(result)
    if args.verbose:
        print(result.info())


def handle_set_token_uri(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    transaction_config = get_transaction_config(args)
    result = contract.set_token_uri(
        token_id=args.token_id,
        uri=args.uri,
        is_appropriately_licensed=args.is_appropriately_licensed,
        transaction_config=transaction_config,
    )
    print(result)
    if args.verbose:
        print(result.info())


def handle_supports_interface(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    transaction_config = get_transaction_config(args)
    result = contract.supports_interface(
        interface_id=args.interface_id, transaction_config=transaction_config
    )
    print(result)
    if args.verbose:
        print(result.info())


def handle_symbol(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    result = contract.symbol(block_number=args.block_number)
    print(result)


def handle_token_by_index(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    result = contract.token_by_index(index=args.index, block_number=args.block_number)
    print(result)


def handle_token_of_owner_by_index(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    result = contract.token_of_owner_by_index(
        owner=args.owner, index=args.index, block_number=args.block_number
    )
    print(result)


def handle_token_uri(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    result = contract.token_uri(token_id=args.token_id, block_number=args.block_number)
    print(result)


def handle_total_supply(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    result = contract.total_supply(block_number=args.block_number)
    print(result)


def handle_transfer_from(args: argparse.Namespace) -> None:
    network.connect(args.network)
    contract = CharactersFacet(args.address)
    transaction_config = get_transaction_config(args)
    result = contract.transfer_from(
        from_=args.from_arg,
        to=args.to,
        token_id=args.token_id,
        transaction_config=transaction_config,
    )
    print(result)
    if args.verbose:
        print(result.info())


def generate_cli() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="CLI for CharactersFacet")
    parser.set_defaults(func=lambda _: parser.print_help())
    subcommands = parser.add_subparsers()

    deploy_parser = subcommands.add_parser("deploy")
    add_default_arguments(deploy_parser, True)
    deploy_parser.set_defaults(func=handle_deploy)

    verify_contract_parser = subcommands.add_parser("verify-contract")
    add_default_arguments(verify_contract_parser, False)
    verify_contract_parser.set_defaults(func=handle_verify_contract)

    approve_parser = subcommands.add_parser("approve")
    add_default_arguments(approve_parser, True)
    approve_parser.add_argument("--operator", required=True, help="Type: address")
    approve_parser.add_argument(
        "--token-id", required=True, help="Type: uint256", type=int
    )
    approve_parser.set_defaults(func=handle_approve)

    balance_of_parser = subcommands.add_parser("balance-of")
    add_default_arguments(balance_of_parser, False)
    balance_of_parser.add_argument("--account", required=True, help="Type: address")
    balance_of_parser.set_defaults(func=handle_balance_of)

    contract_uri_parser = subcommands.add_parser("contract-uri")
    add_default_arguments(contract_uri_parser, False)
    contract_uri_parser.set_defaults(func=handle_contract_uri)

    create_character_parser = subcommands.add_parser("create-character")
    add_default_arguments(create_character_parser, True)
    create_character_parser.add_argument(
        "--player", required=True, help="Type: address"
    )
    create_character_parser.set_defaults(func=handle_create_character)

    get_approved_parser = subcommands.add_parser("get-approved")
    add_default_arguments(get_approved_parser, False)
    get_approved_parser.add_argument(
        "--token-id", required=True, help="Type: uint256", type=int
    )
    get_approved_parser.set_defaults(func=handle_get_approved)

    init_parser = subcommands.add_parser("init")
    add_default_arguments(init_parser, True)
    init_parser.add_argument(
        "--admin-terminus-address", required=True, help="Type: address"
    )
    init_parser.add_argument(
        "--admin-terminus-pool-id", required=True, help="Type: uint256", type=int
    )
    init_parser.add_argument(
        "--character-creation-terminus-pool-id",
        required=True,
        help="Type: uint256",
        type=int,
    )
    init_parser.add_argument(
        "--contract-name", required=True, help="Type: string", type=str
    )
    init_parser.add_argument(
        "--contract-symbol", required=True, help="Type: string", type=str
    )
    init_parser.add_argument(
        "--contract-uri", required=True, help="Type: string", type=str
    )
    init_parser.set_defaults(func=handle_init)

    inventory_parser = subcommands.add_parser("inventory")
    add_default_arguments(inventory_parser, False)
    inventory_parser.set_defaults(func=handle_inventory)

    is_approved_for_all_parser = subcommands.add_parser("is-approved-for-all")
    add_default_arguments(is_approved_for_all_parser, False)
    is_approved_for_all_parser.add_argument(
        "--account", required=True, help="Type: address"
    )
    is_approved_for_all_parser.add_argument(
        "--operator", required=True, help="Type: address"
    )
    is_approved_for_all_parser.set_defaults(func=handle_is_approved_for_all)

    is_metadata_valid_parser = subcommands.add_parser("is-metadata-valid")
    add_default_arguments(is_metadata_valid_parser, False)
    is_metadata_valid_parser.add_argument(
        "--token-id", required=True, help="Type: uint256", type=int
    )
    is_metadata_valid_parser.set_defaults(func=handle_is_metadata_valid)

    name_parser = subcommands.add_parser("name")
    add_default_arguments(name_parser, False)
    name_parser.set_defaults(func=handle_name)

    owner_of_parser = subcommands.add_parser("owner-of")
    add_default_arguments(owner_of_parser, False)
    owner_of_parser.add_argument(
        "--token-id", required=True, help="Type: uint256", type=int
    )
    owner_of_parser.set_defaults(func=handle_owner_of)

    safe_transfer_from_0x42842e0e_parser = subcommands.add_parser(
        "safe-transfer-from-0x42842e0e"
    )
    add_default_arguments(safe_transfer_from_0x42842e0e_parser, True)
    safe_transfer_from_0x42842e0e_parser.add_argument(
        "--from-arg", required=True, help="Type: address"
    )
    safe_transfer_from_0x42842e0e_parser.add_argument(
        "--to", required=True, help="Type: address"
    )
    safe_transfer_from_0x42842e0e_parser.add_argument(
        "--token-id", required=True, help="Type: uint256", type=int
    )
    safe_transfer_from_0x42842e0e_parser.set_defaults(
        func=handle_safe_transfer_from_0x42842e0e
    )

    safe_transfer_from_0xb88d4fde_parser = subcommands.add_parser(
        "safe-transfer-from-0xb88d4fde"
    )
    add_default_arguments(safe_transfer_from_0xb88d4fde_parser, True)
    safe_transfer_from_0xb88d4fde_parser.add_argument(
        "--from-arg", required=True, help="Type: address"
    )
    safe_transfer_from_0xb88d4fde_parser.add_argument(
        "--to", required=True, help="Type: address"
    )
    safe_transfer_from_0xb88d4fde_parser.add_argument(
        "--token-id", required=True, help="Type: uint256", type=int
    )
    safe_transfer_from_0xb88d4fde_parser.add_argument(
        "--data", required=True, help="Type: bytes", type=bytes_argument_type
    )
    safe_transfer_from_0xb88d4fde_parser.set_defaults(
        func=handle_safe_transfer_from_0xb88d4fde
    )

    set_approval_for_all_parser = subcommands.add_parser("set-approval-for-all")
    add_default_arguments(set_approval_for_all_parser, True)
    set_approval_for_all_parser.add_argument(
        "--operator", required=True, help="Type: address"
    )
    set_approval_for_all_parser.add_argument(
        "--status", required=True, help="Type: bool", type=boolean_argument_type
    )
    set_approval_for_all_parser.set_defaults(func=handle_set_approval_for_all)

    set_contract_information_parser = subcommands.add_parser("set-contract-information")
    add_default_arguments(set_contract_information_parser, True)
    set_contract_information_parser.add_argument(
        "--contract-name", required=True, help="Type: string", type=str
    )
    set_contract_information_parser.add_argument(
        "--contract-symbol", required=True, help="Type: string", type=str
    )
    set_contract_information_parser.add_argument(
        "--contract-uri", required=True, help="Type: string", type=str
    )
    set_contract_information_parser.set_defaults(func=handle_set_contract_information)

    set_inventory_parser = subcommands.add_parser("set-inventory")
    add_default_arguments(set_inventory_parser, True)
    set_inventory_parser.add_argument(
        "--inventory-address", required=True, help="Type: address"
    )
    set_inventory_parser.set_defaults(func=handle_set_inventory)

    set_metadata_validity_parser = subcommands.add_parser("set-metadata-validity")
    add_default_arguments(set_metadata_validity_parser, True)
    set_metadata_validity_parser.add_argument(
        "--token-id", required=True, help="Type: uint256", type=int
    )
    set_metadata_validity_parser.add_argument(
        "--valid", required=True, help="Type: bool", type=boolean_argument_type
    )
    set_metadata_validity_parser.set_defaults(func=handle_set_metadata_validity)

    set_token_uri_parser = subcommands.add_parser("set-token-uri")
    add_default_arguments(set_token_uri_parser, True)
    set_token_uri_parser.add_argument(
        "--token-id", required=True, help="Type: uint256", type=int
    )
    set_token_uri_parser.add_argument(
        "--uri", required=True, help="Type: string", type=str
    )
    set_token_uri_parser.add_argument(
        "--is-appropriately-licensed",
        required=True,
        help="Type: bool",
        type=boolean_argument_type,
    )
    set_token_uri_parser.set_defaults(func=handle_set_token_uri)

    supports_interface_parser = subcommands.add_parser("supports-interface")
    add_default_arguments(supports_interface_parser, False)
    supports_interface_parser.add_argument(
        "--interface-id", required=True, help="Type: bytes4", type=bytes_argument_type
    )
    supports_interface_parser.set_defaults(func=handle_supports_interface)

    symbol_parser = subcommands.add_parser("symbol")
    add_default_arguments(symbol_parser, False)
    symbol_parser.set_defaults(func=handle_symbol)

    token_by_index_parser = subcommands.add_parser("token-by-index")
    add_default_arguments(token_by_index_parser, False)
    token_by_index_parser.add_argument(
        "--index", required=True, help="Type: uint256", type=int
    )
    token_by_index_parser.set_defaults(func=handle_token_by_index)

    token_of_owner_by_index_parser = subcommands.add_parser("token-of-owner-by-index")
    add_default_arguments(token_of_owner_by_index_parser, False)
    token_of_owner_by_index_parser.add_argument(
        "--owner", required=True, help="Type: address"
    )
    token_of_owner_by_index_parser.add_argument(
        "--index", required=True, help="Type: uint256", type=int
    )
    token_of_owner_by_index_parser.set_defaults(func=handle_token_of_owner_by_index)

    token_uri_parser = subcommands.add_parser("token-uri")
    add_default_arguments(token_uri_parser, False)
    token_uri_parser.add_argument(
        "--token-id", required=True, help="Type: uint256", type=int
    )
    token_uri_parser.set_defaults(func=handle_token_uri)

    total_supply_parser = subcommands.add_parser("total-supply")
    add_default_arguments(total_supply_parser, False)
    total_supply_parser.set_defaults(func=handle_total_supply)

    transfer_from_parser = subcommands.add_parser("transfer-from")
    add_default_arguments(transfer_from_parser, True)
    transfer_from_parser.add_argument("--from-arg", required=True, help="Type: address")
    transfer_from_parser.add_argument("--to", required=True, help="Type: address")
    transfer_from_parser.add_argument(
        "--token-id", required=True, help="Type: uint256", type=int
    )
    transfer_from_parser.set_defaults(func=handle_transfer_from)

    return parser


def main() -> None:
    parser = generate_cli()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
