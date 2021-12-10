from edpu import git_repo_data as GRD
from edpu import host_alias

def get():
    return {
        'UserData': GRD.Data(
            {
                'PC': 'PC-UserData',
                'Laptop': 'Laptop-UserData',
            },
            GRD.Remotes([], {
                'USBFlash': 'USBFlash-Git-UserData',
            }),
            ['master'],
            ['Cloud1', 'Cloud2', 'Offsite']
        ),
        'ed_python_utils': GRD.Data(
            {
                'PC': 'PC-ed_python_utils',
                'Laptop': 'Laptop-ed_python_utils',
            },
            GRD.Remotes(['origin'], {
                'USBFlash': 'USBFlash-Git-ed_python_utils',
            }),
            ['master'],
            ['Offsite']
        ),
        'ed_python_roaming_data': GRD.Data(
            {
                'PC': 'PC-ed_python_roaming_data',
                'Laptop': 'Laptop-ed_python_roaming_data',
            },
            GRD.Remotes([], {
                'USBFlash': 'USBFlash-Git-ed_python_roaming_data',
            }),
            ['master'],
            ['Cloud1', 'Cloud2', 'Offsite']
        ),
    }

def bootstrap_repos():
    return set(['ed_python_utils', 'ed_python_roaming_data'])

def autopush_repos():
    return set([])

def get_bundle_path():
    paths = {
        'PC': 'C:\\Users\\Username\\Downloads\\GitBundles',
        'Laptop': 'C:\\Users\\Username\\Downloads\\GitBundles',
    }
    return paths.get(host_alias.get())

def get_bundle_hash_path(target_alias, repo_alias):
    paths = {
        'PC': 'C:\\Users\\Username\\Documents\\GitBundles',
        'Laptop': 'C:\\Users\\Username\\Documents\\GitBundles',
    }
    return paths.get(host_alias.get()) + '\\' + target_alias + '-' + repo_alias + '.txt'

def get_user_bundle_info_path():
    paths = {
        'PC': 'C:\\Users\\Username\\Downloads\\GitBundlesUser.txt',
        'Laptop': 'C:\\Users\\Username\\Downloads\\GitBundlesUser.txt',
    }
    return paths.get(host_alias.get())

def get_user_bundle_info_new_path():
    paths = {
        'PC': 'C:\\Users\\Username\\Downloads\\GitBundles\\GitBundlesUser.txt',
        'Laptop': 'C:\\Users\\Username\\Downloads\\GitBundles\\GitBundlesUser.txt',
    }
    return paths.get(host_alias.get())
