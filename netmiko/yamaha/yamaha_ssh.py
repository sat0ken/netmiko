from __future__ import print_function
from __future__ import unicode_literals
import time
from netmiko.cisco_base_connection import CiscoSSHConnection

class YamahaSSH(CiscoSSHConnection):
    def session_preparation(self):
        self._test_channel_read(pattern=r"[>#]")
        self.set_base_prompt()
        self.disable_paging(command="console lines infinity")
        time.sleep(0.3 * self.global_delay_factor)
        self.clear_buffer()

    def exit_enable_mode(self, exit_command="exit"):
        """Exit enable mode."""
        return super(YamahaSSH, self).exit_enable_mode(exit_command=exit_command)

    def save_config(self, cmd="save", confirm=False):
        """Saves configuration."""
        return super(YamahaSSH, self).save_config(cmd=cmd, confirm=confirm)

