AllMyChanges.com to Slack Integration
=====================================

This script starts as a daemon and listen
on a TCP port for calls from AllMyChanges.

Read AllMyChanges.com's help page
[how to setup a web-hook][web-hooks].

Script uses a [python-processor][processor-docs]
to build a processing pipeline.


Installation
------------

    sudo apt-get install python3-dev
    virtualenv --python=python3 env
    source env/bin/activate
    pip install -r requirements.txt

    cp settings.py.example settings.py

After that, edit `settings.py` and enter
all necessary settings.

Output by email was added as example, to
demostrate that you could not only notify to slack,
but also sedn data to different placess simultaneously
and use different message formats.


[web-hooks]: https://allmychanges.com/help/webhooks
[processor-docs]: https://python-processor.readthedocs.org/
