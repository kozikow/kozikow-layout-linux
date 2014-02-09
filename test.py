import os
import re
import sh
import signal


def get_list_of_pids_matching_regex(regex):
  process_lines = re.findall(regex, "\n".join(sh.ps("cax")))
  return [int(line.split()[0]) for line in process_lines if len(line) > 0]

def kill_processes_matching_regex(regex):
  pids = get_list_of_pids_matching_regex(regex)
  for pid in pids:
    try:
      os.kill(pid, signal.SIGTERM)
    except OSError:
      print "Killing process with pid %d (name matches regex %s) gently (" \
            "SIGTERM) failed. sending SIGKILL. " % (regex, pid)
      os.kill(pid, signal.SIGKILL) # If this fails this throws
  assert(len(get_list_of_pids_matching_regex(regex)) == 0)

def kill_old_xcape():
  """
  Two instances of xcape mess up with everything.
  For example when pressing enter two enters are sent to the system.
  The easiest way out is to kill old version of xcape.
  """
  kill_processes_matching_regex(".*ccsm")

if __name__ == '__main__':
  kill_old_xcape()
