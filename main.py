# -*- coding: utf-8 -*-

import logging
import os
import re
import time


logging.basicConfig(format='%(asctime)s %(message)s', filename='log.log', level=logging.DEBUG)


def query_builtin_brightness():
  """Query builtin display's brightness.

  Returns:
    [max brightness, current brightness]
  """
  command = 'ioreg -c AppleBacklightDisplay | grep brightness | sed \'s/.*"brightness"={"max"=\\([0-9]\\{1,4\\}\\),"min"=[0-9]\\{1,4\\},"value"=\\([0-9]\\{1,4\\}\\).*/\\1,\\2/\''
  result = os.popen(command).read()
  return map(lambda x: int(x), result.replace('\n', '').split(','))


def get_external_edid():
  """return first external display's edid"""
  command = 'ddcctl -d 1'
  dinfo = os.popen(command).read()
  result = re.findall(r'edid.name: (.*)\n', dinfo)
  if result:
    return result[0]
  return ''


def set_external_brightness(brightness_level):
  """Set first external dhsplay's brightness

  Args:
    brightness_level
  Returns:
    result from shell
  """
  command = 'ddcctl -d 1 -b {}'.format(brightness_level)
  result = os.popen(command).read()
  return result


if __name__ == '__main__':
  last_brightness_level = 0
  while True:
    _max, current = query_builtin_brightness()
    brightness_level = current / float(_max) * 100
    if abs(brightness_level - last_brightness_level) > 1:
      last_brightness_level = brightness_level
      logging.debug('builtin display\'s brightness: %d', brightness_level)
      if get_external_edid() == 'LG Ultra HD':
        # alter brightness to be set for LG Ultra HD
        # 75 --> 45, 30 minus
        brightness_level -= 30
      result = set_external_brightness(brightness_level)
      logging.debug('external display\'s brightness setting result %s', result)
    time.sleep(6)
