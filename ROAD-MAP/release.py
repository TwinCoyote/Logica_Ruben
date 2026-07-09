"""ctr + alt + p"""
# pylint: disable = W3101,C0301

import requests

# * GET /repos/{owner}/{repo}/releases
URL = "https://api.github.com/repos/TwinCoyote/ESP-ARCADE-32/releases/latest"
VERSION = "1.0.5"


def get_latest_release_tag(link: str) -> tuple[str, str]:
    """Get the tag_name of the latest GitHub release."""
    try:
        response = requests.get(link, timeout=10)
    except requests.Timeout:
        return ("error", "The request timed out while getting the latest release")
    except requests.RequestException as e:
        return ("error", f"Network error while getting latest release: {e}")

    if response.status_code != 200:
        return ("error", f"status {response.status_code}")

    try:
        response_json = response.json()
    except ValueError:
        return ("error", "Invalid JSON response from GitHub API")

    tag = response_json.get("tag_name")
    if not tag:
        return ("error", "tag_name was not found in the API response")

    return ("ok", tag)

# print(get_latest_release_tag(URL))


def get_release(linked: str) -> tuple[str, str]:
    """Download firmware.bin from the latest GitHub release."""
    version = get_latest_release_tag(linked)

    if version[0] != "ok":
        return ("error", version[1])

    tag = version[1]
    link = f"https://github.com/TwinCoyote/ESP-ARCADE-32/releases/download/{tag}/firmware.bin"

    try:
        pet = requests.get(link, timeout=10)
    except requests.Timeout:
        return ("error", "The request timed out while downloading firmware.bin")
    except requests.RequestException as e:
        return ("error", f"Network error while downloading firmware.bin: {e}")

    if pet.status_code != 200:
        return ("error", f"status {pet.status_code} while downloading firmware.bin")

    try:
        with open("firmware.bin", "wb") as archivo:
            archivo.write(pet.content)
    except OSError as e:
        return ("error", f"File write error: {e}")

    return ("ok", f"firmware.bin saved successfully from version {tag}")


resultado = get_release(URL)

if resultado[0] == "ok":
    print(resultado[1])
else:
    print(f"Error: {resultado[1]}")


# * https://github.com/TwinCoyote/ESP-ARCADE-32/releases/download/v1.0.5/firmware.bin


print(get_release(URL))
