# Test P2P Content Services

This is a simple application to test creating content with the P2P Content Services API. It uses two libraries written by the newsapps team.

To install the app, you'll need pip. Easy install pip, and then pip install the requirements.

    $ easy_install pip
    $ pip install -r requirements.txt

You will need to have the following environment variables set in your shell:
`P2P_API_URL` and `P2P_API_KEY`.

Run the test app:

    $ python test_p2p.py
    
The app will print that it's going to try to create content in P2P, and then print the response from the server. When the response is successful, it will print a json object containing P2P's information about the new content item.

To verify the connection settings for the p2p library, use the interpreter:

    $ ipython
    >>> import p2p
    >>> foo = p2p.get_connection()
    >>> foo.config
