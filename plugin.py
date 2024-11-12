from lsp_utils import NpmClientHandler
import os


def plugin_loaded():
    LspTwigPlugin.setup()


def plugin_unloaded():
    LspTwigPlugin.cleanup()


class LspTwigPlugin(NpmClientHandler):
    package_name = __package__
    server_directory = 'language-server'
    server_binary_path = os.path.join(server_directory, 'node_modules', 'twiggy-language-server', 'bin', 'server.js')
