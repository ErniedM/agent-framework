import platform

class SystemInfoModule:
    def collect_data(self):
        system_info = {
            "operating_system": None,
            "release": None,
            "version": None,
            "architecture": None,
            "processor": None,
            "hostname": None,
            "username": None,
            "python_version": platform.python_version()
        }

        # Check the current operating system
        if platform.system() == 'Windows':
            system_info["operating_system"] = 'Windows'
            system_info["release"] = platform.release()
            system_info["version"] = platform.version()
            system_info["architecture"] = platform.machine()
            system_info["processor"] = platform.processor()
            system_info["hostname"] = platform.node()
            system_info["username"] = platform.uname().node

        elif platform.system() == 'Linux':
            system_info["operating_system"] = 'Linux'
            system_info["release"] = platform.release()
            system_info["version"] = platform.version()
            system_info["architecture"] = platform.machine()
            system_info["processor"] = platform.processor()
            system_info["hostname"] = platform.node()
            system_info["username"] = platform.uname().node

        elif platform.system() == 'Darwin':
            system_info["operating_system"] = 'macOS'
            system_info["release"] = platform.release()
            system_info["version"] = platform.mac_ver()[0]
            system_info["architecture"] = platform.machine()
            system_info["processor"] = platform.processor()
            system_info["hostname"] = platform.node()
            system_info["username"] = platform.uname().node

        else:
            # Handle unsupported operating systems
            system_info["operating_system"] = platform.system()

        return system_info
