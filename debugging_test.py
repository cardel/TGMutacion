import subprocess
import pdb


def run_mutpy(target, test):
    command = ['mut.py', '--target', target, '--unit-test', test, '-m', '-c']
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)


def run_tests(test):
    command = ['python3', '-m', 'unittest', test]
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)


if __name__ == '__main__':
    pdb.set_trace()
    # run_tests('test/test_security.py')
    run_mutpy('one_conf.py', 'test/test_security.py')
