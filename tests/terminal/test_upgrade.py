import pytest


@pytest.mark.parametrize("given, expected", [
    ("", "4.3"),
    ("4.3", "4.3"),
])
def test_upgrade_version(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.upgrade import PromptUpgrade

    monkeypatch.setattr("click.prompt", lambda x, default: given or expected)
    monkeypatch.setattr(
        "pygluu.kubernetes.terminal.images.PromptImages.prompt_image_name_tag",
        lambda cls: None,
    )

    PromptUpgrade(settings).prompt_upgrade()
    assert settings.get("GLUU_UPGRADE_TARGET_VERSION") == expected
    assert settings.get("EDIT_IMAGE_NAMES_TAGS") == ""
