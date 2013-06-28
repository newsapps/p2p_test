<h1>Test P2P Content Services</h1>

<p>
This is a simple application to test creating content with the p2p content services API. It uses two libraries written by the newsapps team.
</p> 

<p>
To install the app, you'll need pip. Easy install pip, and then pip install the requirements.
</p>

<pre>
easy_install pip
pip install -r requirements.txt
</pre>

You will need to have the following environment variables set in your shell:
P2P_API_URL and P2P_API_KEY.

To use the app, type python to open the python interpreter and then test_p2p.py. The app will print to the screen that it's going to try to create content in p2p, and then print the response from the server. When the response is successful, it is a json object containing p2p's information about the new content item.

If you want to confirm your p2p connection object config settings, type ipython to open a ipython shell. Type import p2p, then foo = p2p.get_connection, then foo.config, and that will display your configs.