Sync macbook screen brightness to non-Apple external displays.

## Here is how it works(by this version)
I found two useful commands to get this job done.

1. command to query builtin display's brightness;
2. [command][ddcctl] to set external displays' settings using [DDC][ddc] protocol.

So with a periodically running Python script, I can combine those 2 commands together and done.

Run example (python2.7/python3):

```bash
$ python main.py
```

## TODO
A swift version mac app which listens for system events and do the setting job smartly.


[ddcctl]: https://github.com/kfix/ddcctl
[ddc]: https://en.wikipedia.org/wiki/Direct_digital_control