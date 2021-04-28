**Debugging PyDiceroll**
========================

.. figure:: fake_die.png

**PyDiceroll 3.2** keeps a log file of any dice rolls made during its last run. You will find ``PyDiceroll.log`` in the ``Logs``
folder it creates if one isn't there already. In the file you will see mentions of dice being rolled. **PyDiceroll** uses
a default logging mode of ``INFO`` which isn't that verbose. ::

   PyDiceroll_log.setLevel(logging.INFO)

Your **INFO** logging will output as:

   | ...INFO PyDiceroll - Logging started.
   | ...INFO PyDiceroll - roll() v3.2 started, and running...
   | ...INFO PyDiceroll - '3D4' = 3D4+0 = 10

Changing **PyDiceroll's** logging mode to ``DEBUG`` will record debugging messages in the ``Logs\PyDiceroll.log`` file. ::
   
   PyDiceroll_log.setLevel(logging.DEBUG)

Your **DEBUG** logging will output as:

   | ...INFO PyDiceroll - Logging started.
   | ...INFO PyDiceroll - roll() v3.2 started, and running...
   | ...DEBUG PyDiceroll - Asked to roll '3D4':
   | ...DEBUG PyDiceroll - Using three 4-sided dice...
   | ...DEBUG PyDiceroll - Rolled a 4
   | ...DEBUG PyDiceroll - Rolled a 2
   | ...DEBUG PyDiceroll - Rolled a 2
   | ...INFO PyDiceroll - '3D4' = 3D4+0 = 8
   
.. warning::
   Running **PyDiceroll** in ``DEBUG`` mode may create a log file that will be too huge to open. A program of yours
   left running for a long period of time could create millions of lines of recorded log entries. Fortunately, ``PyDiceroll.log`` is
   reset each time your program is run.
   
.. note::
   Any errors encountered will be recorded as ``ERROR`` in the log file, no
   matter which logging mode you've chosen to use.

If your own code has logging enabled for it, be sure to let **PyDiceroll** know by changing ``your_code_name_here`` to
the name of the program you're calling ``roll()`` from. The original line looks like this: ::

   log = logging.getLogger('your_code_name_here.PyDiceroll')

So, if your own code is called ``dungeoneer.py``, then make ::

   log = logging.getLogger('dungeoneer.PyDiceroll')