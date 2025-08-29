# ansibleにてローカルでpingを実行するサンプルプログラム

- タイトルの通り、SSHせずにローカルでpingを発行するプログラム。
- pythonからansibleを実行するための動作確認がしたい。

## 操作メモ

- 必要なパッケージをインストールする。

```shell
pip install ansible-runner ansible
```

- プログラムを実行する。

```shell
$ python3 ansible_ping.py 
core/2.18/reference_appendices/interpreter_discovery.html for more information.
127.0.0.1 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/workspace/venv/bin/python3.12"
    },
    "changed": false,
    "ping": "pong"
}
Ping Results: {'127.0.0.1': {'ping': 'pong', 'invocation': {'module_args': {'data': 'pong'}}, 'ansible_facts': {'discovered_interpreter_python': '/workspace/venv/bin/python3.12'}, 'warnings': ['Platform linux on host 127.0.0.1 is using the discovered Python interpreter at /workspace/venv/bin/python3.12, but future installation of another Python interpreter could change the meaning of that path. See https://docs.ansible.com/ansible-core/2.18/reference_appendices/interpreter_discovery.html for more information.'], '_ansible_no_log': False, 'changed': False}}
```
