import sys
from typing import Any, Coroutine, List, Iterable
from galaxy.api.plugin import Plugin, create_and_run_plugin
from galaxy.api.consts import Platform
from galaxy.api.types import Authentication, Game, LicenseInfo, LicenseType, LocalGame, LocalGameState
from galaxy.api.errors import AuthenticationRequired


class PluginExample(Plugin):
    def __init__(self, reader, writer, token):
        super().__init__(
            Platform.Test,  # choose platform from available list
            "0.1",  # version
            reader,
            writer,
            token
        )

    async def authenticate(self, stored_credentials=None):
        # TODO: implement authentication
        return Authentication('test_user_id', 'Test User Name')


    async def get_owned_games(self) -> Iterable[Game]:
        if not self.authenticated():
            raise AuthenticationRequired()
        # TODO: fetch owned games
        return [Game('test', 'The Test', None, LicenseInfo(LicenseType.SinglePurchase))]

    async def get_local_games(self) -> Iterable[LocalGame]:
        # TODO: fetch local games
        return [LocalGame("test", LocalGameState.Installed)]
    
    async def launch_game(self, game_id: str) -> Coroutine[Any, Any, None]:
        # TODO: implement launching game
        raise NotImplementedError


def main():
    create_and_run_plugin(PluginExample, sys.argv)

# run plugin event loop
if __name__ == "__main__":
    main()