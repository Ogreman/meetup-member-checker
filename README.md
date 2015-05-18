Installation
------------

Recommend using virtualenvwrapper: http://virtualenvwrapper.readthedocs.org/en/latest/

    $ git clone git@github.com:Ogreman/meetup-member-checker.git
    $ cd meetup-member-checker
    $ pip install .
    $ export MEETUP_API_KEY="MY_MEETUP_API_KEY"

See here for retrieval of your Meetup API key: https://secure.meetup.com/meetup_api/key/

Usage
-----

    $ meetup-members check [unique-name] [meetup-url]
    
  Example:
  
    $ meetup-members check werewolf
    Enter Meetup group URL for werewolf: Werewolf-the-Social-Deduction-game-Bristol
    werewolf: 266 existing members.
    werewolf: 266 received members.
    werewolf: No change.

Environment Variables & Virtual Environments
--------------------------------------------

With virtualenvwrapper installed, it is recommended to add the following to the activation hooks:

    $ mkvirtualenv meetup-member-checker
    $ cd $VIRTUAL_ENV/bin
    $ echo export MEETUP_API_KEY="MY_MEETUP_API_KEY" >> postactivate
    $ echo unset MEETUP_API_KEY >> postdeactivate
    $ deactivate
    $ workon meetup-member-checker
    $ echo $MEETUP_API_KEY
    MY_MEETUP_API_KEY
