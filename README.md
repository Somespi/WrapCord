# Wrapcord

Wrapcord is a Python package that provides a simple way to send messages to a Discord webhook.

## Installation

To install the `wrapcord` package, use the following command:

```
$ pip install wrapcord
```


## Usage

To use the `Wrapcord` package, you'll need a Discord webhook URL. If you don't already have a webhook URL, you can create one by following these steps:

1. Go to your Discord server settings
2. Click on "Integrations" and then "Webhooks"
3. Click "Create Webhook"
4. Enter a name for the webhook and choose a channel to post to
5. Click "Copy Webhook URL"

Once you have a webhook URL, you can use the `Wrapcord` package to send messages to it. Here's an example:

```python
from wrapcord import Wrapcord 

webhook = Wrapcord.Webhook("https://discord.com/api/webhooks/123456789012345678/abcdefg1234567")

webhook.send(content="Hello")
```


In the example above, we imported the Wrapcord class from the wrapcord package, initialized it with a Discord webhook URL, and sent a message to the webhook with the content "Hello".

You can also customize the message by specifying additional parameters


```python

webhook.send(
    content="Hello, world!",
    username="My Bot",
    avatar_url="img.png",
    tts=False,
    files=None,
    embeds=[{
        "title": "Example Embed",
        "description": "This is an example embed.",
        "color": 0x00ff00
    }],
    allowed_mentions=None
)

```
In the example above, we specified a custom username and avatar URL for the message, disabled text-to-speech, included an embed with a title, description, and color, and left the files and allowed_mentions parameters as their default values.

For more information on the available parameters, see the Discord webhook documentation.

## Contributing

If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request on the GitHub repository.


## License
Wrapcord is released under the MIT License. See LICENSE for more information.

