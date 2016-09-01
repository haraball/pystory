``pystory``
===========

Keep a local history of everything you do inside your virtual python environment.

Installation
------------

After activating your virtual environment, install the module with::

    pip install pystory

Add the following line to your ``.bashrc``/``.bash_profile`` file to enable ``pystory``::

    export PROMPT_COMMAND='if [ ! -z ${VIRTUAL_ENV+x} ]; then echo "$(date "+%Y-%m-%d.%H:%M:%S") $(pwd) $(history 1)" >> $VIRTUAL_ENV/.pystory; fi'


The contents of `PROMPT_COMMAND <http://www.tldp.org/HOWTO/Bash-Prompt-HOWTO/x264.html>`_ are executed as a regular Bash command just before Bash displays a prompt.

This line adds your last command as an entry to the ``.pystory`` file, which will be placed in your ``$VIRTUAL_ENV/`` folder. 

Ex::

    /Users/username/project/.venv/.pystory


Usage
-----

Check your pystory by typing ``pystory`` while your virtual environment is activated.

::

    $ pystory
    Hist    Count    Command
    1       1.       pip install requests
    2       1.       pip install Django
    5       3.       python
    ...

Note that the output is compressed, so only the last history entry of a command is listed, with the count of times the command is used.

::

    $ pystory find Django
    Commands matching `Django`:
    Hist    Count     Command
    2       1         pip install Django
