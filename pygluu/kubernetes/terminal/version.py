"""
pygluu.kubernetes.terminal.version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This module contains helpers to interact with user's inputs for terminal gluu version prompts.

License terms and conditions for Gluu Cloud Native Edition:
https://www.apache.org/licenses/LICENSE-2.0
"""
import click

from pygluu.kubernetes.common import get_supported_versions


class PromptVersion:

    def __init__(self, settings, version=""):
        self.settings = settings
        if not self.settings.get("GLUU_VERSION"):
            self.settings.set("GLUU_VERSION", version)
        self.prompt_version()

    def prompt_version(self):
        """Prompts for Gluu versions
        """
        versions, version_number = get_supported_versions()

        if not self.settings.get("GLUU_VERSION"):
            self.settings.set("GLUU_VERSION", click.prompt(
                "Please enter the current version of Gluu or the version to be installed",
                default=version_number,
            ))

        image_names_and_tags = versions.get(self.settings.get("GLUU_VERSION"), {})
        # override non-empty image name and tag
        self.settings.update({
            k: v for k, v in image_names_and_tags.items()
            if not self.settings.get(k)
        })
