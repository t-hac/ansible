import os
import ansible_runner

def run_local_ping():
    """
    ローカルホスト(127.0.0.1)に対して Ansible ping モジュールを
    ローカル接続で実行し、結果を dict で返す
    """
    # private_data_dir を作成
    private_data_dir = '/tmp/ansible_runner'
    os.makedirs(private_data_dir, exist_ok=True)

    inventory = "127.0.0.1 ansible_connection=local"

    r = ansible_runner.run(
        private_data_dir=private_data_dir,
        host_pattern='127.0.0.1',
        inventory=inventory,
        module='ping'
    )

    results = {}
    for event in r.events:
        if event.get('event') == 'runner_on_ok':
            host = event['event_data']['host']
            res = event['event_data']['res']
            results[host] = res

    return results

if __name__ == "__main__":
    ping_results = run_local_ping()
    print("Ping Results:", ping_results)
